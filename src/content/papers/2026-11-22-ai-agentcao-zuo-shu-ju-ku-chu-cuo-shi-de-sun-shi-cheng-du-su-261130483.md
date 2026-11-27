---
title: When an AI agent makes a mistake in a database, what decides the damage?
title_zh: AI Agent操作数据库出错时的损失程度影响因素研究
authors:
- Abdullah Kaya
- Cevheri Bozoglan
- Yusuf Gundogdu
affiliations:
- LibreDB Studio project
arxiv_id: '2611.30483'
url: https://arxiv.org/abs/2611.30483
pdf_url: https://arxiv.org/pdf/2611.30483
published: '2026-11-22'
collected: '2026-11-27'
category: Agent
direction: Agent 数据库操作风险管控
tags:
- AI Agent
- Database Security
- Tool Calling
- Risk Evaluation
- MoE
one_liner: 量化对比模型、防护层、数据库引擎三类因素对Agent操作数据库出错后的损失影响
practical_value: '- 电商/推荐系统的数据库操作类Agent优先选用默认自带快照回滚能力的存储引擎（如Cassandra），可将误操作导致的原始业务数据（用户行为、订单等）永久损失降为0

  - 给Agent分配数据库账号严格遵循最小权限原则，搭配前置操作校验防护层，可大幅降低高危误操作的实际执行概率

  - 常规数据库操作任务的工具调用Agent，用4B~12B开源小模型或轻量MoE（3B激活参数）本地部署即可满足需求，无需调用大参数闭源模型，降低成本与延迟'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
当前AI Agent已广泛对接生产数据库执行操作，多次出现误删生产数据的事故，缺乏对Agent误操作后损失的三类影响因素（模型、防护层、数据库引擎）的量化对比结论。
### 方法关键点
1. Layer A：用脚本模拟22种典型数据库误操作，在4种关系型引擎上测试5种权限配置、2种恢复策略下的损失与恢复效果，累计完成874次恢复演练
2. Layer B：用6款4B~12B开源小模型+1款35B MoE（3B激活参数）驱动工具调用Agent，在9款主流数据库（PostgreSQL/MySQL等）上开展9468次风险场景测试，追加2916次补充测试覆盖3款同类引擎
### 关键结果数字
不同数据库的误操作破坏程度差异小，可恢复性差异极大；默认配置下原始数据永久损失率Cassandra为0，最高Valkey为11%、MySQL为7%；同类引擎（如MariaDB与MySQL）的风险表现完全一致。
