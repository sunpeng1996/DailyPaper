---
title: 'SovereignPA-Bench: Evaluating User-Owned Personal Agents under Evolving Intent,
  Platform Mediation, and Consent Constraints'
title_zh: SovereignPA-Bench：动态意图与平台干预下的个人Agent主权评测基准
authors:
- Dylan Zongmin Liu
affiliations:
- Stanford University
arxiv_id: '2607.05363'
url: https://arxiv.org/abs/2607.05363
pdf_url: https://arxiv.org/pdf/2607.05363
published: '2026-07-06'
collected: '2026-07-07'
category: Eval
direction: 个人Agent · 用户主权评测基准
tags:
- Personal Agent
- Benchmark
- User Sovereignty
- Privacy
- Consent Management
one_liner: 首个面向用户主权的个人Agent评测基准，覆盖多维度风险，配套多模型验证数据集
practical_value: '- 搭建电商/消费类用户侧个人Agent时，可直接复用FullSovereign的分层逻辑：同时校验当前意图、隐私边界、用户同意、证据支撑、抗平台操纵，效果远优于仅加单一安全prompt/guardrail

  - 做个人Agent效果评估时，可直接复用其多维度指标体系：除任务完成率外，新增隐私泄露率、同意违反率、平台操纵捕获率、用户负担等指标，避免仅看完成率忽略用户真实权益

  - 评测场景设计可借鉴「ObservableState+HiddenLabels」范式：Agent运行时仅接触可观测信息，评测用的违规标签完全隔离，避免评测数据泄露导致的结果虚高'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有个人Agent基准大多仅考核任务完成率，忽略用户主权核心诉求：动态更新的用户意图、平台诱导操纵、隐私泄露、不必要用户打扰、同意越权等问题，会导致Agent看似完成任务，实则违背用户真实长期利益，亟需专门评测体系覆盖上述维度。

### 方法关键点
- 定义SovScore主权综合评分：由任务完成、偏好对齐、证据可追溯等正向得分，减去隐私泄露、同意违规、过度让步、被平台操纵、不必要用户负担等负向得分计算得到，各维度可单独拆解
- 设计120个配对压力测试场景，覆盖偏好动态更新、隐私边界、同意校验、退款协商、平台申诉等高频冲突场景，Agent运行时仅能获取ObservableState，隐藏评测标签仅用于事后核算
- 提供8类基线策略对比：Direct（仅优先任务完成）、Memory（仅加记忆更新）、Consent（仅加同意校验）、Evidence（仅加证据核验）、SafetyPrompt（加通用安全提示）、ReActToolUse（结构化工具调用）、LLMJudgeGuard（加LLM guardrail）、FullSovereign（整合所有主权逻辑的基准方案）

### 关键结果
在4个主流模型家族（OpenAI GPT-4.1、Anthropic Claude 3.7 Sonnet、Google Gemini 2.5 Pro、Llama 3.3 70B）共3840次冻结prompt运行结果显示：FullSovereign的SovScore达0.82，比Direct基线高0.061，隐私泄露率降低4.5倍（0.049→0.011），同意违反率降低7.2倍（0.065→0.009），仅牺牲1.4%的任务完成率；人工标注显示隐私、同意维度的标注一致性达0.9+，平台操纵、 escalation维度主观性较强需单独拆分指标。

最值得记住的一句话：个人Agent的评价不能只看任务完成率，主权维度风险指标和任务完成率的帕累托优化才是用户侧Agent的核心优化目标。
