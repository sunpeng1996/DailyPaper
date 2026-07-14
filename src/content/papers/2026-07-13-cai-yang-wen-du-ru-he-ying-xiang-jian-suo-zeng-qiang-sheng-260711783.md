---
title: How Temperature Shapes Ideological Discourse in Retrieval-Augmented Generation?
title_zh: 采样温度如何影响检索增强生成中的意识形态话语传播
authors:
- Elmira Salari
- Hazem Amamou
- José Victor de Souza
- Shruti Kshirsagar
- Maria Nunes Delfino
- Anderson Avila
affiliations:
- Wichita State University
- Institut national de la recherche scientifique
- São Paulo Catholic University
arxiv_id: '2607.11783'
url: https://arxiv.org/abs/2607.11783
pdf_url: https://arxiv.org/pdf/2607.11783
published: '2026-07-13'
collected: '2026-07-14'
category: RAG
direction: RAG 生成参数与意识形态偏差管控
tags:
- RAG
- Sampling Temperature
- Ideological Bias
- Discourse Analysis
- LLM Evaluation
one_liner: 揭示采样温度、prompt策略、模型选择对RAG意识形态话语传递的影响规律
practical_value: '- 做电商导购/品牌内容生成类RAG时，若要输出和预设调性对齐的内容，可将采样温度设置为0.5左右，兼顾检索对齐度和生成多样性

  - 若要避免RAG输出传递错误引导（如虚假宣传、极端评价），可采用低温度（≤0.1）+ 负向prompt组合，抑制偏差内容传递

  - 可复用本文语义+词汇+混合相似度的评估框架，用于检测生成内容和品牌话术/合规要求的对齐度

  - 涉及用户观点生成的Agent场景中，小模型更容易被检索到的用户评论带偏立场，需额外加对齐约束'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
RAG被广泛用于降低LLM幻觉，但现有研究忽略了检索文档中的意识形态偏差会被RAG传递、放大的问题，采样温度作为控制生成随机性的核心参数，对意识形态传递的影响机制尚不明确，在医疗、电商等高风险场景可能引发错误引导、舆情风险，亟需厘清二者的关联规律。

### 方法关键点
- 构建1107篇新冠治疗文献的意识形态语料库，分为支持未获批治疗的争议类、符合官方标准的认可类两类
- 采用Lexical Multidimensional Analysis (LMDA)提取3类意识形态维度，识别不同意识形态的特征词汇、话语框架
- 对比4种配置：纯LLM普通prompt、纯LLM增强prompt（加意识形态元数据）、RAG普通prompt、RAG增强prompt，在0.1/0.3/0.5/0.7/0.9五组温度下的生成结果
- 采用语义、词汇、混合三类余弦相似度指标，评估生成内容和参考意识形态话语的对齐度

### 关键结果数字
- RAG配置的意识形态对齐度比纯LLM平均高5%以上，其中RAG+增强prompt在温度0.5时对齐度最高，Qwen模型可达0.864
- 纯LLM对齐度对温度更敏感，RAG配置的对齐度随温度升高平稳上升，0.9时达到峰值
- 负向prompt可使词汇对齐度平均下降12%，且低温度下抑制效果更明显
- 大模型（如GPT-4o-mini）受检索内容的意识形态影响更小，比小模型对齐度低8%左右

### 核心结论
RAG的意识形态传递不是由温度单一决定，而是解码随机性、prompt策略、检索约束三者共同作用的结果，检索grounding可显著降低温度导致的意识形态漂移。
