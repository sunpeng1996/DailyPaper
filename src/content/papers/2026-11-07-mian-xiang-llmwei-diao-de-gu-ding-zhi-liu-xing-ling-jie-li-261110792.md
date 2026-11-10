---
title: Zeroth-Order Riemannian Optimization on Fixed-Rank Manifolds for LLM Fine-Tuning
title_zh: 面向LLM微调的固定秩流形零阶黎曼优化算法
authors:
- Xinjue Wang
- Xiuheng Wang
- Yejun Zhang
- Sergiy A. Vorobyov
- Esa Ollila
affiliations:
- Aalto University
- South China University of Technology
arxiv_id: '2611.10792'
url: https://arxiv.org/abs/2611.10792
pdf_url: https://arxiv.org/pdf/2611.10792
published: '2026-11-07'
collected: '2026-11-10'
category: Training
direction: LLM高效微调 · 零阶黎曼优化
tags:
- LoRA
- Zeroth-Order Optimization
- Riemannian Optimization
- PEFT
- LLM Fine-tuning
one_liner: 提出固定秩流形约束的零阶LLM微调框架，效果优于现有前向仅微调基线且内存开销低
practical_value: '- 低资源LLM微调场景可直接复用该方法：仅需前向传播无需存储激活，80G A100上比LoRA+AdamW节省近70%内存，适合长上下文推荐/Agent的大模型微调，避免OOM

  - LoRA优化可借鉴固定秩流形约束思路：解决传统LoRA因子化表示非唯一的问题，提升低秩更新的训练稳定性，适配推荐场景下多任务小样本微调需求

  - 零阶优化的归一化trick可直接复用：对切空间投影后的随机矩阵做归一化，消除秩和层形状对扰动尺度的影响，提升零阶训练的收敛效果'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有零阶（ZO）LLM微调无需反向传播、可节省大量激活存储，适配长上下文等内存紧张的微调场景，但当前低秩ZO方法存在两类缺陷：基于LoRA因子化的方法存在表示非唯一的冗余自由度，仅约束单步扰动的方法无法保证更新全程的秩限制，收敛性和效果均有提升空间。同时主流一阶LoRA微调的激活存储开销极高，80G A100上OPT-13B长任务容易OOM，亟需低内存的高效微调方案。
### 方法关键点
- 将LLM的低秩增量更新约束在固定秩矩阵流形上，全程保证更新的秩限制，消除因子化表示的冗余自由度
- 设计切空间投影+归一化的零阶黎曼梯度估计器：将随机高斯矩阵投影到当前切空间后做归一化，消除秩和层形状对扰动尺度的影响，单步仅需2次前向传播
- 提出基础版ZO-RGD和带scalar平滑的ZO-RGD-S算法，每次更新后通过截断SVD将增量拉回固定秩流形，保证约束有效性
### 关键结果
在OPT-13B/30B、Llama-3.1-8B、Qwen2.5-7B上测试，对比MeZO、LOZO等前向微调基线：OPT-13B的11个任务中ZO-RGD-S在6个任务上优于SOTA基线LOZO；OPT-30B的RTE任务准确率较LOZO提升5.8个百分点；内存开销稳定在39.4GB，比LoRA+AdamW低近70%，单步时间仅为LOZO的1.8倍。

最值得记住的结论：固定秩流形约束+切空间归一化的零阶优化，可在仅前向传播的低内存开销下，达到接近甚至超过现有低秩零阶微调方法的效果，是长上下文/低资源LLM微调的高性价比方案
