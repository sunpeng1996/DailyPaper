---
title: 'ReFilter: Bridging Embeddings and LLM Filtering for Similar Mobile App Retrieval'
title_zh: ReFilter：融合嵌入检索与LLM过滤的相似移动应用检索框架
authors:
- Buthayna AlMulla
- Maram Assi
- Safwat Hassan
affiliations:
- University of Toronto
- Université du Québec à Montréal
arxiv_id: '2609.25306'
url: https://arxiv.org/abs/2609.25306
pdf_url: https://arxiv.org/pdf/2609.25306
published: '2026-09-21'
collected: '2026-09-23'
category: RecSys
direction: 移动应用检索 · 混合召回过滤框架
tags:
- Information Retrieval
- App Similarity
- Embedding Retrieval
- LLM Filtering
- Hybrid RecSys
one_liner: 提出两阶段混合检索框架ReFilter，兼顾效率与精度实现高准确的功能相似移动应用检索
practical_value: '- 两阶段架构可直接复用：先用量级更轻的Embedding做粗召回筛出Top-K候选，再用LLM做细粒度功能匹配，平衡成本与精度，适合电商同款商品检索、相似内容推荐等场景

  - 嵌入选型结论可复用：针对功能匹配任务，大参数量LLM生成的纯文本嵌入（如Linq-Embed-Mistral）效果优于小模型BGE、甚至多模态嵌入，不必盲目叠加多模态特征引入噪声

  - LLM过滤优化Trick：针对0-shot LLM判断过于保守的问题，补充2-4个覆盖常见错误场景的Few-Shot示例，能在几乎不损失精度的前提下提升召回，比盲目增加示例数收益更高

  - 弃用固定Top-K截断：不同品类/热度的物品相似候选数量差异极大，用LLM动态判断是否相似而非固定返回Top-K，可大幅提升推荐相关性'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有基于Embedding的相似App检索仅能捕捉表层语义相似，无法精准识别可作为功能替代品的App；而直接用LLM对全库做成对功能匹配计算成本极高，无法适配大规模检索场景，亟需兼顾效率与精度的功能相似检索方案。

### 方法关键点
- 两阶段混合架构：第一阶段用Embedding模型对全量App描述文本生成向量，通过余弦相似度粗召回Top-45候选；第二阶段用LLM逐对判断候选与目标App的功能匹配度，筛选出真正可替代的相似App
- 横向对比6种Embedding方案：含3种纯文本Embedding（BGE-AVG、BGE-FIRST、Linq-Embed-Mistral）、3种多模态Embedding（SigLIP2-AVG、SigLIP2-TopN、Voyage多模态），最终选型效果最优的纯文本Linq模型做粗召
- LLM过滤优化：基于0-shot误判场景分析，补充2个覆盖常见错误的Few-Shot示例，在不损失精度的前提下提升召回

### 关键实验
数据集为爬取的Google Play 20635个非游戏类App，人工标注1765对App的功能相似性，覆盖20个品类。纯Embedding召回最优的Linq模型在k=45时F1仅为60%，加入2-shot GPT-5过滤后整体F1提升至90%，返回结果比Google Play官方相似列表的功能相关性更高，单query过滤平均耗时4.2秒、成本0.04美元。

### 核心结论
针对功能相似检索任务，「Embedding粗召+LLM精滤」的混合架构远优于单一Embedding方案，且不必盲目叠加多模态特征，动态适配品类的返回数量远好于固定Top-K截断
