---
title: 'Beyond Backpropagation: Monte Carlo Method Can Train Deep Neural Networks'
title_zh: 跳出反向传播：使用蒙特卡洛方法训练深度神经网络
authors:
- Hong Zhao
affiliations:
- Department of Physics, Xiamen University
- Lanzhou Center for Theoretical Physics, Lanzhou University
arxiv_id: '2607.08406'
url: https://arxiv.org/abs/2607.08406
pdf_url: https://arxiv.org/pdf/2607.08406
published: '2026-07-09'
collected: '2026-07-11'
category: Training
direction: 无梯度深度神经网络训练方法研究
tags:
- Monte Carlo
- Gradient-Free Training
- Backpropagation
- DNN Training
- Transformer
one_liner: 提出单GPU可运行的极简蒙特卡洛无梯度训练方法，可训练20层以上深度网络甚至简单Transformer
practical_value: '- 小场景小模型微调可尝试该无梯度方法，避开梯度消失/爆炸问题，无需BN、残差连接等结构，降低模型工程复杂度

  - 离散权重模型、非常规激活函数（如高斯）的特殊场景模型训练可直接复用该蒙特卡洛训练逻辑，无需适配反向传播规则

  - 模型轻量化剪枝场景可参考其纯剪枝训练思路，直接在训练过程中完成参数压缩，减少后处理剪枝的效果损失'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
当前DNN训练高度依赖BP反向传播，存在固有梯度消失/爆炸问题，高实用性无梯度训练方法长期处于探索阶段

### 方法关键点
采用单GPU即可运行的极简蒙特卡洛算法：随机突变单个参数，仅当loss下降时保留该突变，否则重试；无需BN、残差连接等常规辅助技术即可训练深层网络，天然支持纯剪枝训练、离散权重、高斯等非常规激活函数

### 关键结果
成功训练20层以上深度网络、单隐藏层16384神经元宽网络；可完成简单Transformer在MNIST图像分类、Tiny Shakespeare字符级语言建模任务的训练，验证了无梯度训练的落地可行性
