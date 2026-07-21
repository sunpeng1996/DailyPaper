---
title: Backpropagation-Free Trunk Training via the Split Forward Gradients
title_zh: 基于拆分前向梯度的无需反向传播主干网络训练方法
authors:
- Tian Qin
- Wei-Min Huang
affiliations:
- Lehigh University
arxiv_id: '2607.16612'
url: https://arxiv.org/abs/2607.16612
pdf_url: https://arxiv.org/pdf/2607.16612
published: '2026-07-18'
collected: '2026-07-21'
category: Training
direction: 无反向传播训练 · 前向梯度优化
tags:
- Forward Gradient
- Backpropagation-Free
- Memory-Efficient Training
- Split Learning
- Transformer Training
one_liner: 提出Split-FG拆分前向梯度方法，无需主干反向传播，降显存同时缓解前向梯度高方差问题
practical_value: '- 训练带超大Embedding层的电商推荐/检索模型时，可将Embedding作为头部用闭式梯度更新，上层主干网络用低学习率前向梯度训练，降低反向传播显存开销

  - 边缘端/资源受限硬件的小模型落地场景，可参考Split-FG的主干-头部分拆思路，无需完整反向传播即可完成模型迭代

  - 碰到前向梯度训练效果不如冻结主干的情况，可给主干梯度设置约0.03的学习率缩放因子，避免噪声导致的参数漂移'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
反向传播训练需要存储全部中间激活，显存占用随模型深度、序列长度线性增长，在边缘硬件、光/模拟加速器等无法支持反向传播的场景下无法落地；传统前向梯度无需反向传播，但梯度估计方差随参数量线性增长，难以扩展到大模型。

### 方法关键点
- 将网络拆分为主干（trunk）和头部（head）两部分，头部梯度直接用闭式计算得到精确值，仅主干用Jacobian-vector积做前向梯度估计，大幅降低估计方差
- 主干梯度估计方差与主干参数量正相关，大头部小主干的架构（如带大词表的语言模型、带大Embedding的推荐模型）天然适配该方法
- 针对Adam对噪声梯度更新过强的问题，给主干梯度设置远小于头部的学习率缩放因子，避免主干参数漂移

### 关键结果
在WikiText-103上训练16M参数量的GPT-2风格模型，Split-FG验证困惑度达387，比纯前向梯度基线的2885低7.5倍，比冻结主干的基线668低42%，峰值显存比反向传播低35%；CIFAR-10/100上分别达到60.5%/35.2%的Top-1准确率，均优于其他无反向传播基线。

最值得记住的一句话：混合精确/估计梯度训练时，Adam的归一化只能平衡更新幅度，无法平衡信噪比，估计梯度的参数组需要下调1~2个数量级的学习率才能避免效果劣于冻结参数
