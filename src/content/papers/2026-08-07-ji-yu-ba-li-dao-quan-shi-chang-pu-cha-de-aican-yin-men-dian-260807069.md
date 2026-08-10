---
title: 'Invisible to the Machine: Auditing AI Restaurant, Cafe, and Bar Recommendation
  Against a Complete Market Census'
title_zh: 基于巴厘岛全市场普查的AI餐饮门店推荐效果审计研究
authors:
- Vladimir Pitenin
affiliations:
- Norly Research
arxiv_id: '2608.07069'
url: https://arxiv.org/abs/2608.07069
pdf_url: https://arxiv.org/pdf/2608.07069
published: '2026-08-07'
collected: '2026-08-10'
category: RecSys
direction: 推荐系统审计 · 本地生活POI推荐
tags:
- Recommendation Audit
- POI Recommendation
- LLM Evaluation
- Local Discovery
- RAG
one_liner: 首个基于完整线下餐饮市场普查的AI推荐审计，揭示85%商家AI不可见及双边际可见性规律
practical_value: '- 做本地生活POI推荐/Agent服务时，可复用双边际优化逻辑：召回层优先加权商家文档特征（官网、评价量、第三方提及量、价签信息），排序层再加权星级评分，同时提升推荐准度和中小商家覆盖度

  - 做AI推荐系统审计时，必须严格校验实体匹配准确性，匹配误差会直接导致特征重要性结论完全偏离，同时要避免审计数据收集路径引入的特征偏置

  - 做生成式搜索引擎优化（GEO）类产品时，单轮单次查询的可见性结果无统计意义，需跨引擎、跨query paraphrase重复采样才能得到稳定的可见性度量

  - 本地生活类RAG系统的核心故障风险不是实体虚构，而是数据过时，需要定期同步POI营业状态数据，避免推荐已关停商家'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
AI助手已成为本地生活服务核心搜索入口，过往推荐审计要么是限定候选集的联合实验无法度量真实准入门槛，要么基于头部商家抽样审计无全市场分母无法计算真实不可见率，餐饮类POI推荐的真实效果缺乏全量实测数据，直接关联商家营收。
### 方法关键点
- 普查巴厘岛Canggu、Ubud两个区域共4776家餐饮类POI，构建全市场基准库
- 设计96个分persona的本地餐饮查询模板，7天内对ChatGPT、Claude、Gemini、Perplexity 4个带RAG的生产级AI系统发起2208次查询，收集12439条有效商家提及
- 采用双边际模型分别度量「推荐准入边际」「列表内排序边际」的特征重要性，全程校验实体匹配精度避免结论偏误
### 关键结果
1. 全市场85.6%的商家从未被任何AI系统推荐，即使是有50条以上评价的成熟商家，不可见率也达72.6%
2. 准入边际核心驱动特征为评价量（OR=1.64）、自有官网（OR=1.92）、标价信息（OR=1.54）、第三方提及量（OR=1.44），星级评分对准入无显著影响
3. 排序边际核心驱动特征为星级评分（OR=1.17），第三方提及量对排序无显著影响
4. 商家虚构率仅0.08%，但推荐已关停商家的次数达93次，数据过时是核心故障；不同系统top20推荐集Jaccard相似度仅0.33~0.54
### 核心结论
商家文档完备性决定能不能被AI推荐，评分质量仅能决定推荐排序，8成以上中小商家处于AI流量完全盲区
