---
title: 'The Linguistic Knowledge Benchmark: Do Language Models Know the Foundations
  of Early-Grade Literacy?'
title_zh: 语言知识基准：大语言模型是否掌握低年级识字的基础语言知识？
authors:
- Maxime Lelièvre
- Alasdair Mackintosh
- Dominic Andrews
- Tobias Murray
- Moritz Boos
- Oliver G. B. Garrod
affiliations:
- Fab AI
arxiv_id: '2611.34823'
url: https://arxiv.org/abs/2611.34823
pdf_url: https://arxiv.org/pdf/2611.34823
published: '2026-11-25'
collected: '2026-11-28'
category: Eval
direction: 低资源语言大模型能力评测
tags:
- LLM Evaluation
- Low-resource Language
- Benchmark
- Automated Dataset Pipeline
- Literacy
one_liner: 提出低资源语言识字教学领域语言知识评测基准，配套自动化构建流水线，完成120+模型多语言评测
practical_value: '- 可复用其「LLM生成+项目反应理论筛选+专家审核」的评测集构建流程，快速搭建电商/广告等垂直场景的LLM能力评测集，降低人工标注成本

  - 小语种电商/跨境推荐场景的LLM选型可参考其结论：小参数模型在低资源语种上能力衰减幅度远高于通用语种，优先选择大模型或提前做领域预训练适配

  - 其从官方文档（课程/类目规则/运营规范等）自动生成结构化评测题目的流水线，可直接迁移到业务场景的LLM合规性、领域知识掌握度评测'
score: 4
source: arxiv-cs.CL
depth: abstract
---

### 动机
中低收入国家教学所用低资源语言在LLM训练数据中占比极低，现有评测体系未覆盖识字教学依赖的基础语言知识维度，无法支撑LLM落地低年级识字教学场景。

### 方法关键点
搭建高可复用的半自动化评测集构建流水线，整合LLM驱动的素材梳理、特征合并、题目生成、质量控制模块，引入项目反应理论做题目难度筛选，最终按9个语言领域+7个年级的固定框架组织经专家审核的评测题集。

### 关键结果
- 前沿大模型在英语、斯瓦希里语上的评测准确率均超过90%
- 10B参数以下最优两款小模型英语准确率达91.7%/73.0%，斯瓦希里语仅为51.9%/40.7%
- 移动端可部署的轻量模型平均准确率：英语47%，斯瓦希里语仅24%
