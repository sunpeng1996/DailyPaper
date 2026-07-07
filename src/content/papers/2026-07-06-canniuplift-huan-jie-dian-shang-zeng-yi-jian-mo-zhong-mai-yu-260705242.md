---
title: 'CanniUplift: A Holistic Framework for Mitigating Seller and Incentive Cannibalization
  in E-commerce Uplift Modeling'
title_zh: CanniUplift：缓解电商增益建模中卖家与激励蚕食的整体框架
authors:
- Zuwang He
- Shihao Shu
- Yuli Qu
- Hanyu Gao
- Ziliang Zhang
- Diwei Chen
- Xiangda Yan
- Buyu Gao
- Tanchao Zhu
- Yumeng Li
affiliations:
- Taobao & Tmall Group of Alibaba
arxiv_id: '2607.05242'
url: https://arxiv.org/abs/2607.05242
pdf_url: https://arxiv.org/pdf/2607.05242
published: '2026-07-06'
collected: '2026-07-07'
category: RecSys
direction: 电商增益建模 · 蚕食效应缓解
tags:
- Uplift-Modeling
- Cannibalization
- ITE
- E-commerce
- Multi-task-Learning
one_liner: 针对电商SUTVA失效的两类蚕食问题，提出全局对齐+赎回分解的增益建模框架提升平台增量GMV
practical_value: '- 做平台级优惠券/补贴分配的团队，可直接复用PGA模块，在原有单卖家uplift模型基础上增加全局GMV聚合约束，无需额外特征即可缓解跨店蚕食，提升平台整体增量

  - 有红包/优惠券赎回行为数据的场景，可复用RDD模块，将处理组转化拆分为赎回/非赎回两条路径建模，比单纯加赎回辅助任务更能降低激励归因噪音，减少伪增量估计

  - Treat-Attention结构可迁移到所有异质干预响应建模场景（如不同面额优惠券、不同营销活动效果预估），用干预属性作为Query关联用户历史行为序列，更精准捕捉用户对不同干预的敏感度

  - 该框架已在阿里生产环境落地验证，适合多卖家平台的营销资源分配场景，可作为营销Uplift模型迭代的参考方案，预期能实现成本下降、GMV和ROI同步提升'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统Uplift建模依赖SUTVA假设，在多卖家电商场景下存在两类严重问题：一是卖家级蚕食，补贴仅引导用户在不同店铺间转移消费，平台整体GMV无增长甚至下降；二是激励级蚕食，用户使用已有更高额优惠或本身有购买意愿时，模型错把自然转化归因到分配的补贴上，导致增量估计虚高，两类问题都会造成营销资源浪费，无法实现平台全局增长。

### 方法关键点
- 引入**PGA（Platform-level Global Alignment）**模块：在单卖家uplift预估基础上，增加平台级GMV聚合约束，当模型预估多个店铺同时有高uplift时会被全局损失惩罚，隐式学习跨店替代效应，过滤只利好单卖家但损害平台的伪增量。
- 提出**RDD（Redemption-based Decomposition Denoising）**模块：将处理组转化拆分为赎回优惠券、未赎回优惠券两条路径，用赎回行为作为监督，区分真实由分配补贴带来的转化和自然/其他优惠带来的转化，降低激励归因噪音，效果优于单纯增加赎回辅助任务。
- 设计Treat-Attention机制：以候选店铺+优惠券属性为Query，用户历史行为/激励交互序列为Key/Value，精准建模用户对不同干预的异质响应。

### 关键实验
在阿里大规模工业数据集和合成数据集上对比EUEN、DragonNet等SOTA基线，工业数据集上User AUUC相对最优基线提升6.9%，User QINI提升9.1%；线上A/B测试相对生产基线实现营销成本下降2.45%，平台增量GMV提升4.08%，ROI提升6.69%。

### 核心结论
多卖家平台的营销增益建模不能只优化单卖家局部增长，必须从平台全局视角过滤跨主体蚕食和归因噪音，才能真正实现投入产出比的提升。
