---
title: Adaptive Quantization Preserves Fast Rates for TD Learning over Rate-Limited
  Channels
title_zh: 限速率信道下可保留TD学习收敛速率的自适应量化方法
authors:
- Sreejeet Maity
- Aritra Mitra
arxiv_id: '2611.12878'
url: https://arxiv.org/abs/2611.12878
pdf_url: https://arxiv.org/pdf/2611.12878
published: '2026-11-09'
collected: '2026-11-11'
category: Agent
direction: Agent 通信受限TD学习优化
tags:
- TD Learning
- Reinforcement Learning
- Adaptive Quantization
- Communication Efficiency
- Policy Evaluation
one_liner: 提出BAQ-TD算法，限速率信道下大幅降低通信开销同时保留TD学习最优收敛速率
practical_value: "- 边缘端部署的交互Agent（如端侧推荐/广告触达Agent）可复用批处理+自适应量化方案，大幅降低端云通信带宽开销\n- 分布式RL训练场景下，梯度/更新量传输可借鉴创新点编码+自适应量化策略，在不损失收敛效率的前提下降低通信复杂度\n\
  - 端侧时序用户行为建模的TD类更新可参考该方法，避免全量梯度回传，仅需传输$\boldsymbol{\text{O}(d \text{log} T)}$比特即可达到最优收敛速率"
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
通信受限场景下的强化学习任务中，端侧Agent与云端服务器之间的传输带宽有限，现有量化方案通信复杂度高，无法保留无限制信道下TD学习的最优收敛速率。

### 方法关键点
提出Batched Adaptively Quantized TD（BAQ-TD）算法，核心设计两点：1. 采用批处理机制降低待传输更新量的方差；2. 用自适应量化策略对创新量进行编码传输。

### 关键结果数字
理论证明在信道容量高于特定阈值时，BAQ-TD可在对数因子范围内保留无量化TD的收敛速率；$d$维价值函数参数下，仅需传输$	ext{O}(d 	ext{log}(T))$比特即可达到$	ilde{	ext{O}}(1/T)$的阶最优收敛速率，通信复杂度较此前工作呈指数级下降。
