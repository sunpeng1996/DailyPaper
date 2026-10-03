---
title: 'SoftServe: A Scalable Quasi-Newton Method for Deep Learning'
title_zh: SoftServe：面向深度学习的可扩展拟牛顿优化方法
authors:
- Joohwan Ko
- Tetiana Parshakova
- Diana Cai
- Robert M. Gower
affiliations:
- University of Massachusetts Amherst
- CCM, Flatiron Institute
- Cornell University
arxiv_id: '2610.02182'
url: https://arxiv.org/abs/2610.02182
pdf_url: https://arxiv.org/pdf/2610.02182
published: '2026-10-01'
collected: '2026-10-03'
category: Training
direction: 深度学习训练 · 二阶优化器设计
tags:
- Quasi-Newton
- Second-order Optimizer
- Large-scale Training
- GPU Acceleration
- Optimization
one_liner: 提出适配非凸大模型的可扩展拟牛顿优化器SoftServe，性能优于Adam等主流基准
practical_value: '- 训练电商/广告场景的大参数量深度召回、排序、多任务模型时，可尝试SoftServe替代Adam，解决病态优化问题、降低收敛损失

  - 其用Newton-Schulz迭代替换矩阵分解、转成GPU友好矩阵乘的工程思路，可复用在自研二阶优化器的加速实现上

  - Kronecker因式分解的正定性保持设计，可借鉴到LLM+Rec端到端超大模型的二阶优化适配中，降低显存占用'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
传统拟牛顿（QN）优化方法难以适配深度学习的非凸目标、超大参数量场景，且依赖线搜索、特设曲率修正，计算效率低，无法落地大模型训练。

### 方法关键点
1. 基于变分目标推导正定曲率估计，无需特设曲率修正即可处理非凸场景的负曲率问题；
2. 设计对角、Kronecker因式分解两种变体，从构造上保证正定性，适配超大规模神经网络；
3. 采用稳定的耦合Newton-Schulz迭代做矩阵运算，将高成本矩阵分解替换为GPU友好的矩阵乘法，无需线搜索。

### 关键结果
在循环网络、深度自编码器、物理信息神经网络、136M参数物理信息扩散模型等病态优化任务上，损失普遍低于Adam、Muon、SOAP等主流基准优化器。
