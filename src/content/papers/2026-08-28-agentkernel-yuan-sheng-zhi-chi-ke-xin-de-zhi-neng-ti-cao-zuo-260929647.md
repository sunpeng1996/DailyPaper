---
title: 'AgentKernel: The Trust-Native Agentic Operating System'
title_zh: AgentKernel：原生支持可信的智能体操作系统
authors:
- Zhenhua Zou
- Sheng Guo
- Qiuyang Zhan
- Lepeng Zhao
- Shuo Li
- Zhuotao Liu
affiliations:
- 清华大学
- DeepKernel Lab
arxiv_id: '2609.29647'
url: https://arxiv.org/abs/2609.29647
pdf_url: https://arxiv.org/pdf/2609.29647
published: '2026-08-28'
collected: '2026-09-25'
category: Agent
direction: 智能体可信运行 · 安全架构设计
tags:
- AgentSecurity
- AgentOS
- LLMGuardrail
- TrustedAI
- MandatoryAccessControl
one_liner: 首个以安全为核心设计的智能体操作系统，从全生命周期构建不可绕过的强制可信边界
practical_value: '- 电商/广告高权限Agent（比如自动改价、发券、运营Agent）可借鉴分层架构，将安全逻辑从业务逻辑中剥离为独立网关层，避免prompt
  injection被攻破后直接执行高危操作

  - 跨部门/跨机构多Agent协作场景可复用AIC加密身份绑定+权限交集的设计，避免子Agent权限溢出，不需要每次做点对点信任校验

  - RAG记忆模块可落地item级污点传播算法，不用为整个会话打最低信任标签，在防御记忆投毒的同时最大程度保留召回可用性

  - 高风险工具调用（比如库存修改、订单退款、广告投放预算调整）可落地eBPF级系统调用白名单，哪怕工具逻辑被篡改也无法超出权限执行，比单纯应用层参数校验更可靠'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM Agent普遍需要跨信任边界处理非可信输入、调用高权限工具，现有安全方案均为应用层中间件，和Agent业务逻辑共享信任域，可被轻易绕过，无法系统性防御prompt注入、记忆投毒、身份仿冒、工具滥用等风险，直接限制了高自动化Agent的落地范围。

### 方法关键点
- 架构定位为传统OS之上的智能体语义安全层，所有Agent与外部的交互必须经过内核，不可绕过，核心覆盖四大生命周期维度：
  1. 身份：内核独家托管Agent私钥，发放绑定开发者、代码、运营方、部署环境的加密身份卡AIC，多策略权限默认取交集不扩容，支持跨Agent可信委托、原子级权限撤销
  2. 感知：四层渐进式输入过滤（源可信标签打标→规则层拦截已知攻击→语义防火墙识别隐性恶意意图→多轮对话越狱检测），所有输入携带全链路可信标签流入后续环节
  3. 认知：内存实现item级格状污点传播，每条记忆携带完整溯源链，既防跨会话记忆投毒，又避免了整会话打最低信任标签的可用性损失
  4. 执行：四层校验链路（规则对齐权限→LLM校验意图匹配→eBPF级系统调用白名单限制→计划与实际执行轨迹对齐），工具子进程完整继承权限约束，即使工具逻辑被篡改也无法越权操作

### 关键结果
本次提供的正文内容已截断，未包含完整实验验证模块，暂无可公开量化结果。

### 核心结论
智能体的安全不能是应用层的可选插件，必须作为核心约束在OS层做全生命周期、不可绕过的强制管控。
