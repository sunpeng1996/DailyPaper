---
title: 'QUASAR: Lowering the Loss Floor of Quantization-Aware Training with Loss-Aware
  Reconstruction'
title_zh: QUASAR：基于损失感知重建降低量化感知训练的损失下限
authors:
- Vincent Counathe
- Ben Athiwaratkun
- Christopher De Sa
- Tianyi Zhang
affiliations:
- Cornell University
- Together AI
arxiv_id: '2608.13966'
url: https://arxiv.org/abs/2608.13966
pdf_url: https://arxiv.org/pdf/2608.13966
published: '2026-08-14'
collected: '2026-08-17'
category: Training
direction: LLM低比特量化感知训练优化
tags:
- QAT
- Low-bit Quantization
- LLM Deployment
- Training Optimization
- Inference Optimization
one_liner: 提出轻量损失感知重建的QAT方法，无推理开销下大幅提升2-4bit低比特大模型性能
practical_value: '- 业务侧大模型轻量化部署（如电商客服Agent、推荐文案生成模型）可直接复用QUASAR的QAT流程，仅增加1.4%训练耗时就能大幅提升2-4bit量化模型的推理质量，无推理
  overhead，适配高并发、端侧部署场景

  - 损失感知重建思路可迁移到推荐系统低比特量化场景：用梯度平方的EMA作为权重显著性指标，自适应搜索裁剪范围+加权最小二乘拟合反量化参数，降低召回/排序模型量化后的精度损失

  - 垂域大模型低比特直接适配（如电商垂域大模型微调）可优先选用QUASAR：INT2场景下新任务学习能力比传统QAT+PTQ流程高10.9pp，避免微调后量化导致的能力退化'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
大模型推理已成为部署的主要 recurring 成本，低比特量化是核心降本手段，但传统PTQ在新模型、长上下文场景下性能退化严重；QAT存在前向计算用量化重建权重、反向更新全精度隐权重的结构不匹配问题，导致收敛到更高损失下限，现有优化方案均未针对重建环节优化，而二阶PTQ的重建思路引入QAT的计算成本过高。

### 方法关键点
- 复用AdamW的二阶矩（梯度平方的EMA）作为权重显著性的在线估计，近似Hessian降低计算开销，无额外存储成本
- 每步在少量候选裁剪范围中搜索，对每个范围对应的编码分配，通过显著性加权最小二乘拟合最优反量化scale、zero-point，选择损失感知重建误差最小的结果
- 支持INT2/3/4、NVFP4等主流部署格式，仅修改训练侧重建逻辑，推理侧无任何修改与overhead

### 关键结果
- 在Qwen3、Llama-3.1系列模型上，INT3/4位下KL散度比主流QAT基线低至少10%，INT2下低29%，8个下游任务平均精度提升3.5-4.3pp
- NVFP4场景下相对标准QAT KL散度降低约30%
- 低比特直接微调数学推理任务时，INT2下5个数学基准平均精度比QAT/PTQ基线高至少10.9pp
- 训练单步耗时仅比标准QAT高1.4%

### 核心结论
QAT的损失下限本质由损失感知重建误差决定，仅优化重建环节即可在无推理开销的前提下大幅提升低比特模型性能
