---
title: Learning Complementary Action Modeling from Automotive Maintenance Instructions
title_zh: Learning Complementary Action Modeling from Automo
authors:
- Jiaqi Wu
- Bai Li
- Jochen Hartmann
- Martin Gaedke
- Sander Stuijk
arxiv_id: '2606.27808'
url: https://arxiv.org/abs/2606.27808
pdf_url: https://arxiv.org/pdf/2606.27808
published: '2026-06-26'
collected: '2026-06-29'
category: RAG
direction: RAG
tags:
- RAG
- LLM
one_liner: A minute lexical variation can reverse the procedural meaning of an instruction
  even when the r...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 8
source: arxiv-cs.CL
depth: abstract
---

### 摘要

A minute lexical variation can reverse the procedural meaning of an instruction even when the rest of the sentence remains unchanged. In automotive maintenance instructions, this pattern often appears when an action phrase turns an instruction into its procedural counterpart. The entities, modifiers, and surrounding context remain largely invariant, while the action phrase determines the procedural relation. We define this task as Complementary Action Modeling (CAM). Given a maintenance instruction, the goal is to identify or generate its procedural counterpart by modifying the action phrase while preserving the remaining sentence context. This task focuses on three aspects: distinguishing complementarity from surface similarity, controlling generation at the action-phrase level, and evaluating relational correctness using retrieval, overlap-based, and human evaluation. Using a German automotive maintenance dataset, we examine these questions through candidate matching and controlled Seq2Seq generation. The results show that complementary maintenance instructions are best modeled as procedural associations grounded in subtle lexical cues. They should therefore not be treated as ordinary cases of sentence similarity or synonym-based paraphrasing.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。
