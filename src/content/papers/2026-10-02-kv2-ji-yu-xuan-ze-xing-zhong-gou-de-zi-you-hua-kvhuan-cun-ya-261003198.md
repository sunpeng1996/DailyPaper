---
title: 'KV$^2$: A Self-Refining KV Cache'
title_zh: KV²：基于选择性重构的自优化KV缓存压缩方法
authors:
- Johannes Wesch
- Danni Liu
- Jan Niehues
affiliations:
- Karlsruhe Institute of Technology
arxiv_id: '2610.03198'
url: https://arxiv.org/abs/2610.03198
pdf_url: https://arxiv.org/pdf/2610.03198
published: '2026-10-02'
collected: '2026-10-05'
category: LLM
direction: LLM推理优化 · KV cache压缩
tags:
- KV cache
- LLM Inference
- Compression
- Long Context
- Query Agnostic
one_liner: 提出两阶段无查询依赖KV缓存压缩方案，极端压缩下精度更高且计算/显存开销更低
practical_value: '- 电商RAG/Agent场景的长上下文复用（如商品库、用户会话历史缓存）可直接引入KV²替代现有压缩策略，2%-10%极低缓存预算下保留更多关键信息，大幅降低长上下文推理成本

  - 两阶段筛选思路可迁移到推荐系统长序列用户行为压缩：先用轻量规则（点击权重、时间衰减）筛选高价值行为，再用小模型重打分做最终截断，平衡压缩效果与计算开销

  - 极端压缩优先保留稀疏高价值信息的结论可复用在大模型多轮对话缓存、商品长文本QA等场景，无需全量重构即可降低显存占用'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
长上下文LLM的KV缓存显存开销随上下文长度线性增长，单块A100无法承载百万级上下文70B模型的KV缓存，现有无查询依赖压缩方案要么轻量但精度低，要么全量重构精度高但开销大，无法适配单缓存服务多查询的复用场景（如电商RAG商品库缓存、Agent长期记忆缓存）的极端压缩需求。

### 方法关键点
- 两阶段压缩架构：第一阶段用轻量KeyDiff代理分块选出上下文内高信息量token作为重构查询，第二阶段仅对选中查询做全缓存注意力计算得到最终驱逐分数，无需处理全量token
- 分块处理+全局-局部分离：保留开头注意力sink token，剩余上下文分块处理，重构查询利用全局上下文信息，打分仅在块内完成，平衡效果与计算效率
- 支持自优化迭代：第二阶段输出的分数可直接替换第一阶段代理分数做多轮迭代，弱初始代理场景下可进一步提升效果

### 关键实验
在RULER、Needle-in-a-Haystack、LongBench数据集上对比KeyDiff、Expected Attention、KVzip三类SOTA基线：
- RULER 16K任务2%缓存预算下，平均得分比次优基线高40+百分点
- LongBench 2%缓存预算下，Llama-3.1-8B-Instruct、Qwen3-8B上平均得分分别比次优基线高9.43、16.38分
- 压缩阶段runtime和峰值显存均低于全量重构的KVzip，4K分块配置下达到最优的效率-效果平衡

### 最值得记住的一句话
长上下文的有效信息高度稀疏，极端压缩场景下无需全量重构，仅对少量高价值锚点token做选择性重构即可同时实现更高精度与更低成本
