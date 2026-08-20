---
title: Evaluating Structured Information Extraction with Open Models in a High Risk
  Public Sector Application
title_zh: 高风险公共领域场景下开源模型结构化信息提取效果评估
authors:
- Elias Schubert
- Felix Bießmann
affiliations:
- Berlin University of Applied Sciences
- Einstein Center Digital Future
arxiv_id: '2608.18289'
url: https://arxiv.org/abs/2608.18289
pdf_url: https://arxiv.org/pdf/2608.18289
published: '2026-08-18'
collected: '2026-08-20'
category: Eval
direction: 结构化信息提取 · 大模型效果评测
tags:
- Structured Information Extraction
- OCR
- LLM
- VLM
- Benchmark
one_liner: 构建高风险公共领域文档处理基准，测评开源OCR、LLM、VLM的端到端结构化提取性能
practical_value: '- 处理电商资质审核、售后凭证、商家单据等非结构化材料时，可优先测试VLM方案，同时保留最优OCR+LLM组合作为成本平替

  - 结构化提取场景不要盲目堆大模型参数，参数规模与效果非线性相关，优先优化OCR输出的结构保留度ROI更高

  - 高准确率要求的业务场景（如支付凭证校验、资质审核）不要直接用零-shot开源模型，需叠加人工校验或few-shot微调提升可靠性'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有开源OCR、LLM、VLM生态快速成熟，但缺少真实场景下多步提取 pipeline 的系统评测，尤其EU AI Act定义的高风险领域缺乏可落地的模型选型参考。

### 方法关键点
构建高风险真实场景基准（国际留学项目学生申请材料处理任务），端到端测评35种SOTA开源OCR、LLM、VLM组合的结构化信息提取性能。

### 关键结果数字
VLM整体表现普遍优于OCR+LLM pipeline，但零-shot下所有开源模型可靠性均不足：仅4种配置F1超过0.5，75%的配置F1低于0.25；最优OCR+LLM组合效果可匹配顶级VLM；模型规模与性能非线性相关，OCR输出的结构保留度是独立于下游模型能力的关键影响因子。
