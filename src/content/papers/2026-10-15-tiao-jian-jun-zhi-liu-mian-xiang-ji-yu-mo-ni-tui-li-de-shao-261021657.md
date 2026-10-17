---
title: 'Conditional Mean Flows: Few-Step Densities for Simulation-Based Inference'
title_zh: 条件均值流：面向基于模拟推理的少步密度估计方法
authors:
- Jonas Arruda
- Jan Hasenauer
- Stefan T. Radev
affiliations:
- University of Bonn
- Rensselaer Polytechnic Institute
arxiv_id: '2610.21657'
url: https://arxiv.org/abs/2610.21657
pdf_url: https://arxiv.org/pdf/2610.21657
published: '2026-10-15'
collected: '2026-10-17'
category: Training
direction: 生成模型训练 · 流匹配推理加速
tags:
- Flow Matching
- Generative Model
- Density Estimation
- Inference Acceleration
- MCMC
one_liner: 提出条件均值流实现少步采样与可处理密度评估，大幅降低基于模拟推理的计算开销
practical_value: '- 流匹配少步优化思路可迁移到GenRec场景的采样加速，在保证生成质量的前提下减少推理步数，降低线上生成推荐的延迟

  - 快速密度评估方法可复用在广告/推荐的MCMC采样模块，比如召回重排序的采样环节，数千次密度评估开销可降低2个数量级

  - 独立掩码边际似然估计思路可用于冷启动用户偏好分布建模，无需全量特征即可快速估计用户偏好的边际分布，提升冷启动推荐效率'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
流匹配是基于模拟推理（SBI）的主流生成方法，但推理阶段需数值积分，后验采样成本极高，尤其是MCMC场景需数千次重复密度评估，开销过大难以落地。
### 方法关键点
1. 提出条件均值流框架，同时支持少步采样与可处理密度评估，兼顾流模型的灵活性与推理效率；
2. 均值流目标可精准识别条件流映射，独立掩码机制可直接估计边际似然，同时支持后验与似然近似两类任务。
### 关键结果数字
单步条件均值流的密度估计误差与200步流匹配相当，下游MCMC采样速度提升约200倍，在多类SBI任务上保持精度的同时大幅降低推理开销。
