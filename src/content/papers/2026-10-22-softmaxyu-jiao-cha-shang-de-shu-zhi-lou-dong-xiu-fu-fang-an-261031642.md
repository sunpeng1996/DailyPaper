---
title: A Fix for Softmax and Cross-Entropy
title_zh: Softmax与交叉熵的数值漏洞修复方案
authors:
- Jonathan T. Barron
- Dan Gnanapragasam
- Michael Tschannen
affiliations:
- Google DeepMind
arxiv_id: '2610.31642'
url: https://arxiv.org/abs/2610.31642
pdf_url: https://arxiv.org/pdf/2610.31642
published: '2026-10-22'
collected: '2026-10-24'
category: Training
direction: 模型训练 · 损失函数数值优化
tags:
- Softmax
- CrossEntropy
- NumericalStability
- ModelTraining
- KnowledgeDistillation
one_liner: 修复主流深度学习框架softmax与交叉熵实现的两个数值漏洞，提升训练稳定性与效果
practical_value: '- 训练推荐/搜索大模型、蒸馏上线用小模型时，替换现有softmax/交叉熵实现，可避免分类头梯度消失、学生模型漂移问题

  - 低精度（bf16/fp16）训练场景直接复用该修复方案，无需额外调参即可解决高置信度样本梯度归零导致的训练不动点问题

  - 知识蒸馏压缩场景下，用修复后的损失可消除蒸馏误差，提升小模型与大模型的精度对齐效率'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
主流深度学习框架（JAX/PyTorch/TensorFlow等）的softmax、log-softmax、交叉熵标准实现存在两处未解决的数值bug：一是Softmax Collapse，当目标类logit远高于其他类时，对应梯度会被舍入为0，破坏梯度和为0的数学性质，导致高置信度样本无有效梯度；二是Softmax Cancellation，知识蒸馏场景下学生logit与教师logit接近时，仍会产生非零噪声梯度，导致学生模型漂移。
### 方法关键点
仅对现有logit移位、softmax计算逻辑做极简无额外超参的修改，即可同时修复两个数值漏洞，完全兼容原有训练流程。
### 关键结果
完全消除Slingshot现象，带权重衰减训练的grokking速度显著提升，无权重衰减训练可避免精度崩溃，知识蒸馏场景下完全消除学生模型漂移问题，同时证明记忆阶段logit增长被权重衰减与Adam的ε参数的平衡点约束
