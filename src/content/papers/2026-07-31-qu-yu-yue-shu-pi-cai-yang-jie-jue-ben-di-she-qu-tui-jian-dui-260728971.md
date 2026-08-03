---
title: 'Don''t Contrast the Impossible: Region-Constrained Batching for Contrastive
  User Modeling on a Local Community Platform'
title_zh: 区域约束批采样解决本地社区推荐对比学习不可能负样本问题
authors:
- Seungho Han
- Byeongchang Kim
- Jin Yu
affiliations:
- Danggeun Market Inc. (Karrot)
arxiv_id: '2607.28971'
url: https://arxiv.org/abs/2607.28971
pdf_url: https://arxiv.org/pdf/2607.28971
published: '2026-07-31'
collected: '2026-08-03'
category: RecSys
direction: 推荐系统 · 对比学习负采样优化
tags:
- Contrastive Learning
- Negative Sampling
- User Modeling
- Recommender System
- Local Service
one_liner: 提出区域约束批采样RCBS，消除对比学习地理不可能负样本，提升用户表征与全链路推荐效果
practical_value: '- 本地生活/到店/外卖等带地理约束的推荐业务，可直接用区域同质批构建替换随机批，无需改模型损失即可获得效果提升，落地成本极低

  - 对比学习负采样可先区分系统规则导致的「不可能负样本」与用户主动不交互的「可行负样本」，优先剔除不可能负样本即可天然获得高质量硬负样本

  - RCBS可与IPS等倾向纠偏方法叠加：RCBS先过滤零曝光的不可能负样本，IPS再校正可行样本内的曝光不均，适配更复杂的业务场景

  - 预训练得到的用户表征可直接作为特征注入下游排序、召回、广告模型，增量收益明显，可复用这套预训练+下游注入的落地流程'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
本地社区、外卖、到店等区域约束类推荐平台存在天生的曝光规则限制，86%以上的交易发生在5km半径内，用户根本看不到区域外的物品。传统对比学习的随机批采样会混入大量这类系统规则导致的「不可能负样本」，这类样本无任何用户偏好信号，会严重稀释对比学习损失的有效性，而现有IPS等纠偏方法要求所有样本曝光概率大于0，无法处理这类天生零曝光的负样本。
### 方法关键点
- 提出RCBS（Region-Constrained Batch Sampling），仅修改批构建逻辑，不改动模型架构、损失函数，改造成本极低
- 先将地理空间划分为离散区域单元格，按用户所属区域对用户分组，每个mini-batch仅采样同一区域的用户，确保批内绝大多数物品都是用户可触达的可行负样本
- 支持不同粒度的区域划分与用户自定义曝光半径，可与IPS等损失层纠偏方法完全兼容，叠加使用效果更佳
### 关键结果
实验基于Karrot平台2年生产日志（25M用户、15B行为），对比传统随机批采样基线：
- 预训练任务Recall@10从0.1提升至0.149（+49%），批内不可能负样本占比从98%降至30%
- 下游任务：Feed排序NDCG@10+1.18%，广告排序PR-AUC+3.38%，Feed召回Recall@10+7.56%
- 在线A/B测试：Feed点击+10%，广告CTR+7.46%，eCPM+6.01%，目前已全量部署生产
### 核心结论
对比学习负采样首先要剔除系统规则导致的不可能负样本，可行负样本本身就是更高质量的硬负样本，比复杂的硬负样本挖掘方法改造成本更低、收益更稳
