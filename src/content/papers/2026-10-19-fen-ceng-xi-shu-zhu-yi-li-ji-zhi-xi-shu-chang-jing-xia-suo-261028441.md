---
title: 'Stratified Sparse Attention: Reducing the Sparse-to-Dense Gap at Extreme Sparsity'
title_zh: 分层稀疏注意力：极致稀疏场景下缩小稀疏与稠密注意力的性能差距
authors:
- Sahil Joshi
- Prithvi Dixit
- Aryan Katiyar
- Agniva Chowdhury
- Joseph E. Gonzalez
- Anshumali Shrivastava
- Aditya Desai
- Kumar Krishna Agrawal
affiliations:
- 莱斯大学
- 加州大学伯克利分校
- 斯坦福大学
- 印度理工学院孟买分校
arxiv_id: '2610.28441'
url: https://arxiv.org/abs/2610.28441
pdf_url: https://arxiv.org/pdf/2610.28441
published: '2026-10-19'
collected: '2026-10-23'
category: LLM
direction: LLM长上下文推理 · 稀疏注意力优化
tags:
- Sparse-Attention
- KV-cache
- Long-Context-Inference
- LLM-Inference
- CUDA-Optimization
one_liner: 提出分层稀疏注意力框架，结合确定性检索与分数引导采样，极致稀疏下逼近稠密注意力效果同时实现推理加速
practical_value: '- 电商生成式推荐、长对话Agent场景可直接复用SSA分层策略，将注意力预算按3:2分配给top-k高相关token与分数引导采样，既降低KV
  cache访问开销，又避免长尾相关token被过滤导致的推荐/应答准确率下降

  - 长上下文RAG系统（如电商知识库问答、商品检索）可复用SSA的分层采样逻辑，对召回Chunk先取top-k高相关，剩余部分按语义相似度加权采样，比均匀采样覆盖更多长尾相关知识，降低幻觉

  - 工程上可直接复用SSA的优化CUDA Kernel实现，尤其是PQ压缩proxy打分+两级分层采样的设计，1M以上长上下文场景下可获得2-3倍decode加速，适配高并发实时推荐、大促智能客服场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长上下文LLM推理的核心瓶颈是KV cache访问开销，现有稀疏注意力方法要么仅取top-k高得分token丢失长尾注意力权重，要么对残差token均匀采样方差大，在50×以上极致稀疏度下与稠密注意力的性能差距显著，无法兼顾准确率和推理速度。

### 方法关键点
- 提出分层稀疏注意力SSA框架，自动将注意力预算划分为两部分：高proxy得分token组成heavy set直接保留，剩余预算按proxy得分加权采样残差token
- 采样时对残差token采用重要性加权修正消除采样偏差，理论上可证明其逼近稠密注意力的误差边界，且top-k、top-p、混合top-k+采样都是SSA的特殊情况
- 工程实现优化CUDA Kernel，用PQ压缩的proxy打分降低全上下文扫描开销，两级分层采样减少残差采样延迟，支持paged KV cache适配现有推理框架

### 关键结果
在RULER、LongBench、LOFT、AIME四个长上下文基准，3B到27B共5个模型上测试：50×稀疏度下，Ministral-3-8B在32K上下文准确率从最强基线的81.8%提升到84.2%，128K上下文从63.8%提升到69.3%，分别恢复稠密注意力94%和85%的性能；1M上下文、batch 16下比FlashInfer最高获得2.96×decode加速。

**最值得记住的一句话**：稀疏注意力的性能瓶颈不在于稀疏度高低，而在于预算有限时能否同时覆盖高权重头部token和长尾有效注意力质量，分层加权采样比均匀混合策略效率高得多。
