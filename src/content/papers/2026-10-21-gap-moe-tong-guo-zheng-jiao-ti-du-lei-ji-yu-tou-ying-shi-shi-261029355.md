---
title: 'GaP-MoE : Explicit Expert Specialization in Mixture-of-Experts via Orthogonal
  Gradient Accumulation and Projection'
title_zh: GaP-MoE：通过正交梯度累积与投影实现MoE显式专家专业化
authors:
- Donghyun Jeong
- Yoon-Yeong Kim
affiliations:
- 首尔大学
arxiv_id: '2610.29355'
url: https://arxiv.org/abs/2610.29355
pdf_url: https://arxiv.org/pdf/2610.29355
published: '2026-10-21'
collected: '2026-10-22'
category: Training
direction: MoE训练优化 · 专家专业化
tags:
- MoE
- Expert Specialization
- Gradient Projection
- Representation Collapse
- Training Optimization
one_liner: 提出基于梯度投影的MoE专家专业化方法 无额外损失 缓解表征坍塌 兼容现有架构
practical_value: '- 电商/推荐场景的多兴趣、多场景MoE建模可直接复用这套梯度投影机制，替换原有的同质化抑制辅助损失，避免与排序/召回任务目标冲突

  - 对于流量波动大、路由策略不稳定的业务场景，GaP-MoE在路由失效时仍可保证专家差异化，提升MoE推荐模型的鲁棒性

  - 工程实现成本极低：仅需在梯度反传后增加投影逻辑，无需额外前向/后向计算，可直接作为drop-in模块兼容现有MoE架构

  - 调参可直接复用论文经验：优先在Transformer高层（梯度一致性更高）应用，初始1 epoch线性提升投影强度α从0.1到1，降低训练初期噪声影响'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
稀疏MoE是大模型、推荐系统扩容提效的核心技术路径，但普遍存在专家表征坍塌问题：多专家功能同质化导致模型容量浪费，现有优化方案要么修改路由逻辑仍易出现路由坍塌，要么新增辅助损失易与原任务优化目标冲突，缺乏兼顾效率和有效性的专家专业化方案。
### 方法关键点
- 动态leader选择：对每个token的TopK路由专家，按归一化路由得分采样1个leader，保留其原始任务梯度，其余选中专家为follower
- 梯度正交投影：当follower与leader的历史梯度基余弦相似度超过阈值γ时，将follower梯度投影到leader历史梯度子空间的正交补集，消除更新方向重叠
- 梯度累积缓冲：每个专家独立维护梯度缓冲区，仅以leader身份获得的梯度通过Gram-Schmidt过程生成正交基，按FIFO策略更新，避免投影后的梯度污染缓冲
### 关键实验
- 微调场景：基于BERT在GLUE benchmark上比基线SMoE平均得分高0.1个点
- 从零预训练场景：基于GPT-2在WikiText-103上perplexity从78.8降至76.5，enwik8 BPC从2.005降至1.953
- 鲁棒性验证：完全随机路由无训练时，GaP-MoE比基线SMoE在WikiText-103上PPL低2.28
- 兼容性验证：作为drop-in模块接入XMoE、SimSMoE后可进一步提升各任务表现
### 核心结论
通过直接修正专家梯度而非新增辅助损失的方式实现专业化，是兼顾MoE训练效率和专家差异化的高性价比路径。
