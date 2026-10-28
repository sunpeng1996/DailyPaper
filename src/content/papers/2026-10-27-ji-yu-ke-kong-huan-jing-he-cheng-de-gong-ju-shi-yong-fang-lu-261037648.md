---
title: Scaling Laws for Tool-Use Agents via Controllable Environment Synthesis
title_zh: 基于可控环境合成的工具使用Agent缩放定律
authors:
- Andrew Szot
- Samira Abnar
- Omar Attia
- Abbas Kazerouni
- Michael Kirchhof
- Cheng-Yu Hsieh
- Raviteja Vemulapalli
- Alexander Toshev
affiliations:
- Apple
arxiv_id: '2610.37648'
url: https://arxiv.org/abs/2610.37648
pdf_url: https://arxiv.org/pdf/2610.37648
published: '2026-10-27'
collected: '2026-10-28'
category: Agent
direction: Agent 工具调用能力优化与缩放
tags:
- Tool-Use Agent
- Scaling Law
- Synthetic Data
- Environment Synthesis
- LLM Fine-tuning
one_liner: 提出可控合成工具使用环境的SynthAPI流水线，推导数据配置与Agent泛化能力的量化缩放定律
practical_value: '- 训练电商/广告场景工具调用Agent（导购、客服、投放Agent）时，数据预算充足优先提升工具多样性、初始数据库状态多样性，收益远高于单纯增加同工具下的任务数量

  - 做Agent训练合成数据可复用SynthAPI框架：先生成领域API集合、数据库Schema，再生成任务、初始状态、可执行校验器，保证数据可验证、多样性可控

  - 数据规模较小时优先在固定工具集合下做任务深度训练，规模超过4096任务阈值后再扩展工具多样性，可实现训练预算最优分配

  - 训练任务中添加合理无关干扰数据（如电商场景的无关商品、历史订单），能显著提升Agent在复杂真实场景的泛化能力'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
工具使用Agent的训练高度依赖高质量多步交互数据，但天然互联网数据中这类数据稀缺，现有合成数据方案大多只追求数量，未明确工具多样性、任务多样性、数据库状态等维度的配置对下游泛化的影响，无法指导训练预算的最优分配。

### 方法关键点
- 提出SynthAPI可控环境合成流水线，分两步生成数据：先由Builder LLM生成分领域APP（含Python实现的工具集合、结构化数据库Schema），再生成可执行任务（含指令、初始数据库状态、校验器、专家求解轨迹）
- 支持4个维度的可控调节：APP（工具）数量A、单APP任务数T、单任务初始数据库实例数S、单数据库干扰数据量D，总任务数N=A×T×S
- 基于458752个任务、849个不同规模模型的训练结果，推导数据配置感知的缩放定律，可预测不同计算预算下的最优数据配置

### 关键实验
训练数据覆盖购物、金融、生产力等8个领域，在AppWorld、BFCL、ASTRA-Bench三个主流工具Agent基准上测试：最优数据配置训练的模型比单纯增加任务数的次优配置平均提升7.6~11.6个百分点，比NVIDIA Nemotron公开数据集训练的模型平均提升30.5个百分点；数据配置感知的缩放定律对16倍计算预算外的泛化性能预测MAE仅0.0285，远优于仅看任务数量的基准模型（MAE 0.1706）。

### 核心结论
工具使用Agent训练的缩放核心不是数据总量，而是工具多样性、数据库状态多样性、任务复杂度的合理配置，预算充足时扩展工具和数据多样性远优于堆砌任务数量。
