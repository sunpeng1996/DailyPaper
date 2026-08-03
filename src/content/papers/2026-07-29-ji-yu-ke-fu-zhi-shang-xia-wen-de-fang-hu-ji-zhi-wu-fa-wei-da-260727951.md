---
title: Safeguards Based on Copyable Context Cannot Provide Reliable Safety for LLMs
title_zh: 基于可复制上下文的防护机制无法为大模型提供可靠安全保障
authors:
- Pingyu Wu
- Lingyao Zhu
- Weiming Zhang
- Nenghai Yu
affiliations:
- University of Science and Technology of China
- Hefei AiDA Lab
- Zhejiang Wanli University
arxiv_id: '2607.27951'
url: https://arxiv.org/abs/2607.27951
pdf_url: https://arxiv.org/pdf/2607.27951
published: '2026-07-29'
collected: '2026-08-03'
category: LLM
direction: 大模型安全 · 防护机制有效性验证
tags:
- LLM Safety
- Safety Guardrail
- Trusted Credential
- Dual-use Task
- Adaptive Attack
one_liner: 提出大模型安全三元悖论，证明可复制上下文防护不可靠并给出可信凭证补全方案
practical_value: '- 搭建LLM驱动的电商Agent/推荐系统时，不能仅依赖可复制的prompt、交互历史做安全校验，需叠加用户可信身份凭证降低攻击绕过风险

  - 做LLM内容输出审核时，需区分内容本身与下游使用场景，例如同一份竞品分析内容，对认证商家和未知用户可做分层权限输出

  - 涉及两用风险的LLM服务（如运营策略生成、广告投放方案输出）可参考安全三元悖论做tradeoff，要开放访问+高可用性需接受一定安全基线，要高可靠安全必须做可信身份准入'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有LLM安全防护（安全训练、请求/响应过滤等）仅基于可复制的请求上下文、交互历史做前置校验，无法应对两用任务风险：相同输出可同时帮助合法用户与攻击者，攻击者可模仿良性请求绕过防护。
### 方法关键点
1. 拆分模型输出能力与下游使用证据，推导可复制证据场景下攻击者获得帮助的最坏下限；
2. 提出安全三元悖论：有用能力、可靠安全、开放访问三者无法同时满足；
3. 给出基于不可复制可信凭证的防护补全方案，通过关联下游实际使用信息消除攻击下限。
### 关键结果
两用任务评估、自适应攻击测试、已落地可信访问项目的实测数据均验证了上述结论的实际有效性
