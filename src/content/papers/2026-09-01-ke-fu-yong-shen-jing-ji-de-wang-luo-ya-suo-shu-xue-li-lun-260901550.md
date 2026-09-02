---
title: A Mathematical Theory of Reusable Neural Bases for Network Compression
title_zh: 可复用神经基的网络压缩数学理论
authors:
- Binshuai Wang
affiliations:
- The George Washington University
arxiv_id: '2609.01550'
url: https://arxiv.org/abs/2609.01550
pdf_url: https://arxiv.org/pdf/2609.01550
published: '2026-09-01'
collected: '2026-09-02'
category: Training
direction: 模型训练优化 · 网络参数压缩
tags:
- Network Compression
- Parameter Efficiency
- Memory Optimization
- Model Training
- LRNBA
one_liner: 提出线性可复用神经基架构LRNBA，在稳定训练前提下大幅提升参数效率降低内存开销
practical_value: '- 电商大参数量召回/排序模型可复用LRNBA的共享神经基线性组合思路，相同参数预算下搭建更深更宽网络，提升效果不增加内存开销

  - LLM4Rec、Agent类业务的大模型部署阶段可采用该压缩方案，降低推理端GPU内存占用，大幅控制部署成本

  - 模型压缩落地时可参考其训练稳定性设计，避免常见的压缩后收敛变慢、效果掉点问题'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
大模型规模化应用过程中，训练与推理的内存成本成为核心瓶颈，资源受限团队难以落地大模型方案，现有压缩方法普遍存在训练不稳定、收敛慢、效果退化问题。
### 方法关键点
1. 受RNN设计启发提出线性可复用神经基架构LRNBA，将每个网络块表示为一组共享神经基的线性组合，最大化参数复用率，实现高压缩比；
2. 配套完整数学理论支撑，保障压缩后模型的训练稳定性，无收敛性损失。
### 关键结果
实验验证，相同参数预算下LRNBA构建的模型比传统架构收敛速度更快、最终损失更低，训练全程动态稳定，高压缩比场景下无性能退化。
