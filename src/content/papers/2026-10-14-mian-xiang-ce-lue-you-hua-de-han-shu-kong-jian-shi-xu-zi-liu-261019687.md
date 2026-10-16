---
title: Function-Space Temporal Self-Distillation for Policy Optimization
title_zh: 面向策略优化的函数空间时序自蒸馏方法
authors:
- Aryan Das
- Arnab Bhattacharya
- Vinay Kumar Verma
affiliations:
- Indian Institute of Technology Kanpur
arxiv_id: '2610.19687'
url: https://arxiv.org/abs/2610.19687
pdf_url: https://arxiv.org/pdf/2610.19687
published: '2026-10-14'
collected: '2026-10-16'
category: Training
direction: 大模型训练 · 自蒸馏策略优化
tags:
- Self-Distillation
- Policy Optimization
- RLHF
- Memory Efficiency
- Temporal Consolidation
one_liner: 提出单策略自蒸馏框架FSPO，无需EMA教师，提精度同时降20%显存开销
practical_value: '- 做电商导购Agent、工具调用Agent的RL微调时，可替换现有SDPO/GRPO方案，7B/8B级模型可省20%左右显存，同时平均准确率提升4个点，无需额外存储EMA教师模型

  - 函数空间存储历史分布的思路可复用：做推荐系统多场景持续微调时，不存历史模型快照，仅存稀疏token分布做回放，既稳定训练目标，又降低灾难性遗忘

  - 可靠性自适应监督逻辑可迁移到冷门query/冷门商品推荐优化：当模型在某类样本上反复出错时自动提升标注样本监督权重，效果稳定后逐步降低，平衡泛化与精度

  - 质量+覆盖度双维度的记忆筛选策略，可直接用到RAG片段召回、用户行为序列缓存中，避免重复存储相似样本，提升缓存利用率'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
RLVR已成为LLM post-training的主流范式，但标量奖励存在严重的信用分配问题；现有自蒸馏方法SDPO依赖动态演化的自教师，存在跨迭代目标漂移问题，且需要额外存储EMA教师模型，显存开销随模型规模线性上涨，大模型训练成本居高不下。

### 方法关键点
- 函数空间时序固化：不存储历史模型参数快照，仅留存稀疏的历史next-token分布作为固定训练目标，完全消除EMA教师带来的显存开销
- 特权分歧定向校正：识别无辅助策略严重高估但特权视角（带成功样本上下文）拒绝的token，显式施加惩罚，提供比分布匹配更精准的定向监督信号
- 可靠性自适应接地：根据模型在单个问题上的历史平滑成功率，动态调整标注参考样本的监督权重，模型反复失败时增强监督，效果稳定后逐步降低权重
- 质量+覆盖度双维度时序记忆：筛选存储差异化的成功轨迹，回放时均匀采样不同结构的样本，避免重复学习相似模式，降低跨任务遗忘

### 关键结果
在SciKnowEval的化学、物理、生物、材料4个科学推理数据集+ToolAlpaca工具调用数据集上测试，对比GRPO、SDPO等SOTA基线，5小时训练预算下平均准确率较最强基线高4个百分点，Olmo3-7B-Instruct峰值显存从约70GB降至56GB，同时跨任务保留能力优于所有基线，训练后期单步耗时随效果提升逐步降低。

最值得记住的一句话：时序知识无需通过保存完整模型快照保留，存储稀疏的函数空间输出即可实现更高效、更稳定的自蒸馏训练。
