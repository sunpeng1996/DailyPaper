---
title: 'An analysis of binary isotonic regression: degrees of freedom and implications
  for calibration'
title_zh: 二元保序回归分析：自由度刻画及校准应用启示
authors:
- Raphael Rossellini
- Rina Foygel Barber
- Zhimei Ren
- Jake A. Soloff
affiliations:
- Department of Statistics, University of Chicago
- Department of Statistics and Data Science, University of Pennsylvania
- Department of Statistics, University of Michigan
arxiv_id: '2607.27301'
url: https://arxiv.org/abs/2607.27301
pdf_url: https://arxiv.org/pdf/2607.27301
published: '2026-07-29'
collected: '2026-08-01'
category: Training
direction: 概率校准 · 保序回归理论分析
tags:
- Isotonic Regression
- Calibration
- ECE
- Degree of Freedom
- Binary Classification
one_liner: 推导二元样本保序回归自由度精确紧界，给出首个无分布ECE理论保证
practical_value: '- 电商CTR/CVR预估场景下，用保序回归做概率校准时，可直接复用该论文给出的ECE无分布界，量化校准方案的泛化风险，避免过拟合

  - 小流量实验下的模型校准，可参考该自由度界调整保序回归的分桶粒度，平衡校准精度与泛化性能

  - 排序/召回模型输出概率校准无需额外假设数据分布，即可评估校准误差的理论上限，减少校准调优的试错成本'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
保序回归是二元分类器概率校准的通用后处理工具，但现有研究缺乏二元样本下有限样本自由度的精确刻画，也无无分布的预期校准误差（ECE）理论保证，无法量化校准方案的泛化风险。
### 方法关键点
通过解析数论定位最大化保序回归不同拟合值数量的二元序列，推导得到最坏情况自由度的精确紧界；基于确定性自由度界推导ECE的无分布保证，仅要求标签为二元变量。
### 关键结果
自由度紧界主项为 $rac{3}{(4\pi^2)^{1/3}} n^{2/3}$，优于此前所有边界；得到首个非平凡的无分布保序回归ECE理论保证，完全不依赖模型与数据分布假设。
