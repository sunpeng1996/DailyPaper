---
title: Auditing Source Exposure in Baidu and Google AI Search
title_zh: 百度与谷歌AI搜索的信息来源曝光机制审计研究
authors:
- Yibo Li
- Enci Guan
- Yuedan Cai
- Geng Liu
- Francesco Pierri
affiliations:
- Politecnico di Milano, Italy
arxiv_id: '2609.24407'
url: https://arxiv.org/abs/2609.24407
pdf_url: https://arxiv.org/pdf/2609.24407
published: '2026-09-21'
collected: '2026-09-23'
category: Eval
direction: AI搜索评估 · 跨平台跨语言审计
tags:
- AI Search
- Source Exposure
- Cross-lingual Audit
- Semantic Similarity
- Search Evaluation
one_liner: 跨语言跨平台审计百度谷歌AI搜索的概述触发、来源曝光分布及生成答案差异
practical_value: '- 开发带溯源能力的搜索类Agent时，可复用本文的来源曝光集中度、跨场景重叠度评估维度，优化可信引用的排序与展示策略，提升结果可信度

  - 跨境电商多语言搜索场景，可参考本文的跨语言同义Query生成答案语义相似度评估方法，对齐不同语言下的搜索回答体验，降低用户认知成本

  - 搭建AI搜索结果生态治理机制时，可借鉴本文的审计框架，量化不同垂直领域内容的曝光公平性，规避流量过度向头部域名集中的风险'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
当前AI生成概述已成为搜索界面的核心展示层，但中文场景下AI搜索的来源曝光机制、跨平台行为差异研究存在缺口，缺乏系统性的跨语言对比框架。
### 方法关键点
选取MS MARCO数据集的英文Query及对应人工翻译的中文同义Query，在百度、谷歌两大平台的中英语言设置下开展对照审计，覆盖AI概述触发规则、可见来源域名分布、曝光集中度、跨场景来源重叠度四大维度，同时基于embedding计算同义Query生成答案的语义相似度。
### 关键结果
不同平台-语言设置下的概述可用性、来源曝光策略差异显著；跨场景可见域名集合重叠度极低；同义Query生成答案的中位余弦相似度区间为0.701~0.813，证实语义相似度与来源曝光是AI搜索的两个独立评估维度。
