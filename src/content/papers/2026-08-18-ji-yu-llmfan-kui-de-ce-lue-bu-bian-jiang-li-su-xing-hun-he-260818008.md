---
title: 'Policy-Invariant Reward Shaping from LLM Feedback: A Framework for Hybrid
  RL Agents'
title_zh: 基于LLM反馈的策略不变奖励塑形：混合RL Agent框架
authors:
- Christophe D. Hounwanou
- John Emeka Eze
- Yaé U. Gaba
affiliations:
- African Institute for Mathematical Sciences, Rwanda
- AIRINA Labs, Bénin
- Sefako Makgatho Health Sciences University, South Africa
- African Center for Advanced Studies, Cameroon
arxiv_id: '2608.18008'
url: https://arxiv.org/abs/2608.18008
pdf_url: https://arxiv.org/pdf/2608.18008
published: '2026-08-18'
collected: '2026-08-19'
category: Agent
direction: 混合LLM+RL Agent 奖励塑形优化
tags:
- LLM
- ReinforcementLearning
- RewardShaping
- HybridAgent
- PolicyInvariance
one_liner: 提出势能式LLM反馈奖励塑形方法，保证混合LLM+RL架构最优策略不受LLM错误影响
practical_value: '- 搭建LLM+RL混合Agent（如电商导购Agent、搜索query优化Agent）时优先采用势能式奖励塑形，即使LLM评分错误也只会影响收敛速度，不会破坏最终最优策略

  - 参考框架模块化设计，将LLM planner、RL控制器、Done判定、势能评分模块接口解耦，方便替换组件降低迭代成本

  - LLM子目标与Done判定的词汇不匹配是高频落地故障，可优先采用LLM自身做Done判定，或提前校准子目标输出语法避免调度卡死

  - 可复用论文提供的规划、评分、完成判定、重规划四类prompt模板，快速搭建LLM引导的RL系统原型'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前LLM+RL混合架构中，LLM生成的奖励信号缺乏理论保证，一旦LLM输出错误可能导致RL学到的策略偏离真实任务最优解，现有方案如Text2Reward、Eureka均无法解决该问题；同时长序列稀疏奖励场景下RL探索效率低，纯LLM planner无法落地低阶控制，亟需兼顾LLM引导能力和策略正确性的架构。

### 方法关键点
- 形式化定义目标增强马尔可夫决策过程（GA-MDP），将混合架构拆分为LLM高层规划器+RL低层控制器独立模块，LLM负责输出子目标和状态-子目标进度评分
- 基于经典势能奖励塑形理论，将LLM输出的0~1范围进度评分作为有界势能函数，构造塑形奖励 `F=γΦ(s',g)-Φ(s,g)` 叠加到原始奖励上
- 支持两种重规划触发机制：每H步周期重规划、子目标超过B步未完成触发失败重规划；内置三种Done判定实现：环境事件标志、MLP分类器、LLM直接判定
- 开源完整参考实现，支持本地/云端LLM接入，内置26个单元测试

### 关键实验
- 3状态MDP数值验证：即使势能值达到原奖励的20倍，最优策略与原始MDP完全一致，验证策略不变性
- 20个MiniGrid任务planner单独测试：本地部署Qwen-2.5:14b，解析率100%，平均覆盖54.8%的真实子目标
- MiniGrid-DoorKey-6x6小规模验证：3万步训练下PPO基线成功率28.1%，混合架构成功率9.3%，核心故障为LLM子目标与环境Done判定的词汇不匹配

### 核心结论
LLM反馈作为奖励信号引入RL系统时，只要将其约束为有界势能函数，就可以完全保证最优策略不受LLM错误干扰，仅可能影响收敛速度。
