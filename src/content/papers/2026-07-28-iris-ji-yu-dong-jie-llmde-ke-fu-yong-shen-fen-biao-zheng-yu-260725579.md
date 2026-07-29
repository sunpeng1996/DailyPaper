---
title: 'IRIS: Reusable Identity Representations from Frozen LLMs for Entity Alignment'
title_zh: IRIS：基于冻结LLM的可复用身份表征用于实体对齐
authors:
- Xinran Liu
- Shengtao Li
- Shouqian Shi
- Ge Wang
- Xin-Wei Yao
affiliations:
- 南京大学
arxiv_id: '2607.25579'
url: https://arxiv.org/abs/2607.25579
pdf_url: https://arxiv.org/pdf/2607.25579
published: '2026-07-28'
collected: '2026-07-29'
category: LLM
direction: LLM实体表征 · 跨KG实体对齐
tags:
- Entity Alignment
- Frozen LLM
- Identity Representation
- Knowledge Graph
- Training-free
one_liner: 提出训练无关的IRIS框架，从冻结LLM提取实体稳定身份表征实现跨知识图谱高效实体对齐
practical_value: '- 电商跨平台商品/商家对齐场景可复用IRIS思路，无需微调LLM即可生成跨域统一实体身份表征，大幅降低对齐成本

  - 推荐系统异构知识图谱融合时，可直接用冻结LLM生成实体语义签名做相似度匹配，避免逐对KG训练定制表征模型

  - Agent调用多来源知识库时，可预生成各实体的稳定身份表征，无需重复调用LLM做候选匹配，降低推理延迟'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：传统实体对齐方法依赖显式图结构与文本字段，语义理解能力不足，难以识别异构描述下的相同实体、区分语义相似的不同实体；现有LLM驱动的对齐方法未将语义能力蒸馏为稳定可比的身份空间，依赖特定KG对或候选集，上下文变化时需重复处理。

**方法关键点**：训练无关的IRIS框架直接从冻结LLM抽取身份导向的上下文表征，为每个实体生成类似虹膜的唯一稳定签名，构建统一共享表征空间：实体仅需编码1次，即可跨不同KG直接做相似度比对，无需依赖KG对的定制表征训练、也无需逐候选调用LLM推理。

**关键结果**：在4个主流实体对齐基准、2种冻结LLM骨干上测试，最优IRIS变体在D-Y-15K V2、DBP-WIKI、ICEWS-WIKI、ICEWS-YAGO数据集上Hits@1分别达100.00、99.38、98.31、97.99。
