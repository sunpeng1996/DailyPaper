---
title: 'DAGent: Evaluate-then-Grow Planning for Deep Research Agents'
title_zh: DAGent：面向深度研究Agent的先评估后扩展规划框架
authors:
- Hanwen Liu
- Yuanfu Sun
- Qiaoyu Tan
affiliations:
- New York University
- New York University Shanghai
arxiv_id: '2609.39154'
url: https://arxiv.org/abs/2609.39154
pdf_url: https://arxiv.org/pdf/2609.39154
published: '2026-09-29'
collected: '2026-10-02'
category: Agent
direction: Agent 深度研究DAG规划优化
tags:
- DAG-Planning
- Multi-Agent
- GRPO
- Deep-Research-Agent
- RL-Optimization
one_liner: 提出先评估后扩展的增量DAG规划+结构感知RL优化，提升深度研究Agent效果与效率
practical_value: '- 电商/内容平台的深度调研类Agent（比如用户问"2000元以下适合露营的投影仪推荐"这类多约束长查询）可复用Evaluate-then-Grow范式，每轮基于已检索的商品/信息结果动态调整后续检索策略，避免提前规划冗余检索分支，减少工具调用成本同时提升推荐准确率

  - QueryDoc分层上下文传播机制可迁移到多阶段推荐系统的特征传递：上游召回/粗排模块默认仅向下游传递核心特征摘要，精排模块需要时再召回全量用户行为/商品特征，降低模型context负载的同时避免信息损失

  - DAGRPO的拓扑感知信用分配方案可直接用到多角色推荐Agent的RL训练中，仅给最终推荐结果依赖链上的子模块（召回、排序、文案生成）分配全额奖励，大幅提升RL训练效率和收敛效果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有DAG基多Agent系统普遍采用Plan-then-Patch范式：执行前先完成全量任务规划，出现错误后再修补DAG。这类方案在深度研究、复杂信息检索等长周期任务中存在严重缺陷：初始规划阶段掌握的信息最少，却要做出覆盖全任务的最大决策，很容易生成无效分支，浪费计算资源，且准确率随任务复杂度提升快速下降。
### 方法关键点
- Evaluate-then-Grow增量规划：Orchestrator每轮仅基于已执行节点输出的置信度、不确定性信号扩展一批DAG节点，标记为Uncertain/NotFound的节点触发最多2次重试，直到调度答案合成节点终止任务，无预定义全量规划。
- 分层上下文传播：每个节点执行后输出包含核心结论、解释、置信度的QueryDoc，默认仅传递QueryDoc给下游节点，全量执行轨迹仅在下游调用RECALLTOOL时按需召回，大幅降低单节点context负载。
- DAGRPO结构感知RL优化：基于DAG拓扑给最终答案依赖链上的Executor分配全额奖励，非依赖链节点奖励衰减，同时给违反结构规则的Orchestrator决策加正则，解决传统GRPO全局奖励平均分配的信用错配问题。
### 关键实验
在BrowseComp-Plus、GAIA、xbench-DeepSearch三个深度研究基准上测试，Qwen3-235B-A22B规模下比最强开源基线高5.3/5.8/2.0 Pass@1分，该领先性在4家厂商的4款开源底座、GPT-5 327K场景下均稳定复现；DAGRPO在Qwen3-8B规模下比同预算普通GRPO基线平均高3.0 Pass@1分，同时token、工具调用、步骤开销比Plan-then-Patch方案低20%~40%。
### 核心结论
增量证据驱动的动态规划，比先确定全量方案再事后修补的范式，效果更优、计算成本更低
