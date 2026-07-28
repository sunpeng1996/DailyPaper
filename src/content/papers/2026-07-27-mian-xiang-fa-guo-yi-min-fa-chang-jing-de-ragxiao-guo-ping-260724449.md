---
title: 'Evaluating RAG for French immigration law: a benchmark and baseline study'
title_zh: 面向法国移民法场景的RAG效果评估：基准数据集与基线研究
authors:
- Annia Abtout
- Julien Delaunay
- Monika Ewa Rakoczy
affiliations:
- Talan, Paris, France
arxiv_id: '2607.24449'
url: https://arxiv.org/abs/2607.24449
pdf_url: https://arxiv.org/pdf/2607.24449
published: '2026-07-27'
collected: '2026-07-28'
category: RAG
direction: 垂直领域RAG评测 · 法律行政场景
tags:
- RAG
- Legal Benchmark
- Dense Retrieval
- LLM Evaluation
- Domain LLM
one_liner: 发布法国移民法场景公开RAG评测基准，验证检索增强可有效提升行政指引准确率
practical_value: '- 垂直领域RAG效果验证可参考「参数LLM基线+不同规模模型RAG对照」的实验设计，快速定位检索增益边界

  - 结构化输出类RAG任务（如电商合规审核、准入资质推荐）可复用「分类准确率+召回覆盖率+引用可信度」多维度评估框架

  - 小样本标注垂直场景下，可优先测试dense retrieval增强方案，用低成本方法快速提升任务准确率'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有法律AI基准未覆盖法国国际招聘对应的移民法行政指引场景，纯LLM生成行政建议易出现幻觉，无法满足合规性要求。
### 方法关键点
1. 发布公开评测基准，覆盖居留许可类型推荐、所需材料召回、法律引用覆盖三类核心任务，包含52条标注完成的合成用户profile
2. 对比两类方案在Qwen3.5-9B、Qwen3.5-27B两个模型尺度的效果：无检索的纯参数LLM基线、dense retrieval增强的RAG方案
### 关键结果数字
两个尺度模型加入检索增强后，三类任务的行政指引效果均有提升，其中许可类型分类准确率提升幅度最大，验证了检索grounding对垂直领域高可靠RAG系统的必要性
