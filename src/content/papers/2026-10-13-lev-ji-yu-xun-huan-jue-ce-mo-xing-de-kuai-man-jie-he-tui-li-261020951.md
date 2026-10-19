---
title: 'LEV: Thinking Fast and Deep with Looped Decision Models'
title_zh: LEV：基于循环决策模型的快慢结合推理系统
authors:
- Dingjie Song
- Zhiling Yan
- Yuxuan Zhang
- Lichao Sun
affiliations:
- Lehigh University
- University of British Columbia
- Vector Institute
arxiv_id: '2610.20951'
url: https://arxiv.org/abs/2610.20951
pdf_url: https://arxiv.org/pdf/2610.20951
published: '2026-10-13'
collected: '2026-10-19'
category: LLM
direction: 循环LLM · 自适应推理深度优化
tags:
- Looped Transformer
- Adaptive Computation
- Decision Model
- Early Exit
- LoRA
one_liner: 基于原生预训练循环Transformer，实现单 checkpoint 按需调整推理深度的决策模型
practical_value: '- 电商推荐的粗/精排、搜索query意图识别这类决策场景，可复用LEV的原生循环Transformer+多步联合训练方案，单checkpoint覆盖低延迟高吞吐粗排、高精度精排多场景需求，无需维护多套模型参数

  - 自适应深度的无标注stopper设计可直接迁移：仅预测当前步与最深步输出的一致性，几百条无标注业务流量即可拟合阈值，在算力节省15%~24%的前提下精度损失<1个百分点

  - 针对业务中难易样本分布不均的场景（如大部分query意图简单、少部分复杂多义），可借鉴LEV的算力分配逻辑：简单样本浅步快速输出、复杂样本深步保证精度，填补低延迟区间的精度空白'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前决策模型（类似双系统理论的System1）单前向pass输出结果，推理深度固定，简单问题浪费算力、复杂问题精度不足；生成式CoT推理（类似System2）虽可延长思考链路，但每步都需生成token，延迟高，所有样本均需承担额外推理开销；而在预训练后额外添加的循环结构由于缺少预训练阶段的适配，几乎无收益。
### 方法关键点
- 基于原生预训练的循环Transformer backbone（预训练阶段就加入循环监督信号），替换传统决策模型的固定深度backbone
- 所有循环步共享LoRA适配器和指针头，联合训练所有深度的损失，单个checkpoint支持任意深度推理
- 轻量stopper无标注拟合：仅使用当前步和前一步的输出特征（top概率、类间margin、KL散度等），预测当前结果是否与最深步结果一致，阈值在无标注流量上拟合，无需标注数据
### 关键实验
评测数据集包括JevBench、自建LevBench、Kev系列评测集；对比baseline覆盖Qwen3/3.5系列稠密模型、Kev-0.8B/4B决策模型、级联模型。核心结果：2.6B参数LEV在JevBench上精度从深度1的63.2%提升到深度4的76.2%，提升13个百分点；按需深度设置可节省15%~24%算力，精度损失低于1个百分点；50ms延迟以下场景，1.4B和3B LEV比同延迟稠密模型/级联模型精度高5.4~8.8个百分点。

原生预训练的循环结构可将推理深度变为推理时可调参数，无需维护多套模型即可实现单服务latency-accuracy动态tradeoff
