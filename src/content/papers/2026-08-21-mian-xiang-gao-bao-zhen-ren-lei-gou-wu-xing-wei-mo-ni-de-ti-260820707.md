---
title: Towards Faithful Simulation of Human Shopping Behavior
title_zh: 面向高保真人类购物行为模拟的GUI智能体RecVerse与基准数据集
authors:
- Jiakai Tang
- Yan Mi
- Jing Yu
- Yang Zhang
- See-Kiong Ng
- Qi Cao
- Fei Sun
- Xu Chen
- Wen Chen
- Jian Wu
affiliations:
- Renmin University of China
- University of Chinese Academy of Sciences
- National University of Singapore
- Alibaba Group
arxiv_id: '2608.20707'
url: https://arxiv.org/abs/2608.20707
pdf_url: https://arxiv.org/pdf/2608.20707
published: '2026-08-21'
collected: '2026-08-24'
category: Agent
direction: 电商用户模拟 Agent 架构优化
tags:
- User Simulation
- GUI Agent
- Reinforcement Learning
- Memory System
- Recommender Evaluation
one_liner: 提出分层记忆+轨迹级RL的GUI购物用户模拟智能体RecVerse，开源带真实交互的USB基准数据集
practical_value: '- 分层记忆设计可直接复用：将用户记忆拆分为Working Memory（短期交互）、Episodic Memory（会话轨迹）、Preference
  Memory（长期意图），通过memory-as-action机制让模型自动学习记忆的写入时机与内容，无需人工规则裁剪会话历史，解决长会话上下文溢出问题

  - 轨迹级RL优化方案可迁移到用户建模场景：放弃逐步行为克隆，改用宏观行为分布对齐+微观意图匹配的双层奖励，既能避免模拟用户出现过度探索/过度被动的异常行为，又能保证交互行为符合用户真实购物意图

  - 开源USB数据集可直接用于自建用户模拟模型的训练/评估，其包含5k+带截图的真实购物交互轨迹，支持多轮交互式RL训练，解决过往用户模拟缺乏GUI级真实标注的问题

  - 模拟质量评估框架可复用：采用行为保真度（ATL/CTR/CVR等统计对齐）+意图一致性（层级类目匹配）的双层评估体系，避免仅靠命中率虚高的过交互模拟结果'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有电商用户模拟器存在两大核心痛点：一是长会话记忆处理能力差，要么丢弃历史丢失用户 evolving 状态，要么全量拼接导致上下文溢出、模拟质量随会话长度上升而下降；二是逐步监督优化存在偏差，拟合单步行为噪声易出现过度探索/过度被动等不符合真实用户的行为模式，无法支撑推荐系统的离线评估、RL训练等下游任务。

### 方法关键点
- 认知启发的三层分层记忆：Working Memory存储最近K步视觉+行为上下文（FIFO淘汰），Episodic Memory选择性存储会话级交互事件，Preference Memory蒸馏用户高层购物意图，记忆更新作为动作空间的一部分由模型自动学习写入时机与内容
- 轨迹级RL优化：基于GRPO算法设计双层奖励，宏观奖励对齐点击/加购/购买等行为分布与真实用户的差距，微观奖励基于三级类目匹配评估交互行为与用户意图的一致性，另加格式奖励保证输出可解析执行
- 开源USB基准数据集：包含5274条带页面截图的真实用户购物轨迹，覆盖8种交互类型，支持多轮交互式RL训练与评估

### 关键结果
在USB数据集上对比9个SOTA基线，RecVerse-GUI RL版本相比最强GUI基线STA，item级F1从4.27提升到7.19（+68%），HR从5.92提升到10.45（+76%），层级类目重叠度HCO从23.11提升到32.64（+41%），行为统计指标更贴近真实用户，人类评估中92%的情况优于STA。

### 核心结论
用户行为模拟是过程导向而非目标导向任务，核心目标是还原真实用户的行为分布与意图一致性，而非追求单步动作的预测准确率。
