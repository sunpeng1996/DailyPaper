---
title: 'VisualPatchWorld: Code World Models as Latent Structured Representations for
  Planning'
title_zh: VisualPatchWorld：面向规划的代码化结构化隐表示世界模型
authors:
- Jiaxin Bai
- Jiaxuan Xiong
affiliations:
- Hong Kong Baptist University
arxiv_id: '2607.25236'
url: https://arxiv.org/abs/2607.25236
pdf_url: https://arxiv.org/pdf/2607.25236
published: '2026-07-27'
collected: '2026-07-29'
category: Agent
direction: Agent 代码化世界模型规划优化
tags:
- World_Model
- Program_Induction
- Model_Predictive_Control
- Planning
- Latent_Representation
one_liner: 提出双阶段代码世界模型归纳框架，较最优基线规划成功率提升23.5个百分点
practical_value: '- 双阶段归纳（先选定性结构再拟合参数）可迁移到用户行为建模：先锁定用户消费/点击的定性规律（如大促触发、周度周期）再拟合参数，比端到端黑箱模型可解释性更强，出错时可快速定位结构问题

  - 混合打分策略可直接复用在推荐/搜索链路：用低成本模型（如LR、小MLP）粗排全量候选，再用高精度模型（如大模型、规则引擎）仅校验top30%候选，兼顾效率和效果，比全量精排节省70%以上算力

  - 做电商场景智能Agent（如仓储调度、直播话术规划、售后决策）时，可复用代码化世界模型的可编辑特性，决策逻辑出错时直接修改规则模板，无需全量重训模型'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有世界模型分为两类：神经隐式模型数据驱动易扩展，但动力学逻辑隐式不可解释，出错难以修复；手写物理引擎逻辑明确，但构建成本高、泛化性差。已有的代码化世界模型大多仅优化单步预测精度，未适配长序列规划需求，实际决策效果差。

### 方法关键点
- 双阶段程序归纳：Level1通过主动探测从预设候选集中选择符合场景的动力学定性结构（如接触力驱动、线性导航等），Level2基于多步rollout损失拟合结构的自由参数，输出可直接执行的Python代码作为世界模型。
- 三层感知适配：支持oracle（仿真状态直读）、CV工具（从RGB提取结构化场景图）、VLM（输出语义场景图）三种状态输入，适配不同场景的感知精度要求。
- 混合规划策略：用代码化世界模型对所有候选动作序列打分，可选仅调用高精度物理引擎重排top30%的高潜候选，大幅降低算力开销。

### 关键结果
在LeWM基准的4个控制任务（导航、机械臂到达、推物、3D立方体操作）上测试，VPW平均规划成功率达69.0%，较最优代码世界模型基线高出23.5个百分点；开启混合打分后平均成功率达95.0%，接近物理引擎97.5%的效果天花板，同时减少70%的物理引擎调用量。

### 核心结论
对于需要可解释、可调试决策逻辑的场景，先选对定性动力学结构再拟合参数的思路，效果远好于盲目端到端拟合。
