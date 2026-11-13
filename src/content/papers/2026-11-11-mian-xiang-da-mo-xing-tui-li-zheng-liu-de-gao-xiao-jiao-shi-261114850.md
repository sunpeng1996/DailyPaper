---
title: Effective Teacher Support for Reasoning Distillation
title_zh: 面向大模型推理蒸馏的高效教师分布截断优化方法
authors:
- Lavinia Ghita
- Dhruv Desai
affiliations:
- NVIDIA
arxiv_id: '2611.14850'
url: https://arxiv.org/abs/2611.14850
pdf_url: https://arxiv.org/pdf/2611.14850
published: '2026-11-11'
collected: '2026-11-13'
category: Training
direction: 大模型推理蒸馏 · 训练效率优化
tags:
- Knowledge-Distillation
- LLM-Training
- Reasoning-LLM
- Efficient-Training
- Model-Compression
one_liner: 仅保留教师分布top0.01%词汇的截断蒸馏，无损效果同时降38%训练时间、24%显存
practical_value: '- 做垂直场景小LLM蒸馏（如电商客服、商品文案生成、Agent推理小模型）时，无需计算全词汇KL散度，仅保留教师top 15~100个token即可，效果无损的同时降低训练成本

  - 若模型使用特殊结构token（如电商场景的<商品ID>、<活动标签>、Agent的<调用工具>标记），蒸馏截断时需强制保留这类token，避免输出结构错误

  - 蒸馏前可离线预计算并缓存所有训练样本的教师top k logit，训练阶段无需实时推理教师模型，直接减少38%左右的单步训练时间'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
传统全词汇表正向KL蒸馏需要逐位置计算教师、学生模型在全词汇上的分布对齐，不仅训练计算开销高，教师目标的存储成本也极大。但自回归LLM的next-token概率分布高度集中，绝大多数概率质量集中在极少数token上，因此存在大幅压缩教师分布支持集的优化空间，现有研究尚未明确截断到多大程度不会影响推理生成效果。
### 方法关键点
- 蒸馏时仅保留每个监督位置教师模型top k个最高概率的token，对保留的概率质量重归一化后计算正向KL散度，完全丢弃长尾低概率token的对齐约束
- 针对带结构推理标签的模型（如Qwen3的<think>、</think>标记），强制将结构标签加入保留集合，避免截断导致的输出结构断裂
- 支持离线预缓存教师top k的token ID与对应logit，训练阶段无需实时推理教师模型，同时学生侧仅需计算保留token的logit，无需生成全词汇表logits
### 关键结果
实验在Qwen3 4B→1.7B、8B→4B、Nemotron Nano 12B→9B三个蒸馏对上验证，训练语料包含推理对话、问答两类场景：
- Qwen3系列仅保留0.01%词汇（k=15）时，MMLU-Pro得分与全词汇蒸馏完全持平，无效果下降
- 采用离线缓存+紧凑k-row计算的方案时，单步训练时间降低38%，峰值显存占用降低24%
- Nemotron系列保留0.1%词汇时效果无损，更小的截断会导致无法生成闭合推理标签，说明最优截断阈值与模型家族强相关
### 核心结论
LLM推理蒸馏无需对齐全词汇表分布，仅保留教师top几十到上百个最高概率token即可实现无损效果，可大幅降低训练与存储开销
