---
title: 'AdaRSI: On-Demand Recursive Self-Improvement for Embodied Agents'
title_zh: AdaRSI：面向具身智能体的按需递归自改进框架
authors:
- Peidong Wang
- Ying Chang
- Zhiming Ma
- Xiaocui Yang
- Shi Feng
- Daqi Liu
- Yuzhe Yang
- Xu Cao
- Chuang Wang
- Jian Su
affiliations:
- Northeastern University
- AgiBot
- University of Chinese Academy of Sciences
arxiv_id: '2610.20474'
url: https://arxiv.org/abs/2610.20474
pdf_url: https://arxiv.org/pdf/2610.20474
published: '2026-10-14'
collected: '2026-10-15'
category: Agent
direction: 具身Agent · 递归自优化
tags:
- Embodied Agent
- Recursive Self-Improvement
- VLA
- On-Demand Fine-tuning
- Harness Optimization
one_liner: 提出先优化调用层再按需微调执行器子步骤的具身Agent递归自改进框架
practical_value: '- 可复用「先优化上层调用逻辑，再按需微调底层模型」的分层优化思路：在推荐/广告系统中先优化召回/排序策略编排、prompt规则，再微调子模块模型，大幅降低训练成本

  - 失败归因机制可迁移到业务bad case治理：先排查规则、流程、参数配置类问题，确认是模型能力不足再启动微调，避免无效训练导致的已有能力劣化

  - 跨任务经验复用机制可迁移到多场景Agent运营：将试点场景的优化经验沉淀为决策规则，指导其他场景的资源投入优先级，提升迭代效率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
预训练VLA在长序列未见任务上中途失败率高，现有递归自改进方法要么仅优化上层harness无法补充缺失执行能力，要么全量微调执行器成本极高且可能劣化已有能力，无法区分失败是调用逻辑问题还是执行器能力边界问题。

### 方法关键点
- 分层优化：先由编码Agent迭代优化harness（含技能库、工具集、任务执行流程），修复调用逻辑类失败，无训练成本
- 失败归因：对harness无法修复的失败，通过快照重放子步骤，区分是调用方式问题还是执行器能力不足问题
- 按需微调：仅对执行器能力边界外的子步骤收集自生成演示做微调，验证效果优于原执行器后加入策略库，其余场景默认仍用原执行器
- 跨任务经验复用：试点任务的优化经验沉淀为规则，指导后续任务的训练资源分配，进一步降低冗余投入

### 关键实验
在RoboCasa365的50个任务上测试，基础执行器为GR00T N1.5，无人工标注。对比基线：纯VLA、仅Agent调用VLA、仅优化harness。核心结果：Composite-Unseen任务成功率从4.6%提升到13.8%（是基线的3倍），对比全量微调所有子步骤的方案，仅用28%的GPU时间、22%的自采集演示数据，整体任务成功率比纯VLA高6.4pp。

> 最值得记住的一句话：优先优化上层调用逻辑能解决大部分失败，仅当明确是底层模型能力缺失时才微调，是平衡效果与成本的核心原则
