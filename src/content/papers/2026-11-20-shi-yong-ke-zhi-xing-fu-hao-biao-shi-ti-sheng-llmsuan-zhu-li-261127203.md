---
title: Improved Accuracy Scaling with Problem Complexity in LLM Arithmetic Reasoning
  Using Executable Symbolic Representations
title_zh: 使用可执行符号表示提升LLM算术推理随问题复杂度的精度扩展性
authors:
- Yu-Bin Liu
- Shi-Ju Ran
affiliations:
- Capital Normal University
arxiv_id: '2611.27203'
url: https://arxiv.org/abs/2611.27203
pdf_url: https://arxiv.org/pdf/2611.27203
published: '2026-11-20'
collected: '2026-11-23'
category: Reasoning
direction: LLM推理 · 可执行符号表示优化
tags:
- Arithmetic Reasoning
- Symbolic Representation
- Benchmark
- LoRA
- Complexity Scaling
one_liner: 提出可控算术基准GSM-AB与双斜率框架，验证可执行符号表示可降低LLM算术推理对复杂度的敏感度
practical_value: '- Agent处理电商满减核算、营销预算分配、用户账单计算等数值类任务时，优先用Python-PoT/Lean可执行符号表示替代纯CoT，可大幅提升大数值、多步骤场景的准确率

  - 构建业务效果评估Benchmark时可参考GSM-AB的双维度拆分方法：单独量化数值规模、组合复杂度对模型效果的影响，避免单一指标掩盖不同维度的能力短板

  - 小参数模型（<1.7B）落地推理任务时不建议盲目上符号推理，其对组合复杂度的优化效果仅在1.7B以上参数量级的模型上稳定生效

  - 多推理范式对比微调时，可采用统一训练数据、对齐LoRA参数的实验设置，最大化降低无关变量对结论的干扰'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM数学基准仅反映整体准确率，无法衡量推理能力随问题复杂度上升的衰减规律，纯自然语言CoT推理在数值更大、运算步骤更多的场景下精度暴跌，而可执行符号表示的精度扩展性规律尚不明确，需要可控的评估框架验证其效果。

### 方法关键点
1. 构建GSM-AB可控算术基准，独立控制操作数位数（3-6位）和运算次数（2-6次），共2000道结构匹配的小学数学风格题目，避免结构分布漂移干扰评估
2. 设计双斜率评估框架，分别拟合精度随操作数位数、运算次数的衰减斜率，量化模型对两类复杂度的敏感度
3. 对齐训练配置：相同Qwen3基座（0.6B/1.7B/8B）、相同训练数据、相同LoRA参数，分别微调纯CoT、Lean符号推理、Python-PoT三类范式对比效果

### 关键结果
1. Lean符号推理对比CoT，平均精度在0.6B/1.7B/8B模型上分别提升29.5/44.1/47.8个百分点
2. 8B模型上，Lean对操作数位数的敏感度几乎为0，运算次数增加时精度衰减斜率仅为CoT的29%
3. Python-PoT与Lean效果无统计差异，均大幅优于CoT，6位操作数、6次运算场景下准确率仍保持86%以上，而CoT仅为11%

### 核心结论
可执行符号表示能显著提升LLM算术推理的精度上限，但对组合复杂度的优化效果依赖模型参数量，小模型无法覆盖多步骤符号逻辑的建模需求
