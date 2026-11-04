---
title: 'Agentic Path Maps: Exposing an Agent''s Traversal Through the Garden of Forking
  Paths'
title_zh: Agentic Path Maps：可视化智能体在分叉决策空间的可选执行路径
authors:
- Madeleine Grunde-McLaughlin
- Hafsah Usman
- Daniel Mitroshkov
- Emily Reif
- Nino Migineishvili
- Lakshya Chauhan. Kevin Yu
- Jeffrey Heer
- Daniel S. Weld
affiliations:
- University of Washington
- Allen Institute for AI
arxiv_id: '2611.04183'
url: https://arxiv.org/abs/2611.04183
pdf_url: https://arxiv.org/pdf/2611.04183
published: '2026-11-03'
collected: '2026-11-04'
category: Agent
direction: Agent可解释交互 · 用户依赖优化
tags:
- Agent_Interpretability
- Human_AI_Interaction
- Decision_Making
- Path_Visualization
- User_Study
one_liner: 提出智能体路径图设计空间，实证验证展示可选路径可降低用户对智能体输出的过度依赖
practical_value: '- 电商Agent导购/智能客服场景中，对用户模糊查询（如「推荐适合送人的礼物」），可展示3种不同决策路径的结果（如高性价比/高端/网红款）替代单一推荐，既降低用户对不符合预期结果的不满，也能减少用户过度依赖单一最优解的决策偏差

  - 路径展示数量优先选3条即可，无需展示过多：实验证明9条路径会导致用户认知负荷上升，且有益认知参与度反而下降，能更好平衡用户理解度和交互成本

  - 可复用论文提出的8维设计空间搭建推荐结果的可解释路径展示模块，比如突出不同推荐路径的决策点差异（是否选包邮、是否为新品、是否匹配过往消费偏好），有效提升用户对推荐结果的信任

  - 搜索推荐的模糊Query场景，可采用后验展示多路径结果的方案，替代执行过程中频繁打断用户询问偏好，降低用户交互负担的同时提升推荐结果的匹配准确率'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
AI Agent 执行用户未明确定义的模糊任务时，会自动隐含假设用户偏好，输出的任务合规结果可能不符合用户实际未表述的上下文；既无法在执行中频繁打断用户询问偏好，传统的单一结果展示+执行轨迹可解释方案也无法让用户感知到可选决策空间，容易导致用户过度依赖单一结果做出错误决策。

### 方法关键点
- 梳理10个相关领域的2402篇论文，提炼出Agentic Path Maps的8维设计空间：目标、路径结构、交互发起方、展示时机、内容数量、辅助解释、可视化形式、交互能力
- 控制变量测试路径展示数量这一核心维度，对比单一路径、3条样本路径、9条全量路径三类展示形式的用户行为差异
- 选取数据分析师场景做测试载体，基于BLADE基准的多决策点分析任务作为实验素材，量化用户对结果的依赖度、认知负荷、信念偏差等核心指标

### 关键实验结果
- 48名有基础统计能力的受试者参与组内对照实验：相比单一路径，展示多路径时用户对极端结果的权重降低63%，最终信念与真实结果中位数的偏差降低38%，任务耗时平均增加138秒
- 展示3条路径比9条路径的有益认知参与度更高，9条路径仅提升认知负荷无额外理解收益

### 核心结论
对模糊任务的智能体输出，展示少量可选路径比单一最优解更能降低用户决策偏差，且收益随路径数量上升边际递减
