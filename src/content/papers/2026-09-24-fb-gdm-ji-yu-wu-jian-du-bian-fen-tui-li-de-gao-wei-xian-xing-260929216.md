---
title: 'FB-GDM: Fully-Bayesian Guided Diffusion Models for High-Dimensional Linear
  Inverse Problems via Unsupervised Variational Inference'
title_zh: FB-GDM：基于无监督变分推理的高维线性逆问题全贝叶斯引导扩散模型
authors:
- Gatien Séguy
- Thomas Rodet
arxiv_id: '2609.29216'
url: https://arxiv.org/abs/2609.29216
pdf_url: https://arxiv.org/pdf/2609.29216
published: '2026-09-24'
collected: '2026-09-26'
category: Other
direction: 扩散模型 · 无监督超参动态推断
tags:
- Diffusion Model
- Variational Inference
- Bayesian Inference
- Hyperparameter Optimization
- Image Reconstruction
one_liner: 提出无需逐任务校准超参的全贝叶斯引导扩散模型，在逆问题任务上性能优于基线且鲁棒性更强
practical_value: '- 可将「人工调优超参转为推理阶段变分推断隐变量」的思路迁移到生成式推荐引导生成场景，避免逐业务场景调试引导权重

  - 推理阶段动态平衡先验与观测权重的方法，可复用在RAG生成、多模态商品生成场景，缓解分布偏移下的幻觉问题

  - 线性复杂度的参数更新设计思路可借鉴到高维用户/商品特征实时推理场景，控制额外计算开销'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有基于扩散模型的线性逆问题引导方法（DPS、ΠGDM）依赖逐任务对标ground truth调整 scalar 超参数，泛化性差且落地成本高
### 方法关键点
1. 基于ΠGDM的高斯近似推导闭式条件得分，将去噪近似、观测似然对应的2个精度参数作为隐变量，每步反扩散时通过变分推理自动推断，无需已知噪声水平或ground truth，仅需输入观测值和前向算子
2. 采用可分离因子化设计，参数更新复杂度与像素数线性相关，推理开销与单次ΠGDM运行相当
### 关键结果
CelebA-HQ实验：① 仅靠观测推断参数的FB-GDM比给定真实噪声水平的标称ΠGDM性能最高高14dB，与ground truth校准的ΠGDM oracle性能差距小于0.1dB；② 前向算子、噪声水平、图像分布变化时，鲁棒性远优于DPS和ΠGDM，无DPS常见的幻觉问题
