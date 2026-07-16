---
title: 'Exploring Post-Training Alignment of Small Language Models for Biomedical
  Data-to-Text Generation: A Case Study of Medication Leaflet'
title_zh: 面向生物医学数据转文本的小语言模型训练后对齐研究：以药品说明书为例
authors:
- Xi Yang
- Guodong Liu
- Chuqin Li
- Fan Wu
- Ergin Soysal
- Min Jiang
- Xing He
- Jiang Bian
- Yi Guo
- Shams Zaman
affiliations:
- Eli Lilly and Company
- Indiana University
- Regenstrief Institute
- University of Florida
arxiv_id: '2607.13430'
url: https://arxiv.org/abs/2607.13430
pdf_url: https://arxiv.org/pdf/2607.13430
published: '2026-07-15'
collected: '2026-07-16'
category: Training
direction: SLM训练后对齐 · 数据到文本生成
tags:
- SLM
- Alignment
- SFT
- DPO
- ORPO
- GRPO
one_liner: 对比4种SLM对齐策略在药品说明书生成任务的效果，微调后SLM性能超过GPT-5
practical_value: '- 高保真合规生成场景（如电商商品详情页生成、广告合规文案生成），对齐策略优先选ORPO保障域内生成精度，GRPO保障跨场景泛化性，效果优于SFT/DPO

  - SFT/ORPO训练时可直接复用Prompt Loss Weighting（PLW）trick，按生成文本占比设置prompt部分损失权重，无需额外调参即可稳定提升生成质量

  - 结构化数据转文本场景无需盲目依赖商用大模型，7B量级SLM全参数微调后效果可超过GPT-5，支持本地部署，成本和可控性更优

  - 跨域零-shot生成场景下，GRPO不要使用域内SFT checkpoint初始化，直接用通用指令模型初始化可避免源域过拟合，泛化性提升更明显'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
结构化生物医学数据转患者友好的合规文本（如药品说明书）目前仍依赖人工生产，成本高、难规模化；SLM因计算成本低、支持本地部署，适配医疗隐私合规要求，但不同训练后对齐策略对生成保真度、跨域泛化性的影响缺乏系统性对比，无法指导落地选型。
### 方法关键点
- 对齐策略对比：覆盖SFT、DPO、ORPO、GRPO四种主流对齐方法，统一基于Qwen2.5系列SLM（0.5B/3B/7B）做公平对照
- 训练优化：引入Prompt Loss Weighting（PLW），根据生成文本占总token的比例设置prompt部分损失权重，适配SFT和ORPO训练
- 泛化性验证：构造跨监管体系的FDALeaflets数据集，测试模型在EMA到FDA监管规则分布偏移下的零-shot性能
- 多维度评估：结合lexical指标（ROUGE、METEOR）、语义相似度指标（STS、MoverScore）和LLM-as-Judge（adequacy、幻觉率等）综合评估
### 关键结果
- 域内测试：ORPO+PLW的7B模型STS达0.9752，比SFT基线高0.0093，比DPO高0.0141，所有微调SLM性能均超过GPT-5基线
- 跨域零-shot测试：通用指令初始化的GRPO 7B模型STS达0.9407，比ORPO高0.0228，比GPT-5高0.0112，泛化性最优
- QLoRA微调效果显著差于全参数微调，STS下降约0.04
### 核心结论
高保真结构化转文本场景下，对齐策略的选型影响远大于模型规模和预训练域适配，7B量级SLM全参数微调后效果可超越商用大模型
