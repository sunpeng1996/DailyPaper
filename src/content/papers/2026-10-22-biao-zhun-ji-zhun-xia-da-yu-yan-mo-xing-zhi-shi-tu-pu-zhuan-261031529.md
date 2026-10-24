---
title: An Empirical Study of Recent Large Language Models for Knowledge Graph to Text
  Generation on Standard Benchmarks
title_zh: 标准基准下大语言模型知识图谱转文本生成效果实证研究
authors:
- Priyanka
- Renaud Delbru
- Souhail Bakkali
- Mickaël Coustaty
- Antoine Doucet
affiliations:
- La Rochelle Université
- Siren
- Université de Rennes
arxiv_id: '2610.31529'
url: https://arxiv.org/abs/2610.31529
pdf_url: https://arxiv.org/pdf/2610.31529
published: '2026-10-22'
collected: '2026-10-24'
category: LLM
direction: LLM 知识图谱转文本效果评估
tags:
- KG-to-Text
- LLM Benchmark
- Evaluation Metric
- Text Generation
- Fine-tuning
one_liner: 基准测试KG转文本任务中LLM与微调编解码模型效果，验证两类评估指标的互补性
practical_value: '- 电商商品/商家KG转详情页、营销文案场景，可优先用prompted LLM替代传统微调编解码模型，多三元组场景下信息遗漏、事实矛盾错误更少

  - 评估KG驱动的文本生成效果时，不要仅依赖参考式指标，需叠加基于KG一致性的无参考LLM评估，可有效识别业务不可接受的事实错误

  - 若业务中KG规模波动大，优先选prompt LLM方案，相比微调模型鲁棒性更强，大KG下错误率上升速度更慢'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
传统KG转文本任务长期以微调编解码模型为标准方案，近年LLM能力快速提升，但缺乏系统的效果对比与评估方法有效性验证。
### 方法关键点
覆盖decoder-only、MoE、编解码、闭源GPT等5类不同架构的主流LLM，在WebNLG标准KG数据集上，同时采用参考式指标、经人工标注校准的KG一致性无参考LLM评估，对比微调编解码模型的生成效果。
### 关键结果
1. LLM在参考式指标上已大幅缩小甚至部分场景追平微调模型，在KG一致性指标上表现更优；
2. 两类评估指标相关性极低，分别捕捉生成质量的不同维度，仅用参考式指标会遗漏事实错误、信息遗漏等关键问题；
3. Prompted LLM的事实矛盾、三元组遗漏错误显著少于微调模型，且微调模型的错误随KG规模扩大的上升速度远高于LLM。
