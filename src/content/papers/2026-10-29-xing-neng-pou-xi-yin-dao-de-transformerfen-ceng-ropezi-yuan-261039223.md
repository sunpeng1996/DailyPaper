---
title: 'Where Position Matters: Profiling-Guided Layer-Wise RoPE Allocation in Transformers'
title_zh: 性能剖析引导的Transformer分层RoPE资源分配方法
authors:
- Zhiwei Liu
- Boao Kong
- Bing Liu
affiliations:
- Peking University
arxiv_id: '2610.39223'
url: https://arxiv.org/abs/2610.39223
pdf_url: https://arxiv.org/pdf/2610.39223
published: '2026-10-29'
collected: '2026-10-30'
category: LLM
direction: LLM架构优化 · RoPE资源分配
tags:
- RoPE
- Transformer
- Efficient LLM
- Positional Encoding
- Cross-scale Transfer
one_liner: 通过层级位置依赖剖析实现RoPE资源分层分配，同预算下效果优于均匀分配且支持同模型族跨规模迁移
practical_value: '- 可复用层级性能 profiling 方法：训练早期（10%步数）对推荐/搜索场景的LLM排序层、语义匹配层做资源依赖评估，优先给增益高的层分配RoPE、KV
  cache等资源，同预算下提升效果

  - 跨规模模型迁移策略：小模型的层级资源依赖profile可通过归一化深度映射到大模型，大幅降低大模型架构调优成本，适合业务侧从7B小模型向70B大模型迁移的场景

  - MLA架构适配优化：对于用MLA压缩KV cache的生成式推荐/智能客服Agent，可物理调整不同层的旋转维度，在不损失效果的前提下降低KV cache存储和推理延迟'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
现有RoPE默认所有Transformer层均匀分配旋转维度，忽略不同层对位置信息的异质性需求，要么造成资源浪费，要么约束模型效果；同时大模型调优RoPE配置需要反复全量训练，成本极高，亟需低成本的层级RoPE资源分配方案。

### 方法关键点
- 层级位置依赖量化：通过phase-off干预（关闭某层RoPE、保持其他配置不变）计算各层位置依赖得分，该得分与提升RoPE覆盖率的增益Spearman相关性达0.94以上，可作为可靠分配信号
- 预算约束下的分层分配：固定总RoPE维度预算，给得分Top K的层分配高覆盖率，其余层分配低覆盖率；支持两种实现：固定载波（Q/K维度不变仅部分维度加旋转）、物理MLA分配（直接调整旋转分支维度降低资源消耗）
- 跨规模迁移：同模型族下小模型训练10%步数得到的profile，通过归一化深度线性插值映射到大模型，无需大模型预训练即可得到分配方案

### 关键结果
- 实验在130M/350M/1B参数的Dense和MLA Transformer上开展，对比全量RoPE、均匀半覆盖、随机分层分配三类baseline
- Dense结构下需求引导分配比全量RoPE在1B参数时验证loss低0.0274，存储和计算量完全不变
- MLA结构下需求引导分配比全量RoPE在350M参数时验证loss低0.0007，同时存储降为0.965倍、端到端FLOPs降为0.9476倍

### 核心结论
Transformer不同层对位置信息的需求高度非均匀，通过早期轻量profiling针对性分配RoPE资源，可在不增加甚至降低成本的前提下稳定提升模型效果
