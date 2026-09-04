---
title: 'DoPR: Reusable Compressed Document Prefixes for Efficient LLM Reranking'
title_zh: DoPR：基于可复用压缩文档前缀的高效LLM重排序框架
authors:
- Beiya Dai
- Yifan Wei
- Guang Yang
- Xing Shi
- Xinbing Wang
- Zhouhan Lin
affiliations:
- Shanghai Jiao Tong University
- ByteDance
arxiv_id: '2609.03311'
url: https://arxiv.org/abs/2609.03311
pdf_url: https://arxiv.org/pdf/2609.03311
published: '2026-09-03'
collected: '2026-09-04'
category: RecSys
direction: 搜索推荐 · LLM重排序效率优化
tags:
- LLM Reranking
- KV Cache
- Document Compression
- Efficiency Optimization
- Pointwise Reranking
one_liner: 通过离线预存查询无关的压缩文档前缀状态，大幅降低LLM点式重排序在线开销，效果损失低于3%
practical_value: '- 离线预计算文档压缩KV前缀的思路可直接迁移到电商商品/内容库的LLM重排序场景，尤其适合商品库稳定、重复曝光率高的业务，能大幅降低在线推理延迟

  - 基于自注意力信号的无额外参数关键token选择方法，可复用在prompt压缩、长文档截断等场景，无需新增模块即可实现轻量化重要信息筛选

  - 训练阶段用结构化注意力掩码强制query仅访问压缩前缀的设计，可迁移到其他上下文压缩复用的LLM推理场景，对齐训练推理范式避免效果掉点

  - 推理阶段前缀长度K可独立调整无需重训，方便在线做效果-效率的动态trade-off，适合大促等流量高峰场景的柔性降级'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有LLM点式重排序需对每个query-document对重新编码全文档，同一份文档会被多个query重复处理，产生大量冗余计算，成为在线部署的 latency 和内存瓶颈；现有压缩方法大多绑定特定query无法跨query复用，预计算的文档表示也无法直接作为LLM内部状态用于重排序。
### 方法关键点
- 三阶段架构：训练阶段端到端优化，离线阶段预压缩全量文档生成多层前缀KV状态，在线阶段仅处理query和打分token，直接复用预存前缀
- 无参数关键token选择：基于文档自注意力矩阵的列均值计算每个token的显著性，选top-K作为压缩文档表示，无需额外训练选择器
- 结构化注意力掩码：训练时强制query和打分token仅能访问选中的压缩前缀，对齐训练和推理的信息通路，避免推理时无原文档导致的效果下降
- 灵活调优机制：推理阶段的前缀长度K可独立于训练阶段设置，无需重新训练即可调整效果-效率的trade-off
### 关键实验
以Qwen3 0.6B/4B/8B为骨干模型，在TREC DL、BEIR、BRIGHT三类基准上测试，对比原生全文档Qwen3重排序基线：平均NDCG@10保留率达97.1%~99.5%，文档侧内存最高降低8倍，latency最高加速8.04倍；文档越长、重复访问次数越多，效率收益越明显，同时该方案也兼容Llama等其他Decoder-only模型。
### 核心结论
对于文档/商品库相对稳定的检索场景，把可复用的文档侧计算移到离线，是兼顾LLM重排序效果与在线效率的高性价比方案
