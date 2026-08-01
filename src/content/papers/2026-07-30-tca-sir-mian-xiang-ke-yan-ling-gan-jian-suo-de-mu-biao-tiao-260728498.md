---
title: 'TCA-SIR: Learning Target-Conditioned Abstractions for Scientific Inspiration
  Retrieval'
title_zh: TCA-SIR：面向科研灵感检索的目标条件抽象学习方法
authors:
- Yuto Suzuki
- Farnoush Banaei-Kashani
affiliations:
- Department of Computer Science and Engineering, University of Colorado Denver
arxiv_id: '2607.28498'
url: https://arxiv.org/abs/2607.28498
pdf_url: https://arxiv.org/pdf/2607.28498
published: '2026-07-30'
collected: '2026-08-01'
category: RAG
direction: 跨域检索优化 · 可迁移性度量
tags:
- Cross-domain Retrieval
- Transferability Estimation
- Interpretable Retrieval
- LLM-based Retrieval
- Scientific Information Retrieval
one_liner: 提出基于目标条件抽象的科研灵感检索方法，提升跨域可迁移灵感的检索效果与可解释性
practical_value: '- 电商跨品类关联推荐、广告创意跨行业复用等跨域召回场景，可借鉴TCA思路，在传统语义相似度特征外，新增目标相关可迁移抽象特征做排序，提升长尾关联内容召回率

  - 可解释性要求高的检索场景（如合规素材召回、灵感库检索）可复用「抽象可迁移原理+匹配」范式，同时输出检索依据降低人工审核成本

  - RAG跨域知识检索模块可引入目标条件抽象训练替代直接语义匹配，提升检索准确率的同时减少无关召回'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有科研灵感检索（SIR）仅基于主题相似度排序，无法识别跨领域、无主题重叠但具备可迁移问题解决思路的「远程灵感」，限制高创意性假设生成效果。
### 方法关键点
1. 参考人类思路迁移逻辑，将SIR重定义为目标条件抽象（TCA）任务，检索对象从原论文调整为针对目标问题提取的可迁移抽象原理
2. 提出TCA-SIR框架，先针对检索目标生成候选内容的目标适配抽象，再基于抽象表征预测可迁移性完成排序
### 关键结果
在ResearchBench基准上性能优于现有SIR方法和直接LLM检索，HitRate@top4%较SOTA MOOSE-Chem提升超10个百分点；生成的抽象内容比无训练prompt方案更清晰匹配目标相关机制，兼具更高检索精度和可解释性。
