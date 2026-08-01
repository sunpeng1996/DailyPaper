---
title: Adaptive Nyström for Gaussian Process Regression
title_zh: 面向高斯过程回归的自适应Nyström方法
authors:
- Lulu Kang
affiliations:
- University of Massachusetts Amherst, Department of Mathematics and Statistics
arxiv_id: '2607.27427'
url: https://arxiv.org/abs/2607.27427
pdf_url: https://arxiv.org/pdf/2607.27427
published: '2026-07-29'
collected: '2026-08-01'
category: Training
direction: 高斯过程回归 · 低秩近似训练加速
tags:
- Gaussian Process Regression
- Nyström
- Low-rank Approximation
- Uncertainty Quantification
- Scalable Training
one_liner: 提出贪心选地标点+交错超参优化的自适应Nyström方法，实现近精确GP精度的线性可扩展GPR
practical_value: '- 可复用自适应Nyström的地标点贪心选择策略，优化推荐系统中GPR类不确定性估计模块的训练效率，解决大规模样本下的计算瓶颈

  - 交错地标点扩张与超参优化的框架可迁移至其他低秩近似任务，比如召回层内核矩阵快速计算、用户兴趣嵌入压缩

  - 线性扩展的GPR方案可直接应用于电商冷启动场景的销量预测、用户偏好不确定性建模，在保证精度的前提下降低计算成本'
score: 6
source: arxiv-stat.ML
depth: abstract
---

**动机**：GPR是鲁棒的不确定性量化框架，但O(n³)的计算复杂度限制了其在大规模场景下的落地；传统Nyström低秩近似可将复杂度降至O(nm²)，但精度高度依赖地标点选择，静态选择方案效果不稳定。
**方法关键点**：自适应Nyström方法通过贪心策略选择地标点，最小化核近似误差的迹残差；区别于静态近似方案，将地标点扩张与超参优化交错执行，使地标选择随协方差结构的优化自适应调整。
**关键结果**：在5个基准函数实验中，精度和稳定性显著优于随机地标点选择方案；预测性能与精确GP推理相当，同时计算复杂度随样本量线性扩展。
