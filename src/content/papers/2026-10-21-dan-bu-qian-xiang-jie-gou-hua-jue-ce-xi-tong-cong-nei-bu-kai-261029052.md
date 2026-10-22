---
title: 'Our Own Jev: Typed Decisions in One Forward Pass, from an In-House Judge to
  Open LoRA Models'
title_zh: 单步前向结构化决策系统：从内部Judge到开源LoRA模型
authors:
- Yuchuan Weng
- Chi Liu
- Xin Chen
- Srinivasan Manoharan
affiliations:
- PayPal.AI
arxiv_id: '2610.29052'
url: https://arxiv.org/abs/2610.29052
pdf_url: https://arxiv.org/pdf/2610.29052
published: '2026-10-21'
collected: '2026-10-22'
category: LLM
direction: 大模型结构化决策 · LoRA低成本落地
tags:
- LoRA
- Typed Decision
- LLM Judge
- Inference Optimization
- Low Cost Deployment
one_liner: 实现两类单步前向结构化决策方案，成本仅为传统大模型Judge的1%，性能对标商用系统
practical_value: '- 电商/推荐/Agent场景下的低延迟分类需求（如训练数据标注、用户意图识别、商品合规审核、广告素材打标）可直接复用该架构：冻结大模型骨干+低秩LoRA+单步前向读logits，无需生成文本，成本降99%，且数据完全不出域，适合敏感业务场景

  - 无需额外新增分类头，直接读取大模型原生输出层的选项字母logits即可达到接近商用系统的性能，省去新增参数的训练和部署成本，2B量级小模型即可满足大部分业务需求，适合低资源、端侧部署场景

  - 仅需25K左右的领域标注样本即可训练出可用的LoRA适配器，无需全量微调，适合业务快速迭代试错，例如临时活动的文案分类、大促期间的临时合规审核等场景

  - 样本量<200的小测试集无法检测到10个点以内的性能差异，业务上线前需积累至少千级的领域测试集，避免误判不同方案的实际效果'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有固定选项的结构化决策任务（如数据标注、意图分类、合规审核）普遍采用System 2范式：调用大模型生成结构化输出再解析，不仅成本高、延迟高，还容易出现格式错误；商用API还存在数据泄露风险，无法满足内部私有数据场景的需求。
### 方法关键点
- 内部Judge方案：基于kev架构，冻结4B/27B Qwen骨干，新增rank 16 LoRA适配器与指针头，单步前向即可同时输出多个分类问题的概率，无需生成任何文本
- 开源无参数方案：复用Eikos训练范式，不新增任何参数，直接读取LoRA微调后大模型输出层的选项字母logits，经softmax得到分类概率，单步支持最多26类，更多类别可通过锦标赛方式实现
- 训练优化：采用软交叉熵做知识蒸馏，增加辅助rationale损失，每个样本随机打乱选项顺序避免标签偏置
### 关键结果
- 内部Agent编码会话标注场景：148K条数据全量处理成本从前沿大模型Judge的约$1000降到不到$10，耗时从73小时降到7个A100小时，与大模型标签的匹配度：二分类任务83%~92.5%，8分类任务68%~69.5%
- 公开JevBench硬集测试：35B MoE模型准确率79.3%，与商用Jev系统（73%）无显著统计差异；2B模型准确率61.3%，超过所有kev系列开源 checkpoint
- 消融实验：额外训练输出层的26个字母行无可测量的性能提升，111条样本的小测试集无法区分10个点以内的性能差异

固定选项分类决策场景下，单步前向读logits的System 1方案相比生成式System 2方案成本低两个数量级，性能足够满足业务需求，是落地首选
