---
title: 'Idea2Prior: Auditable Paper Retrieval and Ranking from Research Ideas'
title_zh: Idea2Prior：基于研究想法的可审计学术论文检索与排序系统
authors:
- Shitian Yang
- Ruijie Tao
- Jian Huang
affiliations:
- Johns Hopkins University
arxiv_id: '2610.20857'
url: https://arxiv.org/abs/2610.20857
pdf_url: https://arxiv.org/pdf/2610.20857
published: '2026-10-14'
collected: '2026-10-16'
category: Agent
direction: Agent 学术文献检索系统优化
tags:
- Scholarly Retrieval
- Agent
- Auditable Pipeline
- Citation Expansion
- Joint Ranking
one_liner: 提出可审计的学术论文检索框架，基于多源信息联合排序实现研究想法到文献的精准匹配
practical_value: '- 全链路可审计的pipeline设计可直接复用：将召回、初筛、精排、证据采集各阶段的状态、结果全埋点记录，可解决电商搜索、广告推荐的badcase难定位问题，快速定位是召回漏了还是排序错了

  - 语义关联扩展的召回思路可迁移：基于初筛高相关种子的关联关系（如引文、用户共点击、搭配购买）做二次召回，再做语义匹配过滤，能有效提升电商长尾商品、小众兴趣推荐的召回率

  - 异构缺失感知的排序策略适配业务场景：排序时不强制要求候选的全量信息，缺失详情/评价/特征的候选仍可参与排序，可直接用于商品信息不完备的冷启动推荐、二手商品排序场景

  - 分层难度的测试集构建方法可复用：将query按信息丰富度分EASY/MEDIUM/HARD三档测试，可用于电商搜索query理解、推荐冷启动的效果分层评估'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有基于研究想法找相关论文的方案仅匹配主题词，无法处理术语差异、核心机制不在摘要中的问题，且检索过程黑盒，无法定位漏召回、错过滤的原因，难以满足学术检索的可解释、可审计需求。

### 方法关键点
- 全链路可审计设计：完整记录查询、候选身份、评估结果、过滤原因、PDF获取状态、最终排序的全流程数据，可区分召回缺失、过滤丢失、操作失败三类错误
- 多阶段检索流程：先将用户想法拆解为技术、问题、机制等多维度facet，生成多源检索query召回候选，经身份校验、摘要初筛后，取Top5高相关种子做引文邻居语义扩展，最多保留60个候选进入精排
- 异构证据联合精排：固定尝试获取5个候选的PDF，提取最多6个相关片段，结合完整摘要、初筛评分、资源状态，由Expert模型联合排序输出Top5结果，PDF缺失不直接降低候选权重

### 关键实验
用30个query（EASY/MEDIUM/HARD各10个）测试，对比ChatGPT Web Deep Research、Gemini Web Deep Research两个baseline：整体Hit@5达53.3%，分别比两个baseline高10、16.7个百分点，其中EASY档Hit@5 90%、MEDIUM档50%，均领先baseline20个百分点，仅HARD档20%略低于ChatGPT的30%；单query平均耗时8分53秒，API调用成本平均$0.0945/次。

### 最值得记住的一句话
可审计的检索流程不仅能定位badcase原因，还能在不引入额外生成开销的前提下，有效提升中低难度检索任务的召回准确率。
