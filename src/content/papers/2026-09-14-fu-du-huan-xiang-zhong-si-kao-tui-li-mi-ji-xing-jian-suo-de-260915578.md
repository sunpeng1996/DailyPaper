---
title: 'The Magnitude Mirage: Rethinking Confidence for Reasoning-Intensive Retrieval'
title_zh: 《幅度幻象：重思考推理密集型检索的置信度评估》
authors:
- Jamie Holdcroft
- Abdelrahman Abdallah
- Adam Jatowt
affiliations:
- UNSW Sydney
- University of Innsbruck
arxiv_id: '2609.15578'
url: https://arxiv.org/abs/2609.15578
pdf_url: https://arxiv.org/pdf/2609.15578
published: '2026-09-14'
collected: '2026-09-16'
category: RAG
direction: RAG系统 · 检索置信度优化
tags:
- RAG
- Query Performance Prediction
- Retrieval Confidence
- Zero-cost Optimization
- Reasoning-intensive Retrieval
one_liner: 提出用检索分数分布信号替代原始相似度阈值，零成本提升推理场景RAG弃权性能
practical_value: '- 现有RAG管线可直接替换相似度阈值逻辑：用Score Gap（s1−s_k）或LSMV替代MaxScore阈值，无额外推理、训练成本，零延迟

  - 电商/客服场景的推理类Query（如带时间、属性约束的商品咨询）优先用分布类置信度，可避免召回语义相近但违反约束的文档，降低大模型幻觉

  - 推荐系统语义召回环节可复用该逻辑：对top-k召回分数做分布统计，识别低置信度召回请求，触发兜底策略或降级流程

  - 无需纠结分布类指标选型：从幅度切换到分布的增益是不同分布指标差异的5~10倍，Score Gap和LSMV为最优默认选择'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业界RAG系统普遍通过原始检索相似度阈值做弃权判断，默认分数幅度等同于置信度，但在需要逻辑、时间推理的查询场景下，召回器常给语义相近但违反约束的文档打高分，导致阈值几乎失效（幅度幻象），而LLM做召回校验成本过高，亟需零成本优化方案。

### 方法关键点
- 基于Query Performance Prediction（QPP）框架，对比6种零成本置信度指标：基线MaxScore（s1）、Score Gap（s1−s_k）、Top-k标准差、归一化查询承诺（NQC）、最大迭代标准差、线性化分数幅度方差（LSMV）
- 覆盖三类认知层级检索任务：语义匹配（BEIR）、逻辑推理（BRIGHT）、时间推理（TEMPO），共28个数据集、11种检索架构（稀疏、稠密、推理增强编码器）
- 以二进制检索成功（top-k存在至少1条相关文档，对应RAG下游生成要求）的AUROC为核心评估指标

### 关键结果
- 推理场景下MaxScore阈值接近随机表现：BRIGHT逻辑推理数据集上所有检索模型的MaxScore AUROC仅0.52~0.61，基本无判别能力；TEMPO时间推理数据集上部分模型MaxScore AUROC低至0.536
- 分布类指标最多提升AUROC 0.16：Score Gap和LSMV在BRIGHT上相对MaxScore提升0.06~0.091，在TEMPO上最多提升0.125，在BEIR语义数据集上最多提升0.158
- 端到端RAG验证：10%覆盖率下，Score Gap相对MaxScore将回答准确率从65.8%提升至74.1%，无额外成本

**最值得记住的一句话**：从依赖分数幅度切换到依赖分数分布带来的增益，是不同分布类指标之间差异的5~10倍，优先做范式切换而非纠结具体指标选择
