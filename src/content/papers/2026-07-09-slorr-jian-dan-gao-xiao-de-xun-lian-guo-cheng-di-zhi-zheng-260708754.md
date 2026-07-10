---
title: 'SLORR: Simple and Efficient In-Training Low-Rank Regularization'
title_zh: SLORR：简单高效的训练过程低秩正则化框架
authors:
- David González-Martínez
- Shiwei Liu
affiliations:
- Max Planck Institute for Intelligent Systems
- University of Tübingen
- ELLIS Institute Tübingen
- Tübingen AI Center
arxiv_id: '2607.08754'
url: https://arxiv.org/abs/2607.08754
pdf_url: https://arxiv.org/pdf/2607.08754
published: '2026-07-09'
collected: '2026-07-10'
category: Training
direction: 训练优化 · 低秩模型压缩
tags:
- Low-Rank Regularization
- Model Compression
- LLM Training
- Efficient Inference
- Training Optimization
one_liner: 提出无SVD、不修改模型架构的训练时低秩正则化框架，训练开销极低，提升压缩后模型性能保留
practical_value: '- 对业务中需要小模型部署的场景（端侧推荐模型、离线推理LLM Agent），可直接引入SLORR-Hoyer正则化到训练流程，仅增加不到1%训练开销即可大幅提升低秩压缩后的效果保留，无需修改模型架构

  - 提供的PyTorch自定义算子实现可直接复用，无额外SVD开销，适配现有Transformer/CNN推荐模型训练管线，改造成本极低

  - 针对垂直领域小参数LLM（电商客服Agent、商品文案生成小模型）的预训练/继续训练阶段加入SLORR正则，压缩后可部署在成本更低的GPU上，推理提速的同时效果损失远低于无正则压缩'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
低秩因子分解是主流的模型压缩手段，但直接对训练好的模型做激进压缩会带来显著精度损失；现有训练时低秩正则化方法要么需要每步执行SVD开销极高，要么需要修改模型架构引入额外参数，或者依赖状态缓存调参复杂，难以落地到大模型训练流程。

### 方法关键点
- 核心思路是用GPU友好的Polar Express迭代法近似计算权重矩阵的极因子，替代传统正则化需要的SVD计算，完全无SVD、无状态、不修改原模型架构
- 提供两个可落地变体：SLORR-Hoyer基于平方Hoyer稀疏度度量，SLORR-Nuc基于核范数，两者都有近似精度的理论保证
- 实现极简，可封装为PyTorch自定义算子，仅需在原损失上加正则项即可，适配所有包含线性/卷积层的模型

### 关键实验结果
- 视觉任务：在ImageNet-1K上测试ResNet、ViT系列模型，训练开销低于8%，压缩后精度保留显著优于无正则 baseline 和同类方法LoRITa、Q3R
- LLM任务：预训练135M/560M规模Llama模型，训练平均开销低于1%；压缩后相同参数规模下，验证集困惑度比无正则模型低15%以上，下游零样本任务精度平均高8~12个百分点

### 核心结论
低秩正则化不需要复杂的架构修改或高开销的SVD，仅通过极因子近似就能实现极低开销的训练时压缩感知，是小模型落地性价比极高的优化手段
