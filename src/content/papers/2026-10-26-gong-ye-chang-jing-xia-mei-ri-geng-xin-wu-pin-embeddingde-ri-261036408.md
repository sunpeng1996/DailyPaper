---
title: 'Cross-Day Compatibility of Daily Item Embeddings: An Empirical Study of Alignment,
  Scale Management, and CTR Adaptation'
title_zh: 工业场景下每日更新物品embedding的跨日兼容性实证研究
authors:
- Yicheng Wang
affiliations:
- LY Corporation
arxiv_id: '2610.36408'
url: https://arxiv.org/abs/2610.36408
pdf_url: https://arxiv.org/pdf/2610.36408
published: '2026-10-26'
collected: '2026-10-28'
category: RecSys
direction: 推荐系统 · 物品embedding跨日稳定性优化
tags:
- Item Embedding
- CTR Prediction
- Warm Start
- Embedding Alignment
- Industrial Recommendation
one_liner: 系统实证48种物品embedding跨日兼容方案，给出CTR增益最高的工业落地组合
practical_value: '- 改造成本优先的场景，现有每日Word2Vec pipeline可直接加正交对齐（OP），不改变原有训练流程和召回排序，GAUC相对基准提2.6%

  - 可接受状态继承的场景，选用warm start+每日全局重缩放（warm_norm）方案，将8天累计范数涨幅从102.5%压到8.2%，GAUC相对提4.0%，为实测最优

  - 不要盲目追求embedding召回指标，XSimGCL的Recall@100比Word2Vec高76.4%但CTR反而降0.5%，选型必须结合下游任务指标

  - 下游CTR模型可新增共享低维编码器，自动适配embedding残留漂移，多数场景下跨日余弦相似度优于SVD、随机投影等无监督降维方案'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业推荐/广告场景中，每日更新的物品共现embedding（如Item2Vec）会和次日行为数据配对训练CTR模型，同一物品的embedding跨日存在方向、范数漂移，导致多日数据混合训练时特征兼容性差，现有方案缺乏系统性的工业级对比和落地指导。

### 方法关键点
- 对比两种主流embedding生成范式：Word2Vec（SGNS）、适配物品图的XSimGCL
- 覆盖48种配置，包含四大类干预手段：初始化（ID-init，相同物品跨日初始向量一致）、对齐（正交OP/仿射/MLP映射）、训练约束（warm start、范数管控、球面约束）、下游增强（共享编码器、噪声增强）
- 统一以普通Word2Vec为0%基准，所有指标汇报相对百分比变化，避免涉密数据集细节泄露

### 关键结果
- 基线对比：XSimGCL的Recall@100相对Word2Vec高76.4%，但GAUC反而降0.5%，召回指标不能直接等价下游CTR收益
- 上游干预：ID-init让跨日余弦相似度提51.2%、GAUC提2.2%；正交对齐（OP）让余弦提93.4%、GAUC提2.6%
- 范数管控：普通warm start 8天后范数涨幅达102.5%，加每日全局重缩放（warm_norm）后涨幅压到8.2%，GAUC提4.0%，为所有配置最高
- 下游适配：CTR训练的共享编码器在6种上游方案中的4种上取得最高跨日余弦相似度，优于SVD、随机投影等无监督降维

**最值得记住的一句话**：物品embedding的跨日兼容优化需要上游对齐、范数管控、下游任务适配三层结合，几何和召回指标仅能作为漂移筛查用，最终选型必须以下游任务的GAUC/LogLoss为准
