---
title: 'BaKron: Efficient Quantization with Kronecker-Factored Hessians'
title_zh: BaKron：基于克罗内克分解海森的神经网络高效量化方法
authors:
- Johann Birnick
- Rayan Saab
affiliations:
- University of California San Diego
arxiv_id: '2608.06291'
url: https://arxiv.org/abs/2608.06291
pdf_url: https://arxiv.org/pdf/2608.06291
published: '2026-08-06'
collected: '2026-08-07'
category: Training
direction: 大模型后训练量化 · 海森近似加速
tags:
- Post-training Quantization
- Kronecker Product
- Hessian Approximation
- GPTQ
- LLM Inference
- Matrix Optimization
one_liner: 提出与GPTQ复杂度相当的双维度海森感知量化算法，较同类YAQA/BoA速度最高提升60倍
practical_value: '- 做生成式推荐、电商Agent的团队可直接复用BaKron开源实现，相比GPTQ能保留更多输出侧特征相关性，提升量化后模型的文案生成、召回排序精度

  - 反对角线并行+递归分治的矩阵优化trick，可迁移到推荐系统的大规模embedding压缩、向量召回的批量匹配计算场景，降低延迟和计算成本

  - 递归分层计算全局海森的内存优化方案，可让单卡完成7B/13B规模LLM的高精度量化，无需多卡集群，降低中小团队的量化硬件门槛'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
GPTQ等主流后训练量化方案仅利用输入侧激活的单侧海森信息，无法捕捉输出特征间的相关性，量化精度上限不足；而BoA、YAQA等支持双侧克罗内克分解海森的量化方案，总计算复杂度高达O(m²n²)，矩阵尺寸越大速度越慢，难以落地到Transformer全层量化场景。
### 方法关键点
- 反对角线并行优化：同一反对角线上的权重更新互不依赖，可批量并行处理，将串行步骤从O(mn)降至O(m+n)
- 递归分治架构：延迟批量更新未处理的权重区域，将总计算复杂度从O(m²n²)降至O(mn(m+n))，和GPTQ的立方复杂度持平
- 模块化设计：支持对接任意基础量化器和海森估计器，提供K-FAC风格、Shampoo风格两种海森近似方案，以及低内存的全局海森递归计算流程
### 关键结果
在单张NVIDIA RTX PRO 6000上测试不同尺寸权重矩阵的核心量化耗时，对比GPTQ、等价YAQA的BaKron-antidiag、等价BoA的BaKron-naive：4096×4096矩阵速度比YAQA快26.6倍，8192×8192矩阵速度提升达60倍，核心耗时仅1.84秒，和GPTQ的速度差距在1个数量级以内。
> 最值得记住的一句话：双侧海森感知的量化方案可以在不增加核心计算复杂度的前提下达到和GPTQ相当的速度，同时获得更优的量化精度。
