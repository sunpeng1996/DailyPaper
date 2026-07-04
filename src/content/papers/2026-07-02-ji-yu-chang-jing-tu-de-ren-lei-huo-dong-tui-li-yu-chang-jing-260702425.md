---
title: 'Learning to Evolve Scenes: Reasoning about Human Activities with Scene Graphs'
title_zh: 基于场景图的人类活动推理与场景演化建模
authors:
- Francesca Pistilli
- Simone Alberto Peirone
- Giuseppe Averta
affiliations:
- Politecnico di Torino
arxiv_id: '2607.02425'
url: https://arxiv.org/abs/2607.02425
pdf_url: https://arxiv.org/pdf/2607.02425
published: '2026-07-02'
collected: '2026-07-04'
category: Reasoning
direction: 具身AI · 场景图时序动态推理
tags:
- Scene Graph
- Temporal Reasoning
- Embodied AI
- Video Understanding
- Graph Neural Network
one_liner: 构建扩展Ego4D的时空场景图标注集SG-Ego，提出图模型GLEN实现活动驱动的场景动态结构化推理
practical_value: '- 电商内容理解场景可复用时空场景图的三元组构建逻辑，对用户直播/短视频中的交互行为做结构化建模，提升行为召回准确率

  - 具身导购Agent可借鉴GLEN的活动-场景对齐思路，基于用户当前动作预测后续场景状态变化，主动推送匹配的商品/服务

  - 短视频内容推荐的推理场景可迁移图编辑预测任务思路，将用户行为驱动的内容演化拆解为结构化变换序列，提升长序列推荐可解释性'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有第一人称视频理解方法多依赖隐式视觉/语言对齐表征，缺乏对场景动态的结构化推理能力，无法支撑对人-环境交互的可解释认知。

### 方法关键点
1. 发布SG-Ego数据集，扩展Ego4D新增时空场景图标注，将时序关系三元组整合为场景状态的显式演化描述
2. 推出图模型GLEN，基于场景图序列实现文本动作对齐与时序演化建模
3. 定义新任务A-GEF（活动驱动的图编辑预测），将场景动态建模为当前动作条件下的结构化变换序列

### 关键结果
GLEN在EgoMCQ、EgoCVR等检索基准，EXPLORE-Bench、A-GEF等长时序推理基准上性能优于原始视频基线，在原本仅MLLM能处理的推理场景表现突出，同时具备可解释的场景动态预测能力。
