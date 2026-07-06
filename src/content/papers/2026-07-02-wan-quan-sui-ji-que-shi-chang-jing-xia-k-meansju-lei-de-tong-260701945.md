---
title: Statistical Properties of $k$-means Clustering for Data Missing Completely
  at Random
title_zh: 完全随机缺失场景下k-means聚类的统计性质
authors:
- Xin Guan
affiliations:
- Graduate School of Information Sciences, Tohoku University
arxiv_id: '2607.01945'
url: https://arxiv.org/abs/2607.01945
pdf_url: https://arxiv.org/pdf/2607.01945
published: '2026-07-02'
collected: '2026-07-06'
category: Other
direction: 缺失数据k-means聚类理论分析
tags:
- k-means
- Missing Data
- MCAR
- Clustering
- Statistical Theory
one_liner: 推导缺失数据尤其是MCAR场景下k-means的统计性质，给出严格理论保障
practical_value: '- 电商用户/物品分群时，若特征属于MCAR缺失，可参考论文给出的缺失概率、簇间距充分条件校验k-means聚类结果可靠性

  - 高维稀疏特征场景（如用户行为特征缺数多）下用k-means需注意：仅当簇中心在所有维度均有差异时，收敛性才有理论保证

  - 若缺数场景下k-means聚类结果波动大，可先校验特征缺失率是否超过理论阈值，再调整特征筛选或补全策略'
score: 4
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有面向缺失数据的k-means改进方案多聚焦实际精度提升，缺乏渐近层面的理论支撑，无法为落地场景的结果可靠性提供依据。
### 方法关键点
1. 通用缺失机制下建立√n阶超额风险界，证明估计簇中心的一致性；
2. 针对MCAR（完全随机缺失）场景，推导簇中心估计的√n收敛率与渐近正态性；
3. 给出缺失概率、真实簇间距的充分条件，可判断缺数场景下估计的簇中心是否收敛到全量数据的真实中心；
4. 明确MCAR下达到√n收敛率的前提是k个真实中心在所有维度均不同，高维场景适配存在显著挑战。
### 关键结果
所有理论结论均通过合成缺数数据集的数值模拟验证，可为缺数场景下k-means的工业应用提供严谨理论指导。
