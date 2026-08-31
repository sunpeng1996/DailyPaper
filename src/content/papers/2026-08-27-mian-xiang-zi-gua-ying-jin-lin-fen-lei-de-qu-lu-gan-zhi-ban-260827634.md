---
title: Curvature-Aware Radius Shrinkage for Adaptive Nearest Neighbor Classification
title_zh: 面向自适应近邻分类的曲率感知半径收缩方法
authors:
- Alexandre L. M. Levada
affiliations:
- Federal University of São Carlos
arxiv_id: '2608.27634'
url: https://arxiv.org/abs/2608.27634
pdf_url: https://arxiv.org/pdf/2608.27634
published: '2026-08-27'
collected: '2026-08-31'
category: Other
direction: 自适应近邻分类 · 流形几何优化
tags:
- k-NN
- manifold curvature
- adaptive neighbor search
- intrinsic dimensionality
- classification
one_liner: 提出曲率感知的自适应近邻框架CARSANN，通过局部曲率控制搜索半径提升k-NN分类性能
practical_value: '- 召回阶段的向量近邻搜索可借鉴该思路：针对用户/Item embedding空间的高曲率区域缩小搜索半径，减少噪声召回，提升召回精准度

  - 可将embedding流形的局部曲率作为辅助特征融入排序模型，适配不同特征区域的分布差异，提升排序效果

  - 冷启动场景下，可基于特征空间局部曲率调整近邻采样范围，提升冷启动用户/Item的标签预测与匹配准确率'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
传统k-NN在全特征空间采用固定邻域基数，无法适配底层流形局部几何差异大的异构数据特性，泛化性能受限。
### 方法关键点
1. 先通过TwoNN算法估计数据本征维度，基于PCA生成数据的本征表示；
2. 基于形状算子估计局部平均曲率，动态控制邻域搜索尺度：高曲率区域大幅收缩搜索半径，平坦区域保留较大搜索范围，区别于仅调整邻域数量或局部度量的现有自适应近邻方法。
### 关键结果
- 在70+ OpenML真实数据集上性能优于标准k-NN，与现有自适应近邻方法效果相当；
- 相同基础邻域规模下，45个数据集中40个取得更高均衡准确率，平均均衡准确率从0.6506提升至0.7528；
- 相比固定k=5的标准k-NN，平均均衡准确率从0.6547提升至0.7568，所有提升效果均通过统计显著性检验。
