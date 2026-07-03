---
title: Discrete Diffusion Language Models for Interactive Radiology Report Drafting
title_zh: 面向交互式放射科报告起草的离散扩散语言模型
authors:
- Max Van Puyvelde
- Halil Ibrahim Gulluk
- Wim Van Criekinge
- Olivier Gevaert
affiliations:
- Stanford University School of Medicine, Department of Biomedical Data Science
- Ghent University, Department of Mathematical Modelling, Statistics & Bioinformatics
- Stanford University, Department of Electrical Engineering
arxiv_id: '2607.01436'
url: https://arxiv.org/abs/2607.01436
pdf_url: https://arxiv.org/pdf/2607.01436
published: '2026-06-30'
collected: '2026-07-03'
category: LLM
direction: 大语言模型 · 离散扩散生成范式优化
tags:
- Discrete Diffusion
- MoE
- LoRA
- Autoregressive Generation
- Multimodal LLM
one_liner: 适配MoE离散扩散大模型，在医学VQA任务上性能超同体量AR模型，解码快3.5-4.4倍且支持任意顺序补全
practical_value: '- 可参考MoE离散扩散LLM的双向解码架构，优化文案生成类Agent的任意位置补全能力，适配电商详情页、广告文案的局部修改需求

  - 离散扩散LLM解码速度比同体量AR模型高3.5-4.4倍的结论，可作为生成式推荐、文案生成类任务的基座选型参考，降低推理延迟

  - 同类模型对比时统一LoRA微调配方、采用鲁棒LLM做裁判的评估方法，可复用到生成式推荐、广告文案生成的效果评测流程中'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
当前医疗领域大模型几乎全部采用自回归（AR）生成范式，存在无法灵活补全文本片段、解码速度慢等问题，离散扩散语言模型在通用文本任务上已证明性能可比肩同体量AR模型，但未在垂直领域完成落地验证。
### 方法关键点
1. 适配MoE结构的离散扩散语言模型DiffusionGemma-26B，与同体量AR模型Gemma-4-26B采用完全相同的LoRA微调配方，在医学视觉问答（VQA）数据集上开展基准测试
2. 采用对文本冗长程度鲁棒的LLM裁判做效果评估，消除文本长度偏差对评分的影响
### 关键结果
扩散模型在所有测试集上性能持平或超过AR模型，微调后激活参数仅3.8B，性能可对标前沿多模态大模型，解码速度比AR模型快3.5-4.4倍；额外具备AR模型没有的任意顺序填充能力，支持用户固定局部片段后补全剩余内容，适配交互起草场景需求。
