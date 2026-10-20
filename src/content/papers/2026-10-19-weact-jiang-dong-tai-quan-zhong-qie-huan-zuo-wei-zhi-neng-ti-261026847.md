---
title: 'WeAct: Dynamic Weight Switching as Agent Actions'
title_zh: WeAct：将动态权重切换作为智能体动作的能力调度框架
authors:
- Rui Shi
- Xunjian Yin
- Jiacheng Sang
- Zichuan Liu
- Shuyan Zhou
affiliations:
- Carnegie Mellon University
- Duke University
- Meta MSL
arxiv_id: '2610.26847'
url: https://arxiv.org/abs/2610.26847
pdf_url: https://arxiv.org/pdf/2610.26847
published: '2026-10-19'
collected: '2026-10-20'
category: Agent
direction: Agent 模块化能力调度与持续学习
tags:
- LoRA
- Agent
- Catastrophic Forgetting
- Continual Learning
- Tool Calling
one_liner: 将LoRA适配器选择纳入智能体动作空间，实现模块化能力调用与无遗忘持续适配
practical_value: '- 可复用「能力拆分独立训练LoRA + 工具调用式动态切换」架构，解决推荐Agent多场景（召回/排序/文案生成）能力冲突、灾难性遗忘问题，无需全量重训

  - 对明确分阶段的业务任务（比如电商大促活动策划：需求拆解→选品→文案生成）可采用WeAct-hard固定流程切换LoRA保证稳定性；复杂模糊任务用WeAct-soft自适应调度提升灵活性

  - 新增业务能力仅需训练对应LoRA插入能力库，不影响原有模块性能，适合电商场景快速迭代新需求（如新增价格计算、合规校验能力），大幅降低迭代成本

  - 切换LoRA时仅需重建当前上下文KV cache，整体延迟低于全量微调模型，可直接落地到线上低延迟要求的推荐Agent场景'
score: 9
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
长周期智能体需要在不同任务阶段调用异构能力，传统全量微调或静态LoRA融合存在两大核心痛点：一是共享参数更新会导致灾难性遗忘，此前习得的能力易被后续更新侵蚀；二是静态融合得到的固定权重无法适配不同阶段的专业化需求，拉低各阶段能力表现，同时Prompt级能力调用还会额外占用上下文窗口。

### 方法关键点
- 冻结大模型主干，为不同能力独立训练专属LoRA适配器，每个适配器仅在对应任务阶段的样本上训练，梯度互不干扰，从根源避免灾难性遗忘
- 将`load_lora`、`offload_lora`作为内置工具加入智能体动作空间，复用原生工具调用接口实现动态LoRA切换，无需额外训练路由模块
- 提供两种调度策略：WeAct-hard按固定流程强制切换适配器，适配流程明确的任务保证稳定性；WeAct-soft由模型根据上下文自主选择适配器，适配复杂开放任务保证灵活性

### 关键结果
基于QWEN3-32B测试，覆盖8个深度研究基准数据集，对比全量微调、单LoRA、静态LoRA融合（TIES/DARE-TIES/TSPA）、多Agent编排等基线：WeAct-hard平均准确率达45.47%，相对全量微调提升6.2%，相对最强静态LoRA融合方法提升27.5%，训练计算量低于全量微调，推理延迟比全量微调低20.3%；新增代码能力LoRA、迭代更新写作能力LoRA时，完全不影响原有其他能力的表现。

### 核心启示
按能力边界拆分独立LoRA+运行时动态切换的架构，是兼顾智能体多能力表现、避免灾难性遗忘、支持低成本持续迭代的高性价比路径。
