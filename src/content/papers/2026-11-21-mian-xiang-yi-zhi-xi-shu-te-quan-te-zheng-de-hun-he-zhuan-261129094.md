---
title: 'HME-PFD: Heterogeneous Mixture-of-Experts Privileged Feature Distillation'
title_zh: 面向异质稀疏特权特征的混合专家蒸馏框架HME-PFD
authors:
- Wen Xu
- Xiaomin Zhang
- Yucheng Yang
- Danny Liu
- Xunlong Gui
- Fei Huang
- Sha Meng
affiliations:
- Meta
- University of Toronto
arxiv_id: '2611.29094'
url: https://arxiv.org/abs/2611.29094
pdf_url: https://arxiv.org/pdf/2611.29094
published: '2026-11-21'
collected: '2026-11-24'
category: RecSys
direction: 广告推荐 特权特征蒸馏与MoE优化
tags:
- Knowledge Distillation
- Mixture-of-Experts
- Privileged Feature
- CVR Prediction
- Recommendation System
one_liner: 将特权特征引入学生模型MoE路由，解决异质稀疏特权特征下的蒸馏性能衰减问题
practical_value: '- 电商CVR/CTR模型蒸馏场景，若存在覆盖率低、分布不均的特权特征（如post-click行为），可直接复用HME-PFD框架，训练阶段用特权特征做MoE路由，无需修改推理链路，无线上额外开销

  - 路由模块选择可按业务复杂度权衡：特权特征存在明确的有无规律时用硬编码路由，成本最低；特征交互复杂时用线性/MLP路由，性价比最优，无需盲目上复杂的注意力路由

  - MoE配置可参考实验结论：专家数控制在2~3个、单专家隐层维度对齐共享embedding维度、选top2专家即可获得最优收益，避免过多专家带来的优化难度上升问题'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有特权特征蒸馏（PFD）假设所有训练样本的特权特征全量可用，但工业场景下特权特征（如广告post-click停留时长、跳转行为）往往覆盖率低、分布异质，不同样本的教师软标签信噪比差异极大，均等处理会导致学生模型要么过拟合噪声信号，要么浪费高价值信号，蒸馏效果受损。

### 方法关键点
- 学生模型采用MoE架构作为蒸馏辅助任务头，仅在训练阶段用特权特征做路由，推理阶段完全丢弃辅助任务，无需访问特权特征，不修改线上部署逻辑
- 路由模块支持两类设计：硬编码路由按特权特征有无规则分配样本，适配规则明确的场景；可学习路由支持线性层、MLP、注意力等架构，自动适配复杂的特征分布
- 路由仅决定蒸馏任务的专家分配，主任务（如CVR预测）仍用共享embedding加普通预测头，蒸馏损失和主任务损失加权联合训练

### 关键实验
在Meta两个大规模工业广告CVR预测数据集上实验，基线为无蒸馏的Plain模型。结果：CVR_Large场景下最高降NE 0.09%，CVR_Small场景下最高降NE 0.42%；专家数2~3个时收益最优，4个专家性能下降；单专家隐层维度对齐共享embedding维度时效果最好，选top2专家比top1/top3收益更高。

### 核心结论
特权特征不仅可以用来训教师模型做软标签，还可以在训练阶段用来指导学生模型的样本路由，放大高信噪比信号的学习权重，且完全不增加线上推理成本
