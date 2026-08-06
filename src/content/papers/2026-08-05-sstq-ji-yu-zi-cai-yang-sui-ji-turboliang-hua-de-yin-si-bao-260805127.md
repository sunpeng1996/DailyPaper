---
title: SSTQ:Privacy-Preserving Vector Quantization via Subsampled Stochastic TurboQuant
title_zh: SSTQ：基于子采样随机Turbo量化的隐私保护向量量化方法
authors:
- Adel Javanmard
- David P. Woodruff
- Vahab Mirrokni
affiliations:
- University of Southern California
- Carnegie Mellon University
- Google Research
arxiv_id: '2608.05127'
url: https://arxiv.org/abs/2608.05127
pdf_url: https://arxiv.org/pdf/2608.05127
published: '2026-08-05'
collected: '2026-08-06'
category: Training
direction: 分布式训练 · 隐私保护向量量化
tags:
- Vector Quantization
- Local Differential Privacy
- Federated Learning
- Gradient Compression
- Distributed Optimization
one_liner: 提出融合过完备紧框架、坐标子采样的SSTQ量化框架，实现分布式优化下LDP与低通信成本的平衡
practical_value: '- 电商推荐多端联邦训练场景可复用SSTQ的坐标子采样+1D隐私量化组合方案，在保障用户数据LDP的同时降低跨端梯度传输开销

  - 高维向量（用户Embedding、物品语义向量）跨端压缩传输场景可借鉴其隐私感知码本优化思路，将码本相关MSE从O(4^b)降至O(2^b)，平衡压缩率与精度

  - 低比特量化需求场景可按需选择SSTQ双变体：低码位用Flat Randomized Response，高码位用Metric-Aware Laplace，适配不同端侧资源约束'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
分布式优化/联邦学习场景下，同时满足本地差分隐私(LDP)保障与低通信开销是核心痛点，现有向量量化方法（如vqSGD）依赖高维几何构造，存在维度依赖的高方差缺陷。
### 方法关键点
1. 提出SSTQ框架，融合过完备等范紧框架、坐标子采样、隐私感知一维量化三类技术；
2. 提供两类适配变体：低码位场景用Flat Randomized Response版本，高码位场景用Metric-Aware Laplace版本；
3. 设计隐私感知码本替代优化目标，降低码本引入的误差。
### 关键结果
1. 单客户端仅需⌈log₂N⌉+b比特（N=Θ(d)为框架规模）即可达到最优MSE缩放；
2. 码本相关MSE缩放从O(4^b)降至O(2^b)；
3. CIFAR-10、Fashion-MNIST联邦学习任务上，效用与通信效率均优于现有基线。
