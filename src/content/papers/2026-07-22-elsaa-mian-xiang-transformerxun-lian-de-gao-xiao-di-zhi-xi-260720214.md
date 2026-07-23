---
title: 'ELSAA: Efficient Low-Rank and Sparse Attention Approximation for Training
  Transformers'
title_zh: ELSAA：面向Transformer训练的高效低秩稀疏注意力近似
authors:
- Mahdi Heidari
- Mohammad Mahdi Rahimi
- Jaekyun Moon
affiliations:
- KAIST
- DGIST
arxiv_id: '2607.20214'
url: https://arxiv.org/abs/2607.20214
pdf_url: https://arxiv.org/pdf/2607.20214
published: '2026-07-22'
collected: '2026-07-23'
category: Training
direction: 长上下文LLM · 高效注意力训练
tags:
- Efficient-Attention
- Long-Context
- Low-Rank
- Sparse-Attention
- Transformer-Training
one_liner: 提出稀疏+低秩双分支注意力加分母感知融合，线性复杂度实现长上下文Transformer高效训练，效果超现有高效注意力方案
practical_value: '- 电商长序列用户行为建模可复用双分支架构：稀疏分支捕获近期/高相关交互，低秩分支聚合全局长期行为，将长序列Attention的O(N²)开销降至线性，支持更长行为序列输入提升推荐效果

  - 多分支注意力融合可直接复用分母感知校正Trick：无需新增参数，仅基于各分支的Attention分母质量动态缩放分支输出，即可解决不同归一化尺度的分支输出scale
  mismatch问题，稳定提升混合结构性能

  - 长上下文Agent的历史会话/工具调用结果处理，可复用sortLSH高相关token选择逻辑：无需加载全量KV缓存，即可快速召回高相关上下文，降低长会话推理的内存开销'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有高效注意力方案要么走稀疏路线，仅保留高相关query-key交互，易丢失弱但重要的全局信号；要么走低秩路线，压缩全局上下文易平滑尖峰高置信token依赖，直接混合两类分支会因为各自归一化分母的尺度差异导致效果打折，同时FlashAttention仅优化IO效率不改变二次复杂度，超长上下文训练仍然存在瓶颈。

### 方法关键点
- 不对Transformer的投影矩阵做分解，在QKV生成后直接近似Attention算子：稀疏分支采用sortLSH选择高相似query-key对计算精确Attention，捕获高置信交互；低秩分支采用RACE哈希桶压缩全局KV信息，以线性复杂度获取全局上下文
- 提出分母感知融合项，根据稀疏分支覆盖的Attention分母质量相对低秩分支的比例动态缩放稀疏分支输出，再结合可学习门控加权两个分支结果，避免尺度失配
- 同时支持非因果和因果场景，整体复杂度线性于序列长度

### 关键实验
对比Sort LSH、RACE、无校正双分支、ExactFlash基线：NIAH任务训练长度1024，65536长度下准确率84.2%，远超RACE的2.2%、Performer的83.4%，ExactFlash在32768就OOM；长文本分类ArXiv@64K测试准确率91.47%，比ExactFlash高4pp；64K文本检索任务ExactFlash准确率仅50%（随机水平），ELSAA达65.34%。

长上下文注意力天然同时存在尖峰高置信交互和弥散全局交互，双分支结合+尺度校正能兼顾效果和效率，覆盖精确Attention无法触达的超长序列场景
