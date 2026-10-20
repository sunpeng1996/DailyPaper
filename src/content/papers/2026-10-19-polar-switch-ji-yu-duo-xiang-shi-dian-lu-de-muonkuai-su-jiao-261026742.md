---
title: 'Polar Switch: Fast Muon Orthogonalization with Polynomial Circuits'
title_zh: Polar Switch：基于多项式电路的Muon快速正交化方法
authors:
- Zhehang Du
- Weijie Su
affiliations:
- University of Pennsylvania
arxiv_id: '2610.26742'
url: https://arxiv.org/abs/2610.26742
pdf_url: https://arxiv.org/pdf/2610.26742
published: '2026-10-19'
collected: '2026-10-20'
category: Training
direction: LLM训练优化 · Muon正交化加速
tags:
- Muon
- Optimizer
- Polar Decomposition
- GPU Acceleration
- LLM Training
one_liner: 设计低FLOP多项式电路替换Muon原有五次迭代，正交化速度最高提18.7%且精度相当
practical_value: '- 若使用Muon优化器训练电商/推荐域大模型（如生成式推荐模型、Agent基座），可直接替换原有正交化模块为开源Polar Switch，无精度损失下降低训练耗时8~18%

  - 多项式电路+融合GPU内核的设计思路可复用在其他需频繁矩阵正交化的场景，如推荐侧矩阵分解、语义向量正交归一化预处理

  - 半精度下的数值稳定性约束设计可借鉴到低精度算子自研场景，在避免数值溢出的同时降低显存占用'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
Muon优化器训练LLM的效率优于AdamW，已被用于Qwen3、GLM-5等多个前沿开源大模型训练，但每步迭代的梯度矩阵正交化是核心性能瓶颈，原有五次多项式迭代方案（Polar Express、Gram Newton-Schulz）FLOP开销高，存在明显优化空间。
### 方法关键点
- 设计多项式电路架构：用少量可复用方形矩阵缓存，通过对称矩阵乘序列构造更高次奇次多项式，相同FLOP预算下极坐标逼近精度更高
- 实现融合GPU内核：将矩阵乘、系数缩放、加单位阵操作合并为单个内核，减少显存读写和rounding次数，原生支持float16半精度计算
- 数值稳定约束优化：搜索多项式系数时加入半精度rounding扰动约束，推荐内层深度不超过5的电路避免数值溢出
### 关键结果
- 对比Polar Express，推荐的PS2-55/PS3-55在方阵上运行速度提升15.5~18.7%；对比Gram Newton-Schulz，在长宽比3.25/3.5/8的矩形矩阵上速度提升8.6~16.2%
- 在Modded-NanoGPT、Qwen3-0.6B、Gemma3-1B三个预训练任务上，验证损失与原有方法持平，超过1400万次正交化操作的谱范数误差不超过设计上限的3%
### 核心结论
Muon的正交化瓶颈不需要靠更高次单次迭代解决，通过复用缓存的多项式电路可以在更低FLOP下获得更优的速度与精度trade-off
