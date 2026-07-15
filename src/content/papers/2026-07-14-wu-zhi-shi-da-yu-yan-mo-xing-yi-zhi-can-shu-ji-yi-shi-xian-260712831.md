---
title: 'Knowledgeless Language Models: Suppressing Parametric Recall for Evidence-Grounded
  Language Modeling'
title_zh: 无知识大语言模型：抑制参数记忆实现基于证据的语言建模
authors:
- Roi Cohen
- Yvan Carré
- Nick Lechtenbörger
- Hendrik Droste
- Lucas Kerschke
- Russa Biswas
- Gerard de Melo
- Jan Buys
arxiv_id: '2607.12831'
url: https://arxiv.org/abs/2607.12831
pdf_url: https://arxiv.org/pdf/2607.12831
published: '2026-07-14'
collected: '2026-07-15'
category: Training
direction: LLM预训练优化 · 低幻觉证据导向
tags:
- LLM Pretraining
- Hallucination Reduction
- RAG
- Parametric Knowledge
- Evidence Grounded
one_liner: 通过预训练匿名化命名实体，得到低参数记忆依赖、高上下文证据敏感度的低幻觉大模型
practical_value: '- 电商客服、商品问答等RAG场景可选用KLLM作为基座，大幅降低参数记忆中过时商品信息、错误活动规则导致的幻觉，比普通LLM适配性更高

  - 导购Agent等需调用检索工具的场景，用KLLM做推理基座，可减少参数记忆优先级高于工具返回结果的问题，在证据不完善时鲁棒性更强

  - 商品文案生成、生成式推荐场景，将KLLM绑定给定的商品属性、合规规则作为上下文，可大幅降低模型编造虚假参数、违规宣传内容的风险'
score: 8
source: arxiv-cs.CL
depth: abstract
---

### 动机
LLM参数存储的大量事实知识易过时、不全、与给定上下文冲突，会引发幻觉等不可靠行为，现有RAG等方案无法彻底解决模型优先信任参数记忆的问题。
### 方法关键点
提出KLLM全新预训练范式，预训练语料中对所有命名实体做匿名化处理，切断实体关联的事实知识监督通道，系统性引导模型认知行为从依赖参数记忆转向依赖给定上下文证据推理。
### 关键结果
- 闭卷事实回忆能力大幅降低，上下文问答、事实校验、幻觉检测任务在多模型尺度下均优于匹配基线
- 证据不完善的检索增强场景下，相对标准LLM获得20-25%的相对增益
- 校准能力更优，ECE、Brier分数、AUROC均有提升，拒答行为更可靠
