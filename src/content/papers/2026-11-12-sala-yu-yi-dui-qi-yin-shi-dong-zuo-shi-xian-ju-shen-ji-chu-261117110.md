---
title: 'SALA: Semantically Aligned Latent Actions Enable Dual-Axis Scaling of Embodied
  Foundation Models'
title_zh: SALA：语义对齐隐式动作实现具身基础模型双轴缩放
authors:
- Jiachun Jin
- Zetong Zhou
- Haonan Wang
- Xiao Yang
- Jun Zhu
- Zhijie Deng
affiliations:
- Sharpa Robotics
- SJTU-Sharpa Joint Lab for Embodied AI, SJTU
- Tsinghua University
arxiv_id: '2611.17110'
url: https://arxiv.org/abs/2611.17110
pdf_url: https://arxiv.org/pdf/2611.17110
published: '2026-11-12'
collected: '2026-11-14'
category: Agent
direction: 具身Agent · 跨模态隐空间对齐
tags:
- Embodied AI
- Latent Action Model
- Semantic Alignment
- Foundation Model
- Cross-embodiment Learning
one_liner: 提出无需配对数据的语义对齐隐式动作框架SALA，实现具身基础模型双轴高效缩放
practical_value: '- 跨域无配对数据对齐思路可直接复用：电商场景下用户行为与商品语义隐空间对齐无需严格配对标注，用文本语义相似度做软约束即可降低标注成本

  - 双轴缩放逻辑可迁移到生成式推荐预训练：通用域预训练+任务域微调分层引入数据，既能提升泛化性，又能降低下游任务标注数据需求

  - 隐式动作建模思路可用于电商导购Agent交互决策：避免显式状态预测带来的效率损失，适配实时交互的低延迟要求'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
具身基础模型依赖成本极高的机器人交互标注数据，现有隐式动作模型（LAMs）仅通过视频重构学习表征，易按视觉外观而非动作语义聚类，无法对齐人类与机器人的同语义动作，难以复用低成本的第一人称人类视频数据。
### 方法关键点
1. 无需人机配对数据，利用未配对人机视频的语言描述计算语义相似度，转换为软邻域结构约束隐空间对齐，引导人类动作隐向量向语义相关的机器人隐向量靠拢；
2. 保留机器人动作重构损失，保证隐空间可直接用于控制，最终形成人机共享的统一隐动作空间，可同时用两类数据训练具身基础模型。
### 关键结果
1. 通用人类视频预训练数据量提升时，下游任务机器人动作预测误差持续下降；
2. 任务特定人类视频后训练数据量提升时，真实世界机器人任务成功率大幅提升。
