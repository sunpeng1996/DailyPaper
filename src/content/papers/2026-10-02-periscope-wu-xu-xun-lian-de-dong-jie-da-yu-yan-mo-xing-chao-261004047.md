---
title: 'Periscope: Extending Frozen Language Models Beyond Their Context Window'
title_zh: Periscope：无需训练的冻结大语言模型超上下文窗口推理方法
authors:
- Mohamed Eltahir
- Anas Obayd
- Raed Rashid
- Abdulrahman Alghamdi
- Abdulrahman Mousa
- Abdallah Ahmed
- Tanveer Hussain
- Naeemullah Khan
affiliations:
- King Abdullah University of Science and Technology
- Edge Hill University
arxiv_id: '2610.04047'
url: https://arxiv.org/abs/2610.04047
pdf_url: https://arxiv.org/pdf/2610.04047
published: '2026-10-02'
collected: '2026-10-06'
category: LLM
direction: 大模型长上下文推理 · 无训练窗口扩展
tags:
- LongContext
- FrozenLLM
- InferenceOptimization
- KVCache
- ContextWindowExtension
one_liner: 通过局部+跨步网格探针，让冻结LLM无需微调即可处理平方于原生窗口长度的长文本
practical_value: '- 电商/推荐场景的长文本理解（长商品介绍、全量用户评论、用户历史行为聚合）可直接复用该框架，无需微调现有LLM，用小显存GPU即可处理超长篇文本，省去长上下文模型的部署成本

  - RAG系统的召回后重排环节，可替换现有切块嵌入检索方案，用Periscope的证据地图选TopK高相关块喂给LLM，比嵌入检索准确率高6-11个点，可避免语义匹配漏召回需推理的相关内容

  - Agent处理长任务（全会话上下文承接、长文档分析）时，可复用网格切块+独立探针的设计，比Chain of Agents类串行方案性能高10个点， latency降低2/3'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有长上下文LLM存在三大痛点：1）注意力成本随长度平方增长，KV cache占用显存极高，27B模型读4.5M tokens需要296GB KV cache；2）实际精度随长度快速下降，远达不到标称窗口的效果，多数128k窗口模型在32k长度下精度就腰斩；3）窗口扩展方案需要微调/改架构，无法直接复用已部署的冻结LLM，RAG类提前选块方案又容易漏掉需要推理的相关内容。

### 方法关键点
- 完全无训练的推理框架，不改动冻结LLM的权重与架构：将长文本切为c大小的块，排布为K×K网格，K=⌈√N⌉，N为总块数
- 设计两类独立探针：局部探针读取K个连续块的邻接跨度，跨步探针每K个块取一个采样全文本，共2K次短窗口调用，每次调用长度仅为√(s*c)，s为总文本长度
- 采用相对弃权选项的log odds作为统一评分，每个答案取局部和跨步探针的最高评分之和，自动生成证据地图定位相关块位置，可选直接输出答案或取TopK块二次推理
- 理论最大支持文本长度为W²/c，W为LLM原生窗口大小，计算成本随文本长度呈s^1.5增长，远低于原生全读的s²

### 关键结果
- LongBench v2上，仅读9k tokens（证据地图选TopK块）性能与Qwen3.5-4B最优131k窗口全读持平，比同预算的嵌入选块高6个点、随机选块高9个点
- InfiniteBench（中位数上下文150k）上，比最优262k窗口全读高5个点准确率
- BRIGHT长文档检索任务上，NDCG@10达0.493，超过BM25、嵌入检索、16k窗口前缀读等6个基线
- 27B模型处理4.5M tokens上下文仅需3.1GB KV cache，单张80GB A100即可运行

### 核心结论
长文本决策类任务只需要找到支撑答案的最强证据块，不需要全量读入上下文，基于网格探针的因子化读入可以在大幅降低显存和计算成本的同时达到甚至超过全窗口读入的效果
