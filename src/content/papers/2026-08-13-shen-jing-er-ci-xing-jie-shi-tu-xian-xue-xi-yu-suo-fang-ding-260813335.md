---
title: 'Neural Quadratic Forms: A Unified Minimal Model for Sudden Learning and Scaling
  Laws'
title_zh: 神经二次型：解释突现学习与缩放定律的统一极简模型
authors:
- Liu Ziyin
- Yizhou Xu
- Tomaso Poggio
- Isaac Chuang
affiliations:
- Massachusetts Institute of Technology
- École Polytechnique Fédérale de Lausanne
arxiv_id: '2608.13335'
url: https://arxiv.org/abs/2608.13335
pdf_url: https://arxiv.org/pdf/2608.13335
published: '2026-08-13'
collected: '2026-08-15'
category: Training
direction: 大模型训练动力学 · 缩放定律理论建模
tags:
- Training Dynamics
- Scaling Laws
- Gradient Descent
- Neural Network Theory
- MoE
one_liner: 通过对称约束推导神经二次型统一模型，解释不同NN架构的训练突跳与缩放定律共性
practical_value: '- 做大模型/LLM4Rec预训练、LoRA微调缩放规划时，可复用该理论的幂律指数预测能力，减少超参扫查的算力消耗

  - 微调电商垂域大模型时，可根据训练任务对收敛速度的要求，调整初始权重大小，避免过小初始化带来的过长训练平台期

  - 开发跨Attention、MoE、卷积等多架构的统一训练框架时，可复用结构矩阵$A(x)$的抽象，降低不同架构的训练逻辑适配成本'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
梯度下降训练神经网络时存在两类跨架构普遍存在的矛盾现象：单训练轨迹损失长期处于平台后突降，跨模型/数据/算力尺度的训练损失符合平滑幂律缩放，此前缺乏统一理论解释。
### 方法关键点
利用网络层单元可置换的对称性，结合原点梯度消失、初始化权重趋近于0的约束，推导得到训练初始阶段的通用主导项为二次型$	ext{Tr}[WW^{	op}A(x)]$，所有架构差异被封装到可单独计算的结构矩阵$A(x)$中；训练动力学收敛到序参数$M=WW^	op$，数据矩阵共特征基时可简化为Lotka-Volterra方程，模式逐次激活。
### 关键结果
初始权重越小，模式激活间隔越长，训练平台期是平滑流的奇异极限；大量未解析模式合并时形成幂律训练曲线，理论预测的指数与不同训练方法、架构的数值实验结果完全匹配。
