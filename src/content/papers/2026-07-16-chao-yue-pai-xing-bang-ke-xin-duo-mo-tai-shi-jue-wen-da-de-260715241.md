---
title: 'Beyond the Leaderboard: Design Lessons for Trustworthy Multimodal VQA'
title_zh: 超越排行榜：可信多模态视觉问答的设计经验
authors:
- Sushant Gautam
- Vajira Thambawita
- Michael A. Riegler
- Pål Halvorsen
- Steven A. Hicks
affiliations:
- SimulaMet, Norway
- Simula Research Laboratory, Norway
- Oslo Metropolitan University, Norway
arxiv_id: '2607.15241'
url: https://arxiv.org/abs/2607.15241
pdf_url: https://arxiv.org/pdf/2607.15241
published: '2026-07-16'
collected: '2026-07-19'
category: Multimodal
direction: 多模态大模型 · 可信性设计与评估
tags:
- Multimodal VQA
- PEFT
- LoRA
- Explainable AI
- Robust Evaluation
- Data Governance
one_liner: 基于医疗VQA竞赛9套系统复盘，给出可信多模态模型设计、评估与治理的实操经验
practical_value: '- 多模态推荐/多模态Agent落地时，不能只看准确率指标，必须补充可解释性、推理一致性校验，比如电商商品图文问答场景需校验回答和商品信息的对齐度，避免高准确率下的幻觉问题

  - 用LoRA/QLoRA等PEFT方案微调预训练多模态大模型时，可加入结构化推理约束（如强制输出证据溯源链），相比单纯刷点的方案泛化性、可信度更高，适配异质性用户query场景

  - 多模态系统上线前需做轻量鲁棒性、校准度校验，同时做好数据泄露防控，避免训练集泄露导致线上效果大幅跳水，该逻辑也适配搜索推荐小样本微调场景'
score: 4
source: arxiv-cs.CL
depth: abstract
---

### 动机
医疗多模态AI需要兼顾性能和可解释性，但现有竞赛通常仅靠排行榜准确率排名，无法反映模型落地的真实可信性，缺乏设计选择与推理质量的关联分析。

### 方法关键点
以MediaEval Medico 2025胃肠道内窥镜VQA竞赛为测试集，复盘9套参赛系统的设计选择，对比参数高效微调、结构化推理、显式证据grounding等方案在准确率、推理忠实度上的表现。

### 关键结果
1. 基于预训练backbone的PEFT（如LoRA）微调可拿到很高的竞赛准确率，但答案层面的指标提升不代表推理的忠实性和完整性；
2. 强制结构化推理+显式证据grounding的方案，在异质性问题下表现更稳定；
3. 现有基于词汇重叠的评估指标不足以衡量可信性，需补充证据关联解释、鲁棒性校准校验、泄露感知数据治理流程。
