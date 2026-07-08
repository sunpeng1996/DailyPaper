---
title: 'MANCE: Manifold Aware Concept Erasure'
title_zh: MANCE：流形感知的概念擦除方法
authors:
- Matan Avitan
- Yoav Goldberg
- Yanai Elazar
affiliations:
- Bar-Ilan University
- Allen Institute for Artificial Intelligence
arxiv_id: '2607.03973'
url: https://arxiv.org/abs/2607.03973
pdf_url: https://arxiv.org/pdf/2607.03973
published: '2026-07-03'
collected: '2026-07-08'
category: LLM
direction: LLM表示编辑 · 概念擦除
tags:
- Concept Erasure
- Manifold Learning
- Representation Editing
- LLM Alignment
- Multimodal
one_liner: 提出流形约束假设与MANCE系列方法，在119个多模态设置下实现SOTA非线性概念擦除
practical_value: '- 推荐系统用户画像去偏场景：擦除性别、年龄等敏感属性时可复用流形投影思路，避免破坏用户兴趣核心表示，降低公平性优化对推荐精度的负面影响

  - LLM/Agent对齐场景：做敏感概念、有毒内容擦除时，可直接复用MANCE++的「闭形式预擦除+迭代流形更新」架构，比全空间更新的表示损伤更低，无需全量重训

  - 多模态商品召回场景：CLIP特征去偏（如消除服饰推荐中的肤色、性别刻板印象）可将MANCE集成到特征后处理模块，仅需少量自然样本估计流形，落地成本低'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：概念擦除需移除表示中指定目标概念同时保留其余信息，但现有全空间更新方案易破坏与目标相关的其他有效特征，导致表示可用性下降
**方法关键点**：1. 提出流形约束假设（MCH）：自然表示集中在低维结构化流形上，干预操作约束在流形内可大幅降低对其他信息的损伤；2. 实现MANCE方法：基于目标概念分类器梯度信号迭代更新表示，将更新向量投影到用自然输入预估计的流形空间；3. 推出MANCE+/MANCE++：前置闭形式擦除步骤再执行MANCE，优化概念泄漏-操作精确性的tradeoff
**关键结果数字**：在119个跨文本、视觉的测试设置（覆盖13个LLM、3个NLP概念、40个CelebA-CLIP属性）上验证，MANCE叠加原有方法可稳定降低概念泄漏，MANCE++达到非线性概念擦除SOTA
