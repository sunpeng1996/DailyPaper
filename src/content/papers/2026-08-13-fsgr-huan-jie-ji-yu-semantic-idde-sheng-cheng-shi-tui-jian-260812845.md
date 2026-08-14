---
title: 'FSGR: Mitigating Token Frequency Bias for Fair SID-Based Generative Recommendation'
title_zh: FSGR：缓解基于Semantic ID的生成式推荐的令牌频率偏差
authors:
- Yuchen Zheng
- Sihan Xu
- Jingwen Yang
- Xiangrui Cai
- Haiwei Zhang
- Xiaojie Yuan
affiliations:
- Nankai University
arxiv_id: '2608.12845'
url: https://arxiv.org/abs/2608.12845
pdf_url: https://arxiv.org/pdf/2608.12845
published: '2026-08-13'
collected: '2026-08-14'
category: GenRec
direction: 生成式推荐 · Semantic ID公平优化
tags:
- Semantic ID
- Generative Recommendation
- Fairness
- Token Frequency Bias
- RQ-VAE
- LoRA
one_liner: 提出SID构造到训练的全链路公平优化框架，保精度前提下Gini公平性平均提升超20%
practical_value: '- SID构造阶段可复用OTA最优传输正则+DCR死码重锚定方案，提升码本利用率到接近100%，从源头降低频率偏差，无需修改下游训练逻辑即可部分缓解长尾曝光问题

  - LLM微调阶段可直接复用Hierarchical Frequency Calibration（HFC）层粒度校准策略，按SID层级语义粒度分配校准强度：粗粒度层少校准保精度，细粒度层高校准提公平，无额外推理开销

  - 两阶段训练范式可直接迁移到所有SID-based生成式推荐场景：第一阶段用标准交叉熵做语义对齐，第二阶段用LoRA做公平性微调，避免全量训练的精度损失，平衡效果和训练成本

  - 评估侧可引入SID令牌级Gini系数作为公平性指标，比传统物品曝光Gini更细粒度，能提前定位码本不平衡问题，避免长尾偏差在下游被放大'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有基于Semantic ID的生成式推荐存在被忽略的令牌频率偏差：高频SID令牌被过度预测、低频令牌被低估，导致曝光向头部品类集中，形成「富者越富」的反馈循环，劣化长尾商品曝光公平性。该偏差来自两个环节：一是SID构造阶段码本天然不平衡，宽语义范畴的令牌被大量复用；二是训练阶段的流行度偏差+MLE损失放大高频信号，现有去偏方法未考虑SID的分层语义特性，直接迁移效果差。

### 方法关键点
- **SID构造模块**：提出Balanced Semantic Quantization（BSQ）：① 用OT-based Assignment Optimization（OTA）将每个batch的量化过程建模为最优传输问题，通过KL散度约束软分配对齐均匀分布的传输计划，提升码本整体利用率；② 用Dual-Criteria Re-anchor（DCR）机制定期识别死码，分别锚定到特征空间空洞区域和高密区域，同时补全稀疏区域、缓解拥挤区域的表示压力。
- **训练模块**：采用两阶段策略：① 第一阶段用标准交叉熵训练LLM完成用户行为到SID序列的语义对齐；② 第二阶段用Hierarchical Frequency Calibration（HFC）做公平性微调，对不同SID层按粒度分配校准强度（层越深校准强度越高），通过对数频率先验校准预测logits，缓解预测偏差。

### 关键实验结果
在Amazon 3个公开数据集（Luxury Beauty、Industrial and Scientific、Software）上，对比RQ-VAE、QuaSID等SID构造方法，以及MiLe、WAKL等LLM去偏方法，适配TIGER、Llama3.1-8B、Qwen3-8B三种backbone：平均Gini公平性提升超20%，码本覆盖率接近100%，码本Gini最多降低43.1%，推荐精度（Recall、NDCG）与基线持平甚至略有提升。

### 核心结论
SID-based生成式推荐的公平性优化需要从码本构造和训练阶段全链路协同，分层语义特性是设计去偏策略时不可忽略的核心前提
