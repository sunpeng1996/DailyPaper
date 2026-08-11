---
title: Personalized Communication Skills for Agentic Recommender Systems
title_zh: 面向智能体推荐系统的个性化沟通技能框架
authors:
- Zongwei Wang
- Min Gao
- Guangyu Hu
- Xinyi Gao
- Junliang Yu
affiliations:
- Chongqing University
- The University of Queensland
arxiv_id: '2608.08417'
url: https://arxiv.org/abs/2608.08417
pdf_url: https://arxiv.org/pdf/2608.08417
published: '2026-08-09'
collected: '2026-08-11'
category: MultiAgent
direction: 智能体推荐 · 多智体沟通优化
tags:
- LLM Agent
- Recommender System
- Multi-Agent Collaboration
- Skill Library
- Personalized Routing
one_liner: 提出AgentCom框架，通过分层可复用沟通技能库解决智能体推荐视角狭窄问题，提升推荐准确率
practical_value: '- 可复用技能库设计可迁移：将智能体外部交互逻辑拆分为why-what-how-who四层结构化模块，做成共享可配置组件，无需为每个场景从零开发prompt，大幅降低多智能体推荐的开发成本

  - 故障驱动进化机制可复用：业务上线后自动收集推荐失败case，用LLM诊断问题层级，自动迭代技能库规则，无需人工频繁更新策略，适配电商大促、新品上新等需求快速变化的场景

  - 交互参数可直接复用：实测用户-顾问交互轮次设为3、顾问内部讨论轮次设为1时性价比最高，可直接复用到社交种草、好友推荐类业务的智能体流程，平衡推荐效果与LLM调用成本

  - 低侵入式接入：AgentCom可作为外挂层叠加在现有召回、排序、智能体推荐后端上，无需改造原有架构，即可引入外部用户补充证据，缓解冷启动、用户偏好歧义等痛点'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有智能体推荐系统的UserAgent仅基于自身有限历史行为独立推理，易出现视角狭窄问题，仅关注局部不完整的偏好维度，导致判断不准确。直接引入通用的用户-顾问通信流程效果不佳，因为不同用户的决策状态（冷启动、决策犹豫、对物品陌生等）对应的外部建议需求差异极大，需要个性化的沟通策略。

### 方法关键点
- 构建why-what-how-who四层结构的共享沟通技能库：每层技能为包含适用条件、可执行指令、输出契约的结构化节点，支持层级化扩展，通用技能可复用，细分场景可扩展子技能
- 个性化技能路由：根据用户初始决策状态、历史行为等上下文，LLM路由按why→what→how→who顺序匹配最优技能，生成专属沟通路径
- 故障驱动的技能进化：对推荐失败case，LLM自动诊断问题所属层级，分三类处理：技能不足则生成子技能细化，能力缺口则新增平行技能，路由错误则直接修正路径，无需人工标注即可自动迭代

### 关键实验
在LastFM、Epinions、LibraryThing三个公开数据集测试，对比传统、社交、智能体三类共6种基线，统一用SASRec生成20项候选集，指标为Hit@1。结果显示AgentCom可稳定提升所有基线效果：传统SASRec最高提升17.74%，社交GBSR最高提升7.45%，最优智能体基线MemRec最高提升8.4%，单用户额外LLM成本低于0.01美元。

### 核心结论
智能体推荐的性能提升不仅来自单智能体的推理能力，还来自多智能体之间结构化、个性化的信息交互，补充单用户视角缺失的偏好信号
