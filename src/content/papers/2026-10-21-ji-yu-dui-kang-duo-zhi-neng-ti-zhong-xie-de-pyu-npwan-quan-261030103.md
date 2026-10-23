---
title: Did the Problem Actually Get Harder? Testing LLMs on Paired P and NP-Complete
  Problems Hardened by Adversarial Multi-Agent Rewriting
title_zh: 基于对抗多智能体重写的P与NP完全问题配对LLM推理能力测试
authors:
- Nurul Labib Sayeedi
- Md. Faiyaz Abdullah Sayeedi
- Zabir Al Nazi
- Mahbub E Sobhani
- Shubhashis Roy Dipta
affiliations:
- United International University
- BRAC University
- University of California, Riverside
- University of Maryland, Baltimore County
arxiv_id: '2610.30103'
url: https://arxiv.org/abs/2610.30103
pdf_url: https://arxiv.org/pdf/2610.30103
published: '2026-10-21'
collected: '2026-10-23'
category: Eval
direction: LLM推理能力评估 · 多智能体难例生成
tags:
- LLM Reasoning
- Multi-Agent
- Benchmark
- Adversarial Generation
- Evaluation
one_liner: 构造配对P/NP完全问题的难例基准，区分LLM的推理能力与对问题描述的记忆
practical_value: '- 对抗多智能体重写难例的方法可直接复用，用于构造搜索推荐场景下的query理解、排序策略鲁棒性测试集，替代人工构造难case的高成本方案

  - 区分模型记忆与真实推理能力的评估范式，可迁移到LLM4Rec效果验证，避免误判模型对训练集见过的热门item/query的记忆为泛化能力

  - 可执行有效性门控的设计，可在业务自动生成测试样本时保证标注正确性，降低人工校验成本'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM推理基准要么固定任务描述，要么忽略问题复杂度分类，无法区分模型输出是依赖记忆还是真实推理能力。
### 方法关键点
1. 构建P2NPCBench基准，覆盖12个问题家族，每个NPC问题配相同场景的P类孪生问题，仅存在单结构差异；
2. 提出AgentGAN对抗多智能体框架：生成器重写问题描述直到冻结代码模型答错，同时通过可执行有效性门保证改写前后答案、复杂度类不变，最终得到2114条人工校验的难例。
### 关键结果
测试12款闭源/开源LLM：NPC问题pass@1为35.4%，远低于P类的63.8%；95.1%的模型-问题对在NPC类上错误率更高；10倍运行时长仅将NPC准确率从28.5%提升至31.9%，错误主要来自代码错误而非运行慢；难例改写后两类准确率差距从24.8缩小到14.6，证明原差距部分来自对课本表述的熟悉度而非真实推理能力。
