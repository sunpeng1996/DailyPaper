---
title: 'ActiveSaddler: Automated Curriculum Learning for Agent Harness Optimization'
title_zh: ActiveSaddler：面向Agent Harness优化的自动课程学习框架
authors:
- Sungho Park
- Wonjoong Kim
- Jue Zhang
- Wook-Shin Han
- Pengfei Gao
- Chanyoung Park
- Yongqiang Yao
- Rao Fu
- Elsie Nallipogu
- Qingwei Lin
affiliations:
- POSTECH
- KAIST
- Microsoft
arxiv_id: '2610.00906'
url: https://arxiv.org/abs/2610.00906
pdf_url: https://arxiv.org/pdf/2610.00906
published: '2026-09-30'
collected: '2026-10-02'
category: Agent
direction: Agent Harness优化 · 自动课程学习
tags:
- CurriculumLearning
- AgentHarness
- MultiArmedBandit
- LLMAgent
- Optimization
one_liner: 将自动课程学习引入Agent Harness优化，动态匹配训练场景与短板提升性能
practical_value: '- 迭代电商导购、广告投放等业务自定义Agent的Harness时，可复用失败模式聚合思路：不按单case或粗粒度类别分配优化资源，聚类同根因失败case作为优化单元，大幅提升迭代效率

  - 有限rollout预算下优化Agent能力时，可参考四维度优先级打分逻辑：从失败严重程度、可修复性、影响面、副作用风险四个维度评估短板价值，优先优化投入产出比最高的问题

  - 搭建Agent持续迭代工程框架时，可复用自适应探索-利用平衡策略：已知可修复短板少时优先探索新场景挖新问题，短板多时优先修复已知问题，效率远高于固定轮次探索方案'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent Harness（含Prompt、工具接口、控制逻辑）优化方法仅关注更新逻辑，训练场景全部预设固定，随Harness迭代，已修复场景持续训练无价值，未解决短板得不到足够资源，有限预算下优化效率极低，适配业务动态变化的能力差。

### 方法关键点
- 将训练场景选择建模为非平稳多臂老虎机问题，动态实例化**失败模式臂**：每个臂对应一类同根因的Harness短板，聚合所有触发该失败的场景
- 自适应臂优先级：每次迭代用LLM评估每个臂的学习进度分数，综合严重程度、可修复性、影响面、副作用风险四个维度，按分数采样下一轮优化目标
- 自适应探索控制：动态决策是探索未见过的场景挖掘新失败模式，还是利用已知臂优化现有短板，无需预设固定探索轮次

### 关键实验
在GAIA2、Terminal-Bench 2.0两个通用Agent基准测试，对比AutoSaddler等现有Harness优化器，相同rollout预算下，GAIA2测试Pass@1提升4.4个百分点，Terminal-Bench 2.0提升7.5个百分点；端到端成本效率是固定课程方案的2~4倍。

最值得记住的一句话：Agent Harness优化的效果不仅取决于如何利用反馈更新Harness，更取决于选择哪些训练场景生成反馈。
