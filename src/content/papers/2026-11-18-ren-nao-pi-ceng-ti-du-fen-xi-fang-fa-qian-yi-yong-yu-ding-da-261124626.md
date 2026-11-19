---
title: Transferring an analysis of human brain organization to language models
title_zh: 《人脑皮层梯度分析方法迁移用于定位大语言模型可迁移功能区域》
authors:
- Donghyeok Lee
- Sangwon Yu
- Sangkwon Park
- Hye Youn Park
- Munyoung Chang
- Sungroh Yoon
affiliations:
- Seoul National University
- Upstage AI
- Seoul National University Bundang Hospital
- Seoul National University College of Medicine
arxiv_id: '2611.24626'
url: https://arxiv.org/abs/2611.24626
pdf_url: https://arxiv.org/pdf/2611.24626
published: '2026-11-18'
collected: '2026-11-19'
category: LLM
direction: 大语言模型 · 功能区域定位与权重嫁接
tags:
- LLM
- model grafting
- functional localization
- diffusion map embedding
- reasoning enhancement
one_liner: 借鉴人脑皮层梯度分析定位LLM推理功能层，无训练嫁接即可提升目标模型推理能力
practical_value: '- 针对特定业务能力（如推荐场景用户意图推理、电商规则计算）微调的模型，可借鉴梯度分析方法定位核心功能层段，无需全量重训，仅嫁接对应层即可低成本为现有业务模型注入目标能力，大幅节省训练与适配成本

  - 跨模型能力迁移时优先选择核心功能层段嫁接，相比随机层段可保留90%+原有业务能力（如原有推荐排序准确率、文案生成符合度），避免全量替换带来的效果波动

  - 领域专用LLM（如电商客服Agent、商品合规审核模型）可复用该方法定位领域能力承载层，可在不破坏原有领域能力的前提下，嫁接通用推理层提升复杂问题解决能力'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM能力迁移多依赖全量微调、LoRA适配，成本高且易破坏原有模型已成熟的业务能力，人脑皮层发育中功能区域随能力提升逐步分化的规律，可为LLM内部功能区域定位提供可迁移的分析框架，解决低成本、低干扰的跨模型能力迁移需求。

### 方法关键点
- 借鉴人脑皮层梯度分析流程，用CKA计算LLM每层各模块（注意力、FFN各子层）激活的相似度矩阵，替代脑功能连接矩阵，经扩散映射嵌入得到层间表征梯度
- 对比基座模型与推理微调模型的梯度位移，定位位移峰值对应的连续层段（即推理相关功能区域，占总层数15%~35%）
- 无需额外训练，直接将该层段权重嫁接至同架构的指令微调/领域专用模型中

### 关键结果
跨Ministral、Qwen、Llama三个模型族6个不同参数规模的模型测试：
- 嫁接后数学推理准确率平均提升3.2pp（MATH-87）、4.2pp（AIME2024）、5.1pp（AIME2025），收益随嫁接层与核心功能区的重叠度提升而升高
- 核心功能层嫁接保留91.9%的原有正确答案，远高于随机层嫁接的82.2%
- 方法可扩展到领域模型：医疗模型的功能层嫁接可提升MedQA准确率6.4pp，嫁接通用推理层时可保留91%的原有医疗问答正确率

**最值得记住的一句话**：LLM的特定能力往往集中在少数连续层段，通过表征梯度分析定位后直接嫁接，可实现低成本、低干扰的跨模型能力迁移。
