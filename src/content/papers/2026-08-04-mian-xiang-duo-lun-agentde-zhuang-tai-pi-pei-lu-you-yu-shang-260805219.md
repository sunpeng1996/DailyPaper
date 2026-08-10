---
title: 'When Privileged Guidance Misaligns: State-Matched Routing and Contextualized
  Self-Distillation for Multi-Turn Agents'
title_zh: 面向多轮Agent的状态匹配路由与上下文自蒸馏：解决特权引导错位
authors:
- Junzhuo Liu
- Weiwei Li
- Jun Ling
- Peng Wang
affiliations:
- University of Electronic Science and Technology of China
arxiv_id: '2608.05219'
url: https://arxiv.org/abs/2608.05219
pdf_url: https://arxiv.org/pdf/2608.05219
published: '2026-08-04'
collected: '2026-08-10'
category: Agent
direction: 多轮Agent训练 · 特权自蒸馏优化
tags:
- Multi-turn Agent
- Self-distillation
- On-policy Learning
- LLM Agent
- Privileged Guidance
one_liner: 提出SMRC-SD框架解决多轮Agent训练中状态与参考轨迹错位问题，提升交互任务成功率
practical_value: '- 电商导购/下单多轮Agent训练时，可引入状态匹配机制过滤参考轨迹无效引导，避免错误惩罚合理的探索操作

  - 自蒸馏训练时，对匹配状态可拼接「全量成功路径+当前状态摘要+匹配候选动作」构造教师上下文，提升蒸馏信号质量

  - 多轮交互Agent训练优先保留GRPO基础损失，仅在状态匹配时叠加蒸馏损失，既保证探索性又减少无效监督

  - 状态签名不需要语义匹配，用业务结构化字段（如电商的页面类型、当前SKU、已选属性）做精确匹配即可，工程成本低'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
多轮Agent训练常用基于成功轨迹的特权自蒸馏提供密集监督，但学生Agent探索时会走出参考轨迹未覆盖的状态，直接全局蒸馏会导致状态-参考错位，惩罚正确的探索动作，反而降低训练效果。

### 方法关键点
- 设计状态匹配路由机制：为参考轨迹每个前置状态和学生当前执行状态生成结构化签名，仅当当前状态与参考某位置状态兼容、且对应参考动作在当前可执行时，才触发蒸馏，否则仅保留GRPO损失
- 构造上下文感知蒸馏信号：匹配成功时，教师侧输入拼接全量成功路径、当前状态摘要、匹配的候选动作，让蒸馏信号贴合当前状态，避免全局路径的歧义
- 所有特权模块仅训练阶段使用，推理阶段无额外开销

### 关键实验
在ALFWorld（具身交互）和WebShop（电商购物交互）两个基准测试，对比GRPO、Skill-SD、SDAR、FullPath-SD等基线：用Qwen3-1.7B时ALFWorld任务成功率从0.746提升到0.865，WebShop成功率从0.574提升到0.693；蒸馏路由和上下文构造分别贡献约0.09和0.03的成功率提升。

### 核心结论
可执行参考轨迹是条件性计划，必须先验证其对当前状态的局部适用性，再用来监督多轮策略。
