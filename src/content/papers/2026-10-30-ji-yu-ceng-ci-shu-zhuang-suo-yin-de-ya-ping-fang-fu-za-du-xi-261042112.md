---
title: Subquadratic Attention with a Hierarchical Tree-Structured Indexer
title_zh: 基于层次树状索引的亚平方复杂度稀疏注意力机制
authors:
- Leon Lufkin
- Cutter Dawes
- Alexander Speicher
- Kamesh Krishnamurthy
- Tomás Figliolia
- Beren Millidge
affiliations:
- Zyphra Research
arxiv_id: '2610.42112'
url: https://arxiv.org/abs/2610.42112
pdf_url: https://arxiv.org/pdf/2610.42112
published: '2026-10-30'
collected: '2026-11-02'
category: LLM
direction: LLM长上下文 · 稀疏注意力优化
tags:
- Attention
- KV cache
- Long Context
- Sparse Attention
- LLM Inference
one_liner: 提出仅需少量蒸馏训练的层次树索引稀疏注意力ZHA，实现亚平方缩放且保留长上下文性能
practical_value: '- 长上下文RAG系统可复用ZHA的层次树KV索引设计，替代现有固定top-K召回，用top-p动态选择相关上下文块，降低KV
  cache开销同时提升长文档召回准确率

  - 大模型推理服务可直接复用ZHA的蒸馏方案，仅需优化少量参考查询参数、无需微调基座，就能低成本将现有预训练模型适配长上下文场景，适合电商大促等需要快速上线长上下文能力的场景

  - 推荐系统的用户长序列建模可借鉴ZHA的层次摘要思路，对用户历史行为序列做分层压缩摘要，当前用户意图逐层路由召回相关历史行为，解决长序列建模的性能与精度权衡问题'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
注意力的平方缩放是限制LLM长上下文能力的核心瓶颈，现有优化方案要么表达能力不足（如滑动窗口、固定状态线性注意力），要么仅能获得常数倍加速（如稀疏注意力的索引本身仍为平方缩放），无法支撑百万级以上超长上下文的高效推理。
### 方法关键点
- 核心设计ZHA：基于KV cache构建递归压缩的层次树索引，每层节点为下层连续key chunk的摘要，摘要通过可学习参考查询的注意力加权求和生成
- 训练仅优化少量参考查询参数，基座模型完全冻结，仅需几B token的KL蒸馏即可完成适配，新增参数量不足0.0003%
- 推理采用top-p动态路由：query从树顶向下遍历，每层选择累计注意力占比≥p的节点展开，最终召回的稀疏KV子集做标准注意力计算，无需固定top-K预算
### 关键实验结果
- 基于Qwen3.6-35B适配的ZHA在256K上下文下仅召回1%-6%的KV cache，推理、数学、代码任务性能与稠密注意力几乎持平，RULER长上下文检索精度仅下降3pp
- 对比同设置下的MSA稀疏注意力，LongBench v2得分高14pp，长上下文检索精度优势显著
- 性能模型预测ZHA在48K上下文时速度超过稠密注意力，480K上下文时超过MSA，10亿token上下文下最高可实现417倍的注意力层加速

自然语言序列的注意力有效子集大小随序列长度呈亚线性幂律增长，通过层次索引+动态top-p路由可在几乎不损失精度的前提下实现注意力的亚平方缩放。
