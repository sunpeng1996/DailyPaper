---
title: 'Trace Integrity for LLM Data Agents: A Vision for Auditable Structured Reasoning
  in Real-World Systems'
title_zh: LLM数据代理的链路完整性：真实系统可审计结构化推理框架
authors:
- Srimonti Dutta
- Akshata Kishore Moharir
affiliations:
- W AI USA Research Labs
arxiv_id: '2608.26036'
url: https://arxiv.org/abs/2608.26036
pdf_url: https://arxiv.org/pdf/2608.26036
published: '2026-08-26'
collected: '2026-08-27'
category: Agent
direction: Agent 可审计结构化推理与可靠性评估
tags:
- LLM Agent
- Trace Integrity
- Auditable Reasoning
- CAIT Rate
- Execution Contract
one_liner: 提出Trace Integrity评估标准、CAIT指标与执行合约，解决LLM数据代理答案正确但推理链路无效的问题
practical_value: '- 电商运营/分析师使用的数据查询Agent，可直接引入Trace Integrity的7个校验维度做上线前检测，降低SQL生成错误导致的运营决策失误

  - 线上Agent新增CAIT Rate监控指标，避免仅看答案准确率高估系统可靠性，尤其适配高风险的营收核算、库存盘点类查询场景

  - 给数据类Agent新增执行合约前置校验步骤，先输出结构化计算承诺（关联表、join规则、过滤条件、聚合逻辑）再执行，验证通过后才返回结果，降低隐式错误

  - 电商财务、广告结算等合规场景可存储执行合约作为审计凭证，满足监管回溯要求'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM数据Agent仅靠答案准确率评估可靠性存在严重缺陷，结构化任务中经常出现答案正确但实际计算链路（如SQL的过滤、聚合、join规则）不符合用户意图的隐式错误，自然语言推理的自由性和结构化计算要求的精确性之间的**Structure Gap**导致这类错误无法被现有评估方式识别，在运营、财务、医疗等高风险场景会造成严重决策失误。

### 方法关键点
- 定义**Trace Integrity**作为核心可靠性标准，要求计算链路满足显式、可执行、schema合法、算子符合意图、可重放、答案一致、可审计7个维度
- 提出**Execution Contract**结构化artifact，提前绑定用户意图、schema元素、算子计划、假设、可执行查询、验证状态和答案关联，作为审计载体
- 提出**CAIT Rate**指标，衡量答案正确但链路无效的样本占正确答案的比例，量化隐式错误风险
- 提出隔离原则，默认要求Agent在访问数据值之前先明确计算计划，避免根据结果回溯伪造合理链路

### 关键实验
在BIRD Mini-Dev 100个样例上测试，对比Direct SQL、Operation Summary + SQL、Contract-First SQL三种方案，答案准确率分别为20%、22%、24%，Trace Integrity通过率分别为39%、43%、40%，CAIT Rate分别高达55%、59.1%、45.8%，证明三类指标互相独立，仅靠答案准确率会严重高估系统可靠性。

### 核心结论
LLM数据Agent的可靠性不能仅看答案是否正确，必须确保背后的计算链路可检查、可重放、可审计。
