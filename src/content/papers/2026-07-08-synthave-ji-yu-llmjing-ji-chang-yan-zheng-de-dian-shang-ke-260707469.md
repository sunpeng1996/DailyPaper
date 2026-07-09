---
title: 'SynthAVE: Scalable Synthetic Labeling for E-Commerce with LLM-Arena Validation'
title_zh: SynthAVE：基于LLM竞技场验证的电商可扩展合成标注方案
authors:
- Andrea Scarinci
- Virginia Negri
- Brayan Impata
- Suleiman Khan
- Victor Martinez
- Marcello Federico
affiliations:
- Amazon
arxiv_id: '2607.07469'
url: https://arxiv.org/abs/2607.07469
pdf_url: https://arxiv.org/pdf/2607.07469
published: '2026-07-08'
collected: '2026-07-09'
category: Eval
direction: LLM数据标注 · 电商属性提取
tags:
- Synthetic Labeling
- LLM-as-Judge
- E-commerce
- Attribute Extraction
- Multi-LLM Ensemble
one_liner: 通过多模型多prompt的LLM竞技场做合成标签质检，与人类专家一致性达95.2%，单样本成本仅0.02美元
practical_value: '- 电商属性标注、商品信息质检场景可直接复用多LLM+多样prompt的竞技场框架：选择7款不同厂商的LLM搭配3套差异化prompt，通过多数投票生成标签，能达到95%+的人工一致性，成本仅为人工标注的1/5~1/20

  - 标注流程可优化为分层质检：21个法官全一致的样本直接使用（准确率100%），仅<50%同意的低一致样本送人工审核，能大幅降低标注成本，尤其适合多语言、多品类的大规模标注场景

  - LLM法官选型可参考论文资质门槛：优先选LiveBench得分≥70%、任务专项准确率达标、输出自洽性高、指令遵循好的模型，优先保证模型家族多样性而非prompt多样性，可最大化误差抵消效果

  - 成本敏感场景可选用精简配置：仅用Top3模型家族配3套prompt，成本可降低91%，准确率损失可通过分层质检弥补'
score: 9
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
电商属性提取模型的训练需要覆盖数千品类、属性、多语言的标注数据，组合规模可达数百万条，人工标注成本极高。现有LLM生成合成标注的方案缺少规模化质检机制，合成数据的错误会导致下游模型评测失真，亟需低成本、高一致性的标注质量验证方案。

### 方法关键点
- 合成数据生成：从电商Catalog采样覆盖西/法/意/德4语、229个品类的12726件商品，基于控制生成方法生成CORRECT/INCORRECT/UNKNOWN三类属性标注，保证每个商品对应唯一目标属性和值槽。
- LLM竞技场框架：选择7个不同厂商的LLM家族（Claude 3.5、Amazon Nova、GPT OSS等），搭配3套结构/逻辑完全不同的prompt（直接指令、XML结构化带示例、角色带指南），组成21个独立法官配置，每个样本由所有法官独立打分后通过多数投票生成最终标签。
- 标注校准机制：仅当合成标注与竞技场多数投票不一致时送人工审核，一致样本直接使用，大幅降低人工工作量。

### 关键结果
- 竞技场多数投票与人类专家一致性达95.2%，Cohen’s κ=0.92，单样本标注成本仅0.02美元；可修正83.1%的合成标注错误，坏标签检测的F1达96.6%。
- 21个法官全一致的样本准确率达100%，>85%同意的样本准确率达98.8%，仅1.4%的低一致样本需要人工审核。
- 跨4语言表现稳定，准确率区间94.0%~96.4%，错误中80.5%为UNKNOWN类的混淆，直接对错混淆占比极低。

### 核心结论
不同厂商、不同bias的LLM法官的多样性远重于单个模型的精度，多模型集成可通过误差抵消实现远超单模型的标注准确率，以极低的成本逼近人工标注质量。
