---
title: Native Multimodal Representation Learning for Click-Through Rate Prediction
  in E-Commerce Scenarios
title_zh: 面向电商场景点击率预测的原生多模态表示学习
authors:
- Chao Yi
- Feifan Yang
- Jiawei Feng
- Sishuo Chen
- Zhangming Chan
- Xiang-Rong Sheng
- Han Zhu
affiliations:
- Taobao & Tmall Group of Alibaba
- University of Science and Technology of China
- Peking University
arxiv_id: '2608.24091'
url: https://arxiv.org/abs/2608.24091
pdf_url: https://arxiv.org/pdf/2608.24091
published: '2026-08-25'
collected: '2026-08-26'
category: RecSys
direction: 多模态CTR预测 · 原生表示学习范式
tags:
- Multimodal Representation
- CTR Prediction
- E-commerce Recommendation
- Contrastive Learning
- Representation Alignment
one_liner: 提出Mine-Then-Train范式解决多模态编码器端到端训练CTR失效问题，在淘宝广告场景获CTR+1.5%、RPM+0.5%提升
practical_value: '- 放弃直接端到端联合训练多模态编码器和CTR模型的思路，可规避训练成本激增25倍+效果下降的工业落地坑

  - 可复用Mine-Then-Train范式：先训练轻量化残差标注模型挖掘CTR中多模态可解释的高质量三元组，再微调预训练多模态编码器，兼顾对齐CTR目标和保留原有语义能力

  - 多模态表示接入CTR模型的两种成熟方案可直接复用：一是计算目标与用户历史行为的语义相似度作为特征，二是与ID特征线性融合，无额外架构改造成本

  - 标注模型采用Residual Tuning+Semantic ID设计，既不破坏预训练编码器的通用语义能力，又能高效学习CTR场景增量信息，训练成本远低于端到端方案'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前工业界多模态特征用于CTR预测普遍采用两阶段范式：先预训练多模态编码器，再提取特征接入CTR模型，但预训练任务与CTR优化目标存在天然gap，限制效果上限。尝试端到端联合训练多模态编码器和CTR模型反而出现效果下降、训练成本激增的问题，核心原因是CTR数据中混杂大量非多模态语义驱动的行为（价格对比、误点、位置偏置、兴趣疲劳等），会给参数共享的多模态编码器带来歧义监督，导致更新方向不一致。

### 方法关键点
- 提出Mine-Then-Train范式，分挖掘、训练两阶段，避免编码器直接接触歧义CTR监督信号
- 挖掘阶段：基于残差调优架构训练轻量化多模态标注模型，用Semantic ID嵌入学习CTR场景增量信息，过滤得到同时满足语义相关、有明确用户偏好差异、原有多模态表示无法覆盖的高质量三元组样本
- 训练阶段：用三元组margin损失+原SCL对比损失联合微调预训练多模态编码器，既对齐用户点击偏好，又避免遗忘原有细粒度电商语义能力

### 关键实验
基于淘宝广告场景1.9B行为样本、88M商品、84M用户的真实业务数据，对比已上线的SCL预训练多模态编码器基线：
- 离线：GAUC提升0.22%，AUC提升0.11%
- 线上A/B测试：CTR提升1.5%，RPM提升0.5%
- 端到端训练对照：所有端到端变体均比基线GAUC最高下降0.3%，训练成本最高提升25倍

### 核心结论
多模态编码器的参数共享特性使其对CTR数据噪声的敏感度远高于独立ID特征，直接端到端训练得不偿失，通过数据层过滤高质量监督信号是更适合工业落地的多模态表示对齐方案。
