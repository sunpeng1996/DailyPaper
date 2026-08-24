---
title: 'The Exceedance Design Effect: Effective Sample Size for Thresholds under Clustering'
title_zh: 聚类场景下阈值校准的有效样本量与超量设计效应
authors:
- Adam Noonan
affiliations:
- Independent Researcher
arxiv_id: '2608.21262'
url: https://arxiv.org/abs/2608.21262
pdf_url: https://arxiv.org/pdf/2608.21262
published: '2026-08-21'
collected: '2026-08-24'
category: Other
direction: 统计校准 · 阈值有效样本量计算
tags:
- Effective Sample Size
- Conformal Prediction
- Threshold Calibration
- Clustered Data
- Reliability Estimation
one_liner: 推导聚类关联数据下阈值计算专属有效样本量闭式解，修正现有共形预测校正偏差
practical_value: '- 推荐/广告场景做置信度拒答、违规内容过滤、共形预测的阈值校准时，若校准样本存在聚类关联（如同用户/同query的多组样本），不可直接使用传统有效样本量校正，需按目标阈值位置单独计算有效样本量

  - 共形预测落地时可直接复用论文提出的闭式公式计算实际有效样本量，修正现有共形校正方法的双向偏差，避免上线后阈值实际覆盖率不达标

  - 阈值上线前的可靠性验证不能仅参考多轮平均覆盖率，需单独计算对应分位点的有效样本量，规避单次部署的偏差风险'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
当前共形预测、模型拒答门、安全过滤等ML系统普遍基于校准集分位点设置阈值，效果保证默认校准样本独立，但工业场景样本常存在聚类关联（共享prompt、用户、query等），传统仅适用于均值统计的有效样本量校正方法完全不适用。
### 方法关键点
推导了阈值场景专属的有效样本量闭式法则，其取值仅取决于聚类样本落在阈值同侧的频率，随阈值位置动态变化，与样本数值相似度无直接关联。
### 关键结果
1. 现有共形领域通用校正方法存在双向偏差；
2. 数据集不存在统一有效样本量，每个阈值对应独立的有效样本量；
3. 25028条公开校准集的实际可靠样本量仅约1300；
4. 多轮平均覆盖率无法发现聚类带来的偏差，单次部署会完全承受偏差影响。
