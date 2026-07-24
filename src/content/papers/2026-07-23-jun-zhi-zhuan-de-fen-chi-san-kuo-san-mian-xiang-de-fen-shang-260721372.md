---
title: 'Mean-to-Score Discrete Diffusion: Posterior-Mean Denoisers for Score Entropy'
title_zh: 均值转得分离散扩散：面向得分熵的后验均值去噪器
authors:
- Jingyuan Li
- Xiaoyi Jiang
- Yixuan Jiang
- Wei Liu
- Yi Zhu
- Zuoqiang Shi
- Pipi Hu
affiliations:
- Tsinghua University
- Beijing Institute of Mathematical Sciences and Applications
- Wuhan University
- MathonAI
arxiv_id: '2607.21372'
url: https://arxiv.org/abs/2607.21372
pdf_url: https://arxiv.org/pdf/2607.21372
published: '2026-07-23'
collected: '2026-07-24'
category: Training
direction: 离散扩散模型 · 训练优化
tags:
- Diffusion Model
- Discrete Diffusion
- SEDD
- M2S
- Generative Model
- CTMC
one_liner: 提出M2S离散扩散范式，通过后验均值映射得分，从结构上解决SEDD的贝叶斯不可实现问题，提升生成性能
practical_value: '- 生成式推荐/广告文案/Query生成场景用离散扩散生成token时，可复用M2S思路，避免有限步采样负权重问题，提升生成稳定性

  - 现有SEDD类离散扩散生成任务可先尝试低成本得分投影后处理方案，无需修改模型/采样器即可大幅降低PPL

  - 训练离散扩散生成模型时，优先选择「预测后验均值→映射为得分」的架构，天然满足贝叶斯约束，效果优于后处理方案'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有SEDD离散扩散仅约束得分比为正，未保证贝叶斯可实现性：约1/4训练后得分向量违反坐标边界，超1/2得分与有效干净token后验不兼容，有限步采样易出现负预归一化权重，劣化生成效果。
### 方法关键点
1. 低成本后处理：将原始得分投影到桥多面体，可直接消除所有观测到的负权重；
2. 结构化M2S方案：模型先预测干净token后验均值，再通过依赖核的精确线性映射转换为得分，天然满足贝叶斯可实现性，适配任意满足轻量支撑条件的坐标级CTMC。
### 关键结果
后处理方案无需改动采样器即可将生成PPL从203.6降至175.1；CIFAR-10生成任务中M2S将FID-50k从42.83降至28.09；170M参数文本生成模型128步采样下PPL达143.3，较最优纯均匀SEDD基线低40.3。
