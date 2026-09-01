---
title: 'MI-Distillation: Selecting from Model-Interpolated Instruct-Reasoning Data
  Spectrum for Chain-of-Thought Distillation'
title_zh: MI-Distillation：基于模型插值的思维链蒸馏数据选择框架
authors:
- Yangsong Lan
- Renkai Hu
- HongKai Zheng
- Bo Zhang
- Renzhi Wang
- Hongliang Dai
- Piji Li
affiliations:
- 南京航空航天大学人工智能学院
- 教育部脑机智能技术重点实验室
arxiv_id: '2608.29623'
url: https://arxiv.org/abs/2608.29623
pdf_url: https://arxiv.org/pdf/2608.29623
published: '2026-08-30'
collected: '2026-09-01'
category: Training
direction: 小模型推理 · CoT蒸馏优化
tags:
- Chain-of-Thought
- Knowledge Distillation
- Model Interpolation
- Data Selection
- Small LLM
one_liner: 通过模型插值构造连续指令推理数据光谱，结合SeqLSS指标提升小模型CoT蒸馏性能
practical_value: '- 做端侧电商推荐/Agent小模型蒸馏时，可插值不同风格的大模型生成多粒度监督数据，替代手动混合长短样本的方案，提升小模型推理能力

  - SeqLSS样本选择逻辑可复用到指令微调、RAG蒸馏等场景，通过平衡样本信息量与当前模型的适配度，降低训练震荡、提升收敛效果

  - 小模型蒸馏不要盲目使用大模型的超长推理/解释链，根据学生模型容量匹配监督数据粒度，可获得比固定长短CoT混合更稳定的收益'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
大推理模型（如DeepSeek-R1、QwQ）的长Chain-of-Thought（CoT）推理能力突出，但直接将长CoT作为监督蒸馏给小模型时，效果往往不如更简洁的短CoT；现有混合长短CoT、课程蒸馏等方案依赖手动配置，数据粒度粗糙，无法适配不同容量的学生模型。

### 方法关键点
- 梯度分析发现：长CoT会诱导更大的梯度幅值和更集中的更新方向，仅当学生模型容量足够时才能有效吸收，CoT蒸馏需要平衡监督数据的信息密度与学生模型的分布适配性
- 通过参数插值混合推理导向和指令导向的教师模型，构造连续的Instruct-Reasoning数据光谱，生成不同长度、推理深度的CoT轨迹，覆盖长短CoT之间的中间粒度
- 提出SeqLSS（Sequential Learnable Surprisal Score）指标，结合token级surprisal（信息量）和学生模型的概率分布对齐度（可学习性），自适应筛选对当前学生最优的CoT轨迹

### 关键实验
在Qwen2.5-3B、Llama3.2-3B两个学生模型上验证，对比短CoT、长CoT、混合CoT、课程蒸馏等强基线，在MATH-500、GSM8K、AMC23等7个推理基准上平均准确率分别提升1.12、1.40个百分点，其中MATH-500最高提升3.95个百分点。

### 核心结论
小模型蒸馏的最优监督信号不是最复杂的，而是在信息量和可学习性之间取得平衡的样本。
