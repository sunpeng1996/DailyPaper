---
title: Recommendation Feedback Loops Shape Urban Income Segregation and Venue Visitation
title_zh: 推荐系统反馈环对城市收入隔离与线下商户经营的影响研究
authors:
- Guangyuan Weng
- Lin Chen
- Ciro Beneduce
- Giovanni Mauro
- Massimiliano Luca
- Takahiro Yabe
- Bruno Lepri
- Luca Pappalardo
- Esteban Moro
affiliations:
- 东北大学
- 布鲁诺·凯斯勒基金会
- 意大利国家研究委员会ISTI研究所
- 纽约大学
- 特伦托大学
arxiv_id: '2610.41911'
url: https://arxiv.org/abs/2610.41911
pdf_url: https://arxiv.org/pdf/2610.41911
published: '2026-10-30'
collected: '2026-11-02'
category: RecSys
direction: 位置推荐 · 公平性与反馈环优化
tags:
- Recommender System
- Feedback Loop
- POI Recommendation
- Fairness
- Popularity Bias
- Urban Mobility
one_liner: 基于美国四大都市区仿真，揭示POI推荐反馈环加剧收入隔离与商户流失，给出低成本重排干预方案
practical_value: '- 本地生活/POI推荐团队可新增反馈环仿真评估环节，在离线NDCG等精度指标外，纳入商户存活率、跨群体接触度等长期生态指标，避免仅优化精度造成的生态恶化

  - 解决推荐马太效应可直接复用tail-boost重排trick：给低热度item的打分加固定权重，在15%以内的精度损失下就能降低50%+的小众商户流失，同时缓解群体隔离

  - 所有存在反馈环的推荐场景（电商、内容、本地生活）都需要区分离线评估与在环长期效果，离线精度更高的算法（如基于用户历史复购的召回）可能带来更严重的长期生态问题'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前位置类推荐系统仅用离线精度评估，完全忽略人-AI反馈环的长期影响；而线下商户具备空间约束、容量上限、社交耦合三大和线上商品完全不同的特性，反馈环带来的中小商户流失、收入群体隔离等问题会直接影响城市社会公平与商业生态，但此前没有仿真框架能量化这类长期影响。

### 方法关键点
- 基于美国四大都市区（波士顿、旧金山、底特律、芝加哥）的匿名GPS mobility真实数据，模拟4k-8k分四个收入quartile的居民3年的餐饮出行行为，纳入出行距离、商户容量约束
- 对比4类主流POI推荐算法：UR-POI（用户常去地点召回）、ItemKNN、UserKNN、Markov链模型，设置仅训练1次的离线基线和每周重训的在环实验组
- 提出轻量重排干预tail-boost：对低热度商户的打分加权，在可控精度损失下优化生态指标

### 关键结果
所有算法下至少20%的商户会因反馈环流失，其中55%-75%的流失由重训导致；离线精度最高的UR-POI算法会让收入隔离水平比真实情况高15-21%。在15%以内的离线NDCG损失约束下，tail-boost可降低54%-75%的商户流失，同时降低3%-14%的收入隔离，基本不影响用户消费舒适度。

最值得记住的一句话：离线精度不是推荐系统的唯一评估标准，尤其是涉及线下实体场景的推荐，必须纳入在环仿真的长期生态与社会公平指标，否则算法优化反而会加剧社会不平等与商业生态恶化。
