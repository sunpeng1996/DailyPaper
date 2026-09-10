---
title: 'One Loop, Two Gains: Can Active Learning win the Lottery for Free?'
title_zh: 单循环双收益：主动学习能否免费获得彩票赢票子网络
authors:
- Benedikt Tscheschner
- Eduardo Veas
- Marc Masana
affiliations:
- University of Technology Graz
- Know-Center Research GmbH
- Institute of Visual Computing
arxiv_id: '2609.10311'
url: https://arxiv.org/abs/2609.10311
pdf_url: https://arxiv.org/pdf/2609.10311
published: '2026-09-09'
collected: '2026-09-10'
category: Training
direction: 主动学习·模型剪枝 训练效率优化
tags:
- Active Learning
- Lottery Ticket Hypothesis
- Model Pruning
- Sparse Model
- Training Efficiency
one_liner: 将迭代幅度剪枝融入主动学习训练循环，零额外成本得到95%稀疏度且精度匹配全量模型的赢票子网络
practical_value: '- 电商冷启动少标注场景的搜索/推荐模型训练，可复用I&P框架，将剪枝嵌入主动学习迭代循环，零额外成本得到可直接部署的稀疏模型

  - 针对大模型在线迭代的算力瓶颈，95%稀疏度仍能保持精度，可直接降低每轮重训、未标注候选池打分的耗时，适配大语料/大物品池的召回排序场景

  - 做Agent端侧小模型轻量化时，可借鉴主动学习+剪枝耦合的思路，无需单独跑剪枝流程，大幅降低训练和部署成本'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有深度主动学习（DAL）和迭代幅度剪枝均依赖多轮从零开始重训，算力开销极高，但两个范式长期被独立研究，未挖掘主动学习自带的迭代训练结构与剪枝流程的匹配性，导致DAL在大模型、大未标注池场景下难以落地。

### 方法关键点
提出Improve & Prune（I&P）方法，将幅度剪枝直接嵌入每一轮主动学习的重训周期，无额外计算成本；覆盖多采集函数、多架构、多图像分类数据集，包含主动微调场景，验证非平稳数据范式下赢票子网络的可获得性。

### 关键结果数字
每轮迭代输出的稀疏模型在**95%稀疏度**下精度与全量稠密模型完全持平，同时解决主动学习两大算力瓶颈：单轮模型重训耗时、未标注池采集打分耗时，大幅提升DAL的落地可行性。
