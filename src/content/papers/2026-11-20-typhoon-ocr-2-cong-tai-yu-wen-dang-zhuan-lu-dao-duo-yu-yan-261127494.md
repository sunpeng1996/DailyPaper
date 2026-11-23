---
title: 'Typhoon OCR 2: From Thai Document Transcription to Multilingual, Multi-Task
  OCR'
title_zh: Typhoon OCR 2：从泰语文档转录到多语言多任务OCR
authors:
- Surapon Nonesung
- Natapong Nitarach
- Sittipong Sripaisarnmongkol
- Kunat Pipatanakul
- Warit Sirichotedumrong
affiliations:
- Typhoon, SCB DataX
- AI Singapore
arxiv_id: '2611.27494'
url: https://arxiv.org/abs/2611.27494
pdf_url: https://arxiv.org/pdf/2611.27494
published: '2026-11-20'
collected: '2026-11-23'
category: Other
direction: 多语言多任务OCR · 小参数开源模型
tags:
- OCR
- Multimodal
- GRPO
- Document Understanding
- Open Source
one_liner: 推出0.8B/2B开源多语言多任务OCR，支持prompt驱动抽取与全页结构化解析，性能领先同类开源方案
practical_value: '- 跨境电商场景多语言小票/报关单/商品资质文档解析，可复用prompt驱动单模型完成识别+信息抽取的架构，替代OCR+LLM两步流程降低时延

  - 小参数垂域模型调优可复用GRPO强化学习+未完成响应惩罚规则，可大幅降低生成重复/断句问题，2B模型重复率从3.2%降至0.7%

  - 多语言小模型适配可参考方案：仅在垂域语言标注数据做SFT，可在保留原中英性能几乎不变的前提下，大幅提升垂域语言效果'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
原有Typhoon OCR 1.5仅支持泰语文本转录，无法满足实际场景中特定信息抽取、全页结构保留的需求，OCR后再接LLM抽取的两步流程冗余低效。
### 方法关键点
基于开源文档解析器基座，在标注泰语数据集+公开多语言数据集上做SFT，之后加入带任务奖励、未完成响应惩罚的GRPO强化学习微调，推出0.8B、2B两个小参数版本，单模型支持prompt切换信息抽取、全页结构化解析两类任务，覆盖泰、中、英三语言。
### 关键结果数字
2B版本在泰语MDPBench得分80.7（1.5版本仅68.9）、ThaiOCRBench得分59.91（1.5版本40.45），均为同类开源模型第一；中英指标几乎无下降，英文olmOCR-bench得分84.7（基座84.4）、中英混合OmniDocBench得分90.97（基座91.03）；GRPO将2B模型重复页占比从3.2%降至0.7%
