---
title: 'Cheaper is Better: A Discount-Aware Network for Conversion Rate Prediction
  in E-commerce Recommendation System'
title_zh: 折扣感知网络DANet：面向电商推荐场景的转化率预估模型
authors:
- Ruocong Tang
- Yang Huang
- Xing Fang
- Chenyi Yan
- Chuike Sun
- Jing Wang
arxiv_id: '2607.12578'
url: https://arxiv.org/abs/2607.12578
pdf_url: https://arxiv.org/pdf/2607.12578
published: '2026-07-14'
collected: '2026-07-15'
category: RecSys
direction: 电商推荐 · CVR预估 折扣特征建模
tags:
- CVR Prediction
- E-commerce Recommendation
- Feature Engineering
- Debias
- Discount Modeling
one_liner: 提出融合折扣特征建模的DANet网络，优化电商CVR预估，已落地阿里巴巴天猫APP
practical_value: '- 电商CVR/GMV预估场景可新增折扣率作为核心特征，通过傅里叶时频变换捕捉商品长期折扣趋势，避免短期随机促销波动干扰模型学习

  - 可复用分布去偏模块消除折扣特征分布偏移，覆盖促销组合差异、大促/日常周期差异带来的偏差，提升模型跨场景泛化能力

  - 新增折扣率预测的辅助回归任务，用显式标签约束折扣特征学习，可同时提升CVR精度与GMV正向收益，适配大促等折扣敏感场景'
score: 10
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有电商CVR预估方法大多忽略折扣率这一直接影响用户购买决策的核心定价特征，且折扣特征易受促销组合、平台大促周期影响存在分布偏差，进一步放大样本选择偏误对模型效果的影响。

### 方法关键点
提出折扣感知网络DANet，包含三个核心模块：1. 时频变换模块，基于傅里叶变换提取折扣率频谱，捕捉商品长期折扣趋势，过滤短期促销波动噪声；2. 分布去偏模块，消除用户侧折扣感知偏差，覆盖不同促销组合、大促周期带来的特征偏移；3. 新增折扣率预测的有监督回归辅助任务，通过显式折扣标签约束特征学习，提升估值精度。

### 关键结果
离线实验AUC较基线提升1.61%；线上A/B测试pCVR提升3.63%，GMV提升2.23%，已正式部署于阿里巴巴天猫APP，代码已开源。
