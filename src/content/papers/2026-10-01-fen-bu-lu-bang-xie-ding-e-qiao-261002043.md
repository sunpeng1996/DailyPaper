---
title: Distributionally Robust Schrödinger Bridge
title_zh: 分布鲁棒薛定谔桥
authors:
- Jinhwan Sul
- Panagiotis Theodoropoulos
- Vincent Pacelli
- Jaemoo Choi
- Evangelos Theodorou
affiliations:
- Georgia Institute of Technology
- Department of Aerospace Engineering, Georgia Institute of Technology
arxiv_id: '2610.02043'
url: https://arxiv.org/abs/2610.02043
pdf_url: https://arxiv.org/pdf/2610.02043
published: '2026-10-01'
collected: '2026-10-03'
category: Training
direction: 分布鲁棒优化 · 生成式建模方法
tags:
- Distributional Robustness
- Schrödinger Bridge
- Stochastic Optimal Control
- Generative Modeling
- Wasserstein Distance
one_liner: 提出分布鲁棒薛定谔桥DRSB，解决初始分布漂移下SB的目标分布恢复失效问题
practical_value: '- 做GenRec的用户-物品分布对齐、LLM调用输入分布漂移问题，可引入DRSB的鲁棒优化思路，缓解训练推理分布 mismatch
  导致的效果下降

  - 输入扰动敏感的生成场景（如AIGC商品文案、个性化推荐理由生成），可参考其对抗初始分布更新+控制器训练的交替算法框架提升鲁棒性

  - 度量不同分布间的对齐效果时，可复用其Sinkhorn/Wasserstein梯度近似方法降低计算开销'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
标准Schrödinger Bridge（SB）学习预设初始与目标分布间的随机传输映射，测试时初始分布漂移会导致终端目标分布恢复失败，现有方法无法处理初始分布的不确定性。
### 方法关键点
1. 提出DRSB，在标称初始分布的歧义集内最小化目标的最坏值，目标包含控制能量、终端分布与目标分布的KL惩罚两项；
2. 推导精确变分公式，将固定终端成本子问题关联到随机最优控制与分布鲁棒优化；
3. 设计交替优化算法：更新对抗初始分布、估计终端对数密度比、训练控制器，同时开发Wasserstein、Sinkhorn两种变体近似对抗更新梯度。
### 关键结果
1. 二维传输、图像到图像翻译任务中，相较标准SB输入扰动鲁棒性显著提升，存在小幅标称性能权衡；
2. 高斯混合传输任务中，Sinkhorn DRSB在两个未见过的噪声水平下，平均切片Wasserstein距离均低于固定层级噪声增强方法
