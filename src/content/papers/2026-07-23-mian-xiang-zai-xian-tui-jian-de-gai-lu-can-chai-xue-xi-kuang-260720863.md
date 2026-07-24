---
title: Probabilistic Residual Learning for Online Recommendations
title_zh: 面向在线推荐的概率残差学习框架
authors:
- Wenyuan Wang
- Yusong Zhao
- Zihao Xu
- Hengyi Wang
- Qi Xu
- Zhigang Hua
- Yan Xie
- Yi Wang
- Zihao Zhao
- Bo Long
affiliations:
- Rutgers University
- Meta
- University of Copenhagen
- UIUC
arxiv_id: '2607.20863'
url: https://arxiv.org/abs/2607.20863
pdf_url: https://arxiv.org/pdf/2607.20863
published: '2026-07-23'
collected: '2026-07-24'
category: RecSys
direction: 跨域推荐 · 残差修正与因果去偏
tags:
- Cross-Domain Recommendation
- Residual Learning
- Causal Inference
- User Clustering
- Cold-Start
one_liner: 提出即插即用的概率残差学习框架，结合用户聚类与因果去偏提升任意基础推荐模型的跨域冷启动效果
practical_value: '- 可直接复用PRL的即插即用架构，不改动现有成熟推荐底座（如DLRM、LightGCN）的前提下，通过残差修正模块快速提升跨域/冷启动场景效果，大幅降低底座重训成本

  - 借鉴概率用户聚类+分群建模思路，针对不同用户群训练轻量化残差子模型，比全量用户统一建模效果更优，尤其适配跨国家/跨年龄段的异构用户场景

  - 可复用域级混淆因子边缘化的因果去偏方法，针对电商跨市场的曝光偏差、流行度偏差问题，不需要主动干预收集数据就能实现观测数据去偏，降低跨域迁移的shortcut过拟合风险

  - 针对冷启动用户，可通过少量交互数据推断用户所属聚类，快速匹配对应残差子模型，缓解新用户冷启动的性能衰减'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有深度学习推荐模型黑盒属性强、计算复杂度高，跨域冷启动场景（如新市场拓展、新用户群切入）下难以快速适配，且容易受域内曝光、流行度等混淆因子影响学到虚假关联，同时现有跨域方法大多依赖域间共享用户/物品，落地限制大。

### 方法关键点
- 即插即用架构：固定现有基础推荐模型，仅学习真实标签与基础预测值的残差，不改动底座模型结构与参数
- 概率用户聚类：基于残差分布将用户划分为K个隐式聚类，每个聚类训练专属残差预测子模型，实现本地化建模
- 因果去偏机制：建模域级混淆因子$s_m$，通过do-calculus对混淆因子边缘化，切断混淆因子对用户/物品表征的影响，消除域内虚假关联
- 推理流程：先推断用户所属聚类，调用对应子模型输出去偏后的残差，叠加基础模型预测值得到最终结果

### 关键实验
在XMRec（18个国家市场的电商交互数据集）和MovieLens数据集的跨域冷启动场景下测试，覆盖CDL、DLRM、LightGCN、NCF、PerK共5种主流基础推荐模型：XMRec上Recall@20最高提升8.7倍（NCF底座从0.0131到0.1137），跨国家的品类推荐偏差降低38.5%；MovieLens跨年龄段场景下NDCG@20最高提升277%（NCF底座从0.0251到0.0947）。

### 核心结论
不改动现有推荐底座的前提下，基于残差的分群因果修正，是低代价提升跨域冷启动性能的高性价比方案。
