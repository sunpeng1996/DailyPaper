---
title: Principled Thoughts for Latent Recursive LLM Systems
title_zh: 面向隐式递归LLM系统的表示监督思想训练方法REST
authors:
- Fahd Seddik
- Fatemeh Fard
affiliations:
- University of British Columbia, FARD Lab
arxiv_id: '2609.36159'
url: https://arxiv.org/abs/2609.36159
pdf_url: https://arxiv.org/pdf/2609.36159
published: '2026-09-27'
collected: '2026-09-30'
category: Agent
direction: Agent 隐式递归推理训练优化
tags:
- Latent Reasoning
- MultiAgent
- LLM Training
- Auxiliary Loss
- REST
one_liner: 为隐式递归单/多智体LLM设计4属性监督损失，无推理额外开销，准确率最高提升7.5pp
practical_value: '- 电商多Agent导购/搜索推荐链路的跨Agent隐通信场景，无需修改推理架构，仅在训练阶段给隐状态传递环节加REST的4项辅助损失，即可提升跨Agent信息传递准确率，最高可获7.5pp的效果提升

  - 单Agent隐式推理优化（如Query意图理解、商品文案生成内部思考）优先引入minimality损失，过滤冗余输入信息，在降低推理token开销的同时提升效果；跨Agent通信场景优先引入causality损失，保障隐状态与原文本输出的分布一致性

  - 隐式递归系统的效果评估不能仅看最终输出准确率，需额外监控隐表示碰撞率、冗余信息占比指标，避免CE-only训练导致的隐表示坍缩引发的bad case'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前隐式递归LLM系统（单Agent自递归推理、多Agent跨Agent隐状态通信）仅依赖最终输出的Cross-Entropy（CE）损失训练，存在四大缺陷：隐状态替换文本时的分布偏差、隐状态保留大量无关输入信息、不同输入的隐表示坍缩碰撞、隐状态不保留模型输出分布的不确定性，递归层数或Agent数越多，准确率衰减越严重，且隐通信内容不可解释。
### 方法关键点
- 提出REST训练目标，将有效思想表示的4个核心属性（因果性、最小性、可分性、稳定性）转化为可微损失项，与CE损失加权相加，仅训练跨Agent/跨轮次的隐状态映射层，冻结基座LLM与内部隐状态映射层，推理阶段无架构改动、无新增参数。
- 同时支持单Agent自递归（模型复用自身隐状态做深度推理）、多Agent协作（Agent间通过隐状态传递信息，无需转文本）两大场景。
- 4项损失分别对应解决CE-only的四大缺陷：因果性损失约束隐状态与原文本输出的分布一致性，最小性损失约束隐状态丢弃无关输入信息，可分性损失约束不同输入的隐表示互不碰撞，稳定性损失约束隐状态保留模型输出的分布不确定性。
### 关键结果
覆盖数学、科学、医学、代码生成共7个基准数据集，相同训练数据、算力、隐状态预算下，单Agent场景平均准确率较CE-only提升3.3pp（最高6.5pp），多Agent场景平均提升3.5pp（最高7.5pp），最终答案收敛率提升30%；效果优于CODI、SIM-CoT等同类隐状态监督方法。
**最值得记住的一句话**：CE-only对隐式递归系统的隐表示约束严重不足，仅增加属性级辅助损失即可在无推理额外成本的前提下大幅提升效果。
