---
title: 'Discrete Diffusion Models: A Unified Framework from Tokenization to Generation'
title_zh: 离散扩散模型：从分词到生成的统一框架
authors:
- Ye Yuan
- Weien Li
- Rui Song
- Zeyu Li
- Haochen Liu
- Xiangyu Kong
- Zixuan Dong
- Linfeng Du
- Zipeng Sun
- Weixu Zhang
affiliations:
- McGill University
- Mila - Quebec AI Institute
- University of Cambridge
- University of Toronto
- MBZUAI
arxiv_id: '2607.13431'
url: https://arxiv.org/abs/2607.13431
pdf_url: https://arxiv.org/pdf/2607.13431
published: '2026-07-15'
collected: '2026-07-16'
category: Training
direction: 离散扩散模型 · 统一框架设计
tags:
- Discrete Diffusion
- Tokenization
- Generation Framework
- Training Objective
- Inference Optimization
one_liner: 构建离散扩散模型统一概念框架，梳理主流实现的共性设计空间与权衡
practical_value: '- 做生成式推荐/Query生成时，可基于该框架选型离散扩散方案，替换AR模型实现并行生成降低推理 latency

  - 自定义离散状态空间（如商品Semantic ID、Query token词表）时，可参考框架梳理的训练/推理权衡做适配优化

  - 业务侧落地离散扩散生成时，可复用框架总结的masking/transition等不同实现的适用场景，减少试错成本'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
AR模型作为离散序列生成的主流方案，存在串行解码latency高、长序列生成误差累积的问题；离散扩散模型（DDM）虽具备并行生成、全局迭代优化的优势，但当前各类实现分散无统一框架，选型与优化缺乏系统性参考依据。

### 方法关键点
提出基于底层离散状态空间构造的统一概念框架，将现有转移矩阵、掩码/吸收态、得分/比率三类主流DDM实现，统一映射为同一设计空间的不同实例，系统性梳理了训练目标、推理算法、缩放特性、系统优化、评估协议多维度的共性权衡逻辑。

### 关键结论
框架完整覆盖当前所有离散扩散主流实现范式，明确了分词策略、词表拓扑、领域结构化字母表设计为DDM的核心优化方向，为后续离散扩散的工业落地提供了统一设计参考。
