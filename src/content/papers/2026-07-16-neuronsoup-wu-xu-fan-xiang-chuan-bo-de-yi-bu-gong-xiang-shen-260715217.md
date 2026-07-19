---
title: 'NeuronSoup: Evolving Asynchronous, Shared-Neuron Temporal Graphs without Backpropagation'
title_zh: NeuronSoup：无需反向传播的异步共享神经元时序图演化架构
authors:
- Subodh Kalia
arxiv_id: '2607.15217'
url: https://arxiv.org/abs/2607.15217
pdf_url: https://arxiv.org/pdf/2607.15217
published: '2026-07-16'
collected: '2026-07-19'
category: Training
direction: 无反向传播 · 遗传算法神经架构演化
tags:
- Neuroevolution
- Genetic Algorithm
- Asynchronous Neural Network
- Temporal Computing
- Backpropagation-free
one_liner: 提出基于遗传算法优化的异步共享神经元时序架构，无需反向传播即可实现端到端模型演化
practical_value: '- 端侧/边缘侧电商推荐场景可借鉴神经元共享设计，大幅压缩模型体积，适配算力受限的IoT导购终端

  - 嵌入非可微业务规则/约束的推荐任务可尝试遗传算法替代反向传播做端到端优化，规避可微性限制

  - 多模态推荐推理可复用动态计算深度设计，简单样本缩短链路降时延，复杂样本提升深度保效果'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有深度学习高度依赖反向传播，要求计算图可微、结构固定、计算深度统一，限制了架构灵活性与轻量化空间。

### 方法关键点
1. 替换同步逐层计算为异步延迟介导的信号传播，隐藏神经元跨路径共享，利用信号到达时序与极性产生干涉实现特征交互；
2. 用遗传算法协同优化拓扑、权重、延迟、连接性等全部架构参数，无需构建可微计算图，支持单样本自适应调整计算深度。

### 关键结果
在MNIST 10分类任务（输入为冻结ResNet18特征）上，演化10000代后取得85.9%测试精度，模型仅含266个隐藏神经元、204条激活路径，总大小仅115KB。
