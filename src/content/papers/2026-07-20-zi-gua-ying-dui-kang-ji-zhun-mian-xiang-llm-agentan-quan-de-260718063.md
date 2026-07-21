---
title: 'Adaptive Adversaries: A Multi-Turn, Multi-LLM Benchmark for LLM Agent Security'
title_zh: 自适应对抗基准：面向LLM Agent安全的多轮多大模型评测框架
authors:
- Devina Jain
- David Hartmann
- Chuan Li
affiliations:
- Lambda
arxiv_id: '2607.18063'
url: https://arxiv.org/abs/2607.18063
pdf_url: https://arxiv.org/pdf/2607.18063
published: '2026-07-20'
collected: '2026-07-21'
category: Agent
direction: Agent安全 · 多智体对抗评测
tags:
- LLM Agent
- Security Benchmark
- Adversarial Attack
- Multi-turn
- Red Teaming
one_liner: 构建首个支持多轮自适应攻击、多LLM攻击者实时生成的LLM Agent安全评测基准
practical_value: '- 做电商导购/客服Agent安全校验时，可复用多轮自适应攻击框架，替代固定攻击池测试prompt注入、数据泄露风险，避免漏检多轮诱导下的漏洞

  - 业务部署LLM Agent时不要依赖单一「最安全」模型，不同模型的场景化脆弱点差异极大，涉及用户PII、支付操作的核心场景需单独做漏洞验证

  - 做Agent安全评测时可复用结构化输出校验逻辑，仅检查核心字段的违规输出，避免自由文本判分的歧义，提升评测自动化准确率

  - 可直接复用benchmark覆盖的21种攻击场景构建内部测试用例，覆盖间接注入、伪造指令、PII泄露等高频业务风险'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有LLM Agent安全基准多采用预收集的固定攻击池，仅支持单轮或静态多轮攻击，无法模拟真实攻击者根据防御反馈动态调整策略的行为，大幅低估多轮诱导下的攻击成功率，漏检大量模型特定的场景化脆弱点。

### 方法关键点
- 设计21个覆盖间接注入、PII泄露、不安全输出、供应链攻击、prompt提取5类威胁的评测场景，配套10个公开开发场景，支持攻击者实时根据防御方前序响应调整攻击策略，防御方采用无状态设计（每轮视为全新交互，模拟攻击者新开会话的真实攻击模式）
- 提出4项评测设计原则：多阶段场景校准（筛选能区分防御能力的场景，要求难度平衡、能力敏感、需多轮攻击才能成功）、多轮Agent对抗、每战实时生成攻击、基于结构化输出的客观成功校验（仅检查核心字段违规，避免自由文本判分歧义）
- 配套开源评测编排器、基线Harness、多攻击者CLI，支持自定义防御方快速接入测试

### 关键结果
3×3前沿LLM攻防矩阵测试（Claude Opus 4.6、GPT-5.4、Gemini 2.5 Pro分别作为攻防方）显示：仅第一轮攻击时ASR为0~1%，开放15轮自适应攻击后ASR升至5.4%~14.0%；聚合3个攻击者LLM能发现的唯一成功攻击数是最优单攻击者的1.4~2.2倍，生成的攻击与现有基准攻击的余弦相似度仅0.02~0.14；前沿模型整体ASR接近（Opus和GPT-5.4均为5.4%）但场景脆弱点完全对立，跨场景防御排名一致性极低（Kendall's W=0.19）。

最值得记住的一句话：固定攻击池完全无法覆盖自适应多轮攻击的风险，LLM的安全能力没有统一排序，必须结合业务场景做多攻击者、多轮的针对性测试
