---
title: 'It''s How You Ask: Gender-Associated Linguistic Bias in LLMs'
title_zh: 大语言模型中与性别关联的语言偏见研究
authors:
- Katherine Van Koevering
- Anjalie Field
affiliations:
- Johns Hopkins University
- Data Science and AI Institute
- Computer Science Department
arxiv_id: '2608.13328'
url: https://arxiv.org/abs/2608.13328
pdf_url: https://arxiv.org/pdf/2608.13328
published: '2026-08-13'
collected: '2026-08-14'
category: LLM
direction: LLM公平性 · 语言偏见机制分析
tags:
- LLM Bias
- Gender Fairness
- Linguistic Features
- Transformer Interpretability
- Workplace AI
one_liner: 揭示女性常用语言特征会导致LLM输出质量更低，且这类偏见事后缓解难度极高
practical_value: '- 搭建电商客服/营销文案生成LLM服务时，需测试用户输入含委婉语、疑问后缀等特征时的输出一致性，避免对不同表达习惯的用户输出质量不均

  - 做LLM偏见优化时，优先针对Transformer早期层的语言特征编码做干预，比事后prompt引导、要求用户调整表达的落地效率更高

  - 面向职场人的简历/公文生成类SaaS工具，需预先对齐不同语言风格输入的输出质量阈值，避免放大性别相关的职场不公'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
职场沟通场景已大量使用LLM辅助内容生成与润色，不同性别群体的语言表达习惯存在系统性差异，需明确LLM是否会因此产生不公平的输出差异。
### 方法关键点
针对模糊限制语、反义疑问句、集体指代三类女性常用语言特征，在3类文档场景、4款主流LLM上开展对照测试，对比显性性别线索（如署名）与语言风格的影响差异，同时从Transformer层编码机制分析偏见成因。
### 关键结果
1. 含女性常用语言特征的prompt会触发LLM输出更短、复杂度与正式度显著更低的回复，控制prompt复杂度后效应仍稳定存在；
2. 语言风格对输出的影响远高于显性性别署名，后者几乎无稳定影响；
3. 相关语言特征在Transformer早期层就被编码且与其他特征纠缠，用户无法通过刻意调整表达习惯规避，事后缓解难度极高。
