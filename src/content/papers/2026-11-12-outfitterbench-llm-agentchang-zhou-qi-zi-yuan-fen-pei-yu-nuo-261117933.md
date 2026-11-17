---
title: 'OutfitterBench: Evaluating LLM Agents on Long-Horizon Resource Allocation
  and Commitment Coordination'
title_zh: OutfitterBench：LLM Agent长周期资源分配与承诺协调评测基准
authors:
- Jie Huang
- Yuecheng Hong
- Yao Chen
- Shengding Jiao
- Xudong Liu
- Qiang Ye
affiliations:
- Harbin Institute of Technology
- Peking University
- University of Science and Technology of China
- Independent Researcher
arxiv_id: '2611.17933'
url: https://arxiv.org/abs/2611.17933
pdf_url: https://arxiv.org/pdf/2611.17933
published: '2026-11-12'
collected: '2026-11-17'
category: Agent
direction: Agent长周期资源分配基准评估
tags:
- AgentBenchmark
- LongHorizonPlanning
- ResourceAllocation
- LLM
- BusinessSimulation
one_liner: 搭建户外装备租赁仿真基准测试LLM Agent长时资源分配与履约协调能力
practical_value: '- 做共享租赁、服务预约类履约Agent可复用「资源占用+周转时间+履约约束」的状态校验逻辑，避免超卖/订单冲突

  - 长周期运营Agent评估必须加入简单规则基线做对照，避免LLM推理不稳定导致整体收益跑输基础规则

  - 电商动态定价/库存调度场景可参考「承诺价值对比+调整成本核算」逻辑，平衡即时收益和长期履约风险

  - 多步决策Agent的状态传递可借鉴「每日会话+持久化记录+交接笔记」设计，降低长时上下文遗忘的影响'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM Agent长周期评测多聚焦工具使用、策略探索，鲜有覆盖「历史决策形成的履约承诺约束未来资源分配」的真实业务场景，而这类场景是电商租赁、供应链调度、服务预约等领域Agent落地的核心痛点，缺乏专门基准检验Agent在资源约束下的长期决策连贯性。

### 方法关键点
- 搭建户外装备租赁仿真环境，覆盖200天运营周期+14天结算周期，融合46款淘宝真实商品属性、北京历史天气数据、1100+预约请求，决策目标为最大化最终资产价值（现金+设备残值-负债）
- 核心评测两个维度：1）跨期可行性维护：能否确保历史承诺的预约单不与后续资源分配冲突、预留设备周转/清洁时间；2）跨期资源估值：能否在不确定需求下对比不同资源占用的收益、灵活调整库存/定价/预约规则
- 设计固定规则基线Calendar：基于公开状态、固定定价/库存/履约规则运营，作为Agent性能的参照标准

### 关键实验
对比7款前沿LLM与规则基线的双种子平均表现：仅GPT 6.1 Sol以2556.78元的净收益超过规则基线的1119.51元，其余多款LLM收益低于基线，最差的DeepSeek V4.1 Flash净收益为-573.30元；表现差的Agent普遍存在两个问题：1）21%~34%的预约单存在资源缺口，14%~20%的已确认预约被后续冲突决策影响；2）资源周转率仅为Top模型的70%左右，定价偏低导致履约量高但收益低。

### 核心结论
长周期运营Agent的核心能力是「稳定应用约束规则+动态权衡不同时间点的资源收益」，简单规则基线的表现往往超过大多数通用LLM Agent。
