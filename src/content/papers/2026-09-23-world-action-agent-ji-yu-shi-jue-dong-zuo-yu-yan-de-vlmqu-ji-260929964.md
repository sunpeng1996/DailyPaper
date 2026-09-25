---
title: 'World Action Agent: Harnessing VLMs for Robot Manipulation via World Action
  Rehearsal'
title_zh: World Action Agent：基于视觉动作预演的VLM驱动机器人操控框架
authors:
- Yehang Zhang
- Haojian Huang
- Yifan Chang
- Jianchong Su
- Bohan Zhou
- Yingjie Xu
- Wosong Chen
- Tianhao Zhou
- Chenxu Wang
- Tianyi Zhang
affiliations:
- HKUST(GZ)
- CUHK
- Knowin AI
arxiv_id: '2609.29964'
url: https://arxiv.org/abs/2609.29964
pdf_url: https://arxiv.org/pdf/2609.29964
published: '2026-09-23'
collected: '2026-09-25'
category: Agent
direction: 具身Agent · VLM机器人操控多智体协作
tags:
- Embodied Agent
- VLM
- MultiAgent
- Skill Distillation
- Robot Manipulation
one_liner: 提出多Agent视觉动作工作空间，通用VLM无需微调即可控制机器人，SOTA精度75.6%
practical_value: '- 多Agent分角色协作架构可复用：主决策Agent+工具Agent（想象Agent/技能Agent）分工降低主模型推理负担，适合电商导购Agent、推荐多目标决策场景

  - 非参数化技能库构建思路可迁移：从专家演示、人工干预中提取带参考样例的关系型技能，而非硬编码参数，可用于沉淀电商活动规则、推荐运营经验

  - 动作预演+闭环校正机制可复用：决策前做可行性校验、执行后基于反馈快速修正，适合广告投放策略调优、推荐结果重排的动态决策流程

  - 大模型轨迹蒸馏小模型方案可落地：用大模型交互数据LoRA微调小模型，兼顾效果与推理成本，适合业务端大模型驱动的推荐/Agent系统'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
通用VLM具备丰富知识与空间推理能力，但现有机器人操控方案要么间接用VLM生成约束/代码，要么仅给VLM输入场景视图而非可交互动作空间，存在局部交互细节看不清、动作无法提前校验、感知动作空间不统一三大问题；且微调VLM为VLA会损害原模型的通用推理能力。

### 方法关键点
- 视觉动作工作空间设计：自动生成以交互为中心的正交Contact视图，暴露夹爪、物体、目标的局部毫米级空间关系，视图带投影校准可直接映射到3D坐标
- 动作预演机制：每个动作为可编辑提案，由Imagination Agent做仿真预览与可行性校验，修改后再执行，避免不可逆错误
- 闭环校正：观察到的偏移可直接在视图中拖拽修正，自动映射为末端执行器位移，无需额外坐标转换
- 双路径技能习得：非参数路径从专家视频、人工示教中提取带视觉参考的关系型技能库，跨场景可迁移；参数路径用大模型交互轨迹LoRA微调小VLM，降低落地成本

### 关键实验
在LIBERO-Pro机器人操控基准上，基于LIBERO-90习得技能的WAA平均成功率达75.6%，超过此前SOTA方案ASPIRE的72.0%；技能零样本迁移到robosuite仿真环境平均成功率达100%；用交互轨迹微调Qwen3.5-9B，域外成功率从1.7%提升到43.3%，单episode推理成本仅为同类视觉Agent方案Show-Harness的40%。

**最值得记住的一句话**：无需修改VLM本身，仅通过优化模型的观察输入与决策生效机制，就能充分释放通用大模型的空间推理能力完成复杂具身任务。
