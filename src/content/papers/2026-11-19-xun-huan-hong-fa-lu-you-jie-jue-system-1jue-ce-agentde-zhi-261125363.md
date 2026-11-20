---
title: Stop Going in Circles:Loop-Triggered Routing for System 1 Decision Agents
title_zh: 循环触发路由：解决System 1决策Agent的执行停滞问题
authors:
- Zeming Yu
- Huamin Ma
- Yingyu Chen
- Yuan Sun
- Peng Hu
- Yang Qin
affiliations:
- Sichuan University
- Huawei Technologies
arxiv_id: '2611.25363'
url: https://arxiv.org/abs/2611.25363
pdf_url: https://arxiv.org/pdf/2611.25363
published: '2026-11-19'
collected: '2026-11-20'
category: Agent
direction: Agent执行优化 · 快慢决策协同
tags:
- System 1 Agent
- Decision Routing
- LLM Collaboration
- Long-horizon Task
- Loop Detection
one_liner: 提出基于状态-动作对重复检测的动态路由，无需训练即可协调System1模型与LLM，兼顾长任务成功率和成本
practical_value: '- 可复用循环触发路由思路优化电商导购Agent、搜索推荐Agent：默认用低成本小模型处理常规交互，检测到重复动作（如用户反复查同一个商品、Agent反复调用同款工具无进展）时才切大模型干预，大幅降低推理成本

  - 路由规则无需训练、无需校准模型置信度的设计可直接复用，不用为不同下游小模型单独训练路由模块，降低多模型协同落地成本，适配电商多业务线异构小模型部署

  - 固定阈值τ=2、接管步长B=2的超参组合可直接作为默认值使用，无需大量超参搜索即可平衡干预时机和大模型调用量，适合快速上线

  - 状态key的设计思路可复用：仅提取业务相关核心状态字段（如电商场景的用户当前页面、购物车状态、核心交互动作）做重复检测，避免全量状态比对的性能开销'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
System1决策模型（如Jev）推理快、成本低，单步决策精度高，但在长周期任务中易陷入重复执行相同动作的停滞，无法推进任务；全程用LLM决策虽然成功率高，但推理时间和成本高企，现有快慢协同方案要么需要额外训练快策略，要么需要针对每个模型校准置信度阈值，泛用性差。

### 方法关键点
- 提出LoopRoute路由机制，默认用System1模型决策，通过检测重复「状态-动作对」判断是否停滞；状态key仅提取任务相关核心公开字段，排除步长、全量历史等干扰字段，避免误判
- 当同一状态-动作对重复执行达阈值τ=2时触发LLM接管，接管步长固定为B=2步，完成后立刻交还控制权给System1，无需额外训练或置信度校准
- 维护全局共享执行上下文，System1和LLM共用相同目标、事实表、历史交互记录，确保接管前后上下文一致

### 关键结果
在ALFWorld、MapReader、TextWorld Cooking三个长周期交互benchmark上适配7款LLM验证：
- 相比纯System1方案，任务成功率分别提升21.0%、60.1%、30.1%
- 相比全程LLM控制方案，成功率仅降0.2~10.1个百分点，但平均推理时间降30.7%~66.8%，调用成本降31%~71%
- 相同路由规则可直接适配6款不同的冻结System1决策模型，无需修改阈值，泛用性极强

**最值得记住的一句话：执行层面的重复动作信号比模型置信度更简单可靠，是协调快慢决策的低成本通用触发条件**
