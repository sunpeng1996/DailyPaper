---
title: Low-Rank Ternary Adaptation for Fine-Tuning Transformers
title_zh: 面向Transformer微调的低秩三值适配方法
authors:
- Alexandru-Dragos Manolache
- Yunqiang Li
- Jan van Gemert
affiliations:
- Delft University of Technology
- Amazon Development Center
arxiv_id: '2608.24469'
url: https://arxiv.org/abs/2608.24469
pdf_url: https://arxiv.org/pdf/2608.24469
published: '2026-08-25'
collected: '2026-08-26'
category: Training
direction: 大模型参数高效微调 · 1.58bit三值量化
tags:
- LoRA
- PEFT
- Ternary-Quantization
- 1.58bit
- Transformer
- Fine-Tuning
one_liner: 提出无需反量化的三值域低秩适配方案，微调后模型保持1.58bit精度且性能优于现有低比特PEFT方案
practical_value: '- 对端侧部署的小规格LLM（如电商客服、商品文案生成端侧模型），可采用该三值适配方案微调，将1.58bit模型部署成本降至原16bit的1/10，且无推理
  overhead

  - 现有低比特LoRA微调后重量化导致的精度损失问题，可借鉴乘法式适配而非加法适配的思路，适配时保持量化域一致，避免重量化误差

  - Kronecker乘积的低秩分解方式可复用在超大参数量推荐模型的轻量化微调场景，用远少于常规LoRA的参数量达到相当适配效果'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
三值量化（1.58bit）可将Transformer内存占用降至16bit的1/10，是端侧部署大模型的核心方案，但现有LoRA类PEFT方法适配三值模型时，要么需要反量化回高精度再合并导致重量化误差，要么仅更新量化参数，无法得到保持三值精度的合并模型，难以发挥三值模型的部署效率优势。

### 方法关键点
- 采用乘法式三值适配逻辑：用三值掩码矩阵和原三值权重做哈达玛积，每个掩码元素对应保留、清零、翻转原权重三种操作，全程保持三值域，无需反量化
- 用Kronecker乘积分解适配掩码为两个小型三值矩阵，大幅降低训练参数量，同时保持高更新秩，保证适配表达性
- 训练时优化实值代理矩阵，用直通梯度estimator传递梯度，微调后直接合并掩码到原权重，得到完全三值的部署模型，无额外推理开销

### 关键结果
在Llama-3.2 1B/3B三值模型、BitNet 2B、三值ViT-B/16上验证，对比QLoRA、QA-LoRA等基线：
- Llama-3.2 3B微调后平均准确率比原生三值基线高6.4个百分点，PPL从45.6降至22.3，性能超过2bit SpinQuant基线，比重量化QLoRA准确率高0.8个百分点
- 三值ViT在ImageNet-100上Top-1准确率达83.0%，比重量化QLoRA高4.1个百分点，接近全参数三值微调的85.7%

低比特模型适配时，保持量化域一致性的乘法式适配，比传统加法式LoRA+重量化的方案，能在几乎不损失精度的前提下大幅降低部署成本
