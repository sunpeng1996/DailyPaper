---
title: Prospective Prediction of OOD Degradation from Source-Side Training Dynamics
title_zh: 基于源端训练动态的OOD性能退化前瞻性预测
authors:
- Sasha
- Monin
affiliations:
- University of South Carolina
arxiv_id: '2610.12397'
url: https://arxiv.org/abs/2610.12397
pdf_url: https://arxiv.org/pdf/2610.12397
published: '2026-10-08'
collected: '2026-10-10'
category: Training
direction: 模型训练可靠性 · OOD退化提前预警
tags:
- OOD
- Training Dynamics
- Shortcut Learning
- Distribution Shift
- Model Reliability
one_liner: 利用源端训练动态的时序统计特征实现OOD退化提前预警，跨模型架构可迁移
practical_value: '- 训练推荐/搜索/广告模型时，可跟踪训练过程中置信度、熵的时序统计特征，提前预判大促、新类目上线等OOD场景的性能退化，无需等待线上AB测暴露问题

  - 做模型健康度巡检时，优先采集训练全程的时序统计量，而非仅依赖最终checkpoint的单点指标，预警准确性更高

  - OOD退化预测器可跨模型架构迁移，无需为CNN/MLP/Transformer等不同结构的业务模型单独训练预警模块，落地成本低'
score: 6
source: arxiv-cs.LG
depth: abstract
---

## 动机
模型仅靠训练/验证集指标无法预判分布外（OOD）场景性能退化，待OOD下实际观测到退化时已造成业务损失，亟需低成本提前预警方案。
## 方法关键点
针对捷径学习场景，采集源端训练过程中置信度、熵等指标的时序统计特征，训练轻量逻辑回归预测器，无需观测任何OOD数据即可预判OOD持久退化。
## 关键结果
1. 仅用训练时长的基线无有效预测信号，时序特征的预测效果远优于单点当前值特征；
2. 源端时序统计特征的信息量显著高于单点当前值；
3. 预测器无需额外训练直接从CNN迁移到MLP时，置信度、熵动态特征仍保留充足的预测能力，跨架构适配性强。
