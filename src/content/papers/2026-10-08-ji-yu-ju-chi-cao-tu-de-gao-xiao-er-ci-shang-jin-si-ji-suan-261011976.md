---
title: Efficient quadratic entropy with distance sketches
title_zh: 基于距离草图的高效二次熵近似计算方法
authors:
- Steve Huntsman
affiliations:
- Cynnovative
arxiv_id: '2610.11976'
url: https://arxiv.org/abs/2610.11976
pdf_url: https://arxiv.org/pdf/2610.11976
published: '2026-10-08'
collected: '2026-10-10'
category: Other
direction: 大规模熵计算 · 语义离散度度量
tags:
- Quadratic Entropy
- Distance Sketch
- Random Feature
- Scalable Computing
- Semantic Dispersion
one_liner: 提出基于距离草图的可扩展二次熵近似方法，大幅降低大规模场景下的计算与内存开销
practical_value: '- 推荐系统多样性度量场景下，可复用该方法低开销计算百万级物料分布的语义离散度，无需构造两两距离矩阵

  - 用户兴趣建模中，可快速计算单用户行为序列的兴趣分散程度，适配距离固定、多用户分布动态更新的场景，摊销计算开销

  - 召回/粗排pipeline中可将该二次熵作为多样性正则项嵌入loss，计算复杂度低不会显著增加训练/推理耗时'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有二次熵计算需显式构造样本两两距离矩阵，在样本量十万级、特征维度上百的大规模场景下，内存与时间开销过高，无法支撑多分布批量计算需求。
### 方法关键点
1. 针对欧氏、球面测地线等负型距离，基于随机特征嵌入与投影简化二次熵计算逻辑，避免显式构造完整距离矩阵
2. 摊销单次大矩阵乘法开销，结合控制变量法，适配距离固定、分布p动态变化的高频计算场景
3. 采用无偏蒙特卡洛估计，保证结果精度的同时大幅降低计算复杂度
### 关键结果
在OGB数据集上对比直接成对采样方法，内存与运行时间显著降低，可仅通过引用与文本特征快速识别跨学科影响力范围宽/窄的论文、领域及机构
