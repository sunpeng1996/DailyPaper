---
title: Sample-Adaptive Latent Rewards for Uncertainty-Guided Diffusion Post-Training
title_zh: 面向不确定性引导扩散后训练的样本自适应隐式奖励框架
authors:
- Rui Li
- Yuanzhi Liang
- Ke Hao
- Ziqiao Weng
- Haibin Huang
- Chi Zhang
- XueLong Li
affiliations:
- University of Science and Technology of China
- Institute of Artificial Intelligence, China Telecom (TeleAI)
- Shanghai Jiao Tong University
arxiv_id: '2608.06125'
url: https://arxiv.org/abs/2608.06125
pdf_url: https://arxiv.org/pdf/2608.06125
published: '2026-08-06'
collected: '2026-08-07'
category: Training
direction: 扩散模型后训练 · 奖励不确定性优化
tags:
- Latent Reward Model
- Diffusion Model
- Uncertainty Estimation
- Post-Training
- Reward Optimization
one_liner: 提出SURE隐空间框架，通过带不确定性估计的样本自适应隐式奖励引导扩散模型后训练优化
practical_value: '- 电商生成式推荐的商品图/营销短视频AIGC场景，可引入带不确定性估计的隐式奖励模型替代像素级奖励评估，减少VAE解码开销，提升素材对齐人类偏好的效率

  - 推荐系统排序/召回的Reward建模可复用样本自适应权重思路，对低置信度奖励预测打折扣，避免reward hacking导致的模型优化走偏

  - 大模型RLHF对齐流程可借鉴不确定性加权的局部奖励回传方案，仅回传局部步的加权奖励，降低训练显存占用与计算量'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有隐式奖励模型仅输出标量分数，无预测不确定性估计，生成器无法判断反馈可靠性，易导致优化方向错误、出现reward hacking问题；传统扩散后训练依赖像素空间解码，计算开销大。

### 方法关键点
1. 提出SURE统一隐空间框架，适配图像/视频扩散模型后训练，全程无需像素空间解码与完整去噪计算图
2. SURE-LRM样本自适应隐式奖励模型，为每个带噪隐向量预测高斯分布，均值为奖励分数，方差表示预测不确定性，无需额外人工标注
3. SURE-REFL不确定性引导奖励反馈学习，将方差转换为同过渡步样本的可靠性权重，仅通过局部过渡步回传加权奖励

### 关键结果
SURE-LRM偏好预测效果优于强基线；SURE-REFL在多指标上达SOTA，优化稳定性显著提升，VBench质量、语义、总分均为参评方法最高
