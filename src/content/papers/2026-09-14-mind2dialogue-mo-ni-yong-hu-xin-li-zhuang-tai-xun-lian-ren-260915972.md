---
title: 'Mind2Dialogue: Training Human-Aware Language Models by Simulating User Mental
  States'
title_zh: Mind2Dialogue：模拟用户心理状态训练人类感知型语言模型
authors:
- Zixuan Wang
- Yufan Zhou
- Jinzhou Tang
- Xinle Yu
- Chengjun Wu
- Lyumanshan Ye
- Zhaoxiang Feng
- Letian Peng
- Adyasha Patra
- Fan Bai
affiliations:
- UC San Diego
- KU Leuven
- University of Illinois Chicago
- The Ohio State University
- Johns Hopkins University
arxiv_id: '2609.15972'
url: https://arxiv.org/abs/2609.15972
pdf_url: https://arxiv.org/pdf/2609.15972
published: '2026-09-14'
collected: '2026-09-16'
category: Training
direction: LLM训练 · 对话个性化与心智理论推理
tags:
- Personalized LLM
- User Simulation
- Privileged Distillation
- Theory of Mind
- Conversational AI
one_liner: 通过共享演化心理状态的对话模拟+特权蒸馏，大幅提升LLM个性化与心智理论推理能力
practical_value: '- 做电商导购、客服类个性化对话Agent时，可复用M2D-SIM的用户状态模拟框架，基于共享演化的用户心智状态生成高质量多轮对话训练数据，大幅降低人工标注成本

  - 特权蒸馏范式可直接迁移到业务场景：训练阶段让teacher模型访问后台存储的用户全量画像/行为隐状态生成最优回复，student模型仅用用户可见对话上下文学习，部署无需额外输入，适配现有交互流程

  - 对话+QA混合训练策略可拆分使用：对话样本提升主动回复的个性化表现，QA样本提升用户偏好识别、隐式需求推理准确率，可根据业务场景（比如偏好召回vs智能回复）调整两类样本比例

  - 用户状态分层设计（稳定属性+瞬态情绪/目标）可直接用于电商用户画像的动态更新，适配用户多轮交互中的实时需求变化，提升推荐/回复的精准度'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前训练具备用户感知能力的LLM存在核心监督缺口：真实熟人私域对话标注成本极高无法规模化，公开对话数据集缺少用户未表达的隐含信念、目标、情绪等隐状态标注，基于静态人设生成的合成对话缺乏状态演化连贯性，导致现有模型个性化能力弱、长周期用户意图理解差、心智推理能力不足，无法支撑长期人机协作需求。

### 方法关键点
- 心理学驱动的M2D-SIM模拟器：基于分层用户画像初始化，覆盖终身发展、高频日常、情感需求三类对话场景，将用户状态拆分为稳定属性（长期偏好、价值观）和瞬态属性（当前情绪、短期目标），随交互实时更新
- 共享状态监督机制：用户模拟器与Oracle助教同时访问真实用户隐状态，生成多轮对话，Oracle基于完整状态生成最优回复作为训练目标
- 特权蒸馏范式：student模型训练、部署阶段仅能访问可见对话上下文，无法获取隐式用户状态，通过SFT学习Oracle的回复逻辑
- 混合训练语料：同时包含多轮对话样本和用户偏好相关QA样本，兼顾回复生成和心智推理能力

### 关键结果
在Qwen2.5-7B、Llama3.1-8B、OLMo-3-7B三个开源基座上测试，对比原指令微调模型、Mem0、HumanLM等基线：
1. 个性化指标全面提升：PrefEval偏好跟随生成准确率提升26.6~40.9个百分点，PersonaMem-v2多选准确率提升10.0~13.6个百分点
2. 心智推理能力：Qwen和Llama的BigToM前向信念准确率分别提升13.0、24.8个百分点，OLMo在该指标出现下降，说明收益存在基座差异性

最值得记住的一句话：个性化LLM训练的核心不是单纯注入静态用户画像，而是让模型学会从可见交互中推断用户隐含的演化状态，并基于该状态提供适配服务。
