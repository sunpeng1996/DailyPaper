---
title: 'Verify Smarter, Evolve Further: Efficient Harness Evolution through Behavior-Aware
  Verification'
title_zh: 基于行为感知验证的高效Agent Harness自动演化框架
authors:
- Jinghan Xu
- Yikai Zhang
- Aili Chen
- Weiyuan Li
- Jiaqing Liang
- Deqing Yang
affiliations:
- 复旦大学数据科学学院
- 上海市数据科学重点实验室
- 复旦大学计算机科学与人工智能学院
arxiv_id: '2608.27311'
url: https://arxiv.org/abs/2608.27311
pdf_url: https://arxiv.org/pdf/2608.27311
published: '2026-08-27'
collected: '2026-08-28'
category: Agent
direction: Agent系统 · Harness自动演化优化
tags:
- Agent Harness
- Self-Evolution
- Behavior-Aware
- Verification Efficiency
- Budget Constrained
one_liner: 提出预算感知的HARNESSLENS框架，通过行为感知验证实现低成本高可靠的Agent Harness演化
practical_value: '- 做Agent系统迭代时可复用行为感知验证思路：不要所有修改都跑全量测试集，仅选择和修改点相关的任务验证，大幅降低验证成本，避免无关任务稀释修改效果信号

  - 可借鉴归因证据门机制：接受修改不能只看aggregate指标提升，必须确认提升可归因到本次修改、无其他行为退化，避免迭代过程中引入隐性bug导致效果回退

  - 做提示词、工具配置、工作流等可配置组件迭代时，可复用上下文探索→轨迹诊断→演化迭代的流程，在有限推理预算下实现更稳定的效果提升'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有Agent Harness（决定Agent指令、工具调用、工作流等行为的可配置组件）的演化采用固定测试集或随机采样验证，大量无关任务的rollout浪费预算，聚合指标容易掩盖特定行为退化，导致演化成本高、稳定性差，难以在有限交互预算下实现可靠的Harness迭代。

### 方法关键点
- 三阶段演化流程：①上下文探索：先识别Harness可编辑组件、按目标聚类训练任务，无需执行任务；②轨迹诊断：从执行轨迹中提取可复用经验和重复缺陷，关联对应的行为和可修改组件，过滤证据不足的修改提案；③Harness演化：每次迭代仅选择和修改点相关的任务（覆盖相关目标、工具、退化风险）做验证，对比修改前后的轨迹做归因，确认修改带来可归因的提升且无退化后，再用未使用的训练任务做二次确认才落地修改
- 核心设计：归因证据门，仅接受有明确轨迹证据支撑、无隐性退化的修改，避免无效或有害修改上线

### 关键实验
在Retail、Banking、Terminal-Bench 2.0、BIRD四个基准，OpenCode、Codex、Pi三个Agent Harness上测试，对比Self-Harness、Meta-Harness、HarnessFix三个基线，仅用200单位预算（基线最小预算的2/3，最大的1/24），就实现了7.6%~13.6%的平均跨域效果提升，且不会出现基线普遍存在的效果低于初始版本的退化问题。

**最值得记住的一句话**：可靠的Harness演化不取决于验证的总量，而取决于是否把验证资源精准投向每次修改要改变的目标行为上。
