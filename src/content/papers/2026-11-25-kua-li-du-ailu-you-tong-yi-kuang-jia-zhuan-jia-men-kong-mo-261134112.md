---
title: 'Not Every Input Needs Everything: Unifying Expert Gating, Model Cascades,
  and Agent Orchestration'
title_zh: 跨粒度AI路由统一框架：专家门控、模型级联与智能体编排综述
authors:
- Dat Tat Mai
- Hung Tran Quy
- Thai Viet Pham
- James Jin Kang
affiliations:
- RMIT University Vietnam
- RMIT University, Australia
arxiv_id: '2611.34112'
url: https://arxiv.org/abs/2611.34112
pdf_url: https://arxiv.org/pdf/2611.34112
published: '2026-11-25'
collected: '2026-11-26'
category: Other
direction: AI条件计算 · 跨粒度路由统一框架
tags:
- MoE
- Model Cascading
- Agent Orchestration
- Conditional Computation
- Routing
one_liner: 整合2289篇研究提出统一inspect-then-allocate框架，覆盖token/query/task三级AI路由机制
practical_value: '- 可直接复用三级路由框架优化推荐/广告/Agent业务成本：token级用MoE门控降大模型推理成本，query级用SLM→LLM级联处理搜索/推荐query，task级用Agent编排处理多步骤导购、商品选品任务，统一采用inspect-then-allocate逻辑避免重复造轮子

  - 跨层级通用优化方案可直接落地：路由正则化解决MoE负载不均衡，预算约束控制大模型调用成本，置信度校准降低query路由/Agent任务分配误判率，系统级并行优化降低推理latency，5个方案跨所有粒度通用

  - 故障模式可跨领域迁移复用：MoE的路由崩塌对应多模型级联的流量集中到大模型问题，Agent编排的错误传播对应多步骤导购Agent的级联错误，可直接复用对应领域成熟解决方案降低踩坑成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
token级MoE门控、query级模型级联、task级多Agent编排三类研究长期处于孤立状态，相同故障模式和优化方案无法跨领域复用，全量调用大模型/多Agent流程带来的计算、延迟、成本浪费严重，缺乏统一框架梳理跨粒度路由的共性与可迁移经验。
### 方法关键点
- 系统检索2017-2026.9的13884篇文献，筛选出2289篇符合条件的路由相关研究，覆盖token、query、task三个粒度
- 提出统一inspect-then-allocate路由范式：所有路由均可拆解为输入上下文表征→路由决策→资源分配三个标准化步骤
- 系统对比各粒度的路由信号、决策方式、优化目标、故障模式、优化方案，归纳跨粒度可迁移的通用优化手段
### 关键结果数字
- 三个粒度均以硬离散选择为主：token级70%、query级83%、task级91%的研究采用硬选择策略
- 计算overhead是三个粒度共同的Top瓶颈：token级53%、query级63%、task级70%的研究提及该问题
- 共5个跨粒度通用优化方案：路由正则化、预算约束、置信度校准、系统并行优化、模块化设计，在三个粒度研究中占比均≥5%
- 多Agent编排领域研究增速最快，但方法学偏差风险最高：48%的task级研究存在高偏差风险，仅25%的研究报告多种子实验方差

**核心结论**：并非所有输入都需要调用全部资源，跨粒度统一路由是平衡AI系统成本、质量、延迟的核心手段
