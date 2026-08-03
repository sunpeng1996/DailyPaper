---
title: 'GQ-FSL: Green Quantized Federated Split Learning'
title_zh: GQ-FSL：绿色量化联邦拆分学习
authors:
- Idan Roth
- Lutz Lampe
affiliations:
- The University of British Columbia
arxiv_id: '2607.29659'
url: https://arxiv.org/abs/2607.29659
pdf_url: https://arxiv.org/pdf/2607.29659
published: '2026-07-31'
collected: '2026-08-03'
category: Training
direction: 分布式训练 · 联邦学习能效优化
tags:
- Federated Learning
- Split Learning
- Quantization
- Energy Efficiency
- Edge AI
one_liner: 提出支持不对称精度的绿色量化联邦拆分学习框架，在精度约束下大幅降低边缘系统总能耗
practical_value: '- 端侧小模型联邦训练场景可复用不对称量化策略，客户端用低精度、服务端用高精度，兼顾端侧能耗和模型效果

  - 端云协同训练的模型拆分点可参考论文的联合优化方法，在满足业务精度要求下最小化端侧算力/通信开销

  - 边缘设备部署大模型推理的场景，可复用拆分+不对称量化的思路，降低端侧能耗压力'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
边缘设备部署DNN受严格的算力、能耗约束，传统联邦拆分学习（FSL）通过卸载计算到边缘服务器缓解端侧压力，但切分层数据、子模型的频繁传输仍带来极高能耗，且端侧资源约束易导致全局收敛退化。

### 方法关键点
1. 提出GQ-FSL框架，本地协作训练与无线传输环节均引入随机量化，同时支持客户端、服务端子模型的不对称精度设置，解耦端侧能耗约束与全局收敛退化问题；
2. 构建拆分架构的参数化能耗模型，推导非独立同分布数据下的理论收敛边界；
3. 联合优化DNN切分点、两端精度配置，在满足目标精度约束的前提下最小化系统总能耗。

### 关键结果
对比量化联邦学习、全精度FSL实现更优能效，可支撑资源受限设备上的大规模DNN部署
