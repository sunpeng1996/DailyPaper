---
title: 'PRISM: Powerful Time Series to Image (TS2I) Representations for Multivariate
  Anomaly Detection'
title_zh: PRISM：面向多元时序异常检测的高性能时序转图像表示框架
authors:
- Mateusz Smendowski
- Kamil Faber
- Piotr Nawrocki
- Nathalie Japkowicz
- Roberto Corizzo
affiliations:
- AGH University of Krakow
- American University
arxiv_id: '2608.03926'
url: https://arxiv.org/abs/2608.03926
pdf_url: https://arxiv.org/pdf/2608.03926
published: '2026-08-04'
collected: '2026-08-06'
category: Other
direction: 多元时序异常检测 · 时序转图像表示
tags:
- Time Series Anomaly Detection
- Multivariate Time Series
- Image Representation
- Transfer Learning
- Computer Vision
one_liner: 提出可插拔时序转图像元工作流PRISM，多元时序异常检测性能超越24种时域基线
practical_value: '- 电商/广告场景的流量异常、用户行为异常检测任务可直接复用PRISM的时序转图像映射框架，降低时序特征工程成本

  - 可借鉴MSM统计通道构建方法替代PCA，优化高维时序数据的特征压缩效果，提升异常识别精度11-27%

  - 迁移ImageNet预训练视觉编码器做时序异常检测时，可直接冻结编码器参数仅微调头部，训练速度提升1.8倍且仅损失8%性能

  - 做业务时序异常检测基线选型时，可参考PRISM的7000+实验结论，优先测试时序转图像+视觉backbone方案'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
多元时序异常检测（TSAD）性能高度依赖特征表示设计，现有高维时序转多通道图像的映射规则不明确，视觉backbone能否匹敌时域基线方案尚无统一结论。
### 方法关键点
1. 提出可插拔元工作流PRISM，支持系统化构建与评估基于图像表示的多元TSAD方案
2. 明确通道化设计为核心优化维度，提出基于统计的MSM通道构建方案替代传统PCA
3. 支持对接ImageNet预训练视觉编码器，可选择冻结或微调参数
### 关键结果
累计7000+实验验证，最优PRISM配置在14个数据集的10个上取得VUS-PR最优，较最优竞品平均提升41%；MSM方案较PCA方案性能提升11-27%；冻结预训练视觉编码器可保留92%微调性能，训练速度提升1.8倍
