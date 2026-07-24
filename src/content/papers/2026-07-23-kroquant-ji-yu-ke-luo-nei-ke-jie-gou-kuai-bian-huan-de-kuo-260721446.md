---
title: 'KroQuant: Kronecker-Structured Block Transforms for Efficient Post-Training
  Quantization of Diffusion Transformers'
title_zh: KroQuant：基于克罗内克结构块变换的扩散Transformer高效训练后量化
authors:
- Yann Bouquet
- Alireza Khodamoradi
- Kristof Denolf
- Mathieu Salzmann
affiliations:
- EPFL
- Advanced Micro Devices, Inc.
arxiv_id: '2607.21446'
url: https://arxiv.org/abs/2607.21446
pdf_url: https://arxiv.org/pdf/2607.21446
published: '2026-07-23'
collected: '2026-07-24'
category: Training
direction: 大模型量化 · 扩散Transformer训练后量化
tags:
- PTQ
- DiT
- W4A4
- Kronecker
- Low-Precision-Inference
- Quantization
one_liner: 提出克罗内克结构可学习块变换，实现扩散Transformer的W4A4高精度低开销量化
practical_value: '- 电商场景下部署多模态生成模型（商品图生成、AI文案）时，可直接复用KroQuant的W4A4量化方案，在不损失生成质量的前提下降低推理成本14%以上

  - 当大模型/推荐模型层间归一化（如AdaLN、LayerNorm）无法支持离线吸收激活变换时，可借鉴克罗内克结构的块级可学习变换，平衡在线计算开销和量化精度

  - 可复用Kronecker-LU参数化思路，大幅降低低秩/量化分支的参数量，适合端侧或资源受限场景的推荐/Agent模型部署

  - 量化校准阶段的自动正则化权重分配策略（按初始化损失比例分配λ）可直接迁移到其他PTQ场景，避免人工调参'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
扩散Transformer（DiT）向W4A4低精度量化时，层间AdaLN归一化无法像LLM那样离线吸收激活变换，导致高精度变换必须在线执行，现有方案要么精度有限（SmoothQuant逐通道缩放）要么推理开销过高（固定哈达玛变换、全维可学习变换），难以落地。

### 方法关键点
- 激活变换采用32×32块对角结构，每个块由5个2×2单位行列式LU矩阵的克罗内克乘积参数化，单块仅需15个参数，比全维32×32矩阵小68倍，参数量不到逐通道缩放的一半
- 初始化为块哈达玛矩阵，通过最小化量化前后输出MSE+激活/权重量化误差辅助损失逐层优化，正则化权重按初始化时各损失比例自动分配，避免调参
- 搭配离线LoRaQ权重校准吸收剩余量化误差；推理端实现两种自定义Triton kernel：预计算稠密块的K1 kernel、在线重构块的K2 kernel（参数压缩68倍）

### 关键实验
在PixArt-Σ、SANA、FLUX.1-schnell三个主流DiT上测试，对比SVDQuant、LoRaQ基线，W4A4精度下SDCI数据集上FLUX.1-schnell的LPIPS相对降低17.5%，PixArt-Σ的FID从17.5降到16.9，接近FP16基线的16.6；MI350 GPU上K1 kernel比SmoothQuant最高快14%，K2比FWHT最高快2.45倍。

### 核心结论
当归一化层阻碍离线变换吸收时，块级克罗内克结构可学习变换是兼顾在线量化精度和推理效率的最优解之一。
