---
title: Multi-View Structural Representations for Physically-Consistent TeX Generation
title_zh: 面向物理一致性TeX生成的多视角结构表示方法
authors:
- Daoheng Li
- Jianjun Qian*
- Mengkai Yan
- Jian Yang
affiliations:
- Nanjing University of Science and Technology
- Hohai University
arxiv_id: '2610.25695'
url: https://arxiv.org/abs/2610.25695
pdf_url: https://arxiv.org/pdf/2610.25695
published: '2026-10-19'
collected: '2026-10-24'
category: Other
direction: 多模态TeX生成 · 分层路由MoE优化
tags:
- MoE
- Multi-view Representation
- Hierarchical Routing
- Multimodal Fusion
- Physics-constrained Generation
one_liner: 提出带分层路由的多视角MoE框架MVR-MoE，实现物理一致的轻量高效TeX生成
practical_value: '- 若在推荐系统中引入MoE架构做多源异构特征融合，可参考分层路由设计，从特征视角、专家层两级做自适应调度，提升特征利用效率

  - 生成式任务需满足业务硬约束（如广告合规、价格区间限制）时，可借鉴物理约束嵌入思路，将规则转化为损失项直接约束输出

  - 本研究核心场景为多模态TeX生成，与电商/推荐核心业务匹配度极低，大部分模态处理模块无直接复用价值'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有基于物理约束的低光照图像生成方法高度依赖配对训练数据，无法高效挖掘红外、可见光模态的互补特征，生成结果难以保证物理一致性。
### 方法关键点
1. 提出MVR-MoE框架，挖掘多模态固有结构线索构建多视角表示，通过多视角超连接扩展特征空间，同时保留跨模态共享特征与单模态特有细节
2. 设计分层路由机制，在结构视角层、专家层两个维度调控特征利用策略，自适应挖掘异构特征价值
3. 基于斯特藩-玻尔兹曼定律约束生成的温度、发射率、纹理图，直接将物理规则作为损失项，保证输出的物理一致性
### 关键结果
在多个公开挑战性数据集上，相比基准方法鲁棒性、判别性均实现显著提升，同时模型参数量更低、推理速度更快，满足轻量化要求
