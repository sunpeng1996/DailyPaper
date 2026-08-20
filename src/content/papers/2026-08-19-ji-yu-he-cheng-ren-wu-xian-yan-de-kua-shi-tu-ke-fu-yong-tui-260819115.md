---
title: Pretraining Reusable Inference Across Views with Synthetic Task Priors
title_zh: 基于合成任务先验的跨视图可复用推理预训练
authors:
- Jielong Lu
- Zhihao Wu
- Jiajun Yu
- Zhaoliang Chen
- Haishuai Wang
affiliations:
- Zhejiang University
- Hong Kong Baptist University
arxiv_id: '2608.19115'
url: https://arxiv.org/abs/2608.19115
pdf_url: https://arxiv.org/pdf/2608.19115
published: '2026-08-19'
collected: '2026-08-20'
category: Training
direction: 多视图学习 · 可复用推理预训练
tags:
- Multi-view Learning
- In-Context Learning
- Transfer Learning
- Synthetic Data
- Few-shot Learning
one_liner: 提出SIMPLE多视图上下文学习框架，通过合成任务先验预训练可复用跨视图推理能力，适配少样本/缺视图场景
practical_value: '- 多模态/多特征推荐场景可复用分层推理架构，分别做单特征域内、跨特征域、支持样本-查询样本的三层推理，提升多特征融合效率

  - 小样本冷启动场景可借鉴合成任务先验构造思路，在embedding空间生成不同特征缺失、分布偏移的训练episode，预训练通用融合逻辑，减少下游重训成本

  - 跨任务迁移时可先用冻住的推理backbone快速验证效果，再用轻量Adapter做任务对齐，平衡迁移效率和效果'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有预训练编码器的跨视图表示已可复用，但多视图融合推理逻辑仍需每个下游任务重训，视图相关性、互补性、缺失模式等知识无法跨任务迁移，且真实数据集覆盖的视图配置、任务结构有限。
### 方法关键点
1. 将多视图学习重构为学习可复用的任务条件推理流程而非固定融合函数，提出SIMPLE多视图上下文学习器，基于少量标注支持集预测查询标签；
2. 在embedding空间构造可控合成任务先验，生成包含不同类别结构、视图依赖、可靠性、缺失模式、分布偏移的多样support-query episode；
3. 设计分层推理架构，分别完成视图内、跨视图、支持-查询样本间的推理。
### 关键结果
冻住backbone的SIMPLE版本无需更新就能达到可比性能，轻量Adapter校准后在多数多视图、多组学基准上取得SOTA，验证了多视图推理能力可预训练复用的核心假设。
