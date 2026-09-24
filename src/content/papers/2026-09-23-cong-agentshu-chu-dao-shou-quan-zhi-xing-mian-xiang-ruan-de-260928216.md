---
title: From Agent Output to Authorized Transition
title_zh: 从Agent输出到授权执行：面向软硬件工程的Agile-V保障框架
authors:
- Christopher Koch
arxiv_id: '2609.28216'
url: https://arxiv.org/abs/2609.28216
pdf_url: https://arxiv.org/pdf/2609.28216
published: '2026-09-23'
collected: '2026-09-24'
category: Agent
direction: Agent 工程输出授权保障
tags:
- agentic-engineering
- assurance
- lifecycle-gate
- evidence-admission
- Agile-V
one_liner: 提出跨软件、固件、PCB工程的Agile-V保障脊，统一Agent输出全链路授权校验规范
practical_value: '- 可复用「证据准入四规则」校验Agent生成的推荐策略、广告文案、代码变更：需绑定唯一artifact、固定政策基线、依赖最新、权限匹配，大幅降低幻觉输出上线风险

  - 全流程关卡留痕机制可直接迁移到LLM4Rec迭代管线：merge/上线前二次重检授权，审批/例外设置明确生效范围与有效期，方便问题回溯与追责

  - 若业务涉及Agent自动生成可执行配置（如促销规则、投放策略），可参考这套跨域契约框架做标准化管控，替代零散的人工审批逻辑'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
当前Agent可自主完成代码编写、固件构建、原理图生成等工程任务，但现有沙箱、审批、留痕等保障能力碎片化，缺乏统一标准校验Agent输出的合法性与安全性，无法支撑输出直接落地执行。
### 方法关键点
Agile-V Assurance Spine跨域过渡契约覆盖软件、固件、PCB工程场景，核心规则包括：
1. 证据准入四约束：需通过权威源验证属性、绑定精确artifact与冻结政策基线、依赖版本有效、满足风险适配的独立性与权限要求；
2. 全关卡决策留痕，审批/例外设置明确生效范围与时效，在合并、部署、发布等生效边界二次重检授权。
### 关键结果
输出统一术语体系、可组合架构、领域适配模板、开源实现映射方案与对抗性评估议程，未声称符合监管要求或生产性能优势。
