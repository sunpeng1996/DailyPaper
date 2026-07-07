---
title: 'Born Discrete, Made Smooth: Variational Formulation of Shallow Neural Networks'
title_zh: 生而离散，化而为滑：浅层神经网络的变分公式化
authors:
- Matej Benko
- Pierre Bousquet
- Iwona Chlebicka
- Błażej Miasojedow
affiliations:
- Brno University of Technology
- Université de Toulouse
- INSA Toulouse
- CNRS
- University of Warsaw
arxiv_id: '2607.02003'
url: https://arxiv.org/abs/2607.02003
pdf_url: https://arxiv.org/pdf/2607.02003
published: '2026-07-02'
collected: '2026-07-07'
category: Other
direction: 浅层神经网络训练 · 变分优化理论
tags:
- Shallow Neural Networks
- Variational Calculus
- Optimization Theory
- Generalization Error
- Neural Tangent Kernel
one_liner: 提出用连续变分代理替代浅层神经网络离散训练问题，证明全局适定性与收敛速率
practical_value: '- 主要是学术贡献，业务可借鉴点有限

  - 小规格召回/排序小模型离线训练场景，可尝试借鉴离散转连续优化思路，探索跳过迭代优化的快速训练方案

  - 模型泛化性误差评估可参考本文给出的$1/\alpha$泛化误差上界、$O(1/N)$宽度收敛速率的推导逻辑'
score: 4
source: arxiv-stat.ML
depth: abstract
---

### 动机
神经网络训练的非凸优化、泛化性等底层原理长期缺乏完善理论支撑，现有Wasserstein、平均场方法存在正则性有限、离散化难度大等问题，难以解释过参数化网络的优异表现。
### 方法关键点
将浅层神经网络的离散训练问题转化为加权Sobolev空间上参数密度的$\lambda$-凸泛函连续变分代理问题，借助椭圆正则性与凸分析框架，无需迭代优化，仅求解单个线性系统即可得到最优参数密度。
### 关键结果
1. 泛化误差相对正则参数的收敛速率为$1/\alpha$；
2. 宽度为$N$的有限宽网络达到连续最优解的收敛速率为$O(1/N)$；
3. 填补了神经切线核（NTK）与特征学习机制间的理论鸿沟，为过参数化研究提供了变分法统一框架。
