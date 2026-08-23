---
title: Flow Matching-Based PET Image Reconstruction
title_zh: 基于流匹配的PET图像重建
authors:
- Fumio Hashimoto
- Ziqian Huang
- Tatsuya Yokota
- Kuang Gong
arxiv_id: '2608.20112'
url: https://arxiv.org/abs/2608.20112
pdf_url: https://arxiv.org/pdf/2608.20112
published: '2026-08-20'
collected: '2026-08-23'
category: Other
direction: 医学影像 · 生成式先验图像重建
tags:
- Flow Matching
- Generative Prior
- Image Reconstruction
- PET
- Bayesian Framework
one_liner: 提出融合泊松似然引导的流匹配PET重建方法，实现不同剂量下更优偏置-方差权衡
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 4
source: arxiv-cs.CV
depth: abstract
---

### 动机
扩散模型用于PET图像重建需多步反向采样，数据一致性更新嵌入采样流程效率低；低剂量PET成像受噪声干扰大，现有迭代重建方法量化精度不足，无法兼顾成像质量与效率。
### 方法关键点
1. 构建PET-FlowDPS，将带EM预调节器的泊松似然引导融入FlowDPS框架，实现数据一致性优化与流传播过程解耦
2. 提出基于模型的重建方案，以预训练流匹配模型为先验，在近似贝叶斯框架下统一建模流先验、PET数据精炼、随机传播过程
### 关键结果
在[¹⁸F]FDG脑PET数据集测试中，相比现有基准方法，在所有剂量水平下均实现更优的偏置-方差权衡，验证了流匹配作为生成先验用于定量PET图像重建的潜力。
