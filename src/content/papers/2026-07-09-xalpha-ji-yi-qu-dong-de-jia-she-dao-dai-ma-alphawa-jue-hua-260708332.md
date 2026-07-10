---
title: 'XALPHA: A Memory-Driven AI Quant Researcher for Hypothesis-to-Code Alpha Discovery'
title_zh: XALPHA：记忆驱动的假设到代码Alpha挖掘AI量化研究员
authors:
- Fengyuan Liu
- Yuchen Fu
- Yuqi Wang
- Qi Liu
affiliations:
- The University of Hong Kong
- Grace Investment Machine
arxiv_id: '2607.08332'
url: https://arxiv.org/abs/2607.08332
pdf_url: https://arxiv.org/pdf/2607.08332
published: '2026-07-09'
collected: '2026-07-10'
category: Agent
direction: 自主科研Agent · 量化Alpha因子挖掘
tags:
- Autonomous Research Agent
- Quant Finance
- Alpha Mining
- Closed-loop Learning
- Memory System
one_liner: 提出多脑架构的记忆驱动量化Agent，实现从研报知识到可验证Alpha因子的端到端闭环挖掘
practical_value: '- 可复用三层RMA知识吸收架构：在推荐/广告场景落地业务知识时，先做准入筛选（A层）、机制归类（B层）、可落地模板生成（C层），解决原始文档RAG冗余、不可执行的问题

  - 可迁移三脑分治闭环：Macro规划、Micro执行、Cross反馈沉淀的分层Agent架构，可直接套用到推荐策略迭代、广告创意批量生成等长周期迭代场景，替代零散单步Agent任务

  - 可落地三对齐校验机制：在生成式推荐的物料/规则生成场景，校验业务假设、代码逻辑、业务合理性三者一致，降低上线风险'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有Alpha挖掘方法大多只自动化孤立步骤，无法模拟人类量化研究员吸收研报知识、提出假设、代码验证、经验迭代的完整闭环，生成的因子普遍缺乏金融合理性、样本外鲁棒性差，挖掘效率和质量都无法满足实盘需求。

### 方法关键点
- 设计Report-to-Memory Absorption（RMA）三层知识吸收层：A层筛选可通过OHLCV数据落地的研报片段，B层归类为趋势、反转等大类机制，C层生成可直接用于假设生成的研究原型
- 三脑协作架构：Macro Brain做周期级研究主题规划，筛选研究原型生成假设池；Micro Brain将假设转换为可执行因子代码，完成假设、代码、金融合理性的三对齐校验，再通过代码级演化生成新因子；Cross Brain将因子验证结果沉淀为原型级、代级、周期级多维度反馈，更新记忆指导后续挖掘
- 分层筛选机制：普通筛选保留演化父代因子，精英筛选留存优质机制，入库阶段严格控制因子质量和多样性

### 关键实验
在CSI300 10日收益率预测任务上，对比传统ML、深度学习、主流Alpha挖掘Agent基线，XALPHA的IC达0.0413、ICIR达0.2573、RankICIR达0.3412，年化超额收益率14.12%、信息比率1.5853，显著优于所有基线；跨主题生成的精英因子平均成对相关性仅0.142，多样性和可解释性表现优异。

### 核心结论
将高专业性、长周期的科研类Agent任务拆解为知识吸收-规划执行-反馈沉淀的分层闭环，是替代人类完成复杂迭代工作的核心可行路径。
