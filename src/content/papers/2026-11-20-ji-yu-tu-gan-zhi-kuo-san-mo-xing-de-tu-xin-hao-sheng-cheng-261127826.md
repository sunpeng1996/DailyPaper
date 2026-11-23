---
title: Graph Signal Generation via Graph-Aware Diffusion Models
title_zh: 基于图感知扩散模型的图信号生成方法
authors:
- Vimal K B
- Sergio Rozada
- Antonio G. Marques
- Elvin Isufi
- Hadi J. Rad
affiliations:
- Delft University of Technology
- King Juan Carlos University
arxiv_id: '2611.27826'
url: https://arxiv.org/abs/2611.27826
pdf_url: https://arxiv.org/pdf/2611.27826
published: '2026-11-20'
collected: '2026-11-23'
category: GenRec
direction: 生成式推荐 · 图信号扩散优化
tags:
- Diffusion Model
- Graph Signal Processing
- Recommendation System
- Noise Scheduling
- Graph Neural Network
one_liner: 提出图感知扩散GAD与MASS噪声调度，提升图信号生成质量并大幅减少采样步数
practical_value: '- 做协同推荐等图信号生成任务时，可替换传统各向同性扩散为GAD，将图拓扑先验嵌入扩散前向过程，降低GNN去噪器学习负担，小样本场景收益更显著

  - 扩散模型噪声调度可参考MASS思路，对不同频谱分量设置独立扩散率拉平各分量SNR，降低反向SDE刚度，减少采样步数，适配推荐系统低延迟推理需求

  - 用户交互序列预测、流量补全等图信号生成任务，可直接复用MASS的频谱自适应训练/采样流程，无额外训练参数，仅新增O(n)频谱运算开销'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有扩散模型处理图信号仅在去噪网络侧引入图拓扑，前向噪声节点独立，无法利用图先验降低学习成本；共享扩散率会导致高低频谱SNR指数级分化，高频分量拟合难度大、反向SDE刚度高、采样步数多，难以适配推荐、流量预测等低延迟业务场景。
### 方法关键点
- 设计图感知扩散（GAD），前向过程采用拉普拉斯驱动的图热扩散叠加高斯噪声，将图拓扑先验嵌入扩散的GMRF先验，去噪网络仅需学习数据与先验的偏差，大幅降低拟合成本
- 提出模式自适应SNR调度（MASS），为每个图频谱分量分配独立扩散率，保证所有分量在任意扩散步的SNR一致，均衡各频率拟合误差，理论上将反向SDE刚度从与拉普拉斯条件数线性相关降低到对数相关
- 训练、采样流程仅新增频谱维度逐元素运算，无额外可训练参数，兼容现有GNN去噪器与各类快速采样器
### 关键结果
在合成图信号、协同推荐、交通流量补全、时空预测任务上对比各向同性扩散、共享率GAD等基线：推荐指标提升5~19%，交通补全RMSE最高降低7.8%且采样步数减半，时空预测仅需3步反向采样即可降低MAE/RMSE，反向刚度比共享率方案低488~149000倍。
### 核心结论
将图拓扑先验嵌入扩散前向过程、按频谱自适应调整噪声调度，可同时提升图信号生成质量和采样效率，是生成式推荐等图场景落地的高性价比优化方向。
