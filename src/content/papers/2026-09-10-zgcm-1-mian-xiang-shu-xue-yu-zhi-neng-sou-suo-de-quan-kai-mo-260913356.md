---
title: 'ZGCM-1: A Fully Open and Extremely Efficient Foundation Model for Math and
  Agentic Search'
title_zh: ZGCM-1：面向数学与智能搜索的全开源高效7B基础模型
authors:
- Jiyan He
- Guang Liang
- Hao Liu
- Haoxiang Guan
- Jinbo Sun
- Junyi Guo
- Wenjun Feng
- Yantai Xie
- Yifei Shen
- Bin Shao
affiliations:
- Zhongguancun Academy
- Zhongguancun Institute of Artificial Intelligence
arxiv_id: '2609.13356'
url: https://arxiv.org/abs/2609.13356
pdf_url: https://arxiv.org/pdf/2609.13356
published: '2026-09-10'
collected: '2026-09-15'
category: LLM
direction: 高效大模型 · Agent搜索与数学推理
tags:
- LLM
- Agentic Search
- Mathematical Reasoning
- Long Context
- Efficient Training
one_liner: 开源7B小模型通过混合注意力+MDP训练，推理与智能搜索性能对标千亿级大模型
practical_value: '- 混合滑动窗口+全局注意力5:1的架构可直接复用在长上下文电商导购Agent、多轮搜索推荐场景，KV cache降低6.4倍，256K上下文下吞吐量提升3.94倍，大幅削减长会话推理成本

  - 把Agent交互轨迹转化为MDP状态-动作对做中训练的方法，可迁移到多轮推荐场景的模型训练，仅需短序列SFT即可激活256K长上下文能力，节省训练开销

  - 复用SFT分层过滤策略：质量优先于数量，裁剪约50%低质量候选数据即可提升推理表现，无需盲目扩大训练数据规模，适合垂直场景小样本微调

  - FP8+Muon+TWEO的训练优化组合可直接复用在垂直领域基座微调中，能实现约4.2倍的time-to-loss提升，降低小团队的训练算力成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前前沿数学推理、Agent智能搜索能力基本被千亿参数闭源模型垄断，小参数模型受限于静态容量上限，且主流模型的训练流程、数据配方不透明，算力有限的团队难以复现高性能Agent与推理能力。
### 方法关键点
- 架构：7.39B参数Decoder-only结构，采用5:1比例的门控滑动窗口注意力与全局注意力混合架构，支持256K上下文，KV cache较全注意力降低6.4倍，256K上下文下吞吐量提升3.94倍
- 训练：采用FP8混合精度+Muon优化器+TWEO正则化的组合方案，预训练time-to-loss较BF16/AdamW基线提升4.2倍；渐进式扩展上下文（16K→64K→256K），将Agent交互轨迹转化为MDP状态-动作对做稠密监督
- 后训练：混合think/no-think双模式SFT，分层裁剪50%低质量训练数据提升推理表现，搭配GRPO强化学习对齐能力
### 关键结果
- 7B-8B尺度模型中，14个推理基准平均排名第一，MATH-500准确率97.1%，AIME2026准确率75%，HMMT2025准确率70.4%
- Agent任务性能对标千亿级大模型：WebWalkerQA准确率63.1%，Binary Function Search准确率62%，接近GLM-5.1、Qwen3-235B等大模型表现
### 核心结论
小参数模型无需被动记忆全量公开web数据，通过内部思考链+主动工具调用的双引擎，即可超越参数容量限制，媲美大模型的推理与Agent能力
