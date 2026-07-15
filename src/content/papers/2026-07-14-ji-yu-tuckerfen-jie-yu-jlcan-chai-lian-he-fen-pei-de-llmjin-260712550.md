---
title: 'A JoLT for the KV Cache: Near-Lossless KV Cache Compression via Joint Tucker
  and JL-Residual Allocation for LLMs'
title_zh: 基于Tucker分解与JL残差联合分配的LLM近无损KV缓存压缩方法JoLT
authors:
- Rahul Krishnan
- Volker Schulz
arxiv_id: '2607.12550'
url: https://arxiv.org/abs/2607.12550
pdf_url: https://arxiv.org/pdf/2607.12550
published: '2026-07-14'
collected: '2026-07-15'
category: LLM
direction: LLM推理优化 · KV缓存压缩
tags:
- KV cache
- Tucker Decomposition
- Johnson-Lindenstrauss
- LLM Inference
- Compression
one_liner: JoLT框架联合Tucker分解与JL残差分配，实现LLM KV缓存2-3倍近无损压缩，误差比现有方案低一个数量级
practical_value: '- 部署长上下文LLM做商品文案生成、用户意图理解时，可引入JoLT做KV缓存压缩，在几乎不损失效果的前提下将单卡可承载并发量提升2-3倍，降低推理成本

  - 针对大模型RAG商品检索的长上下文场景，该方法比传统SVD、4bit量化的重构误差低一个数量级，可直接替换现有KV压缩方案保障检索准确率

  - 算力紧张场景可选用FlashJoLT变体，压缩速度提升5-13倍，适配低延迟要求的实时推荐Agent、搜索query理解等在线服务'
score: 8
source: arxiv-cs.CL
depth: abstract
---

### 动机
LLM推理中KV缓存是主要内存开销，长上下文下直接决定吞吐量上限；现有低秩分解、量化两类压缩方法未利用KV缓存三阶张量的不同轴冗余特性，压缩精度和效率存在瓶颈。

### 方法关键点
JoLT将KV缓存视作三阶张量，仅对token、特征轴做部分Tucker压缩，保留头、层轴不变；通过Johnson-Lindenstrauss旋转变换的低比特残差补全截断损失；用拉格朗日对偶按层组、key/value独立分配Tucker秩和残差比特位宽，满足固定字节预算。同步推出随机SVD变体FlashJoLT提升压缩速度。

### 关键结果数字
实现2-3倍近无损压缩，困惑度、GSM8K准确率、RULER大海捞针检索效果与无压缩基线几乎无统计差异；2倍压缩下相对Frobenius误差仅0.009(K)、0.006(V)，比跨层SVD、4bit量化低一个数量级；FlashJoLT在同等效果下压缩速度提升5-13倍。
