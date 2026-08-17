---
title: Boosting Data Augmentation with Stochastic Weight Averaging
title_zh: 利用随机权重平均增强数据增广效果
authors:
- Longde Huang
- Axel Flinth
- Jan E. Gerken
arxiv_id: '2608.14373'
url: https://arxiv.org/abs/2608.14373
pdf_url: https://arxiv.org/pdf/2608.14373
published: '2026-08-14'
collected: '2026-08-17'
category: Training
direction: 深度学习训练优化 · 数据增广与SWA集成
tags:
- Data Augmentation
- Stochastic Weight Averaging
- Model Ensembling
- Equivariance
- Training Optimization
one_liner: 用无需重复训练的SWA替代深度集成，提升数据增广下的模型等变性能
practical_value: '- 推荐/搜索排序模型训练时，可在训练后期引入SWA替代多模型集成，无需额外训练成本就能提升数据增广带来的效果增益

  - 电商多模态内容理解（商品图、标题分类）场景，SWA+数据增广的组合可低成本提升模型对输入变换的鲁棒性

  - 落地成本极低，不需要额外多轮训练，仅需在常规训练收尾阶段收集若干步的权重做平均即可上线'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
数据增广是给通用神经网络注入任务对称性的低成本方案，但要实现完美等变需训练大规模深度集成，重复训练算力成本过高，难以落地。

### 方法关键点
将训练末期的随机权重轨迹用Ornstein--Uhlenbeck过程近似，证明无限宽度限制下，数据增广+SWA的组合可获得远超SWA单独作用的等变增益，无需多轮重复训练，仅需在常规训练后期取多个checkpoint的权重做平均即可实现。

### 关键结果
在CV、图分类的离散/连续对称任务上完成验证，SWA搭配数据增广可在几乎不增加训练成本的前提下，达到接近深度集成的等变性能提升
