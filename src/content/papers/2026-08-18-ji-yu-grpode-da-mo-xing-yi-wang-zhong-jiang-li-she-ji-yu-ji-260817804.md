---
title: An Empirical Study of Reward Specification and Benchmark Reliability in GRPO-based
  LLM Unlearning
title_zh: 基于GRPO的大模型遗忘中奖励设计与基准可靠性实证研究
authors:
- Rubén Balbastre
- Juan Manuel Orduña
- Mariano Pérez
affiliations:
- University of Valencia
arxiv_id: '2608.17804'
url: https://arxiv.org/abs/2608.17804
pdf_url: https://arxiv.org/pdf/2608.17804
published: '2026-08-18'
collected: '2026-08-19'
category: Training
direction: LLM训练 · GRPO遗忘优化
tags:
- GRPO
- LLM Unlearning
- Reward Engineering
- LoRA
- LLM-as-Judge
- Benchmark
one_liner: 对比4种GRPO遗忘奖励设计与SFT预热策略，揭示基准分数无法等价表征实际遗忘行为
practical_value: '- 做基于GRPO/RLHF的内容合规过滤、敏感信息擦除时，不要仅依赖基准指标，必须加LLM/人工审计实际输出，避免出现全量拒绝回复的假成功

  - 冷启动GRPO优化目标行为时，先做SFT预热扩增目标行为的采样概率，解决大模型策略支持不足导致的优化无信号问题

  - 奖励设计优先选型rubric-based LLM judge方案，对比词汇/反拒绝奖励，可同时实现低信息泄漏+高回复有用性，7B模型下语义泄漏率可低至1.6%

  - 多维度评估指标不可互相替代：基准分测目标压制、held-out审计测泛化行为、训练rollout审计测优化分布内表现，需组合使用'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM遗忘任务仅考核目标知识压制、非目标能力保留两个核心指标，忽略了目标相邻prompt下，模型应输出无泄漏的宽泛主题回答而非直接拒绝的实际需求；同时GRPO类RL优化存在奖励 hacking、基准评估结果与实际输出行为不一致的问题，缺乏对不同奖励设计效果的系统性对比。
### 方法关键点
- 基于Qwen2.5-Instruct全系列模型+LoRA微调搭建GRPO遗忘训练框架，对比4类奖励设计：R0-Lex（词汇匹配压制目标）、R1-AntiRefusal（加反拒绝约束）、R2-Rubric（LLM judge偏好无泄漏的宽泛有用回答）、R4-Refusal（对比组，奖励拒绝行为）
- 引入SFT预热机制，先让模型学习宽泛主题回答模式，解决冷启动下GRPO无有效优化信号的问题
- 搭建三层评估体系：RWKU基准指标、held-out样本审计、训练终端rollout审计，多维度刻画实际遗忘行为
### 关键结果
基于RWKU真实知识遗忘基准测试，暖启动下R2-Rubric方案效果最优：3B模型宽泛主题有用性达90.6%，语义泄漏率仅3.9%，拒绝率低于1%；冷启动下小模型易出现拒绝崩溃，0.5B/1.5B模型R0-Lex冷启动拒绝率达100%；相同RWKU遗忘分数下，可能对应拒绝崩溃、残留泄漏、合规宽泛回答等完全不同的行为模式。

**最值得记住的一句话**：仅凭基准遗忘分数无法判定LLM遗忘的实际效果，必须结合多维度行为审计确认最终输出模式。
