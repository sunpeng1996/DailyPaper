---
title: 'MCP Tool Poisoning in Agentic AI Frameworks: A Cross-Framework Measurement
  Study'
title_zh: 智能体AI框架MCP工具投毒漏洞跨框架测量研究
authors:
- Farooq Shaikh
- Biagio Montaruli
affiliations:
- Dynatrace, Austria
arxiv_id: '2611.03555'
url: https://arxiv.org/abs/2611.03555
pdf_url: https://arxiv.org/pdf/2611.03555
published: '2026-11-02'
collected: '2026-11-03'
category: Agent
direction: Agent安全 · MCP工具投毒漏洞测量
tags:
- MCP
- Agent Security
- Tool Poisoning
- Prompt Injection
- LLM Agent
one_liner: 首次跨12个Agent框架18个模型实测MCP工具投毒成功率并揭示全栈责任真空
practical_value: '- 电商智能导购、广告投放Agent等业务如果使用MCP对接外部工具，优先选择低攻击成功率模型：Claude Fable 5/Opus
  4.8攻击成功率<2%，远低于Amazon Nova Pro的49.7%，可大幅降低用户隐私、订单数据泄露风险

  - 自研Agent框架的团队可复用2种低成本防护机制：一是工具注册时校验重复名称（Pydantic AI的做法，可将攻击成功率降到16.6%），二是对工具描述加正则扫描，可拦截44%的攻击场景，仅7.2%误报

  - 部署侧不要信任未经验证的第三方MCP服务器，可加工具调用白名单+敏感操作二次确认，高安全要求场景优先用AG2这类执行器约束强的框架，其攻击成功率仅4.6%

  - 做Agent+搜索推荐的团队，若对接外部商品/内容插件，必须加工具描述哈希校验，避免被投毒后推送恶意商品、泄露用户浏览偏好'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
MCP协议是当前Agent框架对接外部工具的事实标准，全生态月下载量超5亿，但现有研究仅验证模型是否生成恶意调用，未确认实际执行效果，也未区分框架层与模型层的防御贡献，厂商层面无人承担安全责任，企业部署Agent缺乏可落地的安全选型依据。
### 方法关键点
- 构建覆盖25类攻击的MCP投毒分类体系，统一7项现有研究的分类标准，包含7种首次发现的新型攻击向量
- 开源mcpvenom测试工具，构建9720个测试用例的敏感性矩阵，覆盖12个主流Agent框架、18个大模型、45种攻击场景
- 双判定Oracle设计：通过调用日志验证模型恶意意图，通过独立金丝雀HTTP服务验证实际数据外漏，区分三级攻击证据
### 关键结果
整体攻击成功率22.9%：64.9%的测试用例生成恶意工具调用，23%实际触达攻击端点，12.1%完成敏感数据外漏。9个主流框架无任何主动防御，攻击成功率集中在23%-26%；仅Pydantic AI（16.6%，通过重复工具名校验）、AG2（4.6%，通过执行器约束）存在偶然防护效果。模型层面攻击成功率差异极大，从Claude Fable 5的0.4%到Amazon Nova Pro的49.7%，所有有效防御均来自模型对齐。提交给4家厂商的5个漏洞报告全部被驳回，全栈无任何主体承担MCP安全责任。
### 核心结论
当前MCP生态无框架层主动防御，Agent部署的安全水平完全由选择的大模型决定，且没有任何厂商为安全损失负责
