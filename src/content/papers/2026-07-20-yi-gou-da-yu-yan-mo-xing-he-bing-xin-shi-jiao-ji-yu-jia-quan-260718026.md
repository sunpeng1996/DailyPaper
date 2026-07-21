---
title: 'Rethinking Heterogeneous LLM Merging: A Weighted Model Averaging Perspective'
title_zh: 异构大语言模型合并新视角：基于加权平均的无训练融合方法
authors:
- Jiahe Fan
- Yinghao Hou
- Si Chen
- Aiyuan Zhang
- Hong Xie
- Defu Lian
affiliations:
- University of Science and Technology of China
arxiv_id: '2607.18026'
url: https://arxiv.org/abs/2607.18026
pdf_url: https://arxiv.org/pdf/2607.18026
published: '2026-07-20'
collected: '2026-07-21'
category: LLM
direction: 大语言模型 · 异构无训练合并
tags:
- LLM Merging
- Weighted Averaging
- Training-free
- Model Fusion
- Heterogeneous Models
one_liner: 提出无训练维度适配+小比例加权平均策略，实现跨参数规模异构LLM的低成本融合
practical_value: '- 业务场景中多个不同规模的垂直域LoRA微调模型可复用该框架低成本合并，无需额外训练即可融合多场景能力，降低部署成本

  - 小参数规模LLM想升级能力时，可采用截断大模型+小比例插值的方式快速获得性能提升，避免全量微调的高开销，适合推荐/Agent场景的快速迭代

  - 合并时严格控制新增分支权重比例在0.1以下的端点区间，避免中间比例的性能崩溃，同时需做分任务的效果验证，规避能力跷跷板效应导致的部分任务效果下降'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有异构LLM合并方法依赖蒸馏、适配器、语义对齐等额外开销，无法低成本复用不同参数规模的预训练/微调模型资产，业界亟需无训练、低复杂度的异构融合方案来合并多模型的互补能力。

### 方法关键点
- 两种无训练维度适配策略：Union式合并将小模型参数扩展到大模型空间，新增维度零初始化、新增层设为残差恒等映射；Intersection式合并将大模型截断为小模型的参数空间，仅保留匹配维度的参数
- 维度适配后采用小比例加权平均融合，无需语义对齐、适配器、额外训练数据
- 明确有效融合区间：Union式仅在λ∈(0,0.1)或(0.9,1)区间稳定，Intersection式仅在截断大模型权重占比μ∈(0,0.1)区间有效

### 关键实验
在Qwen2.5、Qwen3系列3B到32B的跨规模模型对上验证，覆盖数学推理、代码生成、语义理解等10+类benchmark。Union式合并Qwen2.5-14B与32B，平均得分从单模型最高0.7424提升到0.7525；Intersection式合并Qwen2.5-3B与截断后的32B，平均得分从0.5459提升到0.5716，效果接近TIES等复杂合并方法。

### 核心结论
异构LLM合并无需复杂机制，仅需轻量维度适配+小比例加权平均即可获得可观的能力互补收益，但平衡比例插值易崩溃，且存在任务效果跷跷板效应。
