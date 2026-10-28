---
title: 'Nothing Left Behind: Finding Evidence from a Large Randomized Evaluation Corpus'
title_zh: 《不漏过任何证据：大规模随机评估语料的检索方案对比》
authors:
- Giuliano Martinelli
- Abelardo Carlos Martinez Lorenzo
- Satvik Garg
- Linxi Wang
- Riccardo Orlando
- Piriyakorn Piriyatamwong
- Samuel Paul Fraiberger
affiliations:
- World Bank Group
arxiv_id: '2610.36910'
url: https://arxiv.org/abs/2610.36910
pdf_url: https://arxiv.org/pdf/2610.36910
published: '2026-10-27'
collected: '2026-10-28'
category: RAG
direction: RAG高召回场景检索架构优化
tags:
- RAG
- Semantic Retrieval
- Relevance Filtering
- Embedding
- Recall Optimization
one_liner: 对比标签检索与语义检索+LLM过滤方案，高召回场景下后者证据召回率提升超1倍
practical_value: '- 高召回需求的RAG系统可复用「宽召回语义匹配+LLM relevance过滤」两段架构，相比纯标签召回大幅提升覆盖度，适合电商合规检索、广告素材确权、全量用户评论语义检索等场景

  - 可将现有标签检索结果与语义检索结果做融合，小召回量下能额外提升12%+召回率，无需替换原有标签体系即可快速迭代

  - 召回深度K可做动态配置：探索性场景用小K（如100）保障低延迟，全量核查场景用大K（如2500）保障召回，平衡算力成本和业务效果

  - LLM relevance过滤效果已超过普通人标注一致性，可替代80%+人工初筛工作，适合电商评论打标、售后工单分类等场景'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有基于人工分类标签的检索方案高度依赖标签体系的覆盖度和粒度，细粒度查询易漏召回、粗标签易返回冗余结果，无法满足系统评价、合规核查等高召回需求场景对证据全量覆盖的要求，流畅的生成结果无法保证底层检索的完整性。

### 方法关键点
- 对比两类检索架构：1）标签匹配架构：LLM将查询映射到预设分类体系实体，再召回关联证据；2）语义检索+LLM过滤架构：先直接用embedding匹配干预-结果对文本得到top-K候选，再用LLM判断每个候选和查询的相关性
- 检索单元设为论文内的干预-结果对，比论文级检索粒度更细，避免单篇多内容导致的冗余召回

### 关键实验
数据集为世界银行ImpactAI平台的7354篇随机对照试验（RCT）论文，共74826个干预-结果对，对比基线为现有标签检索系统，测试集包含348条系统评价衍生查询、374条真实用户查询、1000条合成查询。
核心结果：标签检索的召回率固定为45.1%；语义检索+Gemini 2.5 Flash过滤架构在K=2500时召回率达85.0%，较基线高39.9个百分点，用户反馈相关度达94.7%；两类结果融合后K=2500时召回率进一步提升至87.9%；K=2500时总延迟为77.2秒，K=100时仅7秒。

### 核心结论
高召回需求场景下应当用语义检索做发现、标签体系做组织，两类方案互补可同时兼顾覆盖度和结果可解释性。
