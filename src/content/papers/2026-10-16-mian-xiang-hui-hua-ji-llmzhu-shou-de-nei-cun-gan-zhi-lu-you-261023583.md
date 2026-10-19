---
title: 'MARS: Memory-Aware Routing for Session-Level LLM Assistants'
title_zh: 面向会话级LLM助手的内存感知路由框架MARS
authors:
- Minghan Wang
- Jinhang Zuo
- Zhongxiang Dai
- Zhiyong Wang
- Fang Kong
affiliations:
- Southern University of Science and Technology
- City University of Hong Kong
- The Chinese University of Hong Kong, Shenzhen
- Harbin Institute of Technology (Shenzhen)
arxiv_id: '2610.23583'
url: https://arxiv.org/abs/2610.23583
pdf_url: https://arxiv.org/pdf/2610.23583
published: '2026-10-16'
collected: '2026-10-19'
category: Agent
direction: 长会话Agent · 内存与路由协同优化
tags:
- LLM Agent
- Long Session
- Memory System
- Model Routing
- Contextual Bandit
one_liner: 通过共享会话状态耦合内存构建与模型路由，大幅优化长会话LLM助手的质量-内存-成本权衡
practical_value: '- 可复用共享会话状态的设计思路，在电商客服/导购Agent中，将会话意图、上下文依赖度、交互阶段等结构化状态同时作为RAG召回和模型路由的输入，避免内存与路由决策脱节导致的效果下降或成本浪费

  - 路由模块可直接复用LinUCB contextual bandit的在线学习方案，无需提前标注大量路由样本，通过轻量级turn-level反馈（如回答是否符合需求、是否用到正确历史信息）即可迭代路由策略，适配业务动态变化的请求分布

  - 内存构建部分的三层分块（活跃任务状态、最近会话、历史记忆）+ QTM引导的召回范围/数量/优先级控制，可直接迁移到电商多轮导购的RAG系统中，解决长会话历史冗余、旧信息干扰的问题，同时降低context长度成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
长会话LLM助手现有方案中，内存系统和模型路由通常独立决策，忽略二者的强耦合性：内存召回的内容直接决定输入的证据、干扰项和难度，路由选择的模型又决定能否高效利用召回内容，最终要么出现漏关键信息、用旧信息等效果问题，要么因全量上下文+强模型的配置产生极高调用成本，亟需兼顾质量、内存开销、调用成本的协同优化方案。
### 方法关键点
- 设计Query and Topic Manager（QTM）从当前查询、历史交互、内存库中提取结构化共享会话状态，包含会话连续性、内存控制、路由难度三类特征，同时作为内存构建和模型路由的输入
- 内存策略基于会话状态从「活跃任务状态/最近会话/历史记忆」三个块中筛选组装候选内存视图，控制召回范围、数量、优先级，避免冗余信息输入
- 路由模块采用LinUCB contextual bandit，基于会话状态和候选内存视图的统计特征选择匹配的模型，根据选中模型的上下文窗口做最终的内存打包
- 每轮生成后通过轻量级turn-level评估得到质量-成本联合效用反馈，在线更新路由策略，无需微调底层LLM
### 关键实验
在REALMEM（长历史记忆交互数据集，10个persona、1415条查询）和MULTICHALLENGE（结构化多轮会话数据集，245个场景）上对比16种系统配置，核心结果：
1. REALMEM上，MARS保留了全上下文GPT-4o 98.2%的QA效果，仅消耗其14.5%的生成+控制器API成本，内存召回、检索指标均为最优
2. MULTICHALLENGE的状态恢复、版本编辑核心子集上，MARS效果接近最强静态模型Qwen2.5 72B（44/137 vs 45/137），成本更低

**最值得记住的一句话**：长会话LLM系统中，内存构建和模型路由不是独立的前后置步骤，通过共享结构化会话状态做协同决策，是平衡效果和成本的核心有效路径。
