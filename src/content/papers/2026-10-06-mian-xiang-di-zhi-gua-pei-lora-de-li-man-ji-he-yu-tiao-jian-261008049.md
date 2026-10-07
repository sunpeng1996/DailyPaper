---
title: A Riemannian Geometry for Low-rank Adaptation
title_zh: 面向低秩适配（LoRA）的黎曼几何预条件优化方法
authors:
- Shoichiro Takeda
- Shin'ya Yamaguchi
- Satoshi Suzuki
- Yasunori Akagi
affiliations:
- NTT, Inc.
arxiv_id: '2610.08049'
url: https://arxiv.org/abs/2610.08049
pdf_url: https://arxiv.org/pdf/2610.08049
published: '2026-10-06'
collected: '2026-10-07'
category: Training
direction: 大模型参数高效微调 · LoRA优化
tags:
- LoRA
- PEFT
- Riemannian Optimization
- Preconditioning
- Fine-tuning
one_liner: 提出专为LoRA设计的黎曼度量与预条件策略，缩小与全参数微调的效果差距
practical_value: '- 业务中用LoRA微调垂域大模型（如商品文案生成、用户意图理解、推荐prompt生成）时，可直接替换原有梯度预条件，无需修改LoRA架构，不增加训练耗时即可获得稳定效果提升

  - 预条件的工程实现技巧可直接复用：通过公式改写避免显式构造大维度投影矩阵，在保证效果的前提下不引入额外计算开销

  - 对需要频繁微调多场景小样本垂域模型的业务，该方法可在相同计算成本下，缩小LoRA与全量微调的效果差，降低全量微调的资源消耗'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
LoRA是当前大模型参数高效微调的事实标准，但受限于低秩参数化的等价冗余性，与全量微调始终存在效果差距；传统黎曼预条件源自低秩矩阵补全场景，未针对LoRA的优化目标定制，仍存在优化路径冗余、对齐全量微调效果不足的问题。

### 方法关键点
- 针对LoRA固有的参数等价关系$(B,A)\sim(BG^{-1},AG^T)$设计专属黎曼度量，推导得到新预条件公式：对B、A的梯度分别左乘$(I - \frac{1}{2}P_B)$、$(I - \frac{1}{2}P_A)$项，衰减B、A列空间内的梯度分量，保留正交方向分量，让LoRA权重更新方向尽可能对齐全量微调梯度
- 工程实现上通过公式改写避免显式构造$m\times m$级别的大投影矩阵，时间复杂度与传统预条件完全一致，为$O((m+n)r^2)$，无额外计算 overhead

### 关键实验
覆盖语言、视觉、推理三类任务，对比原生AdamW、传统黎曼预条件两个基线：
1. E2E自然语言生成任务（GPT-2 Medium）：预条件加持的AdamW较原生AdamW BLEU提升0.27%、ROUGE-L提升0.16%
2. CLIP ViT-B/32 7个图像分类数据集平均准确率较原生AdamW提升0.47%，较传统预条件提升0.18%
3. LLaMA2-7B 8个常识推理数据集平均准确率较原生AdamW提升0.66%，较传统预条件提升0.37%
三类任务训练耗时均与基线无显著差异。

### 核心结论
LoRA优化的核心逻辑是在低秩参数化允许的更新空间内，尽可能对齐全量微调的梯度方向，消除等价性带来的冗余优化路径即可实现效率与效果的双重提升。
