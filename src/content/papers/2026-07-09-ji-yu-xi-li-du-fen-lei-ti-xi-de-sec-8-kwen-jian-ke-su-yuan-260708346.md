---
title: Grounded Event Extraction from SEC 8-K Filings with a Fine-Grained Taxonomy
title_zh: 基于细粒度分类体系的SEC 8-K文件可溯源事件抽取
authors:
- Rian Dolphin
- Joe Dursun
- Jarrett Blankenship
- Katie Adams
- Quinton Pike
affiliations:
- Massive.com
arxiv_id: '2607.08346'
url: https://arxiv.org/abs/2607.08346
pdf_url: https://arxiv.org/pdf/2607.08346
published: '2026-07-09'
collected: '2026-07-11'
category: Other
direction: 大模型事件抽取 · 可溯源标注
tags:
- Event Extraction
- LLM
- LLM-as-Judge
- Text Annotation
- Fine-grained Taxonomy
one_liner: 提出两阶段可溯源事件抽取系统，对SEC 8-K文件完成119类细粒度标注，最高精度达96%
practical_value: '- 两阶段标注架构可直接复用：第一阶段做输出约束+原文锚定，第二阶段单独做质量打分，适配电商商品/评论细粒度标签标注、广告素材分类等场景，大幅提升标注准确率

  - 模糊n-gram验证锚定原文的trick，可用于RAG系统的生成内容溯源校验环节，有效降低幻觉

  - LLM judge分层评估标签精度的方法，可复用到自定义分类任务的效果评估流程，降低人工标注成本'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
美国上市公司SEC 8-K文件原有SEC item编码粒度过粗，单一分类混杂经济属性差异极大的事件，大模型可实现细粒度标注，但需解决标签可溯源、可靠性验证的核心问题。
### 方法关键点
1. 搭建三级共119类的事件细粒度分类体系；
2. 两阶段抽取框架：第一阶段约束输出仅为合法分类条目，通过模糊n-gram验证将每个标签锚定到原文逐字引用片段；第二阶段基于分类定义对引用片段重新校验，输出标签质量分。
### 关键结果
对2022-2026年29.3万份8-K文件处理得到60.1万个可溯源事件标签并开源；基于5125个分层抽样标签的LLM judge评估显示，精度随质量分从12%单调提升至96%，无依据标签占比从8%降至接近0；消融实验证明仅独立的第二阶段打分可实现质量分校准，事件研究验证分类体系可区分同原始SEC编码下经济属性不同的事件。
