---
title: 'TAGR: Temporally Adaptive Generative Recommendation for Industrial Live-Streaming
  Advertising'
title_zh: 面向工业级直播广告的时序自适应生成式推荐框架TAGR
authors:
- Wencai Ye
- Guangyi Liu
- Chaoyi Wang
- Wenbin Luo
- Shengyu Wang
- Mingjie Sun
- Peng Wang
- Quanming Yao
- Wenjin Wu
- Peng Jiang
affiliations:
- Kuaishou Technology
- Tsinghua University
arxiv_id: '2608.24034'
url: https://arxiv.org/abs/2608.24034
pdf_url: https://arxiv.org/pdf/2608.24034
published: '2026-08-25'
collected: '2026-08-26'
category: GenRec
direction: 生成式推荐 · 动态Semantic ID与时序适配
tags:
- Generative Recommendation
- Semantic ID
- Live-Streaming Advertising
- Temporal Adaptation
- Preference Optimization
one_liner: 在Token、用户意图、偏好对齐三层实现时序自适应的直播广告生成式推荐系统
practical_value: '- 短时效/动态标的（直播、限时商品、动态广告）生成式推荐可复用LSID设计：固定分层词表+定期刷新ID映射，无需全量重建索引，同时兼顾内容实时性与生成稳定性

  - 生成式推荐的NTP损失可引入多维度加权：用反馈深度（加购>点击>曝光）做意图置信度权重、用eCPM/用户价值做业务价值权重，同时优化相关性与商业收益

  - 工业场景RL训练不稳定时可复用IOPO思路：间歇性插入GRPO更新与常规NTP训练交替，既用到当前策略的新鲜反馈，又避免偏离历史行为分布导致训练崩溃

  - 生成式召回落地可参考其架构：LSID到实际标的的实时双向索引+beam search优化，L20 GPU单卡支持2500 QPS、延迟<100ms，满足大规模流量要求'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
直播广告是短视频、电商平台的核心变现渠道，其直播场景、带货商品、用户反馈变化速度远快于常规电商场景：现有生成式推荐依赖静态Semantic ID无法表征动态变化的直播标的，单尺度行为建模难以捕捉用户快速漂移的意图，偏好优化也无法平衡新鲜on-policy反馈与训练稳定性，导致效果无法满足工业场景要求。

### 方法关键点
- Token层：Live Semantic-Collaborative ID（LSID）固定分层词表，仅定期刷新活跃直播广告的ID映射（结合实时场景、商品特征与用户协同信号），无需全量重建索引即可适配直播标的动态变化
- 意图层：Intent-Aware Generation（IAG）对用户进房序列做1/2/10多步长粒度编码，点赞/加购/下单等辅助行为单独作为输入通道，MF-NTP损失按后验反馈深度、用户价值层级、eCPM分位加权，区分不同样本的监督强度
- 对齐层：Intermittent On-Policy Preference Optimization（IOPO）间歇性插入当前策略采样的GRPO更新，其余时间保留NTP监督训练，同时结合行为对齐、价值对齐双奖励，兼顾反馈新鲜度与训练稳定性

### 关键结果
在快手十亿级直播广告数据集上，对比生产基线DLRM，线上A/B测试实现直播间进房率提升8.5%、加购点击率提升7.4%、广告收入提升16.1%，冷启动直播间收入提升18.4%；生成式召回单L20 GPU支持2500 QPS，端到端延迟<100ms，满足工业落地要求。

> 值得记住：非稳态场景下的生成式推荐需从Token表征、用户建模、训练优化全链路做时序适配，才能同时兼顾相关性、稳定性与商业价值
