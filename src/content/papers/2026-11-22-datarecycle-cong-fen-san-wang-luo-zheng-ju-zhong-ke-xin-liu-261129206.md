---
title: 'DataRecycle: Trustworthy Distillation of Structured Data from Scattered Web
  Evidence'
title_zh: DataRecycle：从分散网络证据中可信蒸馏结构化数据
authors:
- Can Liu
- Tengteng Zhu
- Xinyu Jiang
- Xiaolin Wen
- Yong Wang
arxiv_id: '2611.29206'
url: https://arxiv.org/abs/2611.29206
pdf_url: https://arxiv.org/pdf/2611.29206
published: '2026-11-22'
collected: '2026-11-24'
category: Other
direction: 可信数据蒸馏 · 多源信息对齐与溯源
tags:
- Data-Distillation
- Provenance-Tracking
- Information-Extraction
- Ontology-Guided-Retrieval
- Multi-Source-Alignment
one_liner: 提出可溯源交互式系统DataRecycle，从分散网络证据中蒸馏得到带来源的结构化数值事实表
practical_value: '- 做商品舆情、竞品价格、市场数据自动化结构化爬取整理时，可复用本体引导的分层检索策略，减少召回遗漏

  - 搭建多源数据融合的推荐上游特征库时，可复用数据全链路溯源机制，快速定位脏数据来源解决特征一致性问题

  - 电商Agent自动执行市场调研、商情分析任务时，可借鉴多源数据时间/定义/尺度对齐方法，避免数据冲突导致决策错误'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
网页中存在大量分散的量化证据，现有方案存在明显缺陷：搜索引擎返回的文档列表需大量人工提取对齐，生成式AI产出的结果无来源可追溯、存在报告偏差、隐藏多源冲突，结构化蒸馏成本高、错误率高。
### 方法关键点
1. 采用本体引导的自上而下数据采集策略，将用户查询/陈述拆解为实体与属性后召回候选证据；
2. 全链路记录从检索片段到提取值的血缘关系，实现数据完全可溯源；
3. 跨时间、定义、尺度维度对齐异构数据，解决多源数据不一致问题；
4. 以表格视图组织带来源的证据，支持不确定性与冲突源可视化核验。
### 关键结果
经模块级实验、场景验证与用户研究验证，系统可帮助用户高效将网络数值证据整理为带来源关联的结构化表格，快速定位核验数据不确定性与冲突来源。
