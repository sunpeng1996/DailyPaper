---
title: Where, When, and How Many Bits? Scaling Laws for SGD with Stochastic Rounding
title_zh: 何时、何处用多少比特？带随机舍入的SGD缩放规律研究
authors:
- Zhichao Wang
- Michael W. Mahoney
affiliations:
- University of California, Berkeley
- ICSI
- LBNL
arxiv_id: '2610.41074'
url: https://arxiv.org/abs/2610.41074
pdf_url: https://arxiv.org/pdf/2610.41074
published: '2026-10-29'
collected: '2026-11-02'
category: Training
direction: 低精度训练 · 随机舍入缩放规律
tags:
- Low-Precision-Training
- Stochastic-Rounding
- SGD
- Scaling-Laws
- Quantization
one_liner: 推导带随机舍入低精度训练的SGD误差界，给出精度选择、学习率设计的量化指导
practical_value: '- 低精度训练LLM4Rec、业务大模型时，优先仅对前向特征做随机舍入，可保留精确计算的缩放效率，避免反向舍入带来的效果损失

  - 固定训练计算预算时，可降低精度换取更大模型容量或更长训练步长，只要扩容收益超过舍入误差即可提升最终效果

  - 采用参数平均的训练场景可灵活调整前后向精度分配，无需全程保持高计算精度，可显著降低训练成本'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
低精度训练可大幅降低大模型训练的内存占用与计算开销，但随机舍入会引入额外误差，业界缺乏精度配置、模型大小、训练时长与最终效果的量化tradeoff指导。
### 方法关键点
针对两层线性网络小批量SGD训练场景，推导了通用学习率、精度调度策略下的预测误差上下界，分别分析仅前向舍入、仅反向舍入、参数平均等不同训练配置的缩放规律。
### 关键结果
仅前向特征舍入可完全保留精确计算的缩放效率，反向舍入会改变缩放曲线；固定计算预算下，降低精度换更大模型/更长训练的收益超过舍入误差时，最终效果更优；给出指定精度容忍度下的比特数需求，以及反向舍入场景下的学习率调度调整方法，MLP与小Transformer实验验证了理论结论。
