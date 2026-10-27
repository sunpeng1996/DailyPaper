---
title: 'IntentDelta: A Human-Constructed Benchmark for Evolving User Intent'
title_zh: IntentDelta：面向演化用户意图的人工构建多轮交互评估基准
authors:
- Jieyu Zhou
- Zijian Wang
- Yun Wang
affiliations:
- Georgia Institute of Technology
- Microsoft Research
arxiv_id: '2610.33806'
url: https://arxiv.org/abs/2610.33806
pdf_url: https://arxiv.org/pdf/2610.33806
published: '2026-10-24'
collected: '2026-10-27'
category: Agent
direction: Agent 动态用户意图追踪评估
tags:
- User Intent Tracking
- Agent Evaluation
- Multi-turn Interaction
- Conversational Recommendation
- Benchmark
one_liner: 覆盖购物、旅行双场景的动态用户意图基准，可同时评估意图恢复与动作执行效果
practical_value: '- 电商对话推荐/购物Agent可复用其三阶优先级（must-have/preferred/optional）的意图建模方法，解决约束冲突时的自动权衡问题

  - 多轮交互的用户画像更新模块可参考其约束老化检测结论，增加历史有效需求的记忆留存机制，降低早期需求遗忘率

  - 电商/旅行Agent的效果评估可直接复用其「意图理解-动作落地」双层评估框架，替代单一对话流畅度指标，更贴近真实用户体验

  - 处理多约束同时变更的用户请求时，可先做意图变更的结构化拆解，再分别更新意图状态，降低多约束修改场景的识别错误率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有Agent处理复杂多轮任务的基准多基于合成或模拟的用户交互，无法真实还原人类用户因可行性约束、偏好变化动态调整需求的决策逻辑，且普遍缺乏逐轮的人工参考动作标注，难以同时评估Agent的意图理解准确性与落地执行效果，无法覆盖需求增删、优先级调整、约束放松等真实交互场景。
### 方法关键点
- 覆盖WebShop电商购物、TravelPlanner旅行规划双领域，人工构建638条多轮轨迹共3766轮交互，所有轨迹经过两轮交叉验证，标注一致性达97%
- 意图建模拆分must-have（必须满足）、preferred（优先满足）、optional（可选）三级优先级，支持新增、放松、覆盖、重排序四类意图变更操作，覆盖可行性驱动、偏好驱动两类变更触发场景
- 设计双层评估体系：意图层评估检测率、内容准确率、优先级准确率、整体意图恢复率；动作层评估硬约束满足率（Hard Success）、综合动作得分（Action Score），独立衡量意图理解与落地能力
### 关键实验结果
评测11款主流LLM Agent：平均意图恢复率旅行场景仅33.1%、购物场景44.7%；平均动作得分旅行场景31.6%、购物场景41.0%；当用户单轮同时修改多个约束时，意图恢复率相对单约束变更下降超40%；即便意图完全恢复，动作得分仍仅为42.9%（旅行）/58.8%（购物），存在显著的意图-执行gap。
### 核心结论
现有Agent不仅普遍混淆软偏好与硬约束、易遗忘多轮交互中的早期用户需求，且即便完全准确理解用户意图，也存在大量落地执行失败的问题
