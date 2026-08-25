---
title: 'FashionKG-RAG: Knowledge Graph-Enhanced Retrieval-Augmented Generation for
  Fashion Question Answering'
title_zh: FashionKG-RAG：面向时尚问答的知识图谱增强检索增强生成系统
authors:
- Yujuan Ding
- Linyin Luo
- Shijie Wang
- Xu Yuan
- Yunshan Ma
- Yi Bin
- Wenqi Fan
- Qing Li
affiliations:
- 香港理工大学
- 中山大学
- 新加坡管理大学
- 同济大学
arxiv_id: '2608.22688'
url: https://arxiv.org/abs/2608.22688
pdf_url: https://arxiv.org/pdf/2608.22688
published: '2026-08-24'
collected: '2026-08-25'
category: RAG
direction: 知识图谱增强RAG · 垂直领域问答
tags:
- KG-RAG
- Fashion QA
- Knowledge Graph Construction
- Path Re-ranking
- Domain LLM
one_liner: 构建覆盖全时尚生态的权威知识图谱，提出双粒度重排序的训练无关KG-RAG框架提升时尚问答准确率
practical_value: '- 垂直领域KG构建可复用三阶段流水线：先从权威专业资料提取高保真核心三元组，再用通用KG补全实体连通性，最后用验证过的生成知识扩量，兼顾专业性和覆盖度，适合美妆、3C等电商品类知识库搭建

  - 处理高噪声、多概念的用户查询可复用双粒度重排序trick：先将用户query剪枝成核心语义骨架做高召回粗排，再用原始全query做Agent细排，平衡检索广度和精度，可直接迁移到电商咨询、商品问答场景

  - 垂直领域RAG选型可复用结论：通用文本Chunk RAG、公共KG RAG效果往往不如无RAG基线，优先用垂直领域高保真结构化知识做RAG才能带来正向收益，避免盲目上线通用RAG方案'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
时尚是知识密集型领域，通用LLM存在幻觉、缺乏专业领域知识，现有时尚KG仅聚焦商品属性，无法覆盖设计、文化、历史、商业等全生态知识，普通文本RAG和传统KG-RAG在处理概念密度高、噪声多的时尚查询时准确率低，无法满足复杂问答需求。
### 方法关键点
- 构建FashionEcoKG全领域时尚知识图谱：采用三阶段Agent流水线，1）从权威时尚教材中提取高保真三元组作为核心；2）用DBpedia时尚子图做跨域增强，补全孤立实体的连通性；3）用公开资料检索+LLM生成+人工验证的方式扩容，最终包含7299个实体、10592条三元组，覆盖8大类时尚概念。
- 提出训练无关PG-RAG框架：核心为双粒度路径重排序（DGPR）模块，1）Pruning-based Semantic Ranking（PSR）：将用户查询剪枝为核心语义骨架，与KG多跳路径做语义相似度粗排，过滤噪声提升召回；2）Grounding-based Agentic Ranking（GAR）：用原始全查询对粗排候选路径做逐路径Agent打分细排，保障检索结果符合完整用户意图。
### 关键实验结果
在包含2153条多类型多复杂度时尚QA的自建数据集，以及200条独立人工编写的FashionQA-mini测试集上评测：
- PG-RAG搭配Gemini-2.5 Flash最高达到80.74%的整体QA准确率，比无RAG基线高9.8%，比最优传统KG-RAG基线高10.16%；
- 在FashionQA-mini测试集上准确率达85.5%，比无RAG基线高13.5%，比KAPING基线高6.5%；
- 普通文本Chunk RAG、公共DBpedia时尚KG RAG反而会劣化基线LLM性能，只有基于高保真垂直KG的RAG能稳定带来正向收益。

最值得记住的一句话：在知识密集的垂直领域，只有基于高保真、结构化的专用领域知识做RAG才能带来正向性能提升，通用RAG方案甚至可能劣化效果。
