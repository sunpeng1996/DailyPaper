---
title: 'Ballad: Bandit-Based LLM Routing for Automated Heuristic Discovery'
title_zh: BALLAD：基于多臂老虎机的自动启发式发现LLM路由框架
authors:
- Samidha Verma
- Ankit Anand
- Sayan Ranu
affiliations:
- Indian Institute of Technology Delhi
- Google DeepMind
arxiv_id: '2611.17241'
url: https://arxiv.org/abs/2611.17241
pdf_url: https://arxiv.org/pdf/2611.17241
published: '2026-11-12'
collected: '2026-11-13'
category: LLM
direction: LLM路由 · 多臂老虎机优化
tags:
- LLM-Routing
- Multi-Armed-Bandit
- Heuristic-Discovery
- Cost-Optimization
- Online-Learning
one_liner: 提出基于多臂老虎机的自适应LLM路由框架，在自动启发式发现场景超最优单模型且最高降本65.6%
practical_value: '- 多LLM调用场景可复用其bandit路由思路：无需固定选用最贵大模型，基于上尾分位数（而非平均效果）评估模型价值，适配追求最佳单次输出的场景（如Agent工具调用、营销文案生成、推荐规则挖掘）

  - 因果耦合的多步credit分配机制可迁移：针对生成结果依赖历史上下文的序列任务（如推荐规则迭代、多轮Agent推理），用DAG血缘+深度衰减+滑动窗口的方式给上游模型分配贡献，解决非独立决策的归因问题

  - 降本可直接复用：大模型密集调用的业务（如A/B测试规则生成、批量文案优化）可直接套用该无监督路由框架，无需离线标注，仅通过在线反馈即可动态选择最优模型，最高可省60%+API成本'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前自动启发式发现（AHD）系统默认选用更大更贵的LLM可获得更优结果，但实证表明大模型并无稳定性能优势；AHD需数千次LLM调用，成本极高，而现有LLM路由依赖离线标注、假设查询独立，无法适配AHD场景下决策耦合、奖励非平稳、追求最优单结果的核心特性，亟需自适应路由方案。

### 方法关键点
- 将LLM选择建模为多臂老虎机问题，每个LLM对应一个臂，核心设计三个适配AHD的模块：1）混合上尾分位数打分：结合bootstrap估计的上尾分位数和历史最高分，优先筛选能产出罕见高价值结果的模型，而非平均表现更优的模型；2）DAG血缘信用传播：基于启发式的变异血缘DAG，对高价值结果的上游祖先模型按深度衰减分配信用，解决多模型决策耦合的归因问题；3）滑动窗口归一化：仅保留最近W轮观测值，适配模型效用随搜索过程动态变化的非平稳特性，再加UCB探索bonus平衡探索与利用。
- 为FunSearch等AHD pipeline的即插即用组件，无需修改原有提示构造、评估逻辑，无需离线标注。

### 关键实验
在TSP、CVRP、在线/离线背包、图编辑距离5个NP-hard组合优化任务上，对比Gemma 3 12B/27B、Gemini 2.5 Flash/Lite 4个不同量级的模型：BALLAD整体效果优于所有单模型，相比始终调用最贵的Gemini 2.5 Flash，API成本最高降低65.6%，平均降本2.86倍。

### 核心结论
在多轮LLM迭代生成、追求最优单结果的场景，无需固定选用最贵的大模型，自适应路由不仅能超越最优单模型效果，还可大幅降低调用成本。
