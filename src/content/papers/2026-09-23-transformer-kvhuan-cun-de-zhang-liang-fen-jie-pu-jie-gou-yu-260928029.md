---
title: 'Tensor Decomposition of Transformer Key-Value Caches: Spectral Structure and
  Format Comparison'
title_zh: Transformer KV缓存的张量分解：谱结构与格式对比
authors:
- Rahul Krishnan
- Volker Schulz
affiliations:
- Universität Trier
arxiv_id: '2609.28029'
url: https://arxiv.org/abs/2609.28029
pdf_url: https://arxiv.org/pdf/2609.28029
published: '2026-09-23'
collected: '2026-09-24'
category: LLM
direction: LLM推理优化 · KV缓存压缩
tags:
- KV_cache
- Tensor_Decomposition
- Tucker
- RoPE
- Low_Rank_Compression
one_liner: 系统分析KV缓存张量谱结构，对比4种分解压缩性能，给出LLM推理优化最优实践
practical_value: '- 做LLM服务/Agent推理优化时，2~5倍KV缓存压缩优先选Tucker分解，相同存储下重建误差比t-SVD、TT低30%以上

  - K和V必须分配独立压缩预算：V的压缩误差是K的1.7~3.2倍，不要给两者分配相同rank

  - Key的压缩步骤要放在RoPE之前执行，相比post-RoPE压缩可降低41%~64%的重建误差

  - 不要尝试压缩KV缓存的头和层维度：两类维度为近满秩，仅降1层rank就会导致重建误差涨3倍以上'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
自回归Transformer长上下文推理时KV缓存随序列长度线性增长，是设备内存占用的核心瓶颈，现有低秩压缩多采用2D SVD方案，未系统挖掘KV缓存的多阶张量结构，不同张量分解方案的适配性、可压缩维度的边界没有明确结论。

### 方法关键点
- 将KV缓存建模为包含注意力头、token、特征、层组的四阶张量，测量各维度展开的奇异值谱，定义index-like（近满秩不可压缩）维度的判定标准
- 等存储下对比Tucker、CP、张量列（TT）、t-SVD四种经典张量分解的重建误差
- 提出模钉定理，仅通过各维度的谱特征即可判定是否需要保留满秩
- 控制变量测试K/V不对称性、RoPE前后处理对压缩效果的影响

### 关键实验结果
在Mistral-7B-v0.3、LLaMA-2-13B上基于WikiText-2验证集测试，对比2D per-head SVD、Palu、xKV等基线：
1. 2×~5×压缩区间内Tucker误差始终最低，比TT、t-SVD低30%~60%
2. 头和层组维度为index-like满秩，仅压缩1层组rank就会导致重建误差提升3倍以上
3. post-RoPE的key压缩误差比pre-RoPE高41%~64%
4. 相同压缩比下V的重建误差是K的1.7~3.2倍

### 最值得记住的结论
KV缓存仅token和特征维度可压缩，头、层维度必须保留满秩，Tucker分解+pre-RoPE压缩K+独立分配K/V预算是当前最优压缩方案
