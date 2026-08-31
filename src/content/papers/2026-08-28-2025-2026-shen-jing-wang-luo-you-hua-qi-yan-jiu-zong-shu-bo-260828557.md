---
title: 'Blog: Survey of Optimizers'
title_zh: 2025-2026 神经网络优化器研究综述（博客版）
authors:
- Ruoran Xu
arxiv_id: '2608.28557'
url: https://arxiv.org/abs/2608.28557
pdf_url: https://arxiv.org/pdf/2608.28557
published: '2026-08-28'
collected: '2026-08-31'
category: Training
direction: 神经网络训练优化器前沿综述
tags:
- Optimizer
- AdamW
- Muon
- Shampoo
- SOAP
- Training Efficiency
one_liner: 从四大维度梳理2025-2026年神经网络优化器进展，明确无通用最优方案并给出评估规范
practical_value: '- 训练LLM4Rec、电商多模态大模型时，不要盲目替换AdamW，需结合模型规模、batch size、算力预算等场景指标验证矩阵感知类优化器（如Muon、SOAP）的实际收益

  - 低资源训练小样本个性化推荐模型时，可优先选用论文梳理的内存高效优化器、量化优化器状态方案，降低显存占用

  - 优化器选型评估需对齐业务目标：若追求上线迭代速度优先看wall-clock time，若追求训练吞吐优先看tokens/FLOPs，不要直接套用学术榜单结论'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
过往神经网络优化器迭代多围绕Adam变体展开，2025年后设计空间已从坐标级扩展至矩阵/层级，从固定训练周期扩展至动态策略，还需适配分片、低精度计算的状态存储需求，缺乏系统梳理。
### 方法关键点
从时间估计、更新几何、视界管理、表示与系统四大独立维度，串联Muon谱归一化、Shampoo/SOAP历史矩阵统计、自适应混合矩阵方法、内存高效优化器、无调度训练、小批量修正、量化优化器状态等前沿技术。
### 关键结果
矩阵感知类优化器确有实质性进展，但不存在可全场景替代AdamW的通用方案；优化器排名随模型规模、数据参数量比、batch size、调优预算、目标指标（tokens/FLOPs/墙钟时间/显存占用）动态变化，需采用组合化设计思路与更严格的评估协议。
