---
title: Agentic Reinforcement Learning with Observation-Calibrated Self-Distillation
title_zh: 基于观测校准自蒸馏的智能体强化学习方法
authors:
- Yi Yang
- Cong Qin
- Xiaodan Liu
- Chishui Chen
- Qing Dong
- Yan Zhang
- Cao Liu
- Zhao Yang
- Lu Pan
- Jiaye Lin
affiliations:
- Meituan LongCat Interaction
- Nanjing University
- Peking University
- McMaster University
- Fudan University
arxiv_id: '2608.04788'
url: https://arxiv.org/abs/2608.04788
pdf_url: https://arxiv.org/pdf/2608.04788
published: '2026-08-05'
collected: '2026-08-06'
category: Agent
direction: LLM Agent 强化学习训练优化
tags:
- Reinforcement Learning
- GRPO
- Self-Distillation
- LLM Agent
- Credit Assignment
one_liner: 提出观测校准自蒸馏OCSD，消除重放支架得分偏移，为GRPO提供精准token级更新信号
practical_value: '- 训练电商导购/搜索Agent时，可复用双视角重放设计，分离未来观测反馈和重放格式带来的得分偏移，避免自蒸馏引入的噪声

  - 复用NLL引导的高不确定性步骤选择策略，仅对模型拿不准的交互步骤做token级增益调整，既提效又避免全量校准引入的噪声

  - 做GRPO训练优化时，可保留轨迹级奖励的更新方向，仅用自蒸馏信号调整token级更新强度，兼顾全局奖励导向和局部细粒度监督

  - 工程上OCSD仅额外增加1.4%的训练开销，不需要修改GRPO主流程，可低成本集成到现有Agent训练管线中'
score: 9
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM Agent强化学习主流方法GRPO采用全局轨迹级奖励更新所有token，无法区分不同token对任务的贡献；On-Policy Self-Distillation（OPSD）通过特权重放视图生成token级监督，但存在混淆问题：重放得分变化同时包含未来观测的有效信息和重放支架本身带来的偏移，尤其当未来观测作为特权信息时，支架偏移影响更大，导致监督信号不准。

### 方法关键点
- 构造结构完全匹配的双重视图：Full视图包含真实未来观测+未来动作schema，Observation-Ablated视图仅把未来观测替换为固定占位符，其余重放格式、支架完全一致
- 计算两个视图的token得分差作为观测残差，抵消重放支架带来的共同得分偏移，仅保留未来观测带来的有效信号
- 用NLL筛选单条轨迹中top 20%高不确定性步骤，仅对这些步骤的token用残差信号调整GRPO的更新强度，保留原轨迹级奖励的更新方向

### 关键结果
在ALFWorld、WebShop、SearchQA三个Agent基准，用1.7B/4B/8B三个规模的Qwen3模型测试，对比GRPO、GRPO+OPSD、RLSD、SDAR等基线：ALFWorld上8B模型OCSD成功率达87.2%，比GRPO高14个点；WebShop上8B模型OCSD成功率达78.1%，比GRPO高2.6个点；SearchQA上8B模型OCSD平均EM达49.1%，OOD EM达50.6%，泛化性最优；训练额外开销仅1.4%，远低于常规GRPO训练成本。

最值得记住的一句话：做Agent自蒸馏时不要直接用重放视图的得分变化做监督，控制变量消除重放支架本身的偏移，才能获得真正和环境反馈对齐的细粒度信号。
