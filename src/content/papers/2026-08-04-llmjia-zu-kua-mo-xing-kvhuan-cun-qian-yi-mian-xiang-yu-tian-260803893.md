---
title: 'Cross-Model KV Cache Transfer in LLM Families: A Closed-Form Linear Mapping
  for Prefill Reuse'
title_zh: LLM家族跨模型KV缓存迁移：面向预填充复用的闭式线性映射
authors:
- Taekyung Heo
- Rasoul Shafipour
- Ritchie Zhao
- Maximilian Golub
- Mohammad Mahdi Kamani
- Ritika Borkar
- Makesh Tarun Chandran
- Pantea Zardoshti
- Bita Darvish Rouhani
affiliations:
- NVIDIA
arxiv_id: '2608.03893'
url: https://arxiv.org/abs/2608.03893
pdf_url: https://arxiv.org/pdf/2608.03893
published: '2026-08-04'
collected: '2026-08-05'
category: LLM
direction: LLM推理优化 · KV cache复用
tags:
- KV-cache
- LLM-inference
- linear-mapping
- model-orchestration
- prefill-optimization
one_liner: 针对同家族LLM切换的预填充冗余问题，提出梯度自由的跨KV缓存线性映射，速度比重预填充快2.7-25倍
practical_value: '- 电商/客服Agent场景经常根据用户query复杂度切换同基座大小模型，可直接复用该方案迁移历史会话KV缓存，跳过预填充大幅降低首Token延迟，提升用户交互体验

  - 同基座不同参数的业务微调模型（如不同场景的电商推荐话术生成模型）切换时，仅需准备500条领域校准样本即可拟合ridge mapper，成本极低，效果可保留73%以上的原模型精度

  - 线性映射效果差的模型对可替换为两层MLP mapper，最多提升37pp的任务保留率；评估映射质量优先用attention-output cosine而非R²，和下游效果相关性更高'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
工业界LLM部署普遍采用多模型编排策略，包括成本质量级联、会话中途切换模型、请求路由等，每次模型切换都需要重新做预填充生成KV缓存，长上下文场景下预填充成本随序列长度线性上升，现有KV缓存复用方案仅支持单模型，跨模型方案要么需要梯度训练，要么对模型架构约束极强，无法落地。

### 方法关键点
- 首先验证同家族LLM的KV缓存存在强线性结构：Qwen3 14B→32B场景下，单个源层即可解释目标层56%的Key方差、32%的Value方差，叠加多层源层最高可提升到79%和65%
- 设计闭式ridge mapper，三步实现无梯度拟合：1）每个目标层选择Top-k最相关的源层，拼接其KV作为输入；2）Key映射前先剥离RoPE，让映射不受位置约束，可适配任意上下文长度；3）仅用500条长度为1024的FineWeb-Edu序列作为校准集拟合岭回归，无需反向传播训练
- 针对线性映射失效的模型对，可替换为两层MLP mapper，将残差误差转移到注意力不敏感的子空间，大幅提升效果

### 关键实验
在Qwen3、Llama 3.1、Ministral 3三个家族的6组匹配KV（KV头数、单头维度一致）模型对测试：4组适配性好的模型对保留73-98%的standalone精度，映射速度比重新预填充快2.7-25倍；2组适配性差的模型对用MLP mapper最多可提升37pp的HellaSwag保留率；多轮会话切换10轮精度漂移不超过2pp。

最值得记住的结论：跨模型KV映射的效果不取决于误差大小，而取决于误差是否落在目标模型的注意力敏感子空间，用attention-output cosine评估映射质量比R²准得多（Pearson相关系数+0.57 vs -0.2）
