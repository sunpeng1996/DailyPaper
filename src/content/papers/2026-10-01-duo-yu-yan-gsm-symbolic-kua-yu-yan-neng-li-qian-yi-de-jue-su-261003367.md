---
title: 'Multilingual GSM-Symbolic: What determines capability transfer across languages?'
title_zh: 《多语言GSM-Symbolic：跨语言能力迁移的决定因素研究》
authors:
- Kenneth Enevoldsen
- Riley Herchert
- Sofie Mosegaard
- Dan Saattrup Smart
- Simon Enni
- Isaac Chung
- Sofie Bruun
- Ayush Sunil Munot
- Max Müller-Eberstein
- Adnan El-Assadi
affiliations:
- Aarhus University
- Danish Foundation Models
- University of Alabama
- Alexandra Institute
- Syv.ai
arxiv_id: '2610.03367'
url: https://arxiv.org/abs/2610.03367
pdf_url: https://arxiv.org/pdf/2610.03367
published: '2026-10-01'
collected: '2026-10-05'
category: LLM
direction: 大语言模型 · 跨语言能力迁移评估
tags:
- Cross-lingual Transfer
- LLM Evaluation
- Reasoning
- Multilingual LLM
- Dataset
one_liner: 构建覆盖15种语言的符号化数学推理数据集，量化跨语言能力迁移的四大核心决定因素
practical_value: '- 跨境多语言电商/广告/推荐场景的LLM应用选型，优先选择大参数量+推理增强的模型，可大幅缩小低资源小语种和主流语言的性能差距

  - 多语言模型效果评估无需全量标注目标语言数据集，仅需10个目标语言符号模板即可将性能预测误差控制在4.2pp以内，大幅降低评估成本

  - 针对和中文语系差异极大的小语种场景，不要过度依赖增模型规模、加推理能力的通用优化手段，需额外补充针对性语料适配'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有跨语言能力迁移研究缺乏统一可比、不易过拟合的评估数据集，无法量化各影响因素的权重，低资源语言的模型性能优化无明确指导依据。
### 方法关键点
1. 构建Multilingual GSM-Symbolic数据集，覆盖15种语言、3万条匹配问答对，基于符号模板可生成百万级变体，避免模型过拟合；
2. 定量分析四大核心因素对跨语言迁移效果的影响权重，构建跨语言性能预测框架。
### 关键结果
- 模型大小（β=1.77）、语言资源量（β=0.77）、推理能力（β=0.67）为正向影响最大的三个因素，语言类型距离负向影响（β=-0.25）；
- 增大模型规模、增强推理能力可分别缩小高低资源语言性能gap 27%、20%，但对类型差异大的语言效果极弱；
- 预测框架可解释92%的跨语言性能差异，unseen语言性能预测误差仅6.0pp，加入10个目标语言模板后误差降至4.19pp。
