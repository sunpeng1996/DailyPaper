---
title: 'PMOPD: Task Ordering, Cycling, and Parameter-Update Subspace Protection in
  Multi-Teacher On-Policy Distillation'
title_zh: PMOPD：多教师在线蒸馏的任务排序、循环与参数更新子空间保护
authors:
- Youzhi Liu
- Ruobing Zheng
- Boyuan Tong
- Tianqi Li
- Pingqi Li
- Hanbo Bi
- Yi Yuan
- Jingdong Chen
affiliations:
- Ant Group
arxiv_id: '2609.34605'
url: https://arxiv.org/abs/2609.34605
pdf_url: https://arxiv.org/pdf/2609.34605
published: '2026-09-27'
collected: '2026-09-30'
category: Training
direction: LLM多教师在线蒸馏训练优化
tags:
- Knowledge Distillation
- On-Policy Distillation
- Multi-Teacher Distillation
- LLM Training
- Subspace Projection
one_liner: 提出基于子空间投影的多教师在线蒸馏框架，解决多能力融合的能力跷跷板问题
practical_value: '- 多能力融合场景（如电商Agent多技能整合、推荐多目标蒸馏、搜索多域能力融合）可直接复用双投影机制：完成每个任务块后构建低维子空间记忆，同时对梯度和优化器更新做投影，比仅梯度投影额外提升1个点左右的平均效果，有效解决能力跷跷板问题

  - 多任务排序无需穷尽枚举，仅需每任务取10%以内的样本计算双向冲突得分，按低冲突优先排序，即可获得接近最优的训练顺序，大幅降低多任务调优成本

  - 循环训练的周期选择可直接用同任务跨周期子空间相似度作为轻量诊断指标，峰值对应最优周期，无需跑全量实验即可确定最佳训练调度策略'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
多教师在线蒸馏（MOPD）是大模型后训练阶段融合多领域专项能力的主流方案，相比多专家部署可大幅降低推理成本，但现有方法存在严重的能力跷跷板问题——提升某一领域能力会压制其他已习得能力，普通任务混合策略无法识别冲突更新方向，也无法保护之前任务的有效参数更新，难以平衡模型的稳定性与可塑性。

### 方法关键点
- 观测到OPD的累积参数更新会快速收敛到各任务专属的低维子空间，同任务子空间一致性高、跨任务重叠度仅0.13-0.15，为冲突控制提供几何基础
- 设计双投影机制：每完成一个任务块就基于累积参数偏移构建子空间记忆，训练后续任务时同时对梯度和Adafactor优化器更新做投影，移除与保护子空间重叠的冲突分量
- 轻量冲突探针：基于少量样本计算任务间双向冲突得分，按低冲突任务优先排序，避免穷尽搜索任务顺序
- 循环训练策略：每轮重建子空间记忆，通过同任务跨周期子空间相似度选择最优周期，平衡子空间估计稳定性与任务回访频率

### 关键结果
在Qwen2.5-7B、Llama-3.1-8B两个底座上，针对Math、Code、Reason三个任务验证，对比MOPD、参数合并、Open-MOPD等基线，PMOPD在两个底座上分别将三任务平均得分提升2.54、2.09个百分点，且所有单项任务得分均优于基线，无能力牺牲。

**最值得记住的一句话**：多教师在线蒸馏的跨任务冲突本质是参数更新子空间的重叠，通过子空间投影而非全局参数冻结，可在保留模型可塑性的同时避免能力遗忘。
