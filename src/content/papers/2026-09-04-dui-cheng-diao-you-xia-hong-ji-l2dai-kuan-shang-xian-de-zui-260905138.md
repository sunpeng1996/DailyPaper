---
title: 'From 80x to 385x: A Best-Matching-Unit Search at the L2 Roof, Measured Against
  a Symmetrically Tuned Baseline'
title_zh: 对称调优下触及L2带宽上限的最佳匹配单元搜索：最高385倍加速
authors:
- Andrew James Amos
affiliations:
- College of Medicine and Dentistry, James Cook University, Australia
arxiv_id: '2609.05138'
url: https://arxiv.org/abs/2609.05138
pdf_url: https://arxiv.org/pdf/2609.05138
published: '2026-09-04'
collected: '2026-09-08'
category: Training
direction: SOM训练 · GPU kernel性能优化
tags:
- GPU
- CUDA
- Kernel Tuning
- Self-Organizing Map
- BMU Search
- cuSPARSE
one_liner: 对SOM最佳匹配单元搜索与基线cuSPARSE双向对称调优，实现最高385倍加速
practical_value: '- 做算法性能对比需对新方案和基线执行对称调优，避免因基线未充分优化高估自身方案的实际收益

  - BMU搜索的4个优化trick（tile size调优、分块聚类、神经元轴分块、向量化加载）可复用在向量检索、用户聚类等推荐核心场景的GPU加速实现

  - GPU kernel优化可通过roofline模型提前判断性能天花板，避免无意义的过度调优投入'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
当前GPU算法性能对比普遍不对称，仅优化作者自研方案、基线未充分调优会导致结果失真；SOM训练中占主要耗时的最佳匹配单元（BMU）搜索在大规模语料场景下受限于L2带宽，性能存在提升空间。
### 方法关键点
对自研SparseBin SOM算法和cuSPARSE基线采用对称调优策略，通过四个核心杠杆优化BMU搜索：tile size调整、tile成员聚类、神经元轴分块、向量化加载。
### 关键结果
在32×32到512×512的map尺寸下，单epoch速度较原有公开配置提升5.6~10.1倍，相对早期MEDLINE语料所用CUDA实现的加速比从~80x提升至~385x；基线cuSPARSE经对称调优后速度提升2~3倍；调优后kernel达到L2带宽峰值的77%，剩余性能上限仅约1.3x，无大幅优化空间。
