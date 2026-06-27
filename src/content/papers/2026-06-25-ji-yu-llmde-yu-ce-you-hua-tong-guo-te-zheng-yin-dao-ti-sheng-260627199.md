---
title: 'Forecasting With LLMs: Improved Generalization Through Feature Steering'
title_zh: 基于LLM的预测优化：通过特征引导提升泛化能力
authors:
- Humzah Merchant
- Bradford Levy
affiliations:
- University of Chicago
arxiv_id: '2606.27199'
url: https://arxiv.org/abs/2606.27199
pdf_url: https://arxiv.org/pdf/2606.27199
published: '2026-06-25'
collected: '2026-06-27'
category: LLM
direction: LLM特征干预 · 时序预测泛化提升
tags:
- LLM Forecasting
- Sparse Autoencoder
- Feature Steering
- Look-ahead Bias
- Temporal Reasoning
one_liner: 用稀疏自编码器定位LLM内部时间感知特征，放大后可大幅降低预测任务前瞻偏差
practical_value: '- 电商销量、库存、大促流量预测场景可复用该思路：用稀疏自编码器定位LLM内部时间感知特征，放大后降低模型背诵训练数据未来信息的偏差，提升OOD场景预测准确率

  - 推荐系统用户长期行为预测、冷启动时序建模场景，可通过干预LLM内部任务相关可解释特征，无需全量/LoRA微调即可定向优化推理偏好，优化成本大幅降低

  - 商业决策类Agent做活动效果预判、用户增长预测时，可先挖掘和「历史依据依赖」相关的特征，放大后减少幻觉，提升决策的事实一致性'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
LLM用于时序预测时易直接召回训练集中的未来结果产生前瞻偏差，泛化能力弱，难以适配训练数据未覆盖的业务场景。
### 方法关键点
1. 用稀疏自编码器解析LLM内部激活状态，识别出时间感知推理、前瞻偏差两类可解释的独立特征
2. 跨域预测时直接干预特征激活强度，定向放大时间感知特征，无需微调模型参数
### 关键结果
在并购、制药等完全陌生域的预测任务中，放大时间感知特征可降低50%以上的前瞻偏差，同时MMLU-CoT等通用推理性能损失小于2%，直接调控前瞻偏差特征无显著优化效果。
