---
title: Towards Effective Structured Context Modeling for Conversational Recommender
  Systems via Dual-node Monte Carlo Tree Search
title_zh: 基于双节点蒙特卡洛树搜索的对话推荐结构化上下文建模方法
authors:
- Jincheng Zhang
- Chen Huang
- Wenqiang Lei
- See-Kiong Ng
- Yang Deng
affiliations:
- 四川大学计算机学院
- 新加坡国立大学数据科学研究所
- 新加坡管理大学计算与信息系统学院
- 教育部机器学习与产业智能工程研究中心
arxiv_id: '2609.00618'
url: https://arxiv.org/abs/2609.00618
pdf_url: https://arxiv.org/pdf/2609.00618
published: '2026-09-01'
collected: '2026-09-02'
category: RecSys
direction: 对话式推荐 · 结构化上下文建模
tags:
- Conversational Recommendation
- MCTS
- Preference Tracking
- Structured Context
- LLM4Rec
one_liner: 提出双节点MCTS的DREAMS框架，统一建模对话推荐的偏好引导与挖掘，平均准确率提升7.43%
practical_value: '- 可复用双节点分治设计：ELNode负责偏好引导/对话动作规划，EXNode负责召回query结构化生成，拆分交互决策和推荐逻辑，降低单模块复杂度

  - 用户偏好采用JSON结构化存储，显式记录正负向偏好、历史反馈，避免长上下文信息丢失，同时可直接对接下游召回引擎

  - MCTS决策时引入LLM先验概率剪枝搜索空间，搭配历史成功/失败轨迹经验库暖启动，平衡搜索效果和推理延迟，适配业务上线要求

  - FGE²/CGE²/PE²三类错误指标可直接复用在对话推荐系统离线评测中，替代纯成功率指标，定位问题更精准'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有对话推荐（CRS）大多采用自由文本建模上下文，易出现信息过载、无效提问、召回噪声大的问题；少数结构化方案要么仅用JSON存储偏好但忽略状态演化，要么用MCTS做规划但节点无结构化偏好语义，无法同时优化偏好引导和偏好挖掘两个核心目标，甚至会出现已收到用户负反馈仍重复推荐对应物品的低级错误。

### 方法关键点
- 采用树状上下文建模框架，将用户偏好演化建模为结构化对话状态的搜索过程，节点存储JSON格式偏好状态，边对应状态转移
- 设计两类专用节点：ELNode通过MCTS探索对话动作（询问偏好/失败反思/跳转推荐等），动态更新用户正负向、缺失、修正的偏好状态；EXNode将累积的偏好状态精炼为结构化召回query，通过检索匹配度打分选择最优query，降低上下文噪声
- 设计分层奖励函数同时覆盖偏好获取进度、推荐成功率、对话效率，MCTS决策时融合树搜索统计值和LLM先验概率，提升动作合理性

### 关键实验
在Redial、OpendialKG两个公开基准数据集上，和ChatCRS、SAPIENT等10个基准方法对比，平均推荐成功率（SR）提升7.43%，偏好引导效果提升9.35%，偏好挖掘效果提升4.0%；60人参与的真人评估中，SR、R@1等所有指标均优于基线；引入经验库暖启动的DREAMS(EA)版本推理延迟可降到9s，基本满足上线要求。

最值得记住的结论：对话推荐的效果提升不能只靠结构化存储偏好，也不能只靠MCTS做规划，必须把结构化偏好状态作为决策核心，同时打通偏好引导和挖掘两个流程的状态复用。
