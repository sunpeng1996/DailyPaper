---
title: 'From Offline Proxies to Online Decisions: A Layered Engagement Evaluation
  Framework for Conversational AI'
title_zh: 面向对话AI的分层参与度评估框架：打通离线代理与在线决策
authors:
- Xuanyi Li
- Vaskar Nath
- Hossein Amirkhani
- Jay Li
- Alex Deng
affiliations:
- Meta Platforms, Inc.
arxiv_id: '2609.25408'
url: https://arxiv.org/abs/2609.25408
pdf_url: https://arxiv.org/pdf/2609.25408
published: '2026-09-21'
collected: '2026-09-23'
category: Eval
direction: Agent 离线效果评估框架优化
tags:
- Conversational AI
- Offline Evaluation
- A-B Testing
- Engagement Modeling
- Reward Model
one_liner: 提出三层对齐的对话AI离线评估框架，预测A/B测试效果F1达81.1%且无反向错误
practical_value: '- 做Agent/对话推荐的离线效果评估时，可复用三层对齐思路：先对齐标签与业务目标，再对齐打分器与模型行为，最后对齐离线套件与线上实验，避免仅靠离线分类精度就上线

  - 离线评估与线上A/B的对齐不要只看点估计，对比双方置信区间做决策，新增abstention机制可大幅减少反向错误（本场景从31个降为0），降低线上负向风险

  - 有限离线评估算力优先投入多轮交互模拟而非增加单轮case数量：250个核心case滚动3轮的效果优于5000个case单轮打分的效果，算力节省85%

  - 离线评估套件构建可复用critical-turn筛选方法，用LLM标注对话中对用户体验影响大的关键节点采样，小样本下即可提升离线-在线对齐F1 15+百分点'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
对话AI迭代速度快，但线上A/B测试流量有限、读out时间长（该场景需7天），传统离线评估要么只看点相关度，要么没有系统性对齐线上效果，常出现离线涨点线上下跌甚至反向的问题，需要可信任的离线代理优先排序候选模型，减少无效A/B测试消耗。

### 方法关键点
- 三层对齐诊断清单将离线-在线对齐拆解为三个依赖环节：1）标签-业务目标对齐：训练标签需匹配线上A/B测的核心业务指标（如7天参与度）；2）打分器-模型行为对齐：engagement classifier需能区分不同候选模型的行为差异；3）套件-实验对齐：离线测试case分布、打分聚合、校准层需匹配线上实验的组间差异
- 评估协议放弃点估计对齐，对比离线打分稳定性区间和线上A/B置信区间的一致性，设置abstention规则（区间跨0时不做明确判断），避免反向错误
- 框架落地分三阶段：固定评估套件生成候选模型的交互行为，engagement classifier打分，校准层将组间打分差映射为线上参与度变化

### 关键实验
基于Meta内部27个对话AI实验、489组离线-在线对比数据验证，其中113组为校准层冻结后的全新实验：
- 复合框架对比原生classifier打分，F1从34.3%提升至81.1%，反向错误从31个降为0
- 对比5个已上线的其他离线评估器，F1领先25.7个百分点
- 多轮模拟实验中，250个核心case滚动3轮的F1达79.8%，优于5000个case单轮打分的77.6%，算力仅为后者的1/5

**最值得记住的结论**：离线评估的核心不是单模块的离线精度，而是端到端的离线-在线对齐效果，abstention机制是避免线上负向风险的最低成本手段
