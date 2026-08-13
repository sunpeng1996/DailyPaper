---
title: Simplex Relaxation for Discrete Diffusion
title_zh: 面向离散扩散模型的单纯形松弛优化方法
authors:
- Jinya Sakurai
- Patrick Pynadath
- Satoshi Hayakawa
- Jaehong Yoon
- Xulei Yang
- Nancy F. Chen
- Xun Xu
affiliations:
- NTU Singapore
- The University of Tokyo
- Purdue University
- A*STAR IAIC
- A*STAR CFAR
arxiv_id: '2608.10615'
url: https://arxiv.org/abs/2608.10615
pdf_url: https://arxiv.org/pdf/2608.10615
published: '2026-08-10'
collected: '2026-08-13'
category: Training
direction: 离散扩散模型 · 训练目标优化
tags:
- Discrete Diffusion
- Categorical Generation
- Training Objective
- Generative Model
- Simplex Relaxation
one_liner: 提出Simplax类别增强框架，不改动离散扩散加噪流程即可显著提升离散生成任务性能
practical_value: '- 生成式推荐场景做Semantic ID、商品文案、query改写的离散扩散落地时，可直接复用Simplax增强trick，无需改动原有加噪流程即可提升生成质量

  - 离散扩散训练阶段可引入Rao-Blackwellized反向桥目标，在不增加输入复杂度的前提下降低训练方差，加快收敛速度

  - 冷启动少样本离散生成场景（比如新类目下的营销文案生成）可借鉴该方法的分布保留特性，用少量标注样本训练即可覆盖更多合理生成结果'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
离散扩散是文本、符号序列等类别型数据生成的主流方案，但现有性能优化方法需改动底层加噪流程，破坏原有扩散过程的分布特性，落地成本高。
### 方法关键点
1. 引入Simplax精确Dirichlet-类别增强策略，为每个受损类别状态绑定辅助单纯形变量，同时保留原始均匀扩散过程作为类别边缘分布
2. 推导可落地的Rao-Blackwellized反向桥训练目标与随机反向采样器，输入仍为原受损类别状态，无需调整原有扩散模型的输入结构
### 关键结果
- OpenWebText无约束生成任务上优化了困惑度-熵权衡
- 数独生成任务仅用30提示数样本训练，在17提示数（最小唯一可解场景）等全提示密度下准确率达SOTA，无约束生成有效性也为SOTA
