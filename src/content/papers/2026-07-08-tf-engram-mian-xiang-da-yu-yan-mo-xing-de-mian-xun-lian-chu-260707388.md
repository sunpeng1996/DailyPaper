---
title: 'TF-Engram: A Train-Free Engram with SSD-Backed Memory for Large Language Models'
title_zh: TF-Engram：面向大语言模型的免训练SSD存储记忆增强系统
authors:
- Yutang Ma
- Kecheng Huang
- Xikun Jiang
- Zili Shao
affiliations:
- The Chinese University of Hong Kong
- Beijing Institute of Technology, Zhuhai
arxiv_id: '2607.07388'
url: https://arxiv.org/abs/2607.07388
pdf_url: https://arxiv.org/pdf/2607.07388
published: '2026-07-08'
collected: '2026-07-09'
category: LLM
direction: LLM记忆增强 · 免训练推理优化
tags:
- LLM Inference
- Memory Augmentation
- Train-Free
- Storage Hierarchy
- Prefetching
- Engram
one_liner: 提出免训练SSD存储的Engram记忆增强方案，无需训练LLM主干即可提效降显存
practical_value: '- 电商/广告/推荐场景的领域专有名词、商品名、活动话术可直接构建免训练短语记忆库，无需微调LLM主干即可注入领域知识，大幅降低LoRA迭代的训练和部署成本

  - 可复用GPU-DRAM-SSD三级存储架构，将长尾冷知识/冷门商品表征放SSD，仅热数据占显存，适合Agent、端侧生成式推荐等显存受限的部署场景

  - 早退出引导预取思路可迁移到生成式推荐推理管线，提前预取候选Semantic ID、商品表征，隐藏IO延迟，提升每步生成的吞吐量

  - 若业务已用Engram类记忆方案，可替换原有哈希压缩存储为短语级精确存储加层级缓存，避免语义冲突导致的生成错误、推荐结果跑偏'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有Engram式LLM记忆增强依赖GPU端哈希压缩存储，易出现无关短语语义冲突，且需要额外训练，无法低成本扩展领域静态知识；RAG又存在上下文膨胀、注意力开销高的问题，无法高效注入短语级知识（如专有名词、商品名、行业术语），LLM领域适配的成本和推理开销居高不下。
### 方法关键点
- 离线免训练构建短语记忆库：从通用/领域语料挖掘高频短语，用冻结语义编码器生成对应表征，构建短语前缀索引，全程无需微调LLM主干，新增领域知识仅需增量构建索引
- GPU-DRAM-SSD三级存储分层：热短语存GPU缓存，温短语存主机DRAM，冷短语存NVMe SSD，无需哈希压缩，从根源避免语义冲突
- 早退出引导预测预取：在LLM倒数第r层加轻量预取头，提前预测未来可能用到的短语，异步预取到高速存储层，和剩余Transformer层计算重叠，隐藏外部存储的IO延迟
### 关键实验
基于Qwen3-0.6B主干，在MMLU、ARC-Challenge等10个下游基准测试，对比原生主干、参数量匹配的LoRA基线：平均得分从原生的57.6提升到59.4，比LoRA的58.7高0.7个点；SSD存储将GPU显存需求降低70%以上，预取机制可恢复90%以上因外部访问损失的吞吐量。
### 核心结论
静态短语知识不需要通过训练或RAG注入，免训练层级存储加预取的侧路径记忆方案，能以更低的成本和推理overhead实现LLM的领域适配。
