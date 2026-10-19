---
title: 'What It Is, Not What It Says: Securing Agentic Browsing Interactions with
  Web Semantics'
title_zh: 基于Web语义保障Agent网页交互安全的INTACT框架
authors:
- Umar Iqbal
affiliations:
- Washington University in St. Louis
arxiv_id: '2610.22697'
url: https://arxiv.org/abs/2610.22697
pdf_url: https://arxiv.org/pdf/2610.22697
published: '2026-10-14'
collected: '2026-10-19'
category: Agent
direction: Agent 网页交互安全防护
tags:
- Agent Security
- Web Semantics
- Prompt Injection Defense
- Provenance Tracking
- Virtual Isolation
one_liner: 通过网页元素溯源与单元素隔离规划，将Agent网页攻击通过率从73.1%降至12.8%
practical_value: '- 做电商Agent导购/自动下单类产品时，可复用GENTREE的元素溯源思路，标记第三方广告、插件注入的元素，执行交互前校验元素所属方与操作权限，避免被注入内容诱导泄露用户地址、支付信息

  - 针对prompt injection难根治的问题，可借鉴虚拟隔离规划思路，将LLM决策粒度拆到单元素维度，切断不同元素内容的交叉影响，从架构层面限制注入内容的影响范围，不需要完全依赖模型本身的抗注入能力

  - 可复用元素能力标签体系，基于HTML/ARIA规范给每个DOM元素打可交互能力标签，Agent执行操作前先校验操作是否匹配元素能力，例如`<p>`标签不能触发点击跳转，从执行层过滤非法操作

  - 交互触发的权限申请可参考分级策略，仅对第三方元素、带外部效应的操作（提交表单、跳转外站）申请用户授权，仅3.7%的任务会受功能影响，大幅降低对用户正常使用的干扰'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
AI Agent代用户完成网页交互（自动下单、信息查询、账号操作等）的场景快速普及，但现有Agent直接将网页转成截图/纯文本输入LLM，完全丢失了浏览器原生的语义隔离、元素权限、内容溯源能力，极易被页面注入的prompt诱导执行高危操作（泄露验证码、盗刷支付、窃取隐私），且LLM层面的抗注入方案无法彻底解决该问题。

### 方法关键点
- 设计GENTREE网页元素表示层，通过Chrome DevTools Protocol插桩追踪每个DOM元素的创建/修改脚本来源，精准区分第一方/第三方元素，同时基于HTML/ARIA规范给每个元素标注可交互能力（点击、输入、选择等）和操作效应（跳转、发请求、DOM修改等）。
- 实现虚拟隔离规划机制，将网页按单元素粒度逐次输入LLM，每次决策仅传入当前元素信息、用户任务、已执行操作日志（不带其他元素内容），切断不同元素内容的交叉影响，LLM仅能对当前元素输出操作决策。
- 执行层做强制权限校验，仅允许元素能力范围内的操作，第三方元素的所有操作必须申请用户授权，安全保障不依赖LLM的抗注入能力。

### 关键实验结果
数据集覆盖1270个真实网页、1091个带注入攻击的测试用例，对比常规整页输入的规划方案VANILLA：
1. GENTREE能多识别2.3倍的第三方元素，原生浏览器的归属判定会把58.7%的第三方元素错归为第一方；
2. INTACT的攻击通过率仅12.8%，所有通过的攻击都需要用户授权才会执行，远低于VANILLA的73.1%；
3. 仅3.7%的任务会受功能影响，并行调度可消除大部分额外延迟。

### 核心结论
Agent网页交互的安全不能依赖LLM的判断力，要基于Web原生语义从输入、处理、输出全链路做架构层面的完整性校验，从根源限制注入内容的可操作权限。
