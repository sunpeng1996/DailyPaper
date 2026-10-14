---
title: Depth Memory
title_zh: Depth Memory：面向跨层信息存储检索的线性深度记忆架构
authors:
- David González-Martínez
- Philipp Nazari
- T. Konstantin Rusch
- Shiwei Liu
affiliations:
- ELLIS Institute Tübingen
- Max Planck Institute for Intelligent Systems
- Tübingen AI Center
- ETH Zürich
- Liquid AI
arxiv_id: '2610.18809'
url: https://arxiv.org/abs/2610.18809
pdf_url: https://arxiv.org/pdf/2610.18809
published: '2026-10-13'
collected: '2026-10-14'
category: LLM
direction: LLM架构优化 · 跨层深度混合
tags:
- Depth-Mixing
- Transformer
- Residual-Connection
- Linear-Associative-Memory
- RLS
one_liner: 提出统一跨层信息流动的Depth Memory框架，及效果更优的高效线性深度记忆LDM模块
practical_value: '- 针对电商场景下微调小参数LLM做推荐文案生成、Query理解的需求，可将LDM作为轻量化插件替换标准残差连接，仅增加1%参数量即可提升语言建模效果，资源开销远低于mHC、AttnRes等方案

  - LDM的状态回退、窗口化写优化的工程思路可复用在KV cache优化、长序列RAG的状态管理场景，降低峰值显存占用与内存读写开销

  - 将跨层信息流动建模为读写存储的框架思路可迁移到多塔推荐架构的层间特征复用设计，用线性关联记忆替代简单残差累加，提升特征传递效率'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
Transformer架构创新长期聚焦序列、通道两个维度的混合优化，跨层深度维度的信息传递一直沿用ResNet提出的残差累加机制，近年出现的mHC、AttnRes等深度混合方案虽然效果更优，但缺乏统一的理论框架，同时存在显存开销大、推理效率低的问题，亟需兼顾效果与效率的跨层信息传递方案。

### 方法关键点
- 提出Depth Memory（DM）统一框架，将跨层信息流动抽象为多流状态的读写操作，可覆盖标准PreLN Transformer、mHC、AttnRes等现有残差机制
- 提出Linear Depth Memory（LDM）具体实现，维护残差流、线性关联记忆流、逆协方差流三个并行流，将跨层信息检索建模为深度回归问题，通过递归最小二乘法（RLS）实现最优更新
- 硬件感知优化：用状态回退机制避免反向传播时存储每层记忆状态，窗口化写操作减少内存读写流量，基于CuTe DSL实现的内核效率接近标准Transformer

### 关键结果
在400M、1.5B参数的Llama/Qwen-like架构上训练，对比PreLN、mHC、Block AttnRes基线，400M规模下验证集perplexity比PreLN低5.1%、比mHC低1.2%，1.5B规模下验证集perplexity比PreLN低3.5%、比mHC低1.1%，零样本任务平均精度超过所有基线，吞吐量与Block AttnRes相当，优于mHC与Full AttnRes。

### 核心结论
把跨层信息传递建模为存储读写问题，用固定大小的线性关联记忆替代动态增长的层缓存，可在极小参数量开销下同时提升大语言模型的效果与效率。
