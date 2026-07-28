---
title: Singular value soft-thresholding via the polar decomposition
title_zh: 基于极分解的奇异值软阈值计算方法
authors:
- Stephen Becker
affiliations:
- University of Colorado Boulder, Department of Applied Mathematics
arxiv_id: '2607.22484'
url: https://arxiv.org/abs/2607.22484
pdf_url: https://arxiv.org/pdf/2607.22484
published: '2026-07-24'
collected: '2026-07-28'
category: Other
direction: 数值优化 · GPU加速矩阵运算
tags:
- GPU Acceleration
- Singular Value Soft Thresholding
- Polar Decomposition
- Numerical Optimization
- Matrix Operation
one_liner: 提出用极分解替代SVD计算奇异值软阈值，GPU上大幅提速，仅适用于低精度场景
practical_value: '- 涉及核范数正则、奇异值软阈值的LLM/推荐模型训练场景，可将原有SVD实现替换为极分解方案，借助GPU矩阵乘算力优势显著提速

  - 低精度训练、轻量模型量化等对精度容忍度高的场景优先采用该方案，性价比最优

  - 高精度业务场景（如精排模型参数正则计算）不建议使用，避免符号函数不连续性引入的精度误差'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
奇异值软阈值是核范数正则、近端梯度优化的核心子步骤，传统基于SVD的实现通信开销高，GPU上运行效率低下；现有通过极分解计算SVD再求解软阈值的方案仍依赖特征分解、QR分解，性能未达预期。
### 方法关键点
完全绕过SVD步骤，直接通过极分解计算奇异值软阈值；采用Newton-Schulz迭代实现极分解，计算量几乎全部来自矩阵乘法，天然适配GPU并行架构，通信开销远低于SVD、QR等分解算法。
### 关键结果
相比标准SVD实现方案，在GPU上取得显著速度提升；受限于符号函数的不连续性，仅适合低精度应用场景，鲁棒性待后续验证。
