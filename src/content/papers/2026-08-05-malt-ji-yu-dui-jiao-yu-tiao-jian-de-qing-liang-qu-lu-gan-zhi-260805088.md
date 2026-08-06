---
title: 'MALT: Lightweight Curvature-Aware Muon via Diagonal Preconditioning'
title_zh: MALT：基于对角预条件的轻量曲率感知Muon优化器
authors:
- Tongle Wu
- Huanyu Dong
- Ying Sun
- Ziye Ma
affiliations:
- The Pennsylvania State University
- City University of Hong Kong
arxiv_id: '2608.05088'
url: https://arxiv.org/abs/2608.05088
pdf_url: https://arxiv.org/pdf/2608.05088
published: '2026-08-05'
collected: '2026-08-06'
category: Training
direction: 大模型训练 · 优化器设计
tags:
- Optimizer
- Muon
- LLM Pre-training
- Diagonal Preconditioning
- Stochastic Optimization
one_liner: 为Muon引入轻量双边对角预条件，低开销解决曲率各向异性，提升LLM预训练效果
practical_value: '- 训练电商垂域LLM（商品理解、query理解、生成式推荐文案模型等）时，可直接替换AdamW/Muon使用MALTER，收敛速度更快，且内存、耗时开销几乎无增长

  - 业务场景下做优化器二次开发时，可复用「轻量行列对角预条件+正交化+norm grafting」的范式，无需实现复杂的稠密预条件矩阵，落地成本低

  - 训练推荐系统大排序、多模态召回等大规模参数模型时，使用该优化器可减少训练资源消耗，加快模型迭代效率'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有Muon优化器通过Newton-Schulz迭代正交化动量矩阵，缓解了梯度各向异性问题，但未显式建模损失曲面的曲率几何，对曲率各向异性敏感，在高条件数损失场景下收敛速度明显变慢；而现有曲率感知的Muon变种多采用稠密预条件矩阵，内存和计算开销极高，难以落地到大模型训练场景。

### 方法关键点
- 设计MALT优化器，为动量矩阵左右两侧分别构建轻量对角预条件器，仅维护梯度行、列平方范数的指数移动平均，新增内存开销仅为O(m+n)，远低于稠密预条件的O(m²+n²)
- 先对预条件后的动量做正交化，再映射回原参数空间作为更新方向，同时引入norm grafting机制控制更新幅度，避免训练发散
- 进一步提出自适应版本MALTER，在预条件空间加入基于范数的Adam型自适应步长，提升对随机梯度噪声的鲁棒性，仅额外增加1个标量状态

### 关键结果数字
在OpenWebText数据集上预训练GPT-2 Small/Medium/Large，对比AdamW、Muon基线：MALT比Muon验证损失分别降低0.0114/0.0108/0.0125，MALTER比Muon分别降低0.0241/0.0277/0.0164，且内存、单步训练耗时和原Muon几乎一致，MALTER的性能提升幅度与Muon超过AdamW的幅度相当。

**最值得记住的一句话**：曲率感知预条件和噪声自适应步长控制是矩阵感知优化器设计中互补且高效的核心组件。
