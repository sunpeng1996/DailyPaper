---
title: 'Better Starts, Better Ends: Bootstrapped Iterative Self-Reasoning Distillation
  for Compressed Reasoning'
title_zh: BIRD：启始引导的迭代自推理蒸馏实现高效LLM推理压缩
authors:
- Leichao Dong
- Dongxu Zhang
- Yiding Sun
- Qirui Wang
- Yuhan Wang
- Lin Chen
- Jihua Zhu
affiliations:
- 西安交通大学
- 北京大学
arxiv_id: '2607.15736'
url: https://arxiv.org/abs/2607.15736
pdf_url: https://arxiv.org/pdf/2607.15736
published: '2026-07-17'
collected: '2026-07-20'
category: Reasoning
direction: 大语言模型 · 推理压缩 · 自蒸馏
tags:
- LLM
- Chain-of-Thought
- Self-Distillation
- Reasoning Compression
- LoRA
one_liner: 提出两阶段自蒸馏方法BIRD，解决on-policy推理蒸馏冷启动前缀瓶颈，兼顾推理准确率与压缩效率
practical_value: '- 可直接复用BIRD蒸馏框架优化业务中LLM推理模块（如Agent意图理解、商品属性推理），大幅减少CoT token消耗，降低推理延迟与成本

  - 两阶段训练trick可迁移到生成式推荐的LLM微调：先轻量SFT暖启动校准输出分布，再做on-policy优化，收敛更快且效果上限更高

  - prompt-switch技巧可直接落地：用带约束指令（如简洁、口语化）的prompt生成训练数据，用原任务prompt做SFT，可把指令约束变成模型默认行为，无需推理时额外加prompt

  - Token Efficiency（准确率/ln(输出长度)）指标可用来评估业务LLM模块的性价比，平衡效果与推理成本，适合高并发的电商推荐、搜索场景'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
大模型CoT推理普遍存在大量冗余步骤（重复推导、无效自校验、路径偏离），现有on-policy自蒸馏方法从冗余的基础模型冷启动时，KL损失大量作用在噪声高、偏离最优路径的前缀上，仅能做局部修正，收敛到的压缩效率上限低，推理成本高，限制了高并发、低延迟场景的部署。
### 方法关键点
- 两阶段蒸馏架构BIRD：第一阶段做静态启始，用基础模型加简洁指令生成推理轨迹，仅保留答案正确的样本，做1个epoch的轻量LoRA SFT，训练时切换为原任务prompt，将指令诱导的简洁推理能力转化为模型默认行为
- 第二阶段做动态优化，从暖启动模型开始执行on-policy反向KL自蒸馏，教师为定期更新的停止梯度的学生副本并附加简洁指令，损失作用在更干净的有效推理前缀上，避免冗余路径的无效学习
### 关键实验
在Qwen3全系列、DeepSeek-R1-Distill-Llama-8B上测试，数据集覆盖MATH-500、AIME 2024/2025，对比基线包括原生模型、仅推理加简洁prompt、冷启动自蒸馏CRISP。核心结果：Qwen3-8B上MATH-500准确率从86.2%提升至92.0%，平均响应长度从3099token压缩至1115token，Token效率较CRISP提升12%；跨模型场景下DeepSeek-R1-Distill-Llama-8B的MATH-500准确率提升8个点，响应长度压缩33%。
### 核心结论
on-policy自蒸馏的效果不仅取决于教师的构造，更取决于监督信号作用的前缀分布，暖启动让损失聚焦在有效推理路径上，效果远优于冷启动的局部修正。
