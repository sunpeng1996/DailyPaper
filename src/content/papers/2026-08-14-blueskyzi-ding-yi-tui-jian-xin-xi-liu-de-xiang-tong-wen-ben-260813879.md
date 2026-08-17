---
title: 'Whose Posts Get Ranked: Identical-Text Exposure Gaps in Bluesky Custom Feeds'
title_zh: Bluesky自定义推荐信息流的相同文本内容曝光差距分析
authors:
- Yipeng Wang
- Mohit Singhal
affiliations:
- Northeastern University
arxiv_id: '2608.13879'
url: https://arxiv.org/abs/2608.13879
pdf_url: https://arxiv.org/pdf/2608.13879
published: '2026-08-14'
collected: '2026-08-17'
category: RecSys
direction: 推荐系统 · 信息流排序公平性评估
tags:
- Custom feeds
- Exposure bias
- Algorithmic bias
- Feed recommendation
- Fair ranking
one_liner: 基于Bluesky 1366个自定义feed实测，揭示相同文本曝光差距核心关联作者在对应feed的历史表现
practical_value: '- 做feed/搜索排序公平性评估时，可复用「匹配相同内容+控制发布时间差」的对照组构建方法，排除内容本身的干扰

  - 若业务需要扶持冷启动创作者/商家的内容曝光，需明确在排序逻辑中削弱「账号历史feed表现」权重，降低同内容曝光差距

  - 多独立分发渠道场景下，不能默认多渠道就能解决公平性问题，需单独针对每个渠道的排序规则做公平性校验'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
开放社交平台允许用户自定义部署推荐信息流，但当前缺乏对多独立feed分发场景下相同内容曝光公平性的实证研究。
### 方法
对Bluesky平台1366个公开feed的Top50排序结果做重复快照，匹配文本完全一致、发布时间接近、来自不同作者的帖子组，通过固定效应回归分析曝光差距的关联因素。
### 关键结果
- 33%的匹配组中存在同一文本仅单作者帖子上榜的情况
- 新作者相同内容的 reciprocal-rank 权重低0.061，过往在对应feed有上榜记录的作者曝光更高
- 即使新作者粉丝数更多，74%的同内容 head-to-head 对比中曝光仍更低
- 媒体类型、帖子类型等因素经多重比较校正后无统计显著关联
