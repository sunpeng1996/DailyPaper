---
title: 'Spectral Allocation: Why Muon Outperforms Adam, and How to Improve Muon'
title_zh: 基于谱分配理论解析Muon性能优势并提出轻量化改进优化器SAMuon
authors:
- Xiaodong Wu
- Wenyi Yu
- Chao Zhang
- Philip Woodland
affiliations:
- University of Cambridge
- Tsinghua University
arxiv_id: '2608.25990'
url: https://arxiv.org/abs/2608.25990
pdf_url: https://arxiv.org/pdf/2608.25990
published: '2026-08-26'
collected: '2026-08-27'
category: Training
direction: LLM预训练 · 正交优化器改进
tags:
- Optimizer
- Muon
- LLM Pretraining
- Spectral Analysis
- SAMuon
one_liner: 通过离样谱探测分析Transformer损失地貌，提出SAMuon系列优化器较Muon降低13.3%~24%训练token消耗
practical_value: '- 业务侧训练生成式推荐、Agent基座、大模型召回/排序模块时，可直接将Muon替换为SAMuon-lite，仅不到1%额外耗时即可降低13%+训练token消耗，压缩训练成本

  - 优化器设计思路可迁移：先通过离样谱探测分析目标任务损失地貌的稳定特征，基于静态先验做轻量化改进，无需新增持久化状态即可落地

  - 大batch训练场景优先选用完整版SAMuon，batch越大增益越高，适配电商/广告大模型预训练常用的大batch训练配置'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
正交优化器Muon在LLM预训练中收敛速度显著优于Adam，但作用机理未被完全厘清，现有理论无法充分解释其收敛优势，且Muon的统一缩放策略受限于头方向的稳定性约束，未能充分利用损失地貌的谱特性，存在较大优化空间。

### 方法关键点
1. 提出离样谱探测框架，在验证集上测量动量缓冲每个奇异方向的最优步长，发现损失地貌存在稳定的各向异性谱分布：单Volatile Head位于稳定性边缘，最优步长极小，其余Tolerant Bulk最优步长是头的数倍且整体平坦
2. 基于该静态谱先验提出两种SAMuon变体：完整版用随机低秩SVD拟合log秩线性的近头步长分布，lite版用幂迭代仅锚定头方向、统一放大bulk步长，两者均不增加额外持久化优化器状态，额外FLOPs可忽略
3. 仅新增1个超参数γ，γ=1时退化为标准Muon，完全兼容现有Muon训练配置

### 关键实验
在modded-nanogpt 124M~1B参数模型、FineWeb数据集上训练，对比AdamW、Muon（Scion实现）基线，SAMuon达到相同验证损失需少13.3%~24.0%的训练token，SAMuon-lite保留大部分增益，额外wall-clock开销不足1%，且batch越大增益越高。

最值得记住的一句话：优化器设计无需盲目增加复杂自适应机制，先探测损失地貌的稳定静态特征再做轻量化适配，往往能以极低开销获得显著效率提升。
