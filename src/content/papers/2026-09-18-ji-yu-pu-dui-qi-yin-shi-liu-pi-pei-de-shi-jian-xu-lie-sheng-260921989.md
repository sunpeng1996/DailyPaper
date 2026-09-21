---
title: Time series generation with spectrally aligned latent flow matching
title_zh: 基于谱对齐隐式流匹配的时间序列生成方法
authors:
- Camilo Carvajal Reyes
- Felipe Tobar
affiliations:
- Imperial College London
arxiv_id: '2609.21989'
url: https://arxiv.org/abs/2609.21989
pdf_url: https://arxiv.org/pdf/2609.21989
published: '2026-09-18'
collected: '2026-09-21'
category: Other
direction: 时间序列生成 · 生成式建模
tags:
- time series
- flow matching
- generative modelling
- latent space
- Fourier transform
one_liner: 引入傅里叶、小波等多域变换微调损失，解决隐式流时序生成的谱失配问题，提升样本质量与效率
practical_value: '- 做用户行为/销量/流量等业务时序数据增强时，可引入傅里叶/小波域损失，避免生成数据的周期、波动频谱和真实数据偏差，提升增强数据的可用性

  - 训练时序生成类隐式模型时，不要只依赖逐点重构损失，补充信号变换域的对齐损失，可在不明显增加推理开销的前提下提升生成样本真实度

  - 做时序相关下游任务（如销量预测、用户行为预测）需要生成训练代理数据时，可复用该谱对齐隐式流架构，平衡生成质量和计算效率'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
隐式流是低成本高可靠的时间序列生成方案，但隐空间压缩会引入频谱失配等伪影，生成数据不符合真实分布，无法作为训练代理数据用于下游任务。
### 方法关键点
1. 设计谱对齐的隐式流时序生成器，训练时约束流匹配的隐空间保留真实数据的动态属性；
2. 在传统逐点重构损失之外，额外补充傅里叶变换、小波变换、签名变换的多域对齐微调损失，保证生成数据的平滑度、目标频谱特征和真实数据一致。
### 关键结果
在真实世界长程单变量、多变量基准数据集上，相比基线隐式流模型与现有SOTA，信号真实度指标最优，计算效率更高，同时生成样本和训练集的局部结构对齐度显著提升。
