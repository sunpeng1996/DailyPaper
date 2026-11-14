---
title: Improved Elastic Weight Consolidation as an Optimization Constraint for Continual
  Learning
title_zh: 作为持续学习优化约束的改进型弹性权重整合方法
authors:
- Davide Wiest
affiliations:
- Department of Computer Science, TU Darmstadt
arxiv_id: '2611.16039'
url: https://arxiv.org/abs/2611.16039
pdf_url: https://arxiv.org/pdf/2611.16039
published: '2026-11-11'
collected: '2026-11-14'
category: Training
direction: 持续学习 · 正则化训练优化
tags:
- Continual Learning
- Elastic Weight Consolidation
- Regularization
- Optimization
- Fisher Matrix
one_liner: 提出CLOC框架推导EWC隐式梯度加权缺陷，设计IEWC提升多场景持续学习性能
practical_value: '- 电商多场景/多任务推荐持续学习可替换原有EWC正则，避免历史点击、转化预测等旧任务拟合充分的样本掉点

  - LLM4Rec、Agent类模型增量微调时采用IEWC，可降低旧训练数据回放的存储开销，同时保留旧任务性能

  - 推荐样本存在脏数据时，IEWC可避免高梯度脏样本主导重要性矩阵，提升模型鲁棒性'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
EWC是持续学习领域广泛使用的正则化技术，存在隐式按样本损失梯度规模加权的缺陷：拟合充分的样本权重极低，易导致旧任务性能退化，现有EWC-DR仅在分类场景观测到该问题，缺乏通用成因解释。
### 方法关键点
提出CLOC框架，将持续学习建模为保留已学习行为泛函的优化约束，推导证明EWC的经验Fisher是该约束保留单样本损失时的一阶形式；据此设计IEWC，基于旧样本损失水平集的一阶近似惩罚输出变化，移除任意可微损失和输出几何下的梯度加权逻辑，避免脏样本主导重要性矩阵。
### 关键结果
在分类、分割、语言、时序预测、扩散模型等多任务场景下，IEWC变体效果持平或优于EWC，全面超过EWC-DR；ImageNet-R实验中，uniform IEWC对比同配置EWC准确率提升2.00pct（95% CI 0.93-3.07）
