---
title: Tracing and Coordinating Cross-Layer Influence for Multimodal Model Merging
title_zh: 面向多模态模型融合的跨层影响追踪与协调方法
authors:
- Pengyang Zhou
- Xiaobin Tu
- Zhengxi Liu
- Rongkun Xue
- Haochen Li
- Miancan Liu
- Ziyuan Chen
- Yinggui Wang
- Jinkui Ren
- Xiantao Zhang
affiliations:
- Alibaba Cloud
arxiv_id: '2609.12897'
url: https://arxiv.org/abs/2609.12897
pdf_url: https://arxiv.org/pdf/2609.12897
published: '2026-09-11'
collected: '2026-09-14'
category: Multimodal
direction: 多模态大模型 · 专家模型融合
tags:
- Multimodal Model Merging
- MLLM
- Parameter Efficient Tuning
- Model Compression
- Cross-layer Optimization
one_liner: 提出TAC-Merge框架，通过跨层影响建模实现多模态任务专家模型的高效融合，保留互补能力
practical_value: '- 多模态电商搜索/推荐场景可复用TAC-Merge合并不同下游任务（图文检索、商品属性识别、多模态导购问答）的LoRA专家，大幅降低多任务部署的存储与推理成本

  - 跨层影响追踪思路可迁移到多模态召回/排序模型的多任务权重优化，缓解不同任务梯度更新在深度网络中的耦合干扰问题，提升多任务效果均衡性

  - MIM模块结合Ricci曲率与专家预测定义融合目标的方法，可用于多模态特征对齐的优化目标设计，提升图文跨模态语义匹配的精度'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
当前多模态模型融合方法大多沿用单模态方案仅在单层内合并专家更新，忽略了更新的跨层传播效应，导致视觉、文本模态更新的效果耦合，难以同时保留不同任务专家的互补能力，且多任务独立部署的存储、推理成本过高。

### 方法关键点
提出TAC-Merge框架，包含两个核心模块：
1. 多模态影响映射（MIM）：构建更新效应图，结合Ricci曲率与专家预测结果定义统一融合目标，量化单专家更新的跨层多模态影响
2. 耦合合并控制（CMC）：建模系数调整间的交互关系，联合优化区域权重合成统一共享模型

### 关键结果
在多模态问答、视觉推理、图表理解、物体定位等多类任务上验证有效性，融合后的模型可完整保留各专家的互补能力，同时具备对未见过任务的泛化性。
