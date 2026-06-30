---
title: 'PolicyGuard: A Dialogue-Grounded Sub-Agent Verifier for Policy Adherence in
  LLM Agents'
title_zh: PolicyGuard：面向LLM智能体政策合规的对话上下文子智能体验证器
authors:
- Seongjae Kang
- Taehyung Yu
- Sung Ju Hwang
affiliations:
- KAIST
- DeepAuto.ai
arxiv_id: '2606.29225'
url: https://arxiv.org/abs/2606.29225
pdf_url: https://arxiv.org/pdf/2606.29225
published: '2026-06-27'
collected: '2026-06-30'
category: Agent
direction: LLM Agent 合规验证 · 子智能体设计
tags:
- LLM Agent
- Policy Compliance
- Sub-agent
- Tool Calling
- Dialogue Grounding
one_liner: 提出兼具对话感知政策推理与可执行修复的子智能体验证器，提升LLM智能体流程级合规性
practical_value: '- 电商客服/售后类LLM智能体做合规校验时，可复用「离线LLM自动生成工具检查清单+在线子智能体全对话校验」架构，覆盖绝大多数流程级合规要求

  - 拦截违规调用后，返回对话上下文相关的明确修复提示，而非静态报错，能减少一半以上的重试轮次，同时降低误拦截率

  - 仅对变更型工具调用做校验，跳过只读查询类调用，验证任务本身轻量，小模型也可承接，平衡合规性与推理成本

  - 企业面向C端的智能体政策，约三分之二是流程级要求而非参数级，验证必须接入全对话历史，这个结论可直接指导架构设计'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM智能体政策合规方案多为参数级静态校验，仅检查工具调用参数，无法处理占比约三分之二的流程级合规要求（如退款前验证身份、预订前获取用户确认）。这类方案看不到完整对话历史，也无法给出针对性的修复指引，导致合规率低、误拦截多，严重影响用户体验。

### 方法关键点
- 架构：在Agent与环境之间插入子智能体验证器，仅拦截变更型工具调用，只读调用直接放行，控制额外推理成本
- 离线预处理：用LLM四步流水线将原始政策文本自动转换成每个变更工具的YAML检查清单，无需人工编写，要求分为数据校验和流程校验两类
- 在线校验：验证器读取完整对话历史，结合原始政策文本+检查清单逐要求判断，违规则拦截并生成上下文相关的修复提示返回Agent，不执行工具调用

### 关键实验结果
在τ2-Bench航空领域50个任务测试，对比原生ReAct Agent、TOOLGUARD基线，在GPT 5.4/Claude Sonnet 4.6/Gemini 2.5 Pro三个模型上，POLICYGUARD的PASS4（四次试验全通过的任务占比）分别提升+12.0pp/+6.0pp/+12.0pp，违规召回达到近100%，误拦截率仅为参数级方案的一半，近错失率（跳过必要流程仍执行）在Claude上从35.5%降至4.2%。

### 最值得记住的结论
企业C端智能体的多数合规要求是流程级，依赖对话上下文，必须用对话感知的验证方案才能覆盖
