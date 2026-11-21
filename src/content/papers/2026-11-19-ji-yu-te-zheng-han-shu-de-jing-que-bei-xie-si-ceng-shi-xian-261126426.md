---
title: Exact Bayesian layers via characteristic functions
title_zh: 基于特征函数的精确贝叶斯层实现
authors:
- William H. W. Thompson
- Guillaume St-Onge
- Laurent Hébert-Dufresne
- Jean-Gabriel Young
affiliations:
- Vermont Complex Systems Institute, University of Vermont
- School of Electrical Engineering and Computer Science, University of Ottawa
- Department of Computer Science, University of Vermont
- Santa Fe Institute
- Department of Mathematics and Statistics, University of Vermont
arxiv_id: '2611.26426'
url: https://arxiv.org/abs/2611.26426
pdf_url: https://arxiv.org/pdf/2611.26426
published: '2026-11-19'
collected: '2026-11-21'
category: Training
direction: 贝叶斯神经网络 · 无采样变分推理训练
tags:
- Bayesian Neural Network
- Variational Inference
- Characteristic Function
- Uncertainty Estimation
- ReLU Layer
one_liner: 提出基于特征函数的无采样贝叶斯神经网络训练方法，校准精度更高、尾部不确定性估计更准
practical_value: '- 推荐系统冷启动、小流量新策略测试等小样本场景，可借鉴CF-VI无采样不确定性估计方案，替代传统Monte Carlo采样降低推理延迟，同时提升不确定性校准精度，优化排序/召回策略的鲁棒性

  - 电商交易风控、高价值商品销量预测等重尾分布场景，可复用特征函数传播思路，准确捕捉低概率高影响事件的尾部不确定性，避免极端场景下的策略误判

  - 落地BNN做模型校准优化时，可直接复用CF-VI的闭形式ELBO计算方法，天然适配Gaussian、Poisson、Gamma等多种似然，大幅降低BNN的训练与落地成本'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
Bayesian Neural Networks（BNN）可提供有理论支撑的不确定性估计，但传统基于Monte Carlo采样的训练方案计算成本极高；现有无采样变分推理方法默认假设输出为高斯分布，在非高斯业务场景下误差过大，无法适配推荐、风控等多元场景需求。
### 方法关键点
1. 提出CF-Prop不确定性传播框架，通过特征函数直接计算贝叶斯ReLU层的精确输出分布，无需采样即可支持非高斯场景；
2. 基于特征函数传播推导得到闭形式ELBO，适配Gaussian、Poisson、Gamma等多类似然，实现高效无采样变分推理算法CF-VI。
### 关键结果
- CIFAR-100数据集上，CF-VI的校准误差为所有对比方法最低，较次优方案降低约35%；
- 重尾分布的保险理赔数据集上，CF-VI可准确捕捉传统无采样方法、Monte Carlo方法均严重低估的尾部不确定性。
