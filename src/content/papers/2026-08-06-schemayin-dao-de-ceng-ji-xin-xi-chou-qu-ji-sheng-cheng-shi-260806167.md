---
title: Schema-Guided Hierarchical Information Extraction and Semantic Evaluation Using
  Generative AI
title_zh: Schema引导的层级信息抽取及生成式AI语义评估方法
authors:
- Modhurita Mitra
- Jan-Willem Versteeg
- Maarten D. Schermer
- Shiva Nadi Najafabadi
- Marie L. De Bruin
- Lourens T. Bloem
affiliations:
- Research Engineering Team, Information and Technology Services, Utrecht University
- Division of Pharmacoepidemiology and Clinical Pharmacology, Utrecht Institute for
  Pharmaceutical Sciences, Utrecht University
arxiv_id: '2608.06167'
url: https://arxiv.org/abs/2608.06167
pdf_url: https://arxiv.org/pdf/2608.06167
published: '2026-08-06'
collected: '2026-08-07'
category: LLM
direction: 大模型信息抽取与结构化输出评估
tags:
- LLM
- Information Extraction
- Schema-Guided
- Semantic Evaluation
- Zero-Shot
- Structured Output
one_liner: 提出Schema引导的零样本层级信息抽取框架与路径匹配语义评估方案，效率达人类专家30倍
practical_value: '- 电商商品爬虫内容、用户评论、商家资质材料的结构化属性抽取可复用该Schema引导的零样本抽取范式，无需标注即可快速适配新类目属性抽取需求

  - 推荐系统结构化召回/排序特征校验、Query理解结构化输出评估可复用路径匹配+LLM语义对比方案，比字面匹配更贴合业务实际效果

  - Agent调用工具返回的结构化结果校验可直接复用其四级匹配规则（精确/语义/有用/不匹配），灵活适配不同业务的容错要求'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有信息抽取方案难以适配层级嵌套、可变基数的结构化信息提取需求，配套自动化语义评估能力缺失，人工标注/校验成本高、效率低。
### 方法关键点
1. 以嵌入领域知识的Schema作为统一信息模型，支持单次LLM调用零样本完成嵌套、多值属性的全量抽取，无需微调；
2. 评估阶段引入基于路径的语义匹配算法对齐抽取结果与金标准的层级属性，再调用LLM完成属性值语义对比，按业务规则将匹配结果分为精确匹配/语义匹配/有用/不匹配四类。
### 关键结果
在NICE公开的医疗技术评估文档上测试，14个目标属性中12个的F1得分超过90%，单文档抽取耗时比人类专家低30倍，框架可跨LLM模型、跨机构、跨语言迁移。
