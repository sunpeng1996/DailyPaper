---
title: 'Enhancing Procedural Writing Through Personalized Example Retrieval: A Case
  Study on Cooking Recipes'
title_zh: 基于个性化示例检索的流程类写作优化：以烹饪食谱为案例
authors:
- Paola Mejia-Domenzain
- Jibril Frej
- Seyed Parsa Neshaei
- Luca Mouchel
- Tanya Nazaretsky
- Thiemo Wambsganß
- Antoine Bosselut
- Tanja Käser
affiliations:
- School of Computer and Communication Sciences, EPFL, Lausanne, Switzerland
arxiv_id: '2609.17118'
url: https://arxiv.org/abs/2609.17118
pdf_url: https://arxiv.org/pdf/2609.17118
published: '2026-09-15'
collected: '2026-09-16'
category: RAG
direction: 检索增强生成 · 个性化示例召回
tags:
- Personalized Retrieval
- BM25
- LLM Fine-tuning
- Procedural Text
- Example-based Learning
one_liner: 提出多步个性化示例检索pipeline RELEX，提升流程类写作质量与用户体验
practical_value: '- 做个性化内容召回时可复用「先按质量分过滤候选池，再用BM25做语义匹配」的两级管道，平衡相关性与内容质量，适合电商商详、文案生成的参考案例召回场景

  - 面向用户生成内容（UGC）的质量评估场景，可借鉴微调LLM做质量打分的方案，替代人工规则覆盖复杂维度的质量判断

  - 检索结果的增强环节，可结合领域规则+正则表达式低成本生成解释性内容，降低全LLM生成的推理成本'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 动机
现有示例式学习反馈未考虑用户输入差异与先验知识，千人一面的内容易被用户认为冗余无用，流程类文本（如食谱、操作指南）的写作提升缺乏有效的个性化反馈方案。
### 方法关键点
提出RELEX自适应学习系统，核心为三级个性化示例检索管道：1. 用微调LLM预测用户提交的流程类文本质量分；2. 基于质量分从18万+候选库中召回质量更高的同类候选；3. 用BM25实时筛选语义最相似的示例，最终结合领域知识与正则为示例补充个性化解释。
### 关键结果
200人参与的2×2对照实验表明，相比非个性化示例方案，个性化示例组用户写作表现、用户体验均显著更优。
