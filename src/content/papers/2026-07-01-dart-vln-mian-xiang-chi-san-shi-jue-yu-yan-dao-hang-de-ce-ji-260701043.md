---
title: 'DART-VLN: Test-Time Memory Decay and Anti-Loop Regularization for Discrete
  Vision-Language Navigation'
title_zh: DART-VLN：面向离散视觉语言导航的测试时记忆衰减与反循环正则
authors:
- Shaoheng Zhang
- Zhichen Li
- Jie Mei
affiliations:
- 哈尔滨工业大学（深圳）
arxiv_id: '2607.01043'
url: https://arxiv.org/abs/2607.01043
pdf_url: https://arxiv.org/pdf/2607.01043
published: '2026-07-01'
collected: '2026-07-03'
category: Agent
direction: Embodied Agent · VLN 测试时优化
tags:
- VLN
- Test-Time Optimization
- Memory Control
- Anti-Loop Regularization
- Embodied Agent
one_liner: 无需训练的测试时VLN框架，通过记忆衰减和反循环正则提升导航性能与效率，无新增参数
practical_value: '- 对于已上线的冻结骨干模型（推荐排序大模型、对话Agent、导购Agent），可直接在推理侧添加轻量规则优化效果，无需重新训练，迭代成本极低

  - 记忆衰减的三维加权策略可直接复用：用时间间隔、访问频次、特征新颖度给用户历史行为、会话记忆加权，仅修改读侧逻辑无需改动存储结构

  - 反循环正则思路可迁移到推荐去重、对话Agent避免重复提问、路径规划类Agent避免无效回溯，仅在候选得分阶段加惩罚即可实现，无额外推理开销'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
记忆型离散VLN Agent基于冻结骨干推理时普遍存在两类失效问题：一是记忆读取阶段陈旧、冗余的历史证据会干扰当前决策，二是动作选择阶段频繁的局部回溯会拉长轨迹、升高耗时。现有优化方案大多需要重新训练模型或重构整体架构，无法低成本增强已上线的成熟VLN系统。
### 方法关键点
- 测试时记忆衰减：仅在记忆读取侧对每个记忆槽按三个维度动态加权，不修改存储的记忆内容：① 按槽龄做指数衰减，惩罚长时间未更新的陈旧记忆；② 按访问次数惩罚重复观测的低信息密度记忆；③ 按特征新颖度（相邻更新的余弦相似度变化）奖励仍有信息增益的记忆，最终权重做限幅防止过修正。
- 反循环正则：仅在动作选择前对候选动作得分加轻量惩罚：① 对立即返回上一节点的回溯动作加罚；② 对访问次数超过2次的节点加罚，仅修改候选得分，不改动模型结构。
- 整体框架无新增可学习参数，完全不修改冻结的VLN骨干模型，对现有推理流程侵入性极低。
### 关键结果
在R2R、REVERIE两个主流VLN基准上以GridMM为基线验证：
- R2R test unseen 集上，相比基线SR提升1pp，SPL提升1pp，轨迹长度缩短4.4%，runtime降低42.5%；
- REVERIE val unseen 集上，RGSPL提升0.88pp，runtime降低65.4%；
- 反循环正则可将立即回溯率降低约30%，有效减少无效动作。
> 最值得记住：对于已成熟的冻结骨干模型，适度、边界清晰的测试时轻量控制，往往比激进的内存改写或架构重构收益更稳定、落地成本更低。
