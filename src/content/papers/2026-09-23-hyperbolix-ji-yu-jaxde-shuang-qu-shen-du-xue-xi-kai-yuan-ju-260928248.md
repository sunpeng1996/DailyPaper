---
title: 'hyperbolix: Hyperbolic Deep Learning in JAX'
title_zh: hyperbolix：基于JAX的双曲深度学习开源工具库
authors:
- Timo Klein
- Thomas Lang
- Yllka Velaj
- Sebastian Tschiatschek
affiliations:
- University of Vienna, Austria
arxiv_id: '2609.28248'
url: https://arxiv.org/abs/2609.28248
pdf_url: https://arxiv.org/pdf/2609.28248
published: '2026-09-23'
collected: '2026-09-24'
category: Other
direction: 双曲深度学习 · JAX开源工具库
tags:
- Hyperbolic Deep Learning
- JAX
- Flax
- Riemannian Optimization
- Open Source
one_liner: 首个JAX生态通用双曲深度学习库，支持多流形、全栈算子与无精度消去的稳定计算
practical_value: '- 做用户/物品层级建模、长尾分布建模的RecSys从业者可直接用该库快速实现双曲空间嵌入，无需手动封装底层双曲算子

  - 库中预制的双曲注意力、卷积、优化器可直接嵌入现有LLM4Rec、生成式推荐架构，适配JAX生态的训练推理加速能力

  - 双曲面无消去距离计算trick可直接迁移到自研双曲嵌入代码中，解决远距离样本计算NaN、精度大幅下降的问题'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
JAX生态此前缺乏通用、稳定的双曲深度学习工具，手动实现双曲算子易出现精度损失、兼容性差问题，无法支撑大规模双曲模型快速开发。
### 方法关键点
基于Flax NNX构建，统一封装欧氏空间、庞加莱球、双曲面等6类流形的公共接口，实现线性层、注意力、卷积、Riemannian优化器、降维等全栈双曲算子；遵循JAX原生API设计，流形无状态、曲率可 runtime 传入，支持`jax.vmap`批量操作；双曲面两点运算采用无消去公式规避精度损失。
### 关键结果
所有算子均通过float32/float64精度校验；双曲面远距离计算场景下，传统实现返回NaN时，该库仍保持float32精度；MIT许可完全开源。
