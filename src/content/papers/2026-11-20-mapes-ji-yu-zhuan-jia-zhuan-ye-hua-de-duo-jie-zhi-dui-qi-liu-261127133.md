---
title: 'MAPES: Multi-Value Alignment Pipeline via Expert Specialization'
title_zh: MAPES：基于专家专业化的多价值对齐流水线
authors:
- SungHo Kim
- SangKeun Lee
affiliations:
- Korea University, Seoul, South Korea
arxiv_id: '2611.27133'
url: https://arxiv.org/abs/2611.27133
pdf_url: https://arxiv.org/pdf/2611.27133
published: '2026-11-20'
collected: '2026-11-23'
category: LLM
direction: LLM多价值偏好对齐
tags:
- DPO
- Multi-Value Alignment
- LoRA
- Model Merging
- Preference Optimization
one_liner: 通过分价值专家独立训练、偏好感知合并与后调和，解决LLM多价值对齐的跨维度冲突
practical_value: '- 电商/推荐多目标优化场景（如兼顾CTR、CVR、内容合规、用户体验）可借鉴分目标训练专属LoRA专家的思路，仅拆分数据集无需复制，训练成本增加极低，还能避免共享参数下的目标冲突

  - 多专家合并时可复用PAVM的核心设计：引入参数delta与目标优化梯度方向的对齐度作为合并权重，比传统基于参数大小的合并（如TIES、Task Arithmetic）更适配偏好类目标的能力整合

  - 合并后的轻量调和步骤性价比极高：仅用1 epoch的DPO+专家集成KL蒸馏，就能解决参数合并带来的分布偏移问题，带来2~3个点的效果提升，无需额外数据

  - 若业务有多维度的反馈数据，可优先按单样本的目标区分度路由到对应专家训练，比混合所有数据训练的多目标模型效果更优；无细粒度标注时可先用强LLM打伪标签拆分数据'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有LLM偏好对齐方法（包括DPO及其多目标变体）均在共享参数空间优化，多价值维度（如指令遵从、诚实、有用、真实）存在天然冲突，优化单一维度往往会损害其他维度的表现，无法同时满足多维度对齐要求。

### 方法关键点
- 四阶段冲突感知流水线：1）数据路由：每个样本按各价值的得分差分配给区分度最高的价值组，过滤无明确偏好样本并平衡各分组数据量；2）专家训练：每个价值组训练独立的LoRA适配器，用带得分差和排他性权重的DPO损失优化，避免跨价值梯度干扰；3）PAVM合并：先剪枝保留专家参数的高影响delta，再按符号投票确定合并符号，最后用参数delta与对应价值偏好改进方向的对齐度作为加权系数，仅保留正对齐分量；4）后调和：用DPO损失+专家集成分布的KL蒸馏轻量训练，解决合并后的分布偏移。

### 关键结果
基于UltraFeedback数据集训练，对比DPO、CDPO、MODPO等6个强基线，在4个不同规模骨干模型上，5个偏好对齐基准的平均得分比最强基线高1.7~3.6个点，推理能力（GSM8K、GPQA）无明显下降，还能泛化到未训练的无害性价值，最大提升21.1个点，全流程仅比标准DPO多15~19%的GPU耗时。

> 最值得记住的话：多价值对齐的核心是从架构层面分层解决不同阶段的冲突，而非将冲突揉进单一损失函数靠权重调优解决
