---
title: 'Autonomous Information Seeking: A Roadmap for Agentic Recommender Systems'
title_zh: 自主信息获取：智能体推荐系统研究路线图
authors:
- Xinyu Lin
- Yashar Deldjoo
- Sunhao Dai
- Honghui Bao
- Xiaopeng Ye
- Fatemeh Nazary
- Wenjie Wang
- Tommaso Di Noia
- Jun Xu
- Tat-Seng Chua
affiliations:
- National University of Singapore
- Polytechnic University of Bari
- Renmin University of China
- University of Science and Technology of China
arxiv_id: '2607.04433'
url: https://arxiv.org/abs/2607.04433
pdf_url: https://arxiv.org/pdf/2607.04433
published: '2026-07-05'
collected: '2026-07-07'
category: Agent
direction: 智能体推荐系统架构与演进路径
tags:
- Agentic RecSys
- LLM Agent
- Level of Autonomy
- User Simulator
- Recommendation Evaluation
one_liner: 提出基于自主度的智能体推荐系统分类框架，梳理三大范式、评估方案与开放挑战
practical_value: '- 可直接复用L0-L6自主度分级体系，评估现有推荐系统的Agent化改造阶段，根据业务场景选择对应架构：导购类场景优先落地L3工具驱动辅助架构，复杂约束类场景（如旅游套餐、穿搭推荐）采用L4单智能体规划架构

  - 三大范式的落地路径可直接参考：短期优先落地Agent-assisted方案，用Agent增强现有召回、排序、解释模块；长期迭代Agent-as-recommender；用Agent-as-user-simulator生成冷启动数据、模拟在线实验降低试错成本

  - RAG增强推荐的三类设计维度（功能角色/检索内容/检索流程）可直接迁移到现有生成式推荐场景，降低幻觉同时提升个性化程度

  - 工具分类框架（RecTools/外部信息工具/属性工具/多模态工具）可直接用于指导智能体推荐系统的工具模块选型与开发'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统推荐系统为静态单步排序范式，现有LLM增强推荐大多仍为被动响应模式，无法满足多约束、多步决策的复杂推荐场景需求，当前智能体推荐领域缺乏统一分类框架与演进路径，工业落地缺乏明确参考。
### 方法关键点
- 提出L0-L6的推荐系统自主度（LoA）分级体系，从任务规划、上下文感知、交互灵活性、适配性四个维度量化自主能力，当前可落地场景集中在L2-L5区间
- 划分三大核心范式：Agent-assisted推荐（智能体增强现有pipeline，对应L2-L4）、Agent-as-recommender（智能体作为端到端决策者，对应L4-L5）、Agent-as-user-simulator（智能体模拟用户行为，用于训练评估，对应L4-L5）
- 系统梳理各范式核心组件设计：包括RAG增强的三类设计维度、4类推荐工具分类、单智能体5大核心模块、多智能体协作协议
- 总结智能体推荐专属评估体系，覆盖推荐效果、输出质量、Agent过程质量三类维度
### 关键结果
统计2024-2026年3月的相关文献，2025年论文量较2024年增长3倍；Agent-as-recommender是主流范式，L4单智能体架构占比超40%，L5多智能体占比从2024年的22.2%升至2026年的28.6%，Agent-as-simulator占比从13.3%升至24.7%。
> 核心结论：智能体推荐的核心是从「单次排序模型」转向「目标导向的交互式决策系统」，自主度而非模型大小是决定落地价值的核心指标。
