---
title: 'The Embedder''s Dilemma: LLMs Are Better, but at What Cost?'
title_zh: 嵌入器困境：大语言模型性能更优，但代价几何？
authors:
- Adnan El Assadi
- Niklas Muennighoff
- Jinhyuk Lee
affiliations:
- Harvard University
- Stanford University
- Independent Researcher
arxiv_id: '2608.12875'
url: https://arxiv.org/abs/2608.12875
pdf_url: https://arxiv.org/pdf/2608.12875
published: '2026-08-12'
collected: '2026-08-21'
category: Eval
direction: 嵌入与LLM成本性能对比评测
tags:
- Text Embedding
- LLM
- MTEB
- Cost Efficiency
- Retrieval
- Benchmark
one_liner: 量化对比10款LLM与26款文本嵌入模型的性能成本，给出分场景选型建议
practical_value: '- 架构选型优先级：默认用嵌入模型处理分类、语义相似度匹配、聚类等常规任务（如电商商品分类、用户意图识别、相似商品召回），仅对需多文档推理的复杂检索场景考虑LLM，控制成本

  - 成本优化trick：用LLM做检索重排时，可降低推理预算（关闭不必要的CoT输出），多数场景下能保留甚至提升检索效果，同时砍掉28%~81%的推理成本

  - 生产级RAG/推荐召回可沿用「嵌入模型召回TopK + LLM列表重排」的混合方案，推理密集型场景下nDCG@10可提升57%，成本仅为全LLM检索的1/5~1/3'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM能力快速提升，不少从业者考虑用LLM替代传统文本嵌入pipeline，但二者的性能差异、成本差距、适用场景边界尚不明确，缺乏系统的量化对比支撑选型决策。

### 方法关键点
- 覆盖10款主流LLM（含Gemini、Qwen、DeepSeek等6个系列）、26款文本嵌入模型（参数量118M~14B），统一在37任务的自定义评测集MTEB(LLM)上测试，覆盖分类、语义相似度、聚类、对分类、检索5大场景
- 成本核算统一：嵌入模型按H100 GPU实际吞吐量折算成本，LLM按官方API token定价统计，同时在同H100硬件下测试二者吞吐量差异
- 额外验证LLM推理预算调整、少样本提示对效果的影响，以及「嵌入召回+LLM重排」混合架构的性价比

### 关键结果
- 整体性能基本持平：最优LLM（Gemini 3.1 Pro）得分77.6，最优嵌入模型（Octen-8B）得分77.2，差距仅0.4个点，在统计误差范围内
- 分场景差异显著：LLM在推理密集型检索任务上领先8.5分，嵌入模型在分类任务上领先5.6分，其余三类任务二者无统计差异
- 成本差距巨大：同性能下LLM成本是嵌入模型的338~2424倍，同H100硬件下嵌入模型吞吐量是LLM的2.5~736倍

**最值得记住的话：嵌入模型是绝大多数场景的性价比首选，LLM仅适合作为推理密集型检索的补充，不要盲目用LLM替换成熟的嵌入pipeline**
