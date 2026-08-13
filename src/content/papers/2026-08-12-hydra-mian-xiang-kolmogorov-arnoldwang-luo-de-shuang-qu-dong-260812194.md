---
title: 'HYDRA: Hyperbolic Dynamic Representation Architecture for Kolmogorov-Arnold
  Networks'
title_zh: HYDRA：面向Kolmogorov-Arnold网络的双曲动态表示架构
authors:
- Zhao Su
- Yuxin Xia
- Haoran Li
- Jun Shen
- Qi Zhu
- Qingguo Zhou
- Binbin Yong
affiliations:
- Lanzhou University
- Monash University
- University of Wollongong
- Nanjing University of Aeronautics and Astronautics
arxiv_id: '2608.12194'
url: https://arxiv.org/abs/2608.12194
pdf_url: https://arxiv.org/pdf/2608.12194
published: '2026-08-12'
collected: '2026-08-13'
category: Training
direction: KAN架构优化 · 参数高效训练
tags:
- KAN
- Hyperbolic Representation
- Parameter Efficiency
- Low-rank
- Interpretability
one_liner: 针对KAN参数冗余问题提出双曲扩展架构HYDRA，兼顾预测性能、参数效率与可解释性
practical_value: '- 可复用低秩原型块跨维度共享变换的思路，优化推荐系统CTR/CVR预估塔的MLP层、大模型LoRA微调层，降低参数冗余提升推理速度

  - 双曲空间映射+半径控制的方法可迁移到电商用户/物品层级表示建模（如类目树、兴趣分层），缓解欧氏空间表示瓶颈，提升训练稳定性

  - 想要落地KAN做非线性拟合任务（如定价预测、转化率拟合）时，可采用HYDRA的双曲优化架构解决原生KAN参数过大难部署的问题'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
KAN通过将标量权重替换为可学习单变量函数，大幅提升了非线性函数拟合能力，但每个连接分配独立函数的设计带来极高参数冗余，可扩展性、训练与推理效率受限，难以落地工业场景。
### 方法关键点
1. 提出参数高效的KAN双曲扩展架构HYDRA，将向量输入映射到庞加莱球的有界双曲隐空间，在切空间执行KAN风格的函数更新；
2. 引入低秩原型块，跨隐层维度共享函数变换，大幅降低参数规模；
3. 双曲表示的结构化径向坐标天然支持可解释性，额外的半径控制机制避免边界饱和，提升训练稳定性。
### 关键结果
在8个公开基准数据集上，HYDRA预测性能持平或优于原生KAN，同时参数效率、表示可解释性均有明显提升。
