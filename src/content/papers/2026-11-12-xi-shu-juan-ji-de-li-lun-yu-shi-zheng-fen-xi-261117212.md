---
title: Theoretical and Empirical Analysis of Sparse Convolution
title_zh: 稀疏卷积的理论与实证分析
authors:
- Keshvi Tuteja
- Yu-Hsiang Tsai
- Gregor Olenik
- Markus Götz
- Achim Streit
- Hartwig Anzt
- Charlotte Debus
affiliations:
- Karlsruhe Institute of Technology
- Technical University of Munich
- Helmholtz AI
- University of Tennessee
arxiv_id: '2611.17212'
url: https://arxiv.org/abs/2611.17212
pdf_url: https://arxiv.org/pdf/2611.17212
published: '2026-11-12'
collected: '2026-11-14'
category: Other
direction: 稀疏卷积优化 · 端边设备推理加速
tags:
- Sparse Convolution
- GPU Acceleration
- Edge Computing
- Roofline Analysis
- Sparse Neural Network
one_liner: 通过roofline分析稀疏卷积性能特征，提出高稀疏度优化方案，在A100、Jetson Nano上分别实现最高1.65x、1.52x加速
practical_value: '- 端侧轻量推荐模型若采用卷积层做用户/物品特征提取，可复用本文高稀疏度卷积优化方案降低推理延迟

  - 模型剪枝后可参照本文roofline分析方法量化实际推理收益，避免仅靠稀疏率盲目评估压缩效果

  - 多卡部署的大规模推荐推理服务，可借鉴本文稀疏权重的内存访问优化思路缓解带宽瓶颈'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
端边设备计算资源、内存带宽受限，训练剪枝得到的高稀疏卷积核可大幅降低算力与内存开销，但运行时存在内存访问不规则、计算单元负载不均问题，稀疏性难以有效转化为实际性能收益。
### 方法关键点
1. 基于roofline模型分析带稀疏权重的标准卷积的性能特征，量化稠密与稀疏卷积的算术强度差异
2. 针对高稀疏度场景设计优化技术，解决内存访问与负载均衡痛点
### 关键结果
3×3稀疏卷积算术强度仅约10 FLOP/byte，远低于稠密卷积的96 FLOP/byte；优化方案在NVIDIA A100上最高实现1.65倍推理加速，在Jetson Nano端侧设备上最高实现1.52倍加速。
