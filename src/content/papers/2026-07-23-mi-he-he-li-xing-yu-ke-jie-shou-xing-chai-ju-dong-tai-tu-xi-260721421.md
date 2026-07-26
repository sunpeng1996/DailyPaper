---
title: 'Bridging the Gap Between Plausibility and Admissibility: Constraint-Aware
  Flow Maps for Dynamic Graph Systems'
title_zh: 弥合合理性与可接受性差距：动态图系统的约束感知流图
authors:
- Michael Romei de Socio
- Gian Luca Pozzato
- Alessio Merlo
affiliations:
- CASD – School of Advanced Defense Studies, Rome, Italy
- Department of Computer Science, University of Turin, Turin, Italy
arxiv_id: '2607.21421'
url: https://arxiv.org/abs/2607.21421
pdf_url: https://arxiv.org/pdf/2607.21421
published: '2026-07-23'
collected: '2026-07-26'
category: Other
direction: 动态图生成 · 符号约束优化
tags:
- Dynamic Graph
- Conditional Diffusion
- Symbolic Constraint
- Generative Modeling
- Trajectory Prediction
one_liner: 为动态图轨迹生成增加后采样符号约束层，解决统计合理但结构不可行问题
practical_value: '- 做电商用户浏览路径预测、供应链节点流转轨迹生成等动态图任务时，可新增后采样硬过滤模块，既能100%剔除无效轨迹，还能保留84%以上的有效生成样本，平衡有效性和样本量

  - 面对商品依赖关系、多触点用户行为这类复杂度较高的图场景，不要仅依赖生成模型的统计拟合能力，必须叠加符号约束校验模块，提升生成结果可用性

  - 做生成结果合规性校验时，优先排查依赖类约束违规，这类违规占所有无效样本的绝大多数，可大幅降低校验计算开销'
score: 4
source: arxiv-cs.AI
depth: abstract
---

### 动机
生成模型输出的未来系统轨迹具备统计合理性，但无法保证结构可行性，难以支撑动态图场景下的可靠决策。
### 方法关键点
基于条件扩散模型从局部观测生成未来图状态轨迹，新增外部符号层提供三类约束处理能力：硬过滤、软加权、投影修复。
### 关键结果数字
- 紧凑图场景下生成结果无效概率仅0.002996，几乎完全满足可接受性；相同架构下中等复杂度依赖图场景无效概率升至0.155929
- 硬过滤可100%清除保留轨迹中的无效样本，同时保留84.4%的生成样本；软加权可保留有效样本量，但有效性提升有限
- 依赖类约束违规占所有无效样本的绝大多数，符号约束的价值随图结构复杂度升高而提升
