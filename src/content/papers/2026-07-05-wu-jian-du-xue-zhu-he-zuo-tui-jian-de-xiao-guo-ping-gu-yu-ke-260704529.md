---
title: Evaluation and Explainability of Unsupervised Scholarly Collaboration Recommendations
title_zh: 无监督学术合作推荐的效果评估与可解释性研究
authors:
- Md Asaduzzaman Noor
- John W. Sheppard
- Jason A. Clark
affiliations:
- Gianforte School of Computing, Montana State University
- Library, Montana State University
arxiv_id: '2607.04529'
url: https://arxiv.org/abs/2607.04529
pdf_url: https://arxiv.org/pdf/2607.04529
published: '2026-07-05'
collected: '2026-07-08'
category: RecSys
direction: 无监督内容推荐 · 可解释性评估
tags:
- Unsupervised-RecSys
- Content-based-Rec
- Explainability
- Embedding-Retrieval
- Topic-Modeling
one_liner: 对比三类无监督学术合作推荐方法，提出重叠消除评估框架，给出两种互补可解释方案
practical_value: '- 召回链路可参考三类方法选型：冷启动/低特征重叠场景优先用embedding/主题模型，特征充足场景用TF-IDF类词袋方法降本提效

  - 推荐效果评估可复用「消除部分特征重叠的约束场景」设计，避免模型仅依赖简单匹配导致泛化性不足的问题

  - 可解释性模块可采用双路径设计：规则类内置解释保证透明度，大模型生成式解释提升用户可读性，按需适配场景'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
学术跨领域合作推荐场景下历史共著数据稀疏，现有无监督内容推荐方法多依赖词法重叠，泛化性差，同时缺乏可有效衡量真实匹配能力的评估框架和可落地方案。
### 方法关键点
1. 对比三类无监督推荐方案：TF-IDF词法匹配基线、LDA/BERTopic主题类模型、SciBERT+Faiss embedding检索类方法
2. 设计约束评估范式：人为消除研究者间部分出版物重叠，仍以历史共著为代理真值，评估模型脱离词法匹配的泛化能力
3. 提出两类互补可解释路径：基于主题的内生透明解释、基于大模型的检索式事后可读解释
### 关键结果
全信息场景下TF-IDF效果最优，特征重叠大幅降低时性能下降超50%；主题、embedding类方法性能波动不足20%，可捕捉更广泛的分布相似性而非仅依赖词法重叠；两类解释方案分别在透明度、可读性上各有优势。
