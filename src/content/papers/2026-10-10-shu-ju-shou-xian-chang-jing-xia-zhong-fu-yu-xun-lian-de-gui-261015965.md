---
title: 'Scaling Repeated-Data Pretraining: Batch Size, Regularization, and GPU-Time
  Tradeoffs'
title_zh: 数据受限场景下重复预训练的规模化：batch、正则与GPU-时间权衡
authors:
- Sewon Min
affiliations:
- UC Berkeley
- Allen Institute for AI
arxiv_id: '2610.15965'
url: https://arxiv.org/abs/2610.15965
pdf_url: https://arxiv.org/pdf/2610.15965
published: '2026-10-10'
collected: '2026-10-14'
category: Training
direction: LLM训练 · 数据受限预训练优化
tags:
- Repeated-Pretraining
- Batch-Size-Optimization
- Regularization
- Scaling-Law
- GPU-Resource-Allocation
one_liner: 揭示数据受限重复预训练的batch最优规律，给出训练配方与GPU-时间联合分配方案
practical_value: '- 垂直领域小模型（电商垂类LLM、物品Semantic ID生成模型）训练数据有限时，不要盲目用大batch，最优batch比单轮预训练小3-5倍，可利用小batch梯度噪声做隐式正则缓解过拟合

  - 重复训练可直接复用3个trick：每轮epoch重新打包文档为新序列（REPACK）、输入输出embedding权重绑定、embedding层加正权重衰减，可延长有效训练轮次2-3倍，降低验证损失

  - 资源分配不要盲目堆GPU拉满并行度，固定训练deadline下，用更少GPU跑更小batch，可能得到效果更优的模型，适合垂类小模型训推成本优化

  - 推荐系统语义召回/排序模型在垂类用户行为数据有限的场景下，这套batch和正则优化思路可直接迁移，缓解重复刷训练数据的过拟合问题'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM预训练普遍默认单轮遍历无限数据，但高质量人类数据增速远跟不上算力增长，数据受限场景下重复训练同一数据成为必然，现有单轮预训练的batch、正则、资源分配配方完全不适配重复训练场景，过拟合严重，资源利用效率极低。

### 方法关键点
- 针对无限算力有限数据场景，联合优化batch size、学习率、权重衰减、训练轮次，量化batch与验证损失的对应关系
- 提出3个重复训练专用正则策略：REPACK（每轮epoch重新打包文档生成新序列）、输入输出embedding权重绑定、embedding层施加正权重衰减
- 拆分GPU和时间为两个独立约束，划分4种算力 regime，提出不同deadline和GPU预算下的资源分配方案

### 关键结果
实验基于153M/474M/1.5B参数的Decoder-only Transformer，在DCLM-Baseline的0.33B/1B/3B token数据集上训练，对比单轮预训练配方：
1. batch与验证损失呈U型关系，最优batch（64序列）比常规单轮预训练小4-8倍，1.5B模型验证CE从3.124（batch=512）降至2.977
2. 加入3个正则trick后，1.5B模型有效训练轮次从20轮提升到32轮，验证CE进一步降至2.946
3. 固定32K step的时间预算下，用16GPU跑小batch比64GPU跑大batch的1.5B模型验证CE低0.065

### 核心结论
数据受限重复预训练场景下，不要盲目沿用单轮预训练的大batch+满并行度配方，针对性调整batch、正则和资源分配，能以更低成本得到效果更优的模型
