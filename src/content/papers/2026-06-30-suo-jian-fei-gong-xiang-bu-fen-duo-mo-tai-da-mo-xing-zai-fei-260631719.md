---
title: 'Seeing Is Not Sharing: Some Vision-Language Models Overestimate Common Ground
  in Asymmetric Dialogue'
title_zh: 所见非共享：部分多模态大模型在非对称对话中高估共识
authors:
- Nan Li
- Albert Gatt
- Massimo Poesio
affiliations:
- Utrecht University
arxiv_id: '2606.31719'
url: https://arxiv.org/abs/2606.31719
pdf_url: https://arxiv.org/pdf/2606.31719
published: '2026-06-30'
collected: '2026-07-01'
category: Multimodal
direction: 多模态大模型 · 对话共识推理
tags:
- VLM
- Dialogue Grounding
- Common Ground
- Multimodal Bias
- Asymmetric Dialogue
one_liner: 揭示VLMs在非对称协作对话中易将潜在共享信息误判为已达成共识的认知偏差
practical_value: '- 开发电商多模态导购/客服Agent时，不能默认用户对商家侧展示的商品、活动信息已达成共识，需设置交互确认环节明确共识后再推进流程，降低需求误判率

  - 搭建多模态RAG系统时，需明确区分「系统侧已知信息」和「已与用户确认过的共识信息」，两类信息在prompt中做标记区分，减少幻觉输出

  - 对话式推荐的特征体系中可新增共识状态埋点特征，不要仅依赖静态商品/内容特征推断需求，需结合对话历史的确认链路动态调整推荐策略'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
协作场景下的非对称对话中，共享感知不等于共识理解，需通过交互grounding建立共有知识，现有VLMs能否区分「潜在共享信息」和「已确认共识信息」尚未明确。
### 方法关键点
基于HCRC MapTask对话数据集的13077条标注指代表达构造解释匹配任务，系统控制对话上下文、地图信息接入形式（真实图像/文本描述/无意义图像），对5款不同架构的VLMs开展对照评估。
### 关键结果数字
1. 接入真实地图图像时模型整体性能提升，但对齐预测过估偏差上升，非对齐案例准确率下降12%~21%；
2. 同款地图的文本描述也会复现该偏差，无意义图像则完全抑制对齐预测，偏差来源于任务相关内容而非视觉通道本身；
3. 模型普遍依赖静态内容线索而非对话历史的grounding过程追踪共识，该偏差在Qwen3-VL-8B-Instruct上表现最显著。
