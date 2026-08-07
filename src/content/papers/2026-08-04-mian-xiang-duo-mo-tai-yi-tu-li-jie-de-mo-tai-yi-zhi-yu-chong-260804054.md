---
title: Modality Agreement- and Conflict-Aware Prototype Hypergraph Learning for Multimodal
  Intent Understanding
title_zh: 面向多模态意图理解的模态一致与冲突感知原型超图学习
authors:
- Mohnish Raj
- Suraj Kumar
- Soumi Chattopadhayay
- Chandranath Adak
- Ayan Dutta
arxiv_id: '2608.04054'
url: https://arxiv.org/abs/2608.04054
pdf_url: https://arxiv.org/pdf/2608.04054
published: '2026-08-04'
collected: '2026-08-07'
category: Reasoning
direction: 多模态意图识别 · 跨模态融合
tags:
- Multimodal Fusion
- Intent Recognition
- Hypergraph Learning
- Prototype Learning
- Cross-modal Interaction
one_liner: 提出分层原型超图框架MACH，分别建模多模态一致与冲突特征提升意图识别效果
practical_value: '- 直播电商、短视频互动、多模态搜索等场景的用户意图识别任务，可复用双路径融合架构，分开建模模态一致与冲突信号，避免误判反讽、口误等特殊意图

  - 跨模态特征融合流程中可引入样本自适应仲裁机制，动态加权一致/冲突特征，在保留有用不一致信号的同时压制随机模态噪声

  - 分层递进式模态融合策略可迁移至多模态召回、多模态排序场景，从单模态到多模态逐步聚合特征，提升模型训练稳定性与效果'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有多模态融合方法要么强制跨模态对齐，要么将模态不一致作为噪声抑制，忽略了冲突信息本身的意图指示价值（如文字正向但表情/语气负向对应反讽意图），难以覆盖复杂意图场景。
### 方法关键点
1. 提出分层原型超图框架MACH，按单模态→双模态→三模态递进聚合特征
2. 每层分双路径建模：一致路径用稀疏原型超图捕捉跨模态共识模式，冲突路径用专属超图建模跨模态差异
3. 采用样本自适应特征级仲裁机制融合两路特征，配套渐进式优化策略稳定训练
### 关键结果
在多模态意图识别基准数据集上性能优于现有SOTA，消融实验验证分层融合、原型语义优化、一致冲突仲裁三个模块均带来显著效果增益
