---
title: Effective Learning Rate Governs Loss Dynamics in Language Model Pretraining
title_zh: 有效学习率（ELR）主导大语言模型预训练的损失动态
authors:
- Zihan Liu
- Ruiheng Zheng
- Shaobo Zhang
- Changxin Tian
- Kunlong Chen
- Zhiqiang Zhang
- Lei Wu
affiliations:
- Peking University
- Ant Group
arxiv_id: '2608.24814'
url: https://arxiv.org/abs/2608.24814
pdf_url: https://arxiv.org/pdf/2608.24814
published: '2026-08-25'
collected: '2026-08-26'
category: Training
direction: 大模型预训练 · 训练超参优化
tags:
- Effective Learning Rate
- LLM Pretraining
- Loss Dynamics
- Norm Control
- Hyperparameter Tuning
one_liner: 揭示ELR为统一量度，可对齐不同LR、范数控制策略下的LLM预训练损失轨迹
practical_value: '- 训练垂直领域LLM（如商品理解、文案生成、用户意图识别模型）时，可采用ELR优先的超参设计逻辑：先确定最优ELR schedule，再匹配LR和范数控制策略，降低调参成本

  - 跨模型规模复用预训练超参时，替换LR为ELR作为统一量度，可降低跨模型（如从7B到70B）、跨范数控制方法（如从weight decay到Hyperball）的调参误差

  - 功能缩放定律（FSL）改用ELR参数化后，损失动态预测误差可降低12.9倍，可直接复用该改进版FSL做预训练损失预估、训练终止判断，节省训练算力

  - 针对范数控制带来的延迟加速现象，可通过调控ELR后期衰减速率优化最终损失，无需改动现有优化器、范数控制策略的主体逻辑'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
LLM预训练中学习率调度、范数控制（weight decay、Hyperball等）都会显著影响损失动态，但二者长期被视为独立超参，调参成本高、跨策略/跨规模的超参迁移难度大，缺乏统一的核心量度关联二者与损失的关系。

### 方法关键点
- 定义有效学习率$\eta_{eff}^k := \eta_k/\|W_k\|_F$，核心假设是损失动态仅由ELR schedule决定，与LR、参数范数的独立取值无关
- 设计两类对照实验：固定ELR schedule搭配不同LR、预设范数轨迹验证对齐效果；适配LR匹配不同范数控制策略的ELR，验证其对损失的中介作用
- 改进功能缩放定律（FSL），将原参数化中的LR替换为ELR，验证其跨范数控制方法的迁移能力

### 关键结果
- 实验覆盖Llama、Qwen3-MoE、线性注意力等架构，模型规模100M~1B，数据集包括FineWeb、C4、OpenWebText，优化器覆盖AdamW、Muon、Signum
- ELR匹配的损失轨迹平均误差仅为$2.5\times10^{-3}$，远低于种子差异带来的$10^{-2}$级误差；weight decay、Hyperball的效应完全可通过ELR匹配复现，误差分别为$4.8\times10^{-3}$、$1.2\times10^{-3}$
- 基于ELR的FSL在未见过的Hyperball实验上预测误差比原LR-based FSL低12.9倍，可完美解释范数控制带来的延迟加速现象

最值得记住的结论：预训练调参的核心设计对象应该是ELR schedule，而非独立的学习率、weight decay或范数约束。
