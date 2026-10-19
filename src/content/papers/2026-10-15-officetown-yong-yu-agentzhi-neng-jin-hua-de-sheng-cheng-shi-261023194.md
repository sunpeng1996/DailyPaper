---
title: 'OfficeTown: Generative Organizations for Evolving Agent Intelligence'
title_zh: OfficeTown：用于Agent智能进化的生成式组织模拟框架
authors:
- Hongchen Wei
- Daohong Ying
- Zhi Hong
- Aidan Wu
- Bei Liu
- Ruichun Ma
- Yifan Yang
- Qi Dai
- Kai Qiu
- Rui Xu
affiliations:
- Wuhan University
- University of California San Diego
- South China University of Technology
- Cornell University
- Microsoft Research Asia
arxiv_id: '2610.23194'
url: https://arxiv.org/abs/2610.23194
pdf_url: https://arxiv.org/pdf/2610.23194
published: '2026-10-15'
collected: '2026-10-19'
category: Agent
direction: Agent 专业能力评测与训练优化
tags:
- AgentSimulation
- AgentBenchmark
- AgentTraining
- MultiAgent
- LLMAgent
one_liner: 提出模拟专业组织运行的OfficeTown框架，生成真实工作流数据用于Agent评测与训练
practical_value: '- 电商/广告运营Agent可直接复用主-助理协作架构：将复杂投放、活动复盘等任务拆分为「负责人（定目标、审结果）+ 执行助理（调参数、做报表）」模式，实测比单Agent任务完成率提升10%+，还能降低越权操作风险

  - 可借鉴带权限的持久化工作区设计：给不同角色的业务Agent（运营/投放/客服）做数据访问权限隔离，自动留存工作轨迹和中间产物，便于后续审计和迭代

  - 缺乏垂直场景Agent训练数据时，可参考组织模拟思路：用LLM生成对应业务场景的虚拟组织运行轨迹，自动产出标注好的SFT/蒸馏数据，成本仅为人工标注的1/10以下'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent评测与训练多采用孤立任务，无法匹配真实专业工作中任务带上下文、有前后依赖、需跨角色协作的特点，缺乏能规模化生成真实工作场景、任务、反馈的数据源，制约了Agent专业能力的迭代进化。
### 方法关键点
- 输入自然语言描述的组织目标即可自动生成对应组织架构、角色权限、初始资源的虚拟专业组织，角色能力基于O*NET/ESCO职业标准构建
- 模拟真实组织的协作、委托、审核全流程，工作产物、决策、未解决问题持久化存储，自动生成后续关联任务，还原真实工作的前后依赖
- 从模拟工作流中自动抽取带任务时间快照上下文的可执行评测任务、SFT轨迹、在线蒸馏（OPD）任务，无需人工标注
- 配套主-助理协作架构：负责人统筹任务、审核结果，助理在授权工作区内执行，权限隔离避免敏感数据泄露
### 关键实验
构建的OfficeTown Bench覆盖8个专业领域、23个虚拟组织的406个任务，共4836条专家审核的评测标准，配套2202条SFT轨迹、828条OPD任务。核心结果：
1. GPT-6 Astra在Bench上Pass@1仅74.4%，现有前沿模型仍有较大提升空间
2. 用OfficeTown数据训练Qwen3.5-9B，在外部GDPval基准上得分从65.75提升至73.65，提升7.9个百分点
3. 主-助理架构相比MetaGPT、CAMEL等基线，在5个外部专业任务基准上平均提升5%以上
### 核心结论
真实专业工作从来不是孤立的，通过模拟组织运行自动生成带上下文的任务与轨迹，是Agent专业能力进化的高价值可扩展路径
