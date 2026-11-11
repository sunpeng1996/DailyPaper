---
title: 'Hidden Distances: How Likert-Scale Spacing Shapes Algorithmic Voting Advice'
title_zh: 隐性偏差：李克特量表间距如何影响投票推荐算法结果
authors:
- Thomas Broholt Knudsen
- Christian Høst-Madsen
- Vedran Sekara
- Jonas L. Juul
affiliations:
- IT University of Copenhagen, Denmark
- Pioneer Centre for AI (P1), Denmark
arxiv_id: '2611.12313'
url: https://arxiv.org/abs/2611.12313
pdf_url: https://arxiv.org/pdf/2611.12313
published: '2026-11-09'
collected: '2026-11-11'
category: RecSys
direction: 推荐系统 · 量表量化偏差分析
tags:
- Likert Scale
- Recommender System
- Matching Bias
- Sensitivity Analysis
- Preference Matching
one_liner: 量化李克特量表间距赋值参数对投票推荐结果的影响，证实隐性设计选择可产生重大选举效应
practical_value: '- 基于李克特量表做用户偏好匹配的场景（如商品偏好调研、兴趣标签打分），需先做间距赋值的敏感性分析，避免隐性偏差导致推荐结果偏移

  - 涉及匹配类推荐的核心参数（如相似度计算权重、阈值）要做透明度披露，规避算法结果公正性合规风险

  - 可复用α参数化方法量化离散打分选项的赋值差异对推荐结果的影响，快速定位核心敏感参数'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
投票推荐系统（VAA）广泛采用李克特量表收集用户/候选人偏好，计算匹配度时的量表选项赋值无实证依据，其对推荐结果的实际影响未被量化。
### 方法
引入参数α定义「同意/不同意」到「强烈同意/强烈不同意」的距离与「中立」到「同意/不同意」距离的比值，基于丹麦主流VAA全量数据量化不同α取值对推荐结果的影响。
### 关键结果
- 从等距赋值改为α=2时，37.7%的top候选人匹配、21.9%的top政党匹配结果发生变化，无任何用户/候选人回答变更
- 低α值偏向立场强硬的候选人，部分政党推荐量最高提升19.6%；高α值偏向温和派候选人，女性候选人推荐量随α升高而上升
- 结合用户行为数据估算，α取值变化可导致丹麦议会175个席位中4-13个席位偏移，影响幅度接近选举胜负阈值
