---
title: 'OPMD: On-Policy Mechanism Distillation Beyond Output Supervision'
title_zh: OPMD：超越输出监督的同策略大模型机制蒸馏框架
authors:
- Yingdong Shi
- Zhihong Li
- Changming Li
- Jingyi Yu
- Quan Li
- Kan Ren
affiliations:
- ShanghaiTech University
arxiv_id: '2610.14022'
url: https://arxiv.org/abs/2610.14022
pdf_url: https://arxiv.org/pdf/2610.14022
published: '2026-09-28'
collected: '2026-10-19'
category: Training
direction: 大模型蒸馏 · 中间推理机制迁移
tags:
- On-Policy Distillation
- Mechanism Distillation
- Knowledge Distillation
- LLM Training
- Reasoning Transfer
one_liner: 通过两步蒸馏迁移教师模型中间推理机制，效果优于仅输出监督的同策略蒸馏方法
practical_value: '- 做LLM小模型蒸馏时，不要只做输出层KL对齐，可借鉴OPMD两步思路：先训学生兼容的投影层将大模型中间隐态转为学生可用格式，再让学生对齐这些隐态，效果远好于直接MSE对齐隐态

  - 多领域小模型蒸馏场景下，可给每个领域的教师模型训独立投影层，统一蒸馏到同一个学生底座，避免不同领域能力冲突，实测数学+代码双场景下比多教师输出蒸馏平均高3.8个点

  - 电商/推荐场景下用LLM做query改写、商品文案生成的低延时部署时，用OPMD蒸馏可在更短响应长度下拿到更高准确率，相同token成本下准确率比OPD高3-7个点，适合端侧/高并发场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有同策略蒸馏（OPD）仅监督输出层，无法迁移教师模型的中间推理机制；直接对齐师生隐态的方法未考虑隐态对学生后续计算的可用性，几何对齐不代表功能可用，导致复杂推理、多领域适配等场景下蒸馏效果受限。

### 方法关键点
- 分两步蒸馏：第一步构造学生兼容教师，固定师生底座，训练层间投影层将教师隐态转为学生可用的残差信号，优化目标为注入后学生的输出对齐教师输出，而非直接MSE对齐隐态；第二步同策略内化，用学生自身生成的前缀，让原生学生的中间隐态对齐第一步构造的兼容教师隐态，推理时仅保留原生学生，无额外开销
- 支持多教师蒸馏、跨模型家族SFT场景，可搭配LoRA训练，无需改动模型架构

### 关键实验
在数学推理（AMC、AIME 2024/2025）、代码生成（HumanEval+、MBPP+）数据集上验证，对比SFT、OPD、OPRD-Bridge等baseline：单教师场景下AMC准确率比OPD最高高7.04个百分点，相同响应长度下准确率更高，总训练成本仅比OPD高不到20%；双教师（数学+代码）场景下，三个任务分别比多教师OPD高4.31、0.61、6.61个百分点；跨家族SFT（Qwen3→Llama3.1）场景下，仅加机制监督就比纯SFT在AMC上高2.81个百分点。

### 核心结论
几何对齐隐态没有实际价值，只有让学生后续计算能真正用上的隐态迁移，才能有效把大模型的推理能力迁移到小模型上。
