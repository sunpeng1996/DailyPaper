---
title: 'Sign compression for Muon: SignMuon, MuonSign, and the Limits of Error Feedback'
title_zh: 面向Muon优化器的符号压缩：SignMuon、MuonSign及误差反馈的局限性
authors:
- Maria Smirnova
- Alexey Kravatskiy
affiliations:
- MIRIAI
arxiv_id: '2607.29674'
url: https://arxiv.org/abs/2607.29674
pdf_url: https://arxiv.org/pdf/2607.29674
published: '2026-07-31'
collected: '2026-08-03'
category: Training
direction: 大模型训练 · 优化器压缩
tags:
- Optimizer
- Sign Compression
- Muon
- Error Feedback
- Distributed Training
one_liner: 提出1比特压缩的Muon优化器变体，验证效果优于SignSGD，分析理论收敛性与实际效果的背离
practical_value: '- 分布式训练推荐侧LLM召回/排序模型、Agent基座时，可采用SignMuon做1比特参数更新压缩，通信带宽成本降低32倍，效果优于SignSGD

  - 工程落地优先选择LMO后做符号压缩的启发式方案，无需执着于理论收敛性证明，在公开数据集及nanoGPT场景下实测效果最优

  - 符号压缩出现收敛问题时，可尝试在梯度侧引入EF21误差反馈，保障非凸问题收敛性同时仍保持低通信开销'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
分布式训练（尤其联邦学习场景）中参数更新通信带宽占训练耗时比例高，现有SignSGD丢弃矩阵结构效果差，Muon优化器利用矩阵结构效果好但全精度传输通信成本高，亟需低通信开销的矩阵感知优化器。

### 方法关键点
提出三类符号压缩Muon变体：LMO后压缩的SignMuon、LMO前压缩的MuonUSign、双向压缩的MuonSign；分别验证误差反馈加在Muon输出侧和梯度侧的效果差异，推导收敛率。

### 关键结果数字
1. SignMuon单参数仅需1比特，通信成本仅为全精度Muon的1/32，效果优于SignSGD；2. 梯度侧加EF21的变体达到非凸问题标准$oldsymbol{	O(T^{-1/2})}$收敛率；3. 理论上发散的LMO后压缩方案在CIFAR-10、联邦CIFAR-10、nanoGPT任务上效果均优于理论收敛的变体。
