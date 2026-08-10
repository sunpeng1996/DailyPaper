---
title: 'UniJEPA: A Unified Joint-Embedding Predictive Architecture for Task-Agnostic
  Visual World Modeling'
title_zh: UniJEPA：面向任务无关视觉世界建模的统一联合嵌入预测架构
authors:
- An Lanji
- Dawei Liu
- Jin Li
- Haoran Xu
- Mei Chen
- Yu Tian
affiliations:
- University of Electronic Science and Technology of China
arxiv_id: '2608.07409'
url: https://arxiv.org/abs/2608.07409
pdf_url: https://arxiv.org/pdf/2608.07409
published: '2026-08-07'
collected: '2026-08-10'
category: Multimodal
direction: 多模态世界模型 · 自监督表征学习
tags:
- JEPA
- Self-Supervised Learning
- World Model
- Visual Representation
- Embedding
one_liner: 统一图像/视频级JEPA任务，实现无预训练的抗崩溃世界建模，规划速度超生成式模型数十倍
practical_value: '- 多任务统一表征思路可迁移至多模态推荐的商品图/短视频联合表征训练，解决拆分任务带来的表征空间不一致问题

  - 高斯正则化替代EMA/stop-gradient的抗崩塌方案可简化自监督表征训练流程，降低工程实现复杂度

  - 目标特征作为预测目标的零样本规划逻辑可复用至智能导购Agent交互决策链路，大幅降低规划延迟'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有JEPA类方法碎片化，图像、视频级任务各自独立训练encoder、预测器，使用不同抗崩溃正则策略，无法用单一模型统一多尺度视觉世界建模。
### 方法关键点
1. 统一图像级光度变换预测、视频级时序状态预测任务到同一共享隐空间，仅采用嵌入预测损失+高斯正则化的单端到端训练目标
2. 无需EMA、stop-gradient或预训练编码器即可保证encoder-predictor对抗崩溃，隐空间同时学习不变结构与等变动力学
3. 经离线轨迹动作条件后训练后，直接将目标特征作为预测目标即可实现零样本规划
### 关键结果
在图像、视频、控制基准上性能持平或超过任务专属JEPA，仅需1个损失超参数，同等精度下规划速度比生成式世界模型快数十倍
