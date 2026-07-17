---
title: Leveraging Instruction Tuning and Merging for Reasoning Model Adaptation
title_zh: 基于指令微调与模型合并的推理大模型高效适配方法
authors:
- Yu-Du Feng
- Niels Mündler-Sasahara
- Mark Vero
- Martin Vechev
affiliations:
- ETH Zurich
arxiv_id: '2607.14895'
url: https://arxiv.org/abs/2607.14895
pdf_url: https://arxiv.org/pdf/2607.14895
published: '2026-07-16'
collected: '2026-07-17'
category: Training
direction: 推理大模型轻量适配训练
tags:
- Instruction Tuning
- Model Merging
- Reasoning LLM
- LoRA
- Low-cost Adaptation
one_liner: 仅用无推理轨迹的输入输出对低成本适配推理大模型，保留通用推理能力
practical_value: '- 业务侧适配DeepSeek R1等推理大模型搭建Agent时，无需费力收集带推理轨迹的标注数据，直接用普通输入输出对做LoRA
  IFT后与原模型合并，即可在不丢失推理能力的前提下提升业务性能

  - 合并比例选择逻辑可直接复用：准备百级样本的业务校准集，统计推理轨迹非空的比例，选最大α满足推理率≥0.9即可，无需额外搭建reward model或验证器

  - 电商场景定制专用推理模型（如商品卖点生成、售后纠纷推理）时，这套方法单卡H200仅需不到1小时、成本3美元以内，远低于RLHF/RLVR方案，小团队也可快速落地'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前推理大模型（RLM）主流训练范式RLVR依赖自动验证器，仅能适配数学、代码等可客观验证的领域，而电商文案生成、内容摘要、售后问题解答等大量业务场景无可靠验证器；同时这些场景存在海量无推理轨迹的输入输出标注数据，直接用此类数据做指令微调（IFT）会导致RLM丢失推理能力，引发通用能力与业务性能双双下降，亟需低成本的适配方案解决这一矛盾。

### 方法关键点
- 两步流水线：第一步用无推理轨迹的业务输入输出对做LoRA IFT，得到业务适配的微调模型M_IFT；第二步将M_IFT与原RLM做线性权重合并，得到最终模型
- 合并比例α选择：用小型业务校准集统计模型输出非空推理轨迹的比例，选最大的α满足推理率≥预设阈值（实验取0.9），平衡业务收益与推理能力保留
- 效率优化：校准阶段仅生成前几个token即可判断是否输出推理轨迹，无需生成完整回复，配合二分搜索进一步降低计算开销

### 关键结果
在4款开源RLM（OpenThinker 7B、Apriel 15B、DeepSeek R1 Qwen 7B蒸馏版等）、2个无验证器场景（Rust代码生成、文本摘要）上测试，对比纯IFT、IFT+OPD、IFT+KL等基线：保留95.5%的IFT带来的业务任务收益，几乎完全恢复推理能力与通用数学推理（MATH500）性能，端到端成本不到3美元，运行速度比基线快23%~33%。

### 最值得记住的结论
推理大模型适配业务场景时，无推理轨迹的标注数据无需浪费，IFT+模型合并的成本远低于需要推理轨迹、验证器的RL类方案，性价比极高。
