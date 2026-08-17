---
title: 'HERMES: a multi-agent framework for structured knowledge extraction from ultra-long
  documents in geoscience'
title_zh: HERMES：面向地学超长文档结构化知识提取的多智能体框架
authors:
- Ziqi Song
- Zongyuan Xiang
- James G. Ogg
- Bruce S. Lieberman
- Gabi Ogg
- Natalia López Carranza
- Wen Du
- Yufei Ye
- Shuan Li
- Zhong Peng
affiliations:
- Zhejiang Laboratory
- Purdue University
- University of Kansas
- University of Illinois Chicago
- Ant Group
arxiv_id: '2608.14055'
url: https://arxiv.org/abs/2608.14055
pdf_url: https://arxiv.org/pdf/2608.14055
published: '2026-08-14'
collected: '2026-08-17'
category: Agent
direction: 多智体 · 超长文档结构化知识抽取
tags:
- MultiAgent
- Knowledge Extraction
- Long Document Processing
- LLM
- Zero-shot Transfer
one_liner: 提出多Agent框架HERMES，可跨地学领域抽取超长文档结构化知识，效率较纯人工高6倍
practical_value: '- 多Agent调度架构可直接复用在电商海量商品详情页、用户UGC长文本的结构化抽取场景，通过协调LLM对接解析、校验、溯源模块，降低定制开发成本

  - 零样本跨域适配思路可迁移到电商多品类属性抽取、广告素材内容结构化需求，仅需更新领域约束规则即可适配新类目，无需重新训练模型

  - 可参考其人机结合的效率优化逻辑，6倍于纯人工的提效效果可作为自有业务结构化数据生产流程的优化参考指标'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
地学领域大量权威知识沉淀在非结构化超长历史文献中，布局复杂、模态多样，难以被计算利用，现有抽取方案难以适配领域强约束的超长文档处理需求。

### 方法关键点
提出可扩展多Agent框架HERMES，以协调LLM为核心，在统一的文档级抽取流程中整合领域约束、校验规则、证据追溯能力，可同时处理解析后的文本、表格、图片、图表说明等多模态内容。

### 关键结果
在55卷《无脊椎古生物学论丛》落地，提取到32277个化石分类实体、451878条属性，实体平均F1≈0.90，属性平均F1≈0.91；单卷处理效率较纯人工基线提升6倍；无需额外训练即可迁移到古地磁学、地球化学领域，跨域适配性优异。
