---
title: Training LLMs for Multi-Agent Collaboration with Verifiable Information Rewards
title_zh: 基于可验证信息奖励的多智能体协作LLM训练方法
authors:
- Keru Chen
- Sen Lin
- Yingbin Liang
- Nathaniel D. Bastian
- Shaofeng Zou
affiliations:
- Arizona State University
- University of Houston
- The Ohio State University
- Johns Hopkins University
arxiv_id: '2610.17893'
url: https://arxiv.org/abs/2610.17893
pdf_url: https://arxiv.org/pdf/2610.17893
published: '2026-10-13'
collected: '2026-10-15'
category: MultiAgent
direction: 多智能体协作 · LLM后训练优化
tags:
- MultiAgent
- LLM
- RewardDesign
- SelfPlay
- ReinforcementLearning
one_liner: 提出基于团队惊奇度的CoSIR训练框架，跨任务泛化性优且不损失模型通用能力
practical_value: '- 可借鉴细粒度奖励拆分思路：在电商多Agent客服、商品选品协作、搜索推荐多模块协同等场景，将奖励拆分为信息共享、信息请求、信息利用三类，替代单一最终结果奖励，大幅提升协作效率

  - 可复用「玩具环境预训练+下游迁移」范式：先在结构化可验证小环境训练Agent基础协作能力，再迁移到真实业务场景，大幅降低协作训练的标注成本

  - 基于惊奇度下降的信息价值评估方法，可直接用于Agent间通信的价值判定，过滤无效重复信息，降低多Agent系统的通信开销'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM多智能体协作普遍存在隐瞒有用信息、不主动询问缺失信息、忽略队友输入等问题，传统指令微调、仅用最终任务结果反馈的强化学习方法，无法为单条通信内容的价值提供细粒度监督信号，导致协作能力难以泛化到未见过的任务，甚至会损害模型通用能力。
### 方法关键点
- 搭建可验证的评分表玩具训练环境：每个Agent仅持有部分选项的属性评分，需通过通信协作选出总分最高的选项，所有信息的价值均可精准计算
- 设计基于团队惊奇度的贝叶斯评估器：团队惊奇度定义为所有Agent对正确选项的负对数概率之和，分别为信息共享、信息请求、信息利用三类行为分配独立可量化的奖励
- 采用自play PPO进行训练，仅在结构化玩具环境完成训练，不依赖下游任务的人工标注
### 关键结果
在Qwen3-4B、Qwen3-8B、Gemma-3-4B-it三个模型 backbone 上验证，跨7个 unseen 协作任务（含HiddenBench、SILO-BENCH、SplitQA等），相比基线模型总分分别提升24.70、31.85、27.92分；对比仅用最终结果奖励的Outcome-RL，总分领先最高达24.86分，同时GSM8K、MMLU、IFEval等通用能力指标下降不超过0.6个百分点。
### 核心结论
多智能体协作训练不需要在复杂下游任务做标注，在结构化可验证的简单环境训练细粒度协作行为，就能实现跨场景泛化，同时不损失模型通用能力
