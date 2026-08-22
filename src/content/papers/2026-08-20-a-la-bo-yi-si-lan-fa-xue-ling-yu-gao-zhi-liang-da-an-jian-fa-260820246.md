---
title: What Makes a Good Fiqh Retriever? Answer Retrieval for Arabic Islamic Jurisprudence
title_zh: 阿拉伯伊斯兰法学领域高质量答案检索方法评测与优化
authors:
- Somaya Eltanbouly
- Heba Sbahi
- Samer Rashwani
- Abdessalam Bouchekif
- Mutaz al-Khatib
- Shahd Gaben
- Mohammed Ghaly
affiliations:
- Hamad Bin Khalifa University, Qatar
arxiv_id: '2608.20246'
url: https://arxiv.org/abs/2608.20246
pdf_url: https://arxiv.org/pdf/2608.20246
published: '2026-08-20'
collected: '2026-08-22'
category: RAG
direction: RAG 垂直领域检索优化
tags:
- RAG
- Retrieval Evaluation
- Vertical Domain RAG
- Hybrid Retrieval
- Domain Filtering
one_liner: 构建阿拉伯伊斯兰法学检索测试集，评测多类检索策略，验证教法学派感知过滤的显著效果
practical_value: '- 垂直领域RAG系统迭代时优先单独评测检索模块，避免端到端评估无法定位检索/生成侧的错误根因

  - 针对有细分属性（如商品类目、用户分层）的检索场景，新增属性感知前置过滤，可大幅提升细分场景检索准确率

  - 强基线检索模型上叠加混合检索策略收益有限，优化优先级低于领域定制的过滤规则'
score: 4
source: arxiv-cs.IR
depth: abstract
---

### 动机
伊斯兰问答场景RAG系统普遍采用端到端评估，无法区分检索失败与生成失败；且伊斯兰法学中相同问题因所属教法学派不同存在差异判决，需检索返回精准携带所需判决规则的片段。
### 方法关键点
构建阿拉伯伊斯兰法学专用检索测试集，系统性评测稠密检索、词法检索、混合检索、微调、教法学派感知过滤等多类检索策略的表现，同时开展错误分析定位核心挑战。
### 关键结果
最优基线检索器MRR@5达0.524，微调后提升至0.553；强基线模型上叠加混合检索收益有限；教法学派感知过滤可使学派特定问题的MRR@5提升1倍以上；核心挑战为区分主题相似但不含所需判决的片段与有效答案片段
