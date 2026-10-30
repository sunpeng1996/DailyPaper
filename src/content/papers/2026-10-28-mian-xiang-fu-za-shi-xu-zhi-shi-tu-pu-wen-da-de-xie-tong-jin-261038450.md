---
title: 'CoSTA: Co-Evolving Self-Play Timeline Agents for Complex Temporal Knowledge
  Graph Question Answering'
title_zh: 面向复杂时序知识图谱问答的协同进化自玩时间线智能体CoSTA
authors:
- Haikun Liu
- Zhichao Yan
- Shaoru Guo
- Jiawei Gu
- Victor Gutierrez Basulto
- Jiapu Wang
- Ru Li
affiliations:
- Shanxi University
- Singapore University of Technology and Design
- Cardiff University
- Nanjing University of Science and Technology
arxiv_id: '2610.38450'
url: https://arxiv.org/abs/2610.38450
pdf_url: https://arxiv.org/pdf/2610.38450
published: '2026-10-28'
collected: '2026-10-30'
category: Agent
direction: 多智能体协作 · 时序知识图谱问答
tags:
- Multi-Agent
- TKGQA
- Self-Play
- Reinforcement Learning
- Timeline Reasoning
one_liner: 提出多角色共享策略的协同进化自玩框架，复杂时序知识图谱问答达SOTA，小模型优于闭源大模型
practical_value: '- 电商带时序约束的搜索/问答场景可直接复用架构：将「查询拆解-子任务时序证据检索-跨子任务时间约束推理」拆为协调者+worker多智能体流程，避免单智能体上下文内时序证据混杂的错误，适配「去年双11同类最低价商品」这类复杂查询

  - 多智能体训练可复用共享策略+协同进化机制：无需分别训练不同角色的LLM，仅靠角色prompt区分身份，通过角色条件蒸馏初始化+最终结果奖励的跨角色PPO优化，大幅降低多智能体训练成本

  - 时序数据处理可复用时间线导航工具：将用户、商品、订单等实体的关联事件按时间排序为可遍历时间线，提供「邻近时间节点检索」工具，比纯语义召回更准确处理时间先后、区间交集类时序约束'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
复杂时序知识图谱问答（TKGQA）需要处理多事实间的时序依赖，现有单智能体方法会将不同事件的证据、时间戳、中间步骤混在同一上下文，容易被干扰项误导推理；多智能体方案未针对角色间的强依赖做联合优化，单独优化协调者或worker仅能得到局部最优，无法提升最终答案质量。
### 方法关键点
- 时间线中心协作架构：TKG事实按实体+关系预生成时序排序的可导航时间线，协调者拆分问题为子任务分配给独立worker；worker通过语义检索定位时间线入口、时间线读取获取邻域时序证据，返回带原始时间戳的工具观测+子任务结论报告；协调者整合所有证据做跨子任务的时序约束推理，必要时发起多轮补充检索
- 共享策略初始化：通过大模型生成正确协作轨迹作为示范，角色条件蒸馏让单个LLM学习协调者、worker两种角色的行为，仅靠角色prompt区分身份，无需训练独立模型
- 协同进化自玩优化：采用留一法PPO计算单条轨迹的优势，基于最终答案对错的二元奖励做跨角色信用分配，同时更新两种角色的策略，实现协调者与worker的协同进化
### 关键结果
在MultiTQ、TimelineKGQA-CronQuestion、TimelineKGQA-ICEWS-Actor三个基准上对比10种SOTA方法、GPT-5.6 Sol、GPT-6 Astra闭源模型：CoSTA（Qwen3-4B）整体Hits@1分别达86.8%、71.8%、72.6%，在多事实复杂问题上相对基线最高提升15.6pct，4B/8B小模型性能全面超越闭源GPT系列。
### 核心结论
多智能体协作的收益并非来自额外计算量，而是通过任务隔离避免上下文混杂，端到端联合优化的自玩机制让角色动态适配，小模型也能超过大模型的单智能体表现
