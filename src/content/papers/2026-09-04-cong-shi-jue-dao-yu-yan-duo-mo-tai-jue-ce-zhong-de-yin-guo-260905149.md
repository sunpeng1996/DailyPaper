---
title: 'From Vision to Language: Investigating Causal Information Flow in Multimodal
  Decision-Making'
title_zh: 从视觉到语言：多模态决策中的因果信息流研究
authors:
- Davide Testa
- Hugh Mee Wong
- Alessandro Lenci
- Bernardo Magnini
- Albert Gatt
affiliations:
- Fondazione Bruno Kessler (FBK)
- Università di Roma La Sapienza
- Utrecht University
- University of Pisa
arxiv_id: '2609.05149'
url: https://arxiv.org/abs/2609.05149
pdf_url: https://arxiv.org/pdf/2609.05149
published: '2026-09-04'
collected: '2026-09-07'
category: Multimodal
direction: 多模态大模型 · 跨模态因果推理分析
tags:
- VLM
- Causal Intervention
- Multimodal Reasoning
- Information Flow
- Visual Grounding
one_liner: 通过分层因果干预揭示视频文本多模态决策中视觉信息向语言决策的流动规律
practical_value: '- 做电商短视频多模态检索/分类任务时，可在候选query/答案处理阶段强化视觉特征注入，提升VLM决策准确率

  - 跨模态商品语义对齐场景可将名词作为核心锚点，时序类任务（如商品使用步骤识别）重点优化动词的跨模态关联

  - 多模态时序推理任务需同时优化视频帧序列建模与时序文本表达去偏，降低语言偏置对最终效果的干扰'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有VLM评估仅关注最终预测结果，无法追溯视觉信息对语言类决策的贡献机制，难以定位多模态推理的性能短板根因。
### 方法关键点
针对视频类生成式多选任务，对视频-文本注意力通路执行分层因果干预，覆盖空间、因果、时序三类视觉推理场景，精准追踪跨模态信息的流动路径与作用阶段。
### 关键结果
1. 视觉信息主要在模型处理候选答案阶段完成融合，候选答案是最终决策的核心文本锚点；
2. 名词是多模态信息增强的核心语义锚，动词在时序关系处理中作用更显著；
3. VLM时序推理性能短板既来自跨帧序列信息建模缺陷，也和时序表达的固有语言偏置相关。
