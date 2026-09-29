---
title: 'SANTA++: Sampling Attention through Representative Keys'
title_zh: SANTA++：基于代表性Key的免训练长上下文注意力优化方法
authors:
- Kyle Lee
- Christian Z. Pratt
- Ruoyu Fang
- Heekyung Lee
- Avinash Lohitsa
- Ryan Modafe
- Kerem Y. Camsari
affiliations:
- University of California, Santa Barbara
- Flucta, San Francisco
arxiv_id: '2609.35629'
url: https://arxiv.org/abs/2609.35629
pdf_url: https://arxiv.org/pdf/2609.35629
published: '2026-09-28'
collected: '2026-09-29'
category: LLM
direction: 长上下文LLM推理 · KV cache优化
tags:
- KV cache
- Attention Optimization
- Long Context LLM
- Inference Acceleration
- Training-free
one_liner: 免训练长上下文注意力采样方案，将KV访问量降至基线的16%同时保留99%精度
practical_value: '- 电商导购Agent、生成式推荐等长上下文RAG场景可直接复用该方案，无需微调即可降低LLM解码KV访问量，提升用户端响应速度

  - 长用户行为序列的召回/排序模型的注意力计算，可借鉴分组采样+重要性校正的思路，无需读取全量行为序列即可保证计算精度

  - 可与现有KV量化、MLA等KV压缩方案叠加使用，同时降低KV存储开销与内存访问带宽，适配小算力/端侧的推荐/Agent服务部署

  - 对分组路由精度要求高的场景优先用k-means语义分组，对预处理延迟敏感的场景可直接用连续token span分组，精度损失可控'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
长上下文LLM解码时，KV cache读取的内存带宽成本随上下文长度线性增长，是推理延迟的核心瓶颈。传统稀疏注意力方案要么需要扫描全量KV选择高贡献token，仅能降低value读取开销；要么用组均值Key做路由，会因Jensen不等式大幅低估组注意力质量，导致精度损失严重，多数方案还需要额外训练，落地门槛高。

### 方法关键点
- 预填充阶段一次性对KV做分组：先划分父组（支持k-means语义分组或连续token span无聚类分组），每个父组选最多R个真实Key作为代表，其余Key分配到距离最近的代表所属team，存储各team的代表、大小和成员索引
- 解码阶段仅读取每个team的代表Key计算路由权重，用Gumbel-top-K采样选择候选team，仅读取选中team的全量KV计算精确注意力得分
- 加入重要性采样校正：用每个team被选中的条件概率倒数加权其注意力贡献，无偏估计全量注意力结果，新生成的token单独走精确注意力计算

### 关键实验
基于Qwen2.5-7B-Instruct在32K上下文测试，对比FlashAttention基线：
1. LongBench v2上k-means分组保留99.07%的基线精度，KV访问量仅为基线的16.68%
2. HELMET RAG子集保留98%的基线精度，KV访问量为基线的38.49%
3. RTX 5090 Laptop GPU上的Triton实现，attention算子获得1.69倍的加速比

### 核心结论
用真实Key做组代表+重要性校正的免训练采样方案，在几乎不损失精度的前提下可大幅降低长上下文KV访问开销，可与现有KV压缩、缓存淘汰方案叠加使用
