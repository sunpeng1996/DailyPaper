---
title: Train An Imaginative Agent
title_zh: 具备想象力的Agent训练框架Agima
authors:
- Jiaxin Ge
- Junyi Zhang
- Tianning Chai
- Hanjun Yoo
- Chenyang Wang
- Xiuyu Li
- Weijia Shi
- XuDong Wang
- Sewon Min
- Luke Zettlemoyer
affiliations:
- UC Berkeley
- Impossible Research
- University of Washington
- Duke University
arxiv_id: '2610.26845'
url: https://arxiv.org/abs/2610.26845
pdf_url: https://arxiv.org/pdf/2610.26845
published: '2026-10-19'
collected: '2026-10-21'
category: Agent
direction: Agent决策 · 多模态想象规划
tags:
- Agent
- Multimodal
- SFT
- RL
- World Model
one_liner: 提出Agima训练框架，让多模态Agent执行前想象未来状态、自适应规划决策
practical_value: '- 电商/广告不可逆决策场景（如大促预算分配、冷启动item推流）可复用两阶段训练范式：先通过SFT教基础规则和预判逻辑，再通过RL让模型自适应优化策略，降低实环境试错成本

  - 多模态Agent规划可复用「统一模型同时承担策略+世界模型」的架构设计，无需拆分多个独立模块，降低工程落地复杂度，真实/想象状态统一接口可灵活切换

  - 长序列决策场景可借鉴三种想象模式：线性滚动降本、反事实分支在关键决策点筛除死路、前瞻思考对比多路径选最优，比如推荐系统的召回链路多策略对比

  - RL优化时可复用GRPO仅优化推理文本token的设计，生成的状态/预测结果保留为上下文，大幅降低训练算力开销同时保留决策依据'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有Agent决策高度依赖实时环境反馈，试错成本高，且不可逆动作一旦出错损失无法回滚，在低反馈、高风险决策场景（如广告投放、推荐策略调整）泛化能力差，需要具备执行前预判动作后果的规划能力，减少实环境交互成本。

### 方法关键点
- 基于统一多模态Omni模型，同时承担策略（生成动作）和世界模型（生成动作后的视觉状态）职责，真实观测与想象状态接口统一可互换，支撑连续规划
- SFT阶段通过三类轨迹训练基础想象能力：线性滚动（单条路径逐步预测状态）、反事实分支（关键节点试备选动作筛除死路）、前瞻思考（多路径全链路对比选最优）
- RL阶段用GRPO仅优化推理文本token，仅提供任务成功二元奖励，无需额外轨迹标注，让模型自适应学会什么时候需要调用想象、什么时候直接执行

### 关键实验
在Maze2D、Sokoban、Pacman、PushT四个决策任务上，训练用简单样本、测试用未见过的难样本，对比GPT-5.6、Gemini 3.1 Pro、Qwen系列VL模型、无想象同基线模型。核心结果：仅SFT阶段，Sokoban从2箱训练泛化到4箱测试，每5步获取一次真实反馈时成功率40%，是无想象基线（2%）的20倍；Pacman前瞻思考模式比线性滚动成功率最高提升32个百分点；RL后模型自适应将80%以上的反事实分支集中在关键决策点，不额外增加想象预算。

### 核心结论
能预判动作后果、按需调用想象能力的Agent，在低反馈、不可逆动作场景的泛化能力远高于仅靠动作规划的模型。
