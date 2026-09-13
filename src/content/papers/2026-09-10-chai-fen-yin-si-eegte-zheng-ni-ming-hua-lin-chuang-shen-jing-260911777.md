---
title: 'Differentially Private EEG Feature Anonymization: A Privacy-Utility Case Study
  in Clinical Neurophysiology'
title_zh: 差分隐私EEG特征匿名化：临床神经生理学的隐私-效用案例研究
authors:
- Noman Sadiq
- Mohsen Toorani
affiliations:
- University of South-Eastern Norway
- Department of Science and Industry Systems, University of South-Eastern Norway
arxiv_id: '2609.11777'
url: https://arxiv.org/abs/2609.11777
pdf_url: https://arxiv.org/pdf/2609.11777
published: '2026-09-10'
collected: '2026-09-13'
category: Other
direction: 差分隐私 · 敏感数据匿名化
tags:
- Differential Privacy
- Anonymization
- Privacy-Utility Tradeoff
- Healthcare AI
- Data Protection
one_liner: 面向临床EEG特征的差分隐私匿名化方案，覆盖三类部署场景并验证隐私与效用的权衡关系
practical_value: '- 高斯/拉普拉斯噪声校准、灵敏度计算方法可复用在电商用户敏感行为特征的匿名化处理场景

  - 三类DP部署架构（客户端/服务端/去中心化训练）的设计思路可参考跨域推荐的用户隐私保护方案

  - 隐私-效用 tradeoff 量化评估逻辑可用于敏感特征处理后下游推荐/广告任务的效果验证'
score: 3
source: arxiv-cs.LG
depth: abstract
---

### 动机
临床EEG数据用于医疗AI研发时存在敏感信息泄露风险，传统匿名化方案无法应对高维生物信号的重识别、关联推理风险，而强隐私保护又会过度破坏数据特征降低临床效用。

### 方法关键点
- 覆盖三类部署场景：客户端匿名化、中心化服务端匿名化、去中心化本地训练，设计对应的用户级差分隐私保护方案
- EEG预处理及特征提取后，分别注入高斯、拉普拉斯扰动，单独推导全向量校准所需的噪声尺度，通过统计指标和下游ML任务双维度验证数据效用

### 关键结果
差分隐私扰动可无缝集成到EEG处理工作流中，但噪声机制选择、隐私参数配置、灵敏度校准三个因素对数据效用影响极强；小样本、不平衡的临床数据集下，保留下游任务效用的难度显著提升
