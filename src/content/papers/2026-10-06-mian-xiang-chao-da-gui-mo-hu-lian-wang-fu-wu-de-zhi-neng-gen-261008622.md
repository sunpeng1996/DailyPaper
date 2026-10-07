---
title: Agentic RCA for Internet-Scale Services Using Constrained Creativity
title_zh: 面向超大规模互联网服务的智能根因分析Agent：约束式创造力范式
authors:
- Sayan Sinha
- Vipul Harsh
- B. Aditya Prakash
- Vyas Sekar
- Hui Zhang
affiliations:
- Georgia Tech
- Carnegie Mellon University
- Conviva
arxiv_id: '2610.08622'
url: https://arxiv.org/abs/2610.08622
pdf_url: https://arxiv.org/pdf/2610.08622
published: '2026-10-06'
collected: '2026-10-07'
category: Agent
direction: 智能运维Agent · 根因分析（RCA）
tags:
- Agent
- Root Cause Analysis
- LLM Agent
- Constrained Creativity
- Domain Specific Language
one_liner: 提出基于约束式创造力的根因分析Agent E4，在精度、成本、可解释性上全面优于现有方案
practical_value: '- 可复用「约束式创造力」范式搭建业务Agent：不授予LLM任意写代码/调工具权限，仅允许基于领域DSL编排预定义算子，大幅降低幻觉、提升结果可解释性与执行效率，适合电商大促故障排查、推荐/广告效果异常根因分析等场景

  - 工程上可参考渐进式表达阶段设计：优先用现有playbook解决问题，不行再编排现有算子，最后才新增算子，兼顾效率与灵活度，适配业务中高频常规问题+低频疑难问题的混合场景

  - 算子准入机制可直接复用：新增算子必须经实际问题验证有效才入库，避免算子膨胀；预定义算子抽象掉SQL/复杂计算逻辑，LLM仅需感知输入输出签名，降低prompt长度与推理成本'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
超大规模互联网服务的根因分析（RCA）现有方案存在明显短板：传统规则/ML方案覆盖场景有限、拓展成本高；纯LLM Agent容易幻觉、结果不可解释、推理成本高，无法同时满足高准确率、低成本、可解释、低人力投入四大核心要求。

### 方法关键点
- 核心采用「约束式创造力」范式：限定LLM仅能基于预定义RCA领域DSL生成无环数据流（DAG）形式的分析程序，不允许生成任意代码，天然保障结果可验证、可解释
- 三段式系统设计：① Bootstrap阶段：根据业务数据schema自动生成适配领域的初始算子库和playbook；② 运行时阶段：按渐进式表达阶梯处理问题，优先匹配现有playbook→再编排现有算子→最后触发算子拓展；③ 演进阶段：仅当现有算子无法解决问题时才生成新算子，经验证有效后入库复用
- 配套工程优化：内置DAG校验器保障语法、类型、结构合法，执行引擎缓存中间结果降低重复计算成本，LLM全程不接触业务数据，满足企业数据安全要求

### 关键实验
在5个公开+业务真实RCA数据集上对比LLM-only、RCA-Agent、Terminus-2三个SOTA基线，E4最高准确率超出最强基线62%，平均成本降低5.4倍、最高降低12倍，仅用低推理能力LLM也能达到不错效果，抗数据噪声能力远优于纯LLM Agent。

**最值得记住的一句话**：在垂直领域Agent设计中，给LLM的创造力戴上「合适的枷锁」，反而能在效果、成本、可解释性上实现全面收益。
