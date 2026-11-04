---
title: 'Shuffled OPSD: When Semantic Consistency Hurts On-Policy Self-Distillation?'
title_zh: Shuffled OPSD：语义一致性为何会损害同策略自蒸馏性能
authors:
- Qingyuan Zheng
- Zhihao Dou
affiliations:
- Duke University
arxiv_id: '2611.04958'
url: https://arxiv.org/abs/2611.04958
pdf_url: https://arxiv.org/pdf/2611.04958
published: '2026-11-03'
collected: '2026-11-04'
category: Training
direction: LLM训练 · 同策略自蒸馏优化
tags:
- OPSD
- Knowledge Distillation
- LLM Training
- Mathematical Reasoning
- LoRA
one_liner: 提出仅打乱师生共享问题文本、保留教师参考结构的Shuffled OPSD，在数学推理任务上显著优于标准OPSD
practical_value: '- 做LLM微调/自蒸馏时可复用选择性语义扰动思路：训练阶段对师生共享的输入做轻量打乱，保留教师端特权参考信息完整，无需修改推理逻辑即可提升下游性能，落地成本极低

  - 小模型优化场景优先尝试：1.7B小模型涨点是大模型的2-3倍，业务中用小模型做query理解、商品文案生成、个性化推荐reasoning的蒸馏训练时，可直接引入该输入变换

  - 降低自蒸馏训练数据成本：自蒸馏时教师端参考无需与当前问题严格关联，用无关的优质标注样例即可达到接近标准OPSD的效果，可减少配对标注的工作量'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有同策略自蒸馏（OPSD）默认保留师生共享的问题文本语义结构，认为语义一致性是训练的有益前提，但此前未验证该假设的普适性，也未将共享输入结构作为独立的训练优化维度。
### 方法关键点
- 核心设计为**选择性语义扰动**：仅对师生共享的问题文本做单词级打乱，完全保留教师端专属参考样例的结构与内容，推理阶段仍使用原始未打乱输入，无需修改推理逻辑
- 前置验证：将教师端的问题关联解答替换为其他问题的完整标注样例，性能与标准OPSD的差距不超过0.55pp，证明教师参考无需与当前问题严格配对
- 训练用LoRA微调，仅更新学生侧LoRA参数，教师为冻结的初始backbone，损失沿用带KL上限的标准OPSD损失，无额外开销
### 关键结果
在AIME2024、AIME2025、HMMT2025三个数学推理基准上测试Qwen3-1.7B/4B/8B三个模型规模，对比冻结基线、标准OPSD等对照组：单词级打乱的Shuffled OPSD相对标准OPSD的平均准确率提升分别为3.52pp、1.11pp、1.38pp；若同时打乱教师端参考样例，性能会下降1.57~2.41pp。

最值得记住的结论：语义一致性并非OPSD训练的通用最优原则，选择性扰动师生共享输入、保留教师特权参考结构，可在零推理成本的前提下显著提升模型性能。
