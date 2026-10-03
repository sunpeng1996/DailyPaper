---
title: Learning to structure data from user-generated thematic corpora
title_zh: 面向用户生成主题语料的自动结构化学习方法
authors:
- Elishay Avram
- Oren Glickman
- Elad Yom-Tov
affiliations:
- Bar-Ilan University
arxiv_id: '2610.01463'
url: https://arxiv.org/abs/2610.01463
pdf_url: https://arxiv.org/pdf/2610.01463
published: '2026-10-01'
collected: '2026-10-03'
category: LLM
direction: 大模型语料结构化 · 无预定义本体抽取
tags:
- LLM
- Schema Induction
- UGC Mining
- Structured Data Extraction
- Corpus Processing
one_liner: 无需预定义本体的迭代LLM框架，自动从用户生成主题语料挖掘属性Schema并抽取结构化数据
practical_value: '- 电商UGC评论/社区话题挖掘可复用该迭代框架，无需预定义属性ontology，自动抽取商品属性、用户偏好标签，大幅降低人工标注成本

  - 可参考框架中语义重叠属性合并、结构类型分配的pipeline，优化现有推荐系统的用户画像、商品标签体系构建流程

  - 可根据业务精度要求，在小参数指令微调LLM和大模型之间做精度-成本权衡，降低大规模语料处理的推理成本'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
用户生成主题语料（如社交社区、论坛、电商评论）隐含大量领域相关属性，但属性隐含、领域专属、无法提前预知，传统结构化抽取依赖预定义本体，成本高难扩展。

### 方法关键点
提出全自动化迭代框架，无需预定义本体：1）用LLM生成候选属性；2）迭代合并语义重叠属性，为每个属性分配结构类型；3）支持小参数LLM做属性值抽取，可预估精度损失。

### 关键结果
在5个健康类Reddit社区验证：挖掘的属性和人工标注一致性达61%，接近人工标注者之间的62%一致性；3/5场景下10轮内收敛到稳定属性集；结构类型分配准确率82%，属性值抽取F1达0.8；4类LLM系列中，小指令微调模型性能随参数规模提升显著，可灵活做精度成本权衡。
