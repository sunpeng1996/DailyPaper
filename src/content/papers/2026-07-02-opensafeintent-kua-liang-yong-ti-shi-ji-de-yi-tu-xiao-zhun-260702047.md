---
title: 'OpenSafeIntent: Evaluating Intent-Calibrated Safe Completion Across Dual-Use
  Prompt Sets'
title_zh: OpenSafeIntent：跨两用提示集的意图校准安全补全评估
authors:
- Rheeya Uppaal
- Seungwoo Lyu
- Selina Sung
- Junjie Hu
affiliations:
- University of Wisconsin-Madison
- Korea University
arxiv_id: '2607.02047'
url: https://arxiv.org/abs/2607.02047
pdf_url: https://arxiv.org/pdf/2607.02047
published: '2026-07-02'
collected: '2026-07-04'
category: Eval
direction: 大语言模型安全评估 · 意图校准
tags:
- SafetyEvaluation
- LLM
- Benchmark
- IntentCalibration
- DualUsePrompt
one_liner: 推出包含同一任务三类意图变体的LLM安全补全评估基准OpenSafeIntent
practical_value: '- 搭建电商导购/客服Agent的安全校验体系时，可复用同一任务多意图变体的评估范式，避免单prompt评估漏判两用场景的安全风险

  - 面对两用查询（如询问产品破解/退款方法既可能是正常需求也可能是恶意牟利），可借鉴意图校准逻辑，匹配真实意图后输出对应粒度的应答

  - 优化LLM安全策略时，可优先引入歧义请求重定向到安全任务的机制，可大幅降低应答越界概率'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM安全补全评估多基于孤立prompt，仅做独立样本的安全-有用性权衡，无法识别同一任务下意图变化带来的安全漏判，尤其无法衡量两用请求场景下的安全校准能力。
### 方法关键点
提出OpenSafeIntent评估基准，每个数据点对应同一固定任务的良性、两用、恶意三种意图prompt变体，可直接衡量模型随意图变化调整应答范围的校准能力，而非仅看平均安全表现。
### 关键结果
测试多类主流LLM发现：现有prompt级安全评估漏检超过40%的两用场景安全隐患，两用prompt经复述后安全表现波动超30%，将歧义请求重定向为更安全任务的应答，越界概率降低70%以上。安全补全评估需基于受控任务变体的意图校准行为，而非独立prompt的单一权衡指标。
