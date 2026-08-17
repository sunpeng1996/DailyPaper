---
title: Designing Compact Neural Architectures via Neuron Gating and Mixed Activation
title_zh: 基于神经元门控与混合激活的紧凑神经架构设计
authors:
- Abhishek Shukla
- Ankur Sinha
- Faiz Hamid
affiliations:
- Department of Management Sciences, IIT Kanpur, India
- Krishnamurthy Tandon School of AI, IIM Ahmedabad, India
arxiv_id: '2608.14443'
url: https://arxiv.org/abs/2608.14443
pdf_url: https://arxiv.org/pdf/2608.14443
published: '2026-08-14'
collected: '2026-08-17'
category: Training
direction: 神经网络架构搜索 · 紧凑模型优化
tags:
- NAS
- Compact Model
- Bilevel Optimization
- Differentiable Search
- Activation Optimization
one_liner: 提出三种连续松弛的可微NAS方法，适配多类网络架构，生成高精度低参数量的紧凑模型
practical_value: '- 推荐系统排序/召回的MLP/CNN类backbone可直接复用NAS-NG方法，在不损失精度的前提下压缩参数量，降低线上推理延迟

  - 大模型小参数蒸馏场景可引入神经元门控+混合激活的连续松弛思路，替代离散剪枝，实现端到端的小模型结构优化

  - 多场景小模型部署时，可基于该双层优化框架适配业务数据，自动搜索适配场景的最优轻量架构，减少人工调参成本'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
传统离散NAS存在决策离散、搜索空间指数级膨胀、候选模型训练成本高的问题，难以跨MLP、CNN、Transformer等多架构实现高性能紧凑模型搜索。
### 方法关键点
提出基于双层优化的可微NAS框架，将神经元选择、激活函数选择的离散决策替换为连续松弛变量，实现组合架构空间的可微分优化，衍生出三类方法：NAS-NG（神经元门控）、NAS-MA（混合激活）、NAS-NGMA（两者结合），支持端到端训练搜索。
### 关键结果
- MNIST数据集：NAS-NGMA实现98.68%测试精度的MLP仅需7.69M参数，NAS-NG实现99.63%精度的CNN仅需0.26M参数
- CIFAR-10数据集：三类方法精度均优于原生DARTS，可在压缩参数量的同时提升模型预测效果
