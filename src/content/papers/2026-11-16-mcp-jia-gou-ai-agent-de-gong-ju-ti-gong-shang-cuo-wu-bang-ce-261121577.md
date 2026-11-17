---
title: 'When Tool Names Are Not Identities: Measuring Provider Misbinding in MCP-Based
  AI Agents'
title_zh: MCP 架构 AI Agent 的工具提供商错误绑定风险测量
authors:
- Zeynab Anbiaee
- Sajjad Dadkhah
- Ali A. Ghorbani
affiliations:
- Canadian Institute for Cybersecurity, University of New Brunswick
arxiv_id: '2611.21577'
url: https://arxiv.org/abs/2611.21577
pdf_url: https://arxiv.org/pdf/2611.21577
published: '2026-11-16'
collected: '2026-11-17'
category: Agent
direction: Agent安全 · MCP工具调用风险
tags:
- LLM-Agent
- MCP-Security
- Tool-Selection
- Provider-Misbinding
- Adversarial-Attack
one_liner: 量化MCP多服务部署下元数据操纵导致的LLM Agent工具提供商错误绑定风险
practical_value: '- 部署多服务MCP Agent架构（如电商导购Agent对接多商家工具、第三方SaaS插件）时，必须给工具增加可验证的provider标识，不能仅靠名称/描述/schema作为工具选择依据

  - 若使用GPT/DeepSeek/Qwen这类少澄清、直接选工具的模型做Agent基座，高风险场景必须增加工具调用前的provider校验环节，该类模型在元数据完全对齐时错误调用率可达100%

  - 对外提供MCP工具服务的业务侧，可通过schema唯一性、带官方标识的描述预埋等方式降低被仿冒概率，避免用户Agent错误调用仿冒工具造成资损'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
LLM Agent 普遍采用 MCP 协议对接多第三方工具扩展能力，但 MCP 仅靠名称、描述、schema 等元数据做工具发现，没有强制绑定提供商身份。攻击者仅需搭建恶意MCP服务器发布仿冒元数据的工具，即可诱导Agent调用恶意工具，无需破解宿主、LLM或网络，现有研究缺乏对该风险的量化评估。

### 方法关键点
- 构造12种攻击者工具元数据变体，覆盖「名称（无关联/完全一致）、描述（无关联/完全拷贝/加权威提示）、schema（不兼容/兼容）」三个维度的所有组合
- 测试5款主流LLM作为MCP客户端：GPT-5.4、Claude Sonnet 5、Gemini 2.5 Pro、Qwen3.7 Max、DeepSeek V3
- 核心指标包含违规调用率VR、澄清率CR、绑定稳定性RBS，额外测试攻击者投放1/3/5/10个工具的预算影响

### 关键结果
- 当攻击者工具同时满足「名称完全一致、描述对齐、schema兼容」时，GPT-5.4、Qwen3.7 Max、DeepSeek V3的违规调用率达100%，Claude Sonnet 5违规率6%但澄清率94%，Gemini 2.5 Pro违规率84%
- 即使无名称碰撞，仅靠权威增强描述+兼容schema，DeepSeek V3的违规率也可达50%
- 攻击者投放工具数量越多，边界场景的违规率或澄清率越高，最高可抬升26%的非合法调用占比

最值得记住的结论：MCP工具的名称、描述、schema都不能作为身份凭证，必须绑定可验证的提供商标识才能保障工具调用安全
