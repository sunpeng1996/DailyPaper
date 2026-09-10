---
title: 'HybridFLow: SDN-Orchestrated Client Partitioning for Hybrid Federated Learning'
title_zh: HybridFLow：面向混合联邦学习的SDN编排客户端划分框架
authors:
- Osama Abu Hamdan
- Rabin Pandey
- Hao Che
- Engin Arslan
- Md Arifuzzaman
affiliations:
- University of Texas at Arlington
- Meta Platforms, Inc.
- Missouri University of Science and Technology
arxiv_id: '2609.10404'
url: https://arxiv.org/abs/2609.10404
pdf_url: https://arxiv.org/pdf/2609.10404
published: '2026-09-09'
collected: '2026-09-10'
category: Training
direction: 联邦学习训练 · 网络调度优化
tags:
- Federated Learning
- SDN
- Client Partitioning
- Distributed Training
- Hybrid FL
one_liner: 基于SDN全局网络感知实现混合联邦学习客户端动态划分，大幅降低跨silo训练延迟与掉队者影响
practical_value: '- 电商跨区域多主体（子公司/商家/广告主）联合训推荐/广告模型的场景，可借鉴同步+异步客户端分组策略缓解跨网通信延迟问题

  - 分布式训练任务调度模块可引入全局网络状态感知做任务分组，平衡整体训练速度和模型精度损失

  - 闭环反馈校准延迟预估的思路可直接复用在推荐系统分布式召回/排序训练的通信调度逻辑中

  - 跨区域联邦训练场景下可参考本架构，解决非IID数据分布下异步FL精度不达标的问题'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
跨silo联邦学习（FL）支持多地理分布机构不共享原始数据联合建模，但广域网部署下通信延迟占轮次完成时间比重极高，掉队效应被严重放大；混合FL结合同步、异步客户端参与可缓解该问题，但缺乏全局网络状态（共享瓶颈、链路利用率、路径竞争）感知，无法实现精准的客户端划分。

### 方法关键点
1. 提出SDN驱动的闭环编排框架HybridFLow，直接将网络层智能整合进混合FL流程
2. 基于SDN控制器的全局拓扑视图，每轮训练前生成校准后的单客户端通信时间预估，划分同步/异步分组，平衡轮次延迟和更新陈旧度
3. 每轮训练结束后回传实测通信时间，持续迭代优化后续预测精度

### 关键结果
- 相比基准SmartFLow，达到80%目标精度的速度快33~40%，平均轮次时长降低30~40秒
- 非IID数据分布下，FedAsync无法达到目标精度，本方案无此缺陷
