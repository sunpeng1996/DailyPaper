---
title: When Does Scale-Invariant Optimization Become Unstable? An Exact Schedule Law
  with Weight Decay
title_zh: 尺度不变优化的不稳定边界：带权重衰减的精确调度规则
authors:
- Hasan Amin
- Wei-Kai Chang
- Rajiv Khanna
affiliations:
- Purdue University
arxiv_id: '2609.09116'
url: https://arxiv.org/abs/2609.09116
pdf_url: https://arxiv.org/pdf/2609.09116
published: '2026-09-08'
collected: '2026-09-09'
category: Training
direction: 深度学习训练 · 优化调度稳定性分析
tags:
- Optimization
- Weight Decay
- Learning Rate Schedule
- Training Stability
- Scale-Invariant Network
one_liner: 推导尺度不变优化下学习率与权重衰减的离散动力学规则，给出训练稳定性边界与调度指导
practical_value: '- 训练带Normalization层的召回/排序/LLM模型时，可通过论文给出的标量判断当前学习率+权重衰减组合是否在稳定区间，避免训练震荡

  - 调参时可直接在推导的收缩/膨胀 regime 边界附近搜索学习率与权重衰减组合，快速拿到最优训练性能

  - 若用Adam等自适应优化器训练带归一化的大模型，需注意其自淬火效应更弱，要适当下调学习率避免不稳定'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
带归一化层的深度学习模型普遍存在尺度不变性，学习率调度与权重衰减通过参数范数形成隐式反馈环，现有调参方案缺乏精确动力学指导，易出现训练不稳定、性能不达标的问题。
### 方法关键点
1. 推导尺度不变优化下的精确离散时间动力学规则，用单一标量即可表征调度与权重衰减的共同作用，清晰划分收缩/膨胀主导的有效学习率区间；
2. 提出统一齐次优化器框架，从第一性原理层面解释自适应优化器自淬火强度更弱、归一化场景下稳定性更差的机制；
3. 证明固定学习率+权重衰减的组合本质无法维持内部平衡，会产生周期性震荡行为。
### 关键结果
在MLP、CNN、GPT2等模型，MNIST、CIFAR、wikiText、OpenWebText等数据集上预测规律精度极高，在推导的边界处训练性能达到峰值。
