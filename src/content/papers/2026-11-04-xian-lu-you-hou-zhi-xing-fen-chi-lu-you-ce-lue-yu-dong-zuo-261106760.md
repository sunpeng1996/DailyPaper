---
title: 'Route First, See Later: Enabling Vision Agents to Reason Scientifically by
  Separating Routing Policy from Action Spaces'
title_zh: 先路由后执行：分离路由策略与动作空间的科学视觉Agent架构
authors:
- Shubhabrata Mukherjee
- Jeffrey Donatelli
- Daniela Ushizima
affiliations:
- Lawrence Berkeley National Laboratory
- University of California, San Francisco
- University of California, Berkeley
arxiv_id: '2611.06760'
url: https://arxiv.org/abs/2611.06760
pdf_url: https://arxiv.org/pdf/2611.06760
published: '2026-11-04'
collected: '2026-11-05'
category: Agent
direction: Agent 工具路由与执行解耦优化
tags:
- Agent
- Tool Routing
- Action Space
- Vision Agent
- Intent Understanding
one_liner: 提出ZETA架构解耦意图路由与视觉执行，大幅提升语义相近工具的路由准确率
practical_value: '- 工具调用类Agent可复用「路由-执行分离」架构，独立评估路由错误和执行错误，快速定位业务问题，比如搜索推荐的query理解→召回链路的错误归因

  - 语义相近的业务工具（如多模态处理、商品属性识别工具）可通过显式配置「意图→动作」路由规则，不用修改工具集就能大幅提升路由准确率，小模型上可先验证规则适配性再上线

  - 多模态Agent处理需要确定性结果的任务（比如电商商品尺寸测量、资质校验），可将计量逻辑与生成式输出解耦，基于可视化中间结果做确定性计算，提升结果可解释性和可信度

  - 业务Agent的工具调用系统可将路由策略作为独立优化变量，不用改动下游服务就能迭代优化路由效果，降低迭代成本'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前多工具视觉Agent混淆意图路由与视觉执行逻辑，无法区分错误源于路由决策失误还是下游工具执行失败，高可信度要求场景下不可用；仅定义可调用工具动作空间，无法解决语义相近意图的路由混淆问题，比如定位vs分割请求极易被误判，存在明显的路由规范缺口。

### 方法关键点
- 提出ZETA架构，遵循「Route First, See Later」原则，先基于纯文本请求完成意图路由，再调用对应视觉工具，全链路可追溯路由决策、调用工具、中间结果、执行输出四个独立节点
- 明确拆分动作空间（可调用工具集合）与路由策略（意图到工具的映射规则），控制实验中仅修改路由规则、保持工具集合完全不变，隔离路由策略的优化效果
- 计量类任务基于视觉工具输出的几何结果做确定性计算，而非直接生成数值结果，保证结果可追溯、可复现

### 关键实验
基于51条科学意图零样本基准，对比仅提供动作空间、同时提供动作空间+显式路由策略两种设置，在5个LLM上测试：Qwen 3.8的检测路由准确率从60.0%提升到100%，分割路由准确率从6.2%提升到75.0%；Nemotron 3.5的分割路由准确率从37.5%提升到87.5%，仅小模型（如Qwen3 1.7B）上显式规则可能带来性能下降。

### 核心结论
约束Agent的可执行动作范围，不足以明确其应该如何执行动作，路由策略是Agent设计的一等公民，而非工具接口的附属品。
