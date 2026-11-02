---
title: Asynchronous Flow Map Language Models
title_zh: 异步流映射语言模型：支持嵌入预测顺序的单步并行生成方案
authors:
- Chanhyuk Lee
- Wonjung Kim
- Patrick Pynadath
- Jaehoon Yoo
- Satoshi Hayakawa
- Ruqi Zhang
- Jinwoo Kim
- Seunghoon Hong
affiliations:
- KAIST
- Purdue University
- The University of Tokyo
arxiv_id: '2610.42018'
url: https://arxiv.org/abs/2610.42018
pdf_url: https://arxiv.org/pdf/2610.42018
published: '2026-10-30'
collected: '2026-11-02'
category: LLM
direction: 大语言模型 · 单步并行生成优化
tags:
- Flow Matching
- One-step Generation
- Parallel Decoding
- Diffusion LM
- Sequence Modeling
one_liner: 将预测顺序嵌入单步并行语言模型，刷新数推理与逻辑求解任务单步生成SOTA
practical_value: '- 生成式推荐场景做单步item序列生成时，可借鉴异步调度策略：优先生成高置信度核心item（如用户明确偏好的品类），再引导其余item生成，提升推荐匹配度

  - LLM蒸馏加速场景可复用自蒸馏目标，将多步迭代的生成顺序内化到单步模型隐藏层计算中，兼顾生成速度与效果，适合低延迟要求的文案生成、推荐理由生成场景

  - 对有明确生成顺序约束的场景（如电商文案的标题-卖点-优惠结构），可直接用预定义调度表训练aFMLM，省去teacher预训练成本，压缩训练周期30%以上'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有自回归、掩码扩散模型可通过迭代步骤利用预测顺序提升生成质量，但单步并行语言模型无迭代步骤可承载顺序信息，导致生成质量远低于迭代模型，无法同时满足低延迟、高质量的生成需求。

### 方法关键点
- 定义异步流：为每个token分配独立的去噪进度时间，支持两种调度模式：预定义固定调度（如左到右、逻辑顺序）、自适应调度（基于模型置信度优先完成高确定性token的去噪）
- 推导合法异步流映射形式，设计自蒸馏训练目标，将异步流的调度顺序完全内化到模型隐藏层计算中，仅需单步前向即可生成完整序列
- 工程优化：支持从MDLM预训练权重初始化，降低训练收敛成本；通过噪声下采样减少生成方差；预定义调度场景可直接从头训练，无需预训练teacher模型

### 关键实验
在Sudoku求解、GSM8K代码生成两个任务上测试，对比FMLM、AlphaDLM等10余种单步生成基线：单步生成场景下，aFMLM（熵限调度）在Sudoku-Hard准确率达11.8%，GSM8K准确率达11.4%，均为当前SOTA；预定义调度场景下训练总成本从5GPU小时降至3.2GPU小时，降低36%。

最合适的预测顺序不仅能提升迭代生成质量，还可通过流蒸馏内化到单步模型的层间计算中，在无推理调度开销的前提下保留顺序带来的效果增益。
