---
title: 'CATeye: Coupled Attribute-Topology Invariance Learning for Voucher Abuse Detection'
title_zh: CATeye：面向优惠券欺诈检测的属性-拓扑耦合不变性学习框架
authors:
- Tian Tian
- Shuaicheng Niu
- Hao Kuang
- Yuanhang Hu
- Dong Li
- Zhiqi Shen
affiliations:
- Nanyang Technological University
- Lazada Inc.
- Alibaba Group
arxiv_id: '2609.01425'
url: https://arxiv.org/abs/2609.01425
pdf_url: https://arxiv.org/pdf/2609.01425
published: '2026-09-01'
collected: '2026-09-02'
category: Other
direction: 电商风控 · 跨域图异常检测
tags:
- Graph Anomaly Detection
- Domain Generalization
- Invariance Learning
- Voucher Abuse Detection
- GNN
one_liner: 通过属性+边双不变性选择器过滤耦合分布偏移，提升跨域优惠券欺诈检测F1最高8.61%
practical_value: '- 跨地域/跨时间的电商风控场景可复用AIS+EIS双选择器架构，先过滤非不变属性再采样不变子图，缓解分布偏移带来的模型效果衰减

  - 图风控模型遇到属性偏移连带拓扑偏移问题时，可参考本框架的多视图学习目标，分别约束域不变表征与域专属噪声的学习

  - 电商优惠券、满减等促销活动的反作弊场景可直接基于开源CATeye代码做适配，快速上线效果优于现有基线的检测模型'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
电商优惠券欺诈模式跨时间、跨地域快速迭代带来分布偏移，现有GNN检测模型受属性-拓扑耦合偏移影响（属性偏移连带拓扑偏移，经消息传递放大噪声），效果衰减快，需频繁重训。

### 方法关键点
1. 设计属性不变性选择器（AIS）：学习节点自适应掩码，过滤非不变属性
2. 设计边不变性选择器（EIS）：基于保留的不变属性采样不变子图，隔离非不变边
3. 基于拆分的不变/非不变组件构建多视图，用视图专属目标强化域不变表征，抑制域专属噪声

### 关键结果
在Lazada私有数据集和公开基准上，对比9个域泛化、图异常检测强基线，平均F1最高提升8.61%，代码已开源。
