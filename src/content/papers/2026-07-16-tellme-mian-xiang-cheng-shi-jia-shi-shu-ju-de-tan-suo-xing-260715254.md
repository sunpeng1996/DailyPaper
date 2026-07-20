---
title: 'teLLMe Why (Ain''t Nothing but a Jam): Exploratory Causal Analysis of Urban
  Driving Data'
title_zh: teLLMe：面向城市驾驶数据的探索性因果分析系统
authors:
- Qiwei Li
- Jorge Ortiz
affiliations:
- Rutgers University, Department of Electrical and Computer Engineering
arxiv_id: '2607.15254'
url: https://arxiv.org/abs/2607.15254
pdf_url: https://arxiv.org/pdf/2607.15254
published: '2026-07-16'
collected: '2026-07-20'
category: Other
direction: LLM辅助观测数据因果分析工具
tags:
- Causal Analysis
- Schema-Aware LLM
- Observational Data
- Structure Learning
- Natural Language Query
one_liner: 结合因果结构学习与schema感知LLM，实现观测交通数据的自然语言因果查询与假设生成
practical_value: '- 可复用schema-aware LLM映射自然语言到结构化查询的方案，优化电商导购Agent、运营分析工具的用户query理解能力，降低结构化查询门槛

  - 因果分析中bootstrap稳定性校验+显性输出模型假设、不确定性的设计，可迁移到推荐/广告策略的观测数据归因场景，避免错误结论

  - PC算法+DoWhy的轻量因果结构学习与效应估计pipeline，可直接复用做电商用户行为、商品转化的因果假设挖掘，降低归因分析成本'
score: 4
source: arxiv-cs.AI
depth: abstract
---

### 动机
交通部门拥有大量无干预的观测类视频数据，无法直接回答降雨、高峰时段等因素对拥堵、交通安全的因果问题，现有工具也不支持非技术用户通过自然语言发起因果查询。
### 方法关键点
1. 先从行车记录仪标注数据构建结构化事件表，采用PC算法做因果结构学习，搭配bootstrap做稳定性校验，结合线性回归、DoWhy实现查询特异性的因果效应估计；
2. 用schema感知LLM将用户自然语言问题映射为结构化因果查询，自动识别处理变量、结果变量与目标子群体；
3. 输出包含效应估计、调整集、DAG支持、建模假设的因果卡，搭配自然语言解释，定位为假设生成工具而非输出确定性因果结论。
### 关键结果
在BDD交通事件数据集的案例研究中，系统可准确挖掘天气、高峰时段、交通密度之间的合理因果关系，同时明确输出不确定性与建模选择。
