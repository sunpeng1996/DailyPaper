---
title: 'Diagonal Equivalence in State Space Models: Characterization, Retrieval Rank,
  and Selective Extensions'
title_zh: 状态空间模型的对角等价：表征、检索秩与选择性扩展
authors:
- Dennis Rochau
affiliations:
- Technische Universität Berlin
arxiv_id: '2611.03101'
url: https://arxiv.org/abs/2611.03101
pdf_url: https://arxiv.org/pdf/2611.03101
published: '2026-11-02'
collected: '2026-11-03'
category: LLM
direction: 大语言模型 · 状态空间模型结构优化
tags:
- State Space Model
- Mamba
- GPU Kernel
- Sequence Modeling
- Diagonal Equivalence
one_liner: 明确SSM对角等价判定条件，推出两款改进结构及优化内核，性能超越Mamba系列基线
practical_value: '- 长序列用户行为建模场景可直接复用本文优化的H100 fused GPU内核，替换原有Mamba实现，获得几何平均10%+的训练速度提升，降低长序列召回/排序的训练成本

  - HybridMamba的混合衰减设计可迁移到用户兴趣建模，通过配置不同衰减率的状态块，同时捕捉短期高频点击、长期低频复购等多周期兴趣，提升推荐精准度

  - SSD-MIMO的多值路由机制适配多目标推荐场景，可在单个SSM层同时建模点击、加购、转化等多个目标的序列依赖，减少多目标模块的参数冗余'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
现有选择性状态空间模型（SSM）如Mamba系列缺乏统一的对角等价分类框架，不同结构的表达能力边界、性能瓶颈不清晰，官方实现的GPU内核训练效率还有优化空间，无法满足电商推荐长序列用户行为建模等场景对大吞吐量、低显存占用的需求。

### 方法关键点
- 给出SSM固定基对角等价的充要判定条件：转移矩阵族两两可交换且每个矩阵可在对应数域上对角化，同时明确固定基对角等价与输入输出等价的差异，前者可保留原始系数条件窗口、支持并行扫描加速。
- 设计两款改进SSM结构：SSD-MIMO支持MIMO接口下的多独立值路由，提升局部检索秩；HybridMamba融合Mamba 1的逐坐标衰减、Mamba 2的头设计与Mamba 3的复数旋转、双端点写入特性，混合不同衰减规律的状态块。
- 实现适配NVIDIA Hopper架构的fused GPU内核，支持bf16精度、SISO/MIMO接口、可变初始状态与可微分跨段状态续传。

### 关键结果
- 训练速度：5种H100 bf16工作负载下，SISO配置几何平均训练速度超越官方Mamba 1/3，Mamba 2恢复版本与官方性能接近。
- 多token召回任务：小模型设置下，两款结构在最难层级表现优于Mamba 1-3，SSD-MIMO路由2-4个独立值时效果最优。
- 语言建模：500M参数模型训练2B token时，两款结构测试损失优于Mamba 1/2，HybridMamba训练到10B token时损失接近Mamba 3 SISO。

所有对角等价的SSM本质上都是带乘性掩码的未归一化标量模式线性注意力，可通过统一框架实现性能优化。
