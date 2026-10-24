---
title: 'From Structured Records to Patient Narratives: Preserving Clinical Alignment
  in LLM-Generated Health Summaries'
title_zh: 结构化临床记录转患者可读叙事：LLM生成健康摘要的临床一致性保留
authors:
- Bayram Ayadi
- Florian Geissler
- Johanna Schmidhuber
affiliations:
- University of Passau, Germany
- Fraunhofer Institute for Cognitive Systems IKS, Munich, Germany
arxiv_id: '2610.31467'
url: https://arxiv.org/abs/2610.31467
pdf_url: https://arxiv.org/pdf/2610.31467
published: '2026-10-22'
collected: '2026-10-24'
category: Other
direction: LLM生成摘要 · 事实性约束优化
tags:
- RAG
- LLM
- Constrained Generation
- Factuality
- Summarization
one_liner: 提出结合RAG与结构化证据约束的生成框架，提升LLM生成健康摘要的临床一致性
practical_value: '- 做结构化数据转自然语言的C端生成场景（如电商用户消费报告、物流通知文案）时，可复用「结构化证据约束+RAG」的双重校验框架，降低生成内容事实漂移风险

  - 面向C端的生成式文案优化，可参考多维度评估逻辑：同时校验事实一致性、关键信息保留度、可读性三个维度，做针对性trade-off调优

  - 对生成内容不确定性保留要求高的场景（如预售到货时间提醒、风险告知文案），可引入prompt级显式约束，提升不确定性信息的传递准确率'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
可穿戴健康设备产生的大量结构化生理记录，转译为患者易懂的自然语言时，LLM简化表达过程易出现语义漂移，扭曲临床精准含义，存在用户误导风险。
### 方法关键点
面向经期健康监测场景，构建prompt驱动的约束生成框架，融合结构化证据硬约束与RAG检索证据校验双重机制；采用NLI语义对齐、原子事实性、可读性三类指标体系评估生成效果。
### 关键结果数字
在3款LLM、4500份生成摘要测试集上，显式grounding约束稳定提升临床一致性：其中不确定性信息保留能力提升最显著，基于检索证据做事实性校验时，整体事实性保持或提升，信息遗漏问题的改善效果随模型不同存在差异；临床一致性提升会伴随可读性下降、专业术语占比升高的trade-off效应。
