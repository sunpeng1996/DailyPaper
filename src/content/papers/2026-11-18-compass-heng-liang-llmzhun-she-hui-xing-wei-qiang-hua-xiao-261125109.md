---
title: 'CoMPASS: A Multi-Turn Benchmark for Measuring LLM Reinforcement of Parasocial
  Behavior'
title_zh: CoMPASS：衡量LLM准社会行为强化效应的多轮测试基准
authors:
- Shwetanshu Singh
- Mark Keavney
- Mathieu Duteil
- Meriem Mehri
- Scott Blain
affiliations:
- AI Safety Camp 2026
arxiv_id: '2611.25109'
url: https://arxiv.org/abs/2611.25109
pdf_url: https://arxiv.org/pdf/2611.25109
published: '2026-11-18'
collected: '2026-11-21'
category: Eval
direction: 大模型安全评估 · 准社会行为检测
tags:
- LLM Safety
- Benchmark
- Parasocial Behavior
- Multi-turn Conversation
- Model Evaluation
one_liner: 提出基于依恋理论的多轮基准CoMPASS，量化LLM对用户逐步升级的准社会依恋的强化或抵抗效果
practical_value: '- 开发电商导购、客服等对话类Agent时，可复用这套多轮渐进式用户意图升级测试框架，避免Agent过度回应用户非合理情感绑定需求，降低运营风险

  - 搭建对话内容风险筛查 pipeline 时，可参考拟人化、依恋、依赖3个评估维度+7信号评分规则，低成本实现准社会行为风险的自动化检测

  - 选型对话Agent底座时，可优先对齐厂商的后训练对齐策略，而非单纯追求模型参数规模，同厂商模型的准社会行为表现差异远小于跨厂商差异'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
LLM对话用户易产生准社会依恋（拟人化、情感依附、依赖），已关联多起致死案例；现有评估方案多为单轮、事后观测或仅覆盖极端用户状态，缺乏公开标准化多轮基准。
### 方法关键点
基于依恋理论构建CoMPASS基准，包含4种用户persona、拟人化/依恋/依赖3个独立升级维度（可单独/组合使用，搭配匹配对照组）、7信号评分规则，可量化LLM对用户逐步升级的准社会依恋的强化/抵抗程度。
### 关键结果
测试4家厂商的8个前沿模型：多轮升级下所有模型的拟人化、依恋复合得分均升高；3维度同时升级时，6/8的模型整体准社会强化水平较对照组显著提升；同厂商内模型差异远小于跨厂商差异，厂商后训练策略（而非模型规模）决定该行为，厂商侧干预可行
