---
title: 'The Right Information Extraction Pipeline Depends on the Document: Accuracy-Energy
  Trade-offs for Small, Local Models'
title_zh: 按需选择信息提取管线：小规模本地模型的精度-能耗权衡
authors:
- Christoph Walser
- Mauricio Fadel Argerich
- Jonathan Fürst
affiliations:
- Zurich University of Applied Sciences, Switzerland
- Universidad Politécnica de Madrid, Spain
arxiv_id: '2609.31341'
url: https://arxiv.org/abs/2609.31341
pdf_url: https://arxiv.org/pdf/2609.31341
published: '2026-09-25'
collected: '2026-09-28'
category: Other
direction: 小模型本地部署 · 精度能耗权衡
tags:
- Information Extraction
- Small LLM
- VLM
- Energy Efficiency
- On-premise Deployment
one_liner: 针对隐私场景本地部署的≤8B小模型，给出不同文档类型下精度能耗最优的信息提取管线配置
practical_value: '- 电商资质审核、发票识别等批量隐私文档处理场景优先开启batching，可无精度损失降低38%-85%单页能耗，大幅削减算力成本

  - 文档处理管线按类型拆分：纯文本类（如商家协议、合规文本）用小参数纯文本LLM+传统OCR，富布局类（如发票、表单）用VLM，兼顾精度与成本

  - 低吞吐单请求场景优先采用FP8量化降本，批处理场景下量化收益有限可按需选择，避免不必要的精度损失'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
隐私敏感场景下信息提取（IE）无法使用云服务，需本地部署≤8B小模型，但不同布局的文档适配的IE管线差异大，缺乏可落地的精度-能耗权衡指南。
### 方法关键点
覆盖输入表示、模型族、推理配置3个维度，在近纯文本的Kleister-NDA合同数据集、富布局的VRDU表单数据集上，系统评测纯文本小模型、VLM的精度和能耗表现。
### 关键结果数字
1. batching是最高效的能耗优化手段，无精度损失下可降低单页能耗38%-85%；
2. 单请求场景下FP8量化可降低能耗27%-32%，批处理场景下收益降至9%-19%；
3. 神经OCR能耗是传统OCR的17倍，未达帕累托最优；
4. 纯文本场景下小纯文本模型+轻量解析器方案，精度、能耗均优于所有VLM配置。
