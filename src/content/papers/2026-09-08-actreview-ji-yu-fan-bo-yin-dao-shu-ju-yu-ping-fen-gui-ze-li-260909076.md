---
title: 'ActReview: Rebuttal-Guided Training Data and Rubric Rewards for Actionable
  Peer Review Generation'
title_zh: ActReview：基于反驳引导数据与评分规则奖励的可执行审稿生成
authors:
- Yiling Ma
- Yilun Zhao
- Sihong Wu
- Ziyu Chen
- Manasi Patwardhan
- Arman Cohan
affiliations:
- Yale University
- University of Chicago
- TCS Research
arxiv_id: '2609.09076'
url: https://arxiv.org/abs/2609.09076
pdf_url: https://arxiv.org/pdf/2609.09076
published: '2026-09-08'
collected: '2026-09-09'
category: Training
direction: 大模型训练优化 · 结构化奖励设计
tags:
- SFT
- GRPO
- Rubric Reward
- LLM Alignment
- Actionable Generation
one_liner: 利用审稿-反驳对构建训练数据，结合双任务SFT与GRPO规则奖励生成可落地审稿意见
practical_value: '- 对需要生成可执行建议的场景（如商品差评回复、用户反馈整改方案、推荐结果解释），可采用「问题诊断-解决方案」双任务拆分替代端到端生成，提升输出针对性与落地性

  - 缺乏明确标注时，可挖掘交互对（用户差评-商家回复、用户投诉-客服解决方案）作为隐式监督信号，低成本构造高质量训练数据集

  - RLHF阶段可使用实例感知的定制化rubric代替通用奖励模型，既能降低标注成本，又能提升优化方向精准度，适配电商场景多维度输出质量要求

  - 长文本生成任务训练阶段，用检索到的局部相关上下文代替全量长文本输入，可在不损失效果的前提下降低算力开销'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM生成的审稿反馈多仅识别问题，缺乏可落地的修改指导；现有审稿生成数据集无明确的问题-修改关联标注，通用RLHF的scalar奖励信号过于粗粒度，无法适配开放生成任务的多维度质量要求，难以生成精准可执行的输出。

### 方法关键点
- 任务拆分：将可执行审稿生成拆分为**诊断声明生成**（定位论文具体缺陷）和**可执行建议生成**（给出What/Where/How/预期效果的结构化修改方案）两个子任务
- 数据集构造：从OpenReview爬取4万条审稿-反驳对，以作者反驳为隐式监督，对齐审稿弱点与修改路径，构造ActReview-40K训练集；同步构建1000条人工标注的ActReview-Bench benchmark
- 训练框架：先对Qwen3-8B-Base做多任务SFT，再用GRPO做对齐优化，奖励为每个实例定制的candidate-aware弱点专属rubric，结合硬约束和加权软指标计算奖励，避免通用奖励偏差

### 关键实验
对比GPT-5.1、Gemini-3.1-Pro等闭源模型及DeepReviewer等开源审稿模型，ActReview-RL在可执行性指标上相对最优基线提升19%，人工评估调整胜率超70%，严重技术错误率仅6.29%，为所有参评模型最低。

### 核心结论
交互场景中的响应对可作为低成本隐式监督信号，结合结构化任务拆分与实例定制的奖励规则，能大幅提升开放生成任务输出的可落地性
