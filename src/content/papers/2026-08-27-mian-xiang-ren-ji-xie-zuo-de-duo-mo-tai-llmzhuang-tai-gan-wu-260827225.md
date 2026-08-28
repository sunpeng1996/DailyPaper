---
title: 'STEP: State-Aware Task Estimation and Planning with Multi-Modal LLMs for Human-Robot
  Collaboration'
title_zh: 面向人机协作的多模态LLM状态感知任务估计与规划框架STEP
authors:
- Maitrey Gramopadhye
- Prakash Baskaran
- Xiao Liu
- Songpo Li
- Soshi Iba
affiliations:
- University of North Carolina at Chapel Hill
- Honda Research Institute
arxiv_id: '2608.27225'
url: https://arxiv.org/abs/2608.27225
pdf_url: https://arxiv.org/pdf/2608.27225
published: '2026-08-27'
collected: '2026-08-28'
category: Agent
direction: Agent人机协作·多模态LLM任务规划
tags:
- Multi-modal LLM
- Task Planning
- Human-Robot Collaboration
- State Tracking
- In-context Learning
one_liner: 引入结构化状态跟踪与迭代优化，大幅提升多模态LLM生成的人机协作任务规划可执行性
practical_value: '- 做Agent长序列规划时，可借鉴结构化JSON状态跟踪机制，通过预测每步动作后的状态变化，减少LLM幻觉，提升动作执行准确率

  - 多轮rollout优化方案可复用：每轮规划后计算当前状态与目标的距离，截断无效动作，从最优状态重新迭代规划，平衡效率和目标达成率

  - 状态表示可模块化扩展：针对不同业务场景（如电商导购Agent、内容生成流程控制），可自定义状态字段，通过分步骤CoT引导LLM输出结构化状态'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前多模态LLM用于人机协作长周期任务规划时存在两大短板：一是缺乏系统状态感知与转移跟踪能力，易生成偏离目标的幻觉动作；二是自然语言输出的规划粒度较粗，存在执行歧义。现有状态跟踪方案要么依赖环境实时状态查询，要么将状态跟踪与规划拆分，无法适配工业场景无额外交互的需求。

### 方法关键点
- 分阶段Pipeline：输入用户历史操作序列+当前环境图像+少量in-context示例，依次完成任务意图估计、当前环境结构化JSON状态生成、未来动作序列预测、每步动作对应的状态转移迭代传播
- 模块化结构化状态设计：针对装配场景自定义4维块状态字段（放置位置、朝向、顶面朝向、相对位置），可扩展适配其他场景
- Rollout迭代优化：每轮生成动作与状态序列后，计算各状态与目标状态的距离（状态字段差异数），截断无效动作，从距离最小的状态重新发起下一轮规划，直到达到目标或最大轮次

### 关键实验
基于模拟块装配场景的495条人机协作操作序列（共8种装配任务），对比以AntGPT为基础的SOTA基线：动作可执行性相对提升32.8%，最终状态误差相对降低14.8%；多轮rollout可进一步降低最终误差，方案在GPT-4o、GPT-4.1、GPT-5等多模型上效果稳定，仅小模型GPT-4o mini因任务估计准确率低表现欠佳。

> 最值得记住的结论：长周期LLM规划的可靠性，本质上依赖对每一步操作后状态变化的可量化跟踪，而非单纯依赖动作序列的语义合理性。
