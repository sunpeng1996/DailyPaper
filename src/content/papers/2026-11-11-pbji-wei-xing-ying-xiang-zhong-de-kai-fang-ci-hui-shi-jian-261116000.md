---
title: 'Predicting the Needle in a Petabyte Scale Haystack: Open-Vocabulary Event
  Anticipation in Satellite Imagery'
title_zh: PB级卫星影像中的开放词汇事件预测方法
authors:
- Shreelekha Revankar
- Mikhail Klassen
- Creon Levit
- Ash Hoover
- Kavita Bala
- Bharath Hariharan
affiliations:
- Planet Labs
- Cornell University
arxiv_id: '2611.16000'
url: https://arxiv.org/abs/2611.16000
pdf_url: https://arxiv.org/pdf/2611.16000
published: '2026-11-11'
collected: '2026-11-15'
category: Other
direction: 卫星影像 · 开放词汇事件预测
tags:
- Vision-Language Model
- Open-Vocabulary
- Event Forecasting
- Unsupervised Data Mining
- Remote Sensing
one_liner: 利用跨时间视觉语言嵌入向量差实现无标注卫星事件自动发现与长周期预判
practical_value: '- 跨时间点嵌入向量差的语义变化检测思路，可迁移到推荐系统用户兴趣漂移预判、内容生命周期变化建模场景，大幅提升变化检测效率

  - 无标注自动数据引擎的构建方法，可复用在电商/广告领域长尾稀有样本批量挖掘，降低人工标注成本

  - 长周期时序事件完成时间预测方案，可迁移到新品生命周期预判、营销活动效果峰值时间预估等业务场景'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
全球每日卫星影像规模达PB级，提前预判森林砍伐、城市建设等事件可实现及时干预，但现有方案无法同时完成开放词汇下的事件位置、类型、结束时间预测，且稀有事件人工标注成本极高，无法覆盖全球规模。
### 方法关键点
将不同时间点卫星影像的vision-language model嵌入的向量差作为语义变化表征，直接在隐空间搜索语义变换：1）构建无人工标注的全球事件自动发现引擎；2）生成含2.1万+位置、64+事件类型、200万+影像的全球最大卫星事件数据集SatEvents-21k；3）训练全局事件预测模型。
### 关键结果数字
事件变化检测最高F1达93.5%，预测事件检索效果超基线3.5倍，事件结束时间预测中位数误差仅3天，最远可提前9个月完成预测。
