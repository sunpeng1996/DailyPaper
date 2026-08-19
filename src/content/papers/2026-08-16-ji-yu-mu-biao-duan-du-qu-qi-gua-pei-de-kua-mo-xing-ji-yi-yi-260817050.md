---
title: Cross-Model Memory Transfer via Target-Side Reader Adaptation
title_zh: 基于目标端读取器适配的跨模型记忆迁移方法
authors:
- Mingyuan Li
- Guangsheng Yu
- Xu Wang
- Shaoxiong Ji
affiliations:
- ELLIS Institute Finland
- University of Turku
- University of Technology Sydney
arxiv_id: '2608.17050'
url: https://arxiv.org/abs/2608.17050
pdf_url: https://arxiv.org/pdf/2608.17050
published: '2026-08-16'
collected: '2026-08-19'
category: LLM
direction: 大语言模型 · 跨模型外部记忆迁移
tags:
- External Memory
- Cross-Model Transfer
- Engram
- Lightweight Adaptation
- Knowledge Reuse
one_liner: 提出跨模型Engram记忆迁移框架，仅训练目标端轻量读取器即可复用源模型冻结外部记忆
practical_value: '- 电商商品/用户知识的跨LLM迁移场景可复用该框架：将业务训练好的Engram外部记忆冻结，仅适配目标模型侧轻量读取器即可低成本完成知识迁移，避免全量微调或RAG的检索延迟

  - 读取器设计trick可直接复用：采用双内存注入层+多分支门控的轻量读取器架构，可大幅提升记忆复用效果，无需修改记忆表本身

  - 业务落地可选择两种部署模式：若源模型和目标模型接口兼容可直接复用冻结记忆+源读取器零成本部署，效果不足时再补充少量目标端数据微调读取器，兼顾成本和效果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM知识利用分为两类：RAG类非参数方法存在检索延迟高、上下文开销大、与主干融合浅的问题；参数微调方法知识与模型权重绑定，难更新、难审计、难跨模型迁移。Engram式哈希外部记忆介于两者之间，但此前未验证其能否脱离源模型跨主干复用，存在知识资产无法沉淀、跨模型迭代成本高的痛点。

### 方法关键点
- 分词器无关的地址标准化方案：对输入文本做NFKC归一化、小写、去重音等预处理，基于标准n-gram哈希寻址，避免不同模型分词差异导致的记忆地址不匹配
- 仅训练目标端轻量读取器：冻结源模型训练好的记忆表，读取器支持单/多层注入、多分支门控设计，将记忆向量投影到目标模型残差流完成融合，训练参数量仅为从零训练记忆的3%
- 支持两种部署模式：接口兼容时可直接复用源读取器零成本部署，也可微调目标端读取器进一步提升效果

### 关键实验
在Wikitext-103、5个主流QA数据集上验证，覆盖Pythia、Qwen、TinyLlama、LLaMA、Mistral等模型家族：跨模型迁移最高实现15.7%的困惑度相对降低；双2层4分支读取器在QA任务上平均得分达38.8，追平原模型复用记忆的效果，优于RAG、LoRA、MLP Memory等基线

### 核心结论
外部记忆的可迁移性不仅取决于记忆表本身的内容，更取决于目标侧读取器和记忆的对齐能力，无需修改记忆表即可通过适配读取器大幅提升跨模型复用效果
