---
title: 'Weaken to Strengthen: Weakening-Induced On-Policy Self-Distillation for Large
  Reasoning Models'
title_zh: 弱化为强化：面向大推理模型的弱化诱导同策略自蒸馏
authors:
- Yecheng Wu
- Song Han
- Han Cai
affiliations:
- Massachusetts Institute of Technology
- NVIDIA
arxiv_id: '2610.38681'
url: https://arxiv.org/abs/2610.38681
pdf_url: https://arxiv.org/pdf/2610.38681
published: '2026-10-28'
collected: '2026-10-30'
category: Training
direction: 大语言模型推理 · 无特权信息自蒸馏训练
tags:
- Self-Distillation
- On-Policy Training
- LLM Reasoning
- Quantization
- Pruning
one_liner: 无需特权信息，通过原模型与弱化副本的对比信号实现推理模型自蒸馏提升
practical_value: '- 垂域小推理模型（如电商导购Agent、推荐理由生成模型）迭代时，可直接用WISD在无标注prompt上做自蒸馏，无需额外标注数据，大幅降低提升模型推理能力的成本

  - 弱模型构造可直接复用成熟的低比特量化、量级剪枝工具，不需要额外训练弱模型，工程落地成本极低，可快速在业务模型上验证效果

  - 可将强弱对比信号的思路迁移到生成式推荐的模型对齐阶段：用低精度/剪枝版本的生成式推荐模型作为负向参考，强化原版模型对高相关item、优质文案的生成偏好，提升生成推荐的准确率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有同策略自蒸馏方法依赖特权信息（如参考解答、专家演示、环境反馈）构造更强的自教师，仅有无标注prompt时无法落地，且特权信息易导致教师与学生分布偏移，影响知识迁移效果。

### 方法关键点
- 反转传统自蒸馏的强弱构造逻辑：将原模型作为强端，通过无训练的权重退化操作构造弱端副本，两者的token级对数概率差作为监督信号，无需任何特权信息
- 弱模型提供两种开箱即用构造方式：3比特对称分组量化、1/6阈值分组量级剪枝，仅修改注意力和FFN投影权重，保留嵌入、输出头、归一化等参数，确保输出分布可直接对比
- 采用离线DOPD训练流程：原模型基于无标注prompt生成轨迹，冻结的强弱模型对轨迹打分得到缓存监督信号，初始化自原模型的学生基于倾斜KL散度目标训练，推理仅用学生模型

### 关键实验
覆盖Qwen3/3.5/3.6、OLMo-3等5款不同规模（4B~35B）、架构（稠密/MoE）的推理模型，在数学推理（AIME、HMMT）、代码生成（LiveCodeBench）共5个基准测试，对比OPSD、SDPO等需特权信息的SOTA自蒸馏方法：量化版本平均准确率提升4.0pct，剪枝版本平均提升5.5pct，在23/25的模型-基准组合上取得正向收益，效果超过依赖特权信息的基线。典型收益：剪枝将Qwen3.5-4B在HMMT2025准确率从57.7%提升至70.5%，在LiveCodeBench v6从39.1%提升至56.7%。

### 核心结论
无需额外标注或特权信息，仅通过原模型与自身退化版本的对比就能构造有效监督信号实现推理能力提升，大幅降低自蒸馏落地门槛
