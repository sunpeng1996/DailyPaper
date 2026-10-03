---
title: 'From Scroll to Sale: Exploring the Impact of Interaction Type and Device Price
  on TikTok Advertisements'
title_zh: 《从划屏到成交：探究交互类型与设备价格对TikTok广告的影响》
authors:
- Nazanin Sabri
- Cat Mai
- Haodi Zou
- Isha Varada
- Damon McCoy
- Deepak Kumar
- Kristen Vaccaro
affiliations:
- University of California San Diego
- New York University
arxiv_id: '2610.00684'
url: https://arxiv.org/abs/2610.00684
pdf_url: https://arxiv.org/pdf/2610.00684
published: '2026-09-30'
collected: '2026-10-03'
category: RecSys
direction: 短视频广告推荐策略实证研究
tags:
- TikTok
- Ad Recommendation
- Dynamic Pricing
- User Segmentation
- Empirical Study
one_liner: 通过受控实验量化TikTok广告负载、内容与用户交互、设备价格的关联规律
practical_value: '- 可将设备价格作为用户收入分层的低成本特征，用于差异化广告投放：高价值设备用户降低广告负载提升体验，低端设备用户优先推送折扣类转化广告

  - 可将用户点赞/分享行为、平台停留时长作为广告负载上调的触发信号，在可控的用户体验折损范围内提升广告变现效率

  - 广告策略灰度测试可复用本文的受控账号+多组对照设备的实验范式，减少用户属性混淆变量对实验结论的干扰'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 动机
当前靶向广告研究多聚焦年龄、性别等人口属性，短视频平台基于收入分层的差异化广告投放规律缺乏公开量化审计数据，动态定价策略的实际落地效果也未得到系统性验证。
### 方法关键点
采用56个自动化账号、12台分低/中/高三档价格的设备（作为用户收入代理），累计收集超8万条TikTok视频数据，控制变量测试设备价格、交互类型（点赞/评论/分享）、人口属性对广告负载、广告内容的影响。
### 关键结果
整体广告负载为29.4%；用户点赞/分享行为、平台停留时长均会显著提升广告负载；高端设备用户接收的广告数量更少，低端设备用户收到的折扣类广告占比更高。
