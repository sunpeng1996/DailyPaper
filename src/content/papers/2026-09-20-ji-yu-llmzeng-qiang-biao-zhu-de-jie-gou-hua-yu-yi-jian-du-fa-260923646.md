---
title: 'Beyond Relevance: Structured Semantic Supervision for Product Search with
  LLM-Augmented Annotations'
title_zh: 基于LLM增强标注的结构化语义监督商品搜索方法
authors:
- Girish A. Koushik
- Swapnil Bhosale
- Samarth Agrawal
- Hadeel Sadany
- Constantin Orasan
- Xiatian Zhu
- Diptesh Kanojia
affiliations:
- University of Surrey
- eBay USA
- Birmingham City University
arxiv_id: '2609.23646'
url: https://arxiv.org/abs/2609.23646
pdf_url: https://arxiv.org/pdf/2609.23646
published: '2026-09-20'
collected: '2026-09-23'
category: RecSys
direction: 电商搜索 · LLM增强标注结构化监督
tags:
- ProductSearch
- LLMAnnotation
- DualEncoder
- Reranker
- ESCI
one_liner: 通过LLM生成结构化属性加人类标注语义信号优化电商搜索，无人工配置接近性能上限
practical_value: '- 标注流程可复用：先用LLM生成query/商品的结构化属性、相关性解释作为预标注，再让人类仅做修正和打分，可大幅降低标注成本

  - 低性能query优化技巧：不要全量用LLM生成的合成标注，仅对基线排名差、语义模糊的长尾query调用LLM做语义增强，避免引入噪声

  - 架构选型参考：小参数量MiniLM在早精度（nDCG@3/5）上优于大参数量Qwen3，性能差距可忽略的前提下优先选轻量模型降低推理成本

  - 特征优先级参考：人类标注的解释文本和评论带来的收益远高于标量centrality特征，预算有限时优先保证文本类监督信号而非额外标量标签'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
电商搜索传统粗粒度相关性标签无法区分仅语义相关的周边商品与真正满足用户购买意图的核心商品，纯LLM合成标注常与人类意图存在偏差，亟需更有效的结构化语义监督信号提升排序质量。

### 方法关键点
- 数据层：基于ESCI数据集子集，先用Llama 3.1 8B零/少样本生成4类query属性、7类商品属性及相关性解释作为预标注，再由人类标注binary centrality标签、修正相关性打分、编辑解释文本
- 架构层：采用两阶段检索架构，第一阶段双编码器召回：文本特征用冻结all-MiniLM-L6-v2编码，与结构化属性的MLP编码向量加和后做余弦相似度匹配；第二阶段MLP重排，输入拼接的文本嵌入、分类特征、数值特征输出相关性分数
- 实验分三种配置：Q+P（仅LLM生成属性，无人工可上线）、Q+P+H（人类标注为性能上限）、Q+P+Synth-H（LLM合成人类信号替代）

### 关键结果
- 测试集含75条query、984条query-商品对，人类标注上限Q+P+H nDCG@10达0.9382，无人工的Q+P配置也达到0.9258
- Qwen3.5-27B合成标注整体nDCG@10为0.9150，对基线nDCG<0.6的低性能query最多提升48pp，对高性能query有小幅负向收益
- 消融实验显示：移除人类修正的解释文本nDCG@10降7.75pp，移除centrality仅降0.1pp

> 最值得记住：LLM在搜索推荐场景的核心价值是暴露和近似结构化语义监督信号，而非直接替代人类标注。
