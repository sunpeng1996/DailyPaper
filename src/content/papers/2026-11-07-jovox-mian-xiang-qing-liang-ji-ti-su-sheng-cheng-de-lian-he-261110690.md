---
title: 'JoVox: Joint Hierarchical Flow Matching for Lightweight Voxel Generation'
title_zh: JoVox：面向轻量级体素生成的联合层级流匹配方法
authors:
- Xiangjun Tang
- Jianqi Chen
- Peter Wonka
affiliations:
- King Abdullah University of Science and Technology (KAUST)
arxiv_id: '2611.10690'
url: https://arxiv.org/abs/2611.10690
pdf_url: https://arxiv.org/pdf/2611.10690
published: '2026-11-07'
collected: '2026-11-10'
category: Other
direction: 3D体素生成 · 高效流匹配建模
tags:
- Flow Matching
- Voxel Generation
- Hierarchical Modeling
- Efficient Generation
- 3D Vision
one_liner: 提出联合层级流匹配框架JoVox，实现高效高精度的轻量级体素生成
practical_value: '- 层级生成类任务可借鉴联合分布学习思路，替代分层独立建模，减少上层错误向下传导，可复用在多粒度召回、分层用户建模等推荐场景

  - 跳级预测trick可直接复用，分步生成任务中单次输出两级结果，减半推理步数，适配低延迟的电商推荐、广告投放业务

  - 生成后回溯修正早期决策的unmasking策略，可用于生成式推荐的候选一致性校验、Agent工具调用的决策纠错场景'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有体素生成方案存在精度和效率的矛盾：高精度方案计算开销大，轻量方案生成质量差；传统层级生成方法粗粒度层决策生成后无法修正，易输出合理但错误的结果。
### 方法关键点
1. 提出离散流匹配框架JoVox，学习体素全层级的联合分布而非每层独立建模，允许已生成的细粒度单元信息参与粗粒度单元决策
2. 引入两级预测机制，单次推理直接生成高两级的细粒度单元，将模型处理层数减半，同时提升生成质量
3. 设计unmasking策略，生成细粒度单元后回溯修正早期粗粒度决策的不一致问题
### 关键结果
相比SOTA方案TRELLIS.2，训练吞吐量提升8倍，前向FLOPs降至1/15，仅需4张GPU即可训练（原SOTA需32张），Chamfer距离降低11%，生成质量更优
