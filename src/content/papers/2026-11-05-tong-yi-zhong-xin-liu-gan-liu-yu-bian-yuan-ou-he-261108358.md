---
title: Unifying Central Flow, Rod Flow, and the Edge Coupling
title_zh: 统一中心流、杆流与边缘耦合
authors:
- Eric Regis
- Sinho Chewi
affiliations:
- Yale University
arxiv_id: '2611.08358'
url: https://arxiv.org/abs/2611.08358
pdf_url: https://arxiv.org/pdf/2611.08358
published: '2026-11-05'
collected: '2026-11-08'
category: Training
direction: 深度学习训练优化 · 梯度下降建模
tags:
- Gradient Descent
- Continuous-time Model
- Training Optimization
- Adam
- Momentum
one_liner: 提出边缘耦合框架统一梯度下降稳定边缘下的中心流与杆流两种连续时间模型
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
梯度下降在稳定边缘会沿Hessian尖锐方向震荡，传统梯度流连续时间近似无法刻画该震荡行为，已有的中心流、杆流两种可刻画震荡的连续时间模型关联关系不明确。
### 方法关键点
1. 提出边缘耦合作为统一框架：边缘耦合是定义在连续迭代上的泛函，其临界点对应梯度下降的不动点与二周期轨道
2. 推导得出中心流和杆流是不同时间尺度的粗粒度近似：杆流仅对最快时间尺度粗粒度，中心流同时对快、中时间尺度粗粒度
3. 基于边缘耦合进一步推导了Heavy Ball、Adam等动量优化器的杆流与中心流形式
### 关键结果
在代表性神经网络架构上实验验证，推导的流可在训练全阶段（包括从稳定域到稳定边缘的过渡阶段）精准跟踪离散迭代过程
