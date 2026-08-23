---
title: 'Fourier is Frontier: Frequency-Aware Autoencoding for High-Fidelity Music
  Reconstruction'
title_zh: 傅里叶是前沿：面向高保真音乐重建的频率感知自编码器
authors:
- Kangdi Wang
- Yusheng Dai
- Jin Xu
affiliations:
- Qwen Team, Alibaba
- Monash University
arxiv_id: '2608.19843'
url: https://arxiv.org/abs/2608.19843
pdf_url: https://arxiv.org/pdf/2608.19843
published: '2026-08-20'
collected: '2026-08-23'
category: Other
direction: 高保真音频重建 · 频率感知自编码器
tags:
- Audio Autoencoder
- STFT
- High-Fidelity Generation
- Activation Function
- Latent Representation
one_liner: 提出频率感知复谱自编码器ear-VAE2，解决高压缩率下音频重建的高频丢失、相位不一致等问题
practical_value: '- 电商短视频/广告音频生成场景可复用Duplex-Aware Refiner的分频带修正思路，解决高压缩率下音频高频丢失、立体声失真问题，提升生成音频保真度

  - 多模态特征编码优化可借鉴「针对模态固有结构（如音频频域轴）设计专属激活与修正模块」的思路，平衡参数量与特征保真效果

  - 跨模态检索/存储场景可参考本文高压缩率下的特征保真方法，优化音频特征压缩方案，在降低存储成本的同时保留核心语义信息'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
高压缩率下的连续隐空间音频自编码器普遍存在高频丢失、相位不一致、立体声坍缩三类问题，根源是波形自编码器无显式频率轴，无法实现逐频带定向修正。
### 方法关键点
1. 对比5种同算力预算的表征方案，验证复STFT（短时傅里叶变换）全频带/高频谱距离最低，可直接访问每个频点的幅度与相位；
2. 提出ear-VAE2复谱自编码器，设计Spec-SnakeBeta激活函数为每个频点学习周期激活，采用依频率的初始化策略，效果优于其他激活方案且参数量更低；
3. 新增Duplex-Aware Refiner模块，基于声音定位双工理论对幅度、相位做逐频带定向修正。
### 关键结果
在546条的Song Describer数据集上，ear-VAE2在7个重建指标中5个取得最优；Duplex-Aware Refiner较无约束版本降低19.4% Mel距离，残差输出维度减少45%，获得专业音频工程师更高评分；下游生成器采用其隐向量在12个自动评估指标上全部最优
