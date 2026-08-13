---
title: Can Frontier LLMs Match Natively Multimodal Embeddings? A Comparison on Hard-Negative
  Text-to-Image Retrieval
title_zh: 难负例图文检索场景下前沿大模型与原生多模态嵌入的性能对比
authors:
- Archan Dutta
- Vyanktesh Kanungo
affiliations:
- Westcliff University
arxiv_id: '2608.11343'
url: https://arxiv.org/abs/2608.11343
pdf_url: https://arxiv.org/pdf/2608.11343
published: '2026-08-11'
collected: '2026-08-13'
category: RecSys
direction: 多模态图文检索 技术方案对比评估
tags:
- Text-to-Image Retrieval
- Hard Negative
- Multimodal Embedding
- LLM Reranking
- Zero-shot Evaluation
one_liner: 对比难负例图文检索中多模态嵌入与大模型的性能，证明精度相当、嵌入方案latency低4个数量级
practical_value: '- 电商商品图文搜索、UGC内容配图检索等固定候选集场景，优先选用Gemini Embedding 2级别的原生多模态嵌入方案，预计算后在线
  latency 较LLM rerank低4个数量级，embedding生成成本可摊销到海量查询，性价比更高

  - 若候选池小且高频更新（如实时上新的小众品类、个性化临时候选集），可选用GPT-4.1/Claude Sonnet级多模态LLM做零样本rerank，精度和领先多模态嵌入无统计差异，无需预计算overhead

  - 内部评估检索系统性能时，可参考论文的难负例构造方法：在用户query文本嵌入空间筛选语义最相似的样本构造测试集，更贴合真实业务中的语义歧义场景，评估结果更具参考性

  - 复杂场景可结合两类方案优势：大规模全库召回用多模态嵌入做初筛，TopN候选集再用多模态LLM做细粒度rerank，兼顾低延迟和高精度'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前多模态图文检索存在两条主流技术路线：一是以Gemini Embedding 2、Amazon Nova 2为代表的原生多模态嵌入，可将文本、图像等多模态内容映射到统一向量空间做相似度匹配；二是GPT-4.1、Claude Sonnet等前沿多模态大模型，可直接输入查询和所有候选图像完成排序。两者在贴近业务真实难度的难负例场景下的精度、延迟、成本差异尚未有直接对比结论，对工业界选型参考价值极高。
### 方法关键点
- 数据集基于Flickr30k构造，共1000条查询，每条对应25个候选：1个正例+24个难负例，难负例在caption的文本嵌入空间筛选语义最相似的对应图像，最大化检索歧义，贴合真实业务难度
- 对比4类零样本方案：原生多模态嵌入（Gemini Embedding 2、Amazon Nova 2通用索引模式）、多模态LLM直接排序（GPT-4.1、Claude Sonnet 4.6），LLM排序时随机打乱候选顺序避免位置偏置
- 评估指标采用Recall@1、Recall@3、MRR，搭配McNemar检验、Wilcoxon秩和检验做显著性验证，同时统计端到端耗时和在线排序耗时
### 关键结果
- 精度层面：Gemini Embedding 2 Recall@1达0.804，GPT-4.1为0.789，Claude Sonnet 4.6为0.796，三者性能无统计学显著差异；Amazon Nova 2通用索引模式Recall@1为0.673，显著低于前三类
- 耗时层面：预计算完成后，Gemini Embedding 2处理1000条查询仅需0.66s，较GPT-4.1的6100s、Claude Sonnet的9415s快4个数量级；嵌入方案成本一次性支付可摊销，LLM成本随查询量线性增长
### 核心结论
固定大规模候选集优先选多模态嵌入兼顾精度和低延迟，小批量动态候选集用多模态LLM做rerank精度足够且无预计算overhead
