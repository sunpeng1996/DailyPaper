---
title: Collaborative Synthetic Data Generation for Knowledge Transfer in Federated
  Learning
title_zh: 面向联邦学习知识迁移的协同合成数据生成方法
authors:
- Maximilian Andreas Hoefler
- Karsten Mueller
- Wojciech Samek
affiliations:
- Fraunhofer Heinrich Hertz Institute
- BIFOLD
- Technical University Berlin
arxiv_id: '2607.07565'
url: https://arxiv.org/abs/2607.07565
pdf_url: https://arxiv.org/pdf/2607.07565
published: '2026-07-08'
collected: '2026-07-09'
category: Training
direction: 联邦学习 · 隐私保护训练
tags:
- Federated Learning
- Differential Privacy
- Synthetic Data
- Knowledge Transfer
- One-shot Learning
one_liner: 带(ε,δ)差分隐私保障的单轮联邦学习框架FedKT-CSD，兼顾低通信开销与异质性鲁棒性
practical_value: '- 跨端隐私合规的推荐模型训练可复用该框架思路：用公开预训练autoencoder做共享隐空间，仅传输类条件隐层统计量而非原始数据，大幅降低端侧通信与计算开销

  - 差分隐私落地可参考其「安全聚合后加校准噪声」的实现方式，在保障(ε,δ)隐私合规的前提下最小化对模型效果的损伤

  - 单轮联邦训练的设计可直接迁移至多端用户行为数据联合建模场景，避免多轮通信的延迟与隐私风险'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
单轮联邦学习（OSFL）可大幅降低传统联邦学习的通信 overhead，但现有方案大多缺乏正式隐私保障，无法同时满足低通信量、异质性数据鲁棒性、严格隐私保护三个核心要求。
### 方法关键点
FedKT-CSD框架复用公开预训练autoencoder构建全局共享隐空间，客户端仅需1次前向传播编码私有数据，计算类条件隐层统计量后上传，无额外训练开销；服务端通过secure aggregation聚合统计量，添加校准差分隐私噪声后解码生成合成数据集，用于全局模型训练。
### 关键结果
天然具备(ε,δ)差分隐私保障，端侧计算、通信成本极低；跨多数据集、异质性场景下效果与非隐私基线持平甚至更优，支持大规模客户端扩展
