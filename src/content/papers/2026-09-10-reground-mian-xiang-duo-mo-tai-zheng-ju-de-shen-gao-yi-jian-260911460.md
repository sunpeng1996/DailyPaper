---
title: 'ReGround: Grounding Reviewer Comments in Multimodal Evidence'
title_zh: ReGround：面向多模态证据的审稿意见溯源数据集
authors:
- Serwar Basch
- Lizhen Qu
- Iryna Gurevych
affiliations:
- TU Darmstadt UKP Lab
- Hessian Center for AI (hessian.AI)
- Monash University
arxiv_id: '2609.11460'
url: https://arxiv.org/abs/2609.11460
pdf_url: https://arxiv.org/pdf/2609.11460
published: '2026-09-10'
collected: '2026-09-13'
category: RAG
direction: 多模态长文档证据溯源数据集与检索测评
tags:
- Multimodal_Retrieval
- Dataset
- Long_Document
- Evidence_Grounding
- RAG
one_liner: 构建万级规模审稿意见多模态证据溯源数据集，验证多模态信号对长文档检索的增益
practical_value: '- 构建长文档检索标注数据集时，可借鉴「利用用户/作者回复中的显式引用作为弱监督标注源」的思路，大幅降低标注成本，比如电商场景可从客服回复中提取用户问题对应商品详情页的证据

  - 长文档多模态RAG系统设计时，不要直接做全文档检索，可先做证据类型（文本段落/表格/图片）分类再分域检索，优先解决证据类型推理瓶颈，能有效提升召回准确率

  - 多模态检索任务中不能仅依赖OCR转写的文本信号，表格、图片的独立编码特征能提供纯文本缺失的互补信息，可单独设计模态召回分支再融合结果'
score: 4
source: arxiv-cs.CL
depth: abstract
---

**动机**：现有长文档证据溯源基准均面向显式信息查询场景，缺乏针对模糊非结构化意见（如审稿意见、用户反馈）锚定多模态证据的标注数据，无法支撑审稿辅助、长文档QA等场景的算法研发。
**方法关键点**：1. 基于「作者 rebuttal 中会显式标注审稿意见对应论文证据位置」的观察，通过弱监督方式构建数据集，无需人工标注即可获得高准确率的锚定关系；2. 数据集共覆盖3656篇匿名学术投稿的10267条审稿意见，关联16274条多模态证据（文本段落/表格/图片）；3. 将溯源任务建模为检索任务，对多种主流检索方案做了系统测评。
**关键结果**：全文档直接检索表现极差，证据类型推理是当前方案的核心瓶颈，引入多模态信号可提供纯文本检索缺失的互补信息，显著提升召回效果。
