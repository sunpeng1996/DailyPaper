---
title: 'Decompose, Estimate, Select: Coverage-Aware Context Construction for Long-Form
  RAG'
title_zh: 分解、预估、选择：面向长文本RAG的覆盖感知上下文构建方法
authors:
- He Tu
- Aleena Bosco Kurumthottam
- Torsten Suel
affiliations:
- New York University Shanghai
- New York University
arxiv_id: '2610.40314'
url: https://arxiv.org/abs/2610.40314
pdf_url: https://arxiv.org/pdf/2610.40314
published: '2026-10-29'
collected: '2026-10-30'
category: RAG
direction: 长文本RAG · 覆盖感知上下文优化
tags:
- RAG
- Long-Form Generation
- Context Selection
- Query Decomposition
- Self-Feedback
one_liner: 提出覆盖感知RAG检索流水线与无额外检索自反馈环，提升长文本回答覆盖度
practical_value: '- 电商场景商品QA、长文案生成类RAG可直接复用覆盖感知上下文选择逻辑，通过查询分解+子问题-文档覆盖度矩阵+贪心选档，在有限上下文窗口下覆盖更多用户关注的商品维度，避免冗余信息占用配额

  - 复用无额外检索的自反馈环设计，先让LLM自我批判首次回答未用到的有效信息再二次生成，可低成本提升长生成任务（如商品评测、活动规则说明）的信息完整性，实测Vstrict提升0.086，仅损失少量精度

  - 多意图搜索召回可借鉴覆盖训练bi-encoder的负样本构造思路，加入冗余负样本（仅覆盖已命中子问题的文档），让召回模型同时学习相关性与信息增量

  - 长文本生成业务无需盲目追求检索覆盖度，实验证明检索侧覆盖度提升不一定能转化为生成侧答案覆盖度，上下文利用率才是核心瓶颈，同等预算下优先优化生成侧信息利用效率ROI更高'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统RAG基于相关性的检索易返回大量冗余信息，忽略复杂查询多维度的信息覆盖需求，尤其长文本生成场景下，有限上下文窗口被重复信息占用，导致回答缺漏关键信息；过往方法单纯提升检索侧覆盖度，忽略LLM对上下文的实际利用率，检索侧增益无法转化为回答质量提升。
### 方法关键点
- 检索pipeline：用LLM将复杂查询分解为10个独立子问题，通过覆盖训练的bi-encoder重排BM25召回的top100候选，再用cross-encoder预测文档×子问题的覆盖度矩阵，最终用贪心最大边际覆盖算法选择topK文档，优先筛选能覆盖更多未覆盖子问题的文档
- 自反馈生成环：无需额外检索，基于相同的已选上下文，让LLM先自我批判首次回答未充分利用的文档再二次生成，引导LLM充分利用已有上下文信息
- 训练策略：bi-encoder训练时加入冗余负样本（仅覆盖已命中子问题的文档），让模型学习判断文档的信息增量而非仅相关性；cross-encoder在85万条文档-子问题问答对数据上训练覆盖度预估
### 关键实验
在TREC RAG 2024数据集测试，检索侧α-nDCG@10从0.625提升到0.702，接近参考nugget上限0.718，且未损失相关性；生成侧加入2轮自反馈后，关键信息完整度Vstrict提升0.086，信息转移率提升0.065，仅损失0.042的句子精度。对比黄金oracle检索，即使检索侧覆盖度从0.799提升到0.888，生成侧答案覆盖度无显著提升，反而转移率更低。
### 核心结论
长文本RAG优化中，检索侧覆盖度提升不一定能转化为生成质量提升，上下文利用率才是核心瓶颈，优先优化生成侧信息利用效率比盲目提升检索覆盖度投入产出比更高
