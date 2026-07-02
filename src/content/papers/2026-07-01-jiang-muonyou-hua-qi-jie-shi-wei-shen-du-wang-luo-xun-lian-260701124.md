---
title: Muon as a Residual Connection
title_zh: 将Muon优化器解释为深度网络训练过程中的隐式残差连接
authors:
- Hao Huang
affiliations:
- Zhejiang University
arxiv_id: '2607.01124'
url: https://arxiv.org/abs/2607.01124
pdf_url: https://arxiv.org/pdf/2607.01124
published: '2026-07-01'
collected: '2026-07-02'
category: Training
direction: 大模型训练 · Muon优化器机制解释
tags:
- Muon
- optimizer
- residual connection
- representation preservation
- neural network training
one_liner: 提出Muon正交更新等价于隐式残差连接，平衡局部梯度保真与下游表示可用性
practical_value: '- 训练LLM4Rec、电商搜索推荐大模型时，可优先尝试Muon替换Adam优化器，尤其深层Transformer结构，能加速端到端收敛，同时提升召回/排序下游任务的表示质量

  - 现有训练流程中如果暂不切换优化器，可借鉴Muon的设计思路，对Embedding层、Attention的Value/Output矩阵的更新增加轻量正交化约束，平衡局部梯度下降效率和全局表示可用性

  - 设计多阶段训练的推荐系统（如预训练Embedding+下游微调排序）时，可参考梯度保真-表示保留的trade-off思路，对预训练阶段的更新做适当正则，避免破坏特征表示，降低下游微调的收敛成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
Muon作为近年表现最优的大模型训练优化器之一，已在NanoGPT、DeepSeek V4、Kimi K2等场景验证效果，但现有解释多依赖谱范数、信任域、曲率等复杂数学框架，缺少面向普通深度学习从业者的直观机制性解释，也无法为优化器设计提供简单可落地的指导原则。
### 方法关键点
- 将Muon的正交更新等价为隐式残差连接：残差连接显式在网络权重中加入正交变换，Muon则通过优化轨迹隐式注入正交更新，同时兼顾当前步梯度下降需求与下游层的表示可用性
- 提出梯度保真度-表示保留性权衡框架：正交化会修改原始梯度方向，降低当前层局部优化的梯度保真度，但能让学习到的表示拥有更扁平的奇异谱，降低下游优化问题的条件数，提升端到端训练效率
- 设计两组受控线性实验验证机制：两阶段线性模型实验（先训练上层参数再固定上层训练下层）、τ调度交替更新实验（按不同周期交替更新上下层参数）
### 关键结果
- 两阶段实验：600步上层训练后，SGD的局部拟合误差0.0312优于Muon的0.0447，但下游层训练到相同误差阈值时，Muon可节省115步
- τ调度实验：所有调度策略下Muon的端到端收敛速度均优于SGD，τ=600时最多可节省4578步，联合训练（τ=0）场景下也能节省1519步
> 最值得记住：优化器的优劣不能仅通过单层局部损失的下降速度判断，还要兼顾其产出的表示对下游任务的可用性
