---
title: 'Atlas: Making Sense of Long Horizon Agent Trajectories'
title_zh: Atlas：面向长周期AI Agent运行轨迹的可解释工作空间系统
authors:
- Sangho Suh
- Joseph Chee Chang
- Pao Siangliulue
- Amy X. Zhang
- Matt Latzke
- Jonathan Bragg
- Doug Downey
- Daniel S. Weld
affiliations:
- Allen Institute for AI
- University of Washington
arxiv_id: '2610.30548'
url: https://arxiv.org/abs/2610.30548
pdf_url: https://arxiv.org/pdf/2610.30548
published: '2026-10-22'
collected: '2026-10-23'
category: Agent
direction: Agent长周期轨迹可解释 · 人机交互
tags:
- Agent Trajectory
- Long-Horizon Agent
- Sensemaking
- Human-Agent Interaction
- Provenance
one_liner: 提出长周期Agent复盘三层框架，搭配轨迹树与多视图投影大幅降低科研人员后验理解成本
practical_value: '- 长周期业务Agent（如电商自动化选品、投放优化Agent）的复盘工具可复用「目标-决策-产出」三层关联设计，将用户初始需求、Agent每步决策理由、中间产出做双向链路，避免用户翻海量日志追溯逻辑。

  - 多视图投影思路可迁移到推荐/广告效果归因场景：同一批召回item/投放素材可按需切换点击时序视图、价格分布散点图、类目聚类视图、关联规则图谱，降低运营重复拉表分析成本。

  - 轨迹树分支设计可用于电商Agent决策审计：显式标注Agent选择/放弃的定向人群、出价策略、素材方案及对应理由，大幅降低投放后审计工作量，快速定位效果异常的决策点。'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
当前长周期AI Agent已能独立完成文献检索、实验分析等复杂任务，但用户复盘未监控的长周期Agent运行结果时存在三大核心痛点：无法追溯输出与初始目标的关联、不清楚Agent关键决策的依据、海量异构输出难以整合分析，纯线性日志+单轮问答的复盘形式效率极低。

### 方法关键点
- 提出后验可解释三层框架：分为目标层（锚定初始需求）、决策层（结构化呈现所有决策）、产出层（支持多视图分析），三层通过provenance链路双向关联，支持跨层跳转。
- 核心功能1：轨迹树，将Agent运行过程拆解为分支结构，显式标注已探索、已放弃、待探索的所有方向，每个节点附带决策理由、关联产出、与初始目标的关联逻辑。
- 核心功能2：产出多视图投影，同一批异构产出支持6种视图切换：列表、时间线、聚类、对比表格、笛卡尔散点图、关系图谱，选择/标记状态跨视图同步。

### 关键结果
14人被试内实验对比基线（聊天框+产出查看器的标准Agent工作空间），Atlas在决策透明度、产出可解释性、目标关联性三个核心维度评分均显著更高，主观工作量降低30%以上，13/14参与者优先选择Atlas；6人探索性部署进一步验证了实际工作场景的可用性。

### 最值得记住的一句话
计算的价值是获得洞察，而非产出数字，长周期Agent的价值不只在执行效率，更要能帮助人理解执行过程、获得有效洞见。
