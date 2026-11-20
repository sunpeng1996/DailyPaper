---
title: 'Pro$^2$ Agent: Scientific Problem Probing for Autonomous AI R&D'
title_zh: Pro² Agent：面向自主AI研发的科学问题探测智能体
authors:
- Yixiong Chen
- Liqian Peng
- Tian Tan
- Ziqian Lin
- Blake Jianhang Chen
- Chao Zhao
- Yaojie Liu
- Alec Go
- Alan Yuille
affiliations:
- Google
- Johns Hopkins University
arxiv_id: '2611.25357'
url: https://arxiv.org/abs/2611.25357
pdf_url: https://arxiv.org/pdf/2611.25357
published: '2026-11-19'
collected: '2026-11-20'
category: Agent
direction: AI研发Agent · 问题状态建模
tags:
- LLM Agent
- Auto Research
- MLE Agent
- Problem State
- Hypothesis Testing
one_liner: 提出以显式问题状态为核心的自主AI研发智能体，刷新MLE-Bench基准最优成绩
practical_value: '- 做推荐系统长周期迭代、AB效果归因类Agent任务时，可引入显式Problem State结构，结构化存储性能瓶颈、候选解法、置信度与验证证据，替代纯代码/效果日志迭代的思路，避免局部修改陷入次优解

  - 可复用三角色Agent分工架构：用强LLM作为规划角色（对应PI Agent）管控核心目标与问题认知，用轻量化低成本LLM作为实现、评审角色做编码、单变量校验，兼顾效果与推理成本，适合搭建推荐策略调优、实验分析的自动化Agent流水线

  - 做策略迭代实验时严格执行单变量控制，用Git分支隔离每个实验快照，避免多变量混淆导致的归因错误，可直接落地到推荐AB实验、召回/排序策略迭代的实验管理流程中'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有自主AI研发Agent以代码库为核心状态，仅记录代码修改历史与对应效果，不显性维护对任务瓶颈的认知，复杂任务下容易在局部次优解内循环，算力利用率低且收敛速度慢。

### 方法关键点
- 定义Problem State为核心第一类状态，结构化存储识别到的性能瓶颈、支撑证据、对应候选解法、每个解法的置信度与验证证据，每个Problem State与Git快照一一绑定
- 三阶段研发流程：初始化阶段先做runtime资源/约束探测+针对性文献检索，生成初始Problem State与基线代码；科学探索阶段按「置信度/历史探索次数」的优先级做单变量假设验证，动态更新Problem State的置信度；工程优化阶段用带算力成本惩罚的MCTS仅调节超参数、batch size等工程变量，禁止修改核心算法逻辑
- 三角色多Agent协作：强LLM作为PI Agent维护Problem State、设定研发目标；轻量化LLM作为Implementation Agent执行编码、调试；Reviewer Agent做代码审计、单变量隔离校验

### 关键结果
- 在全量75任务MLE-Bench基准上，24小时单A100预算下奖牌率达70.7%，追平当前公开SOTA；48小时预算下奖牌率达76.0%，为目前公开最优成绩
- 在PostTrainBench基准上，以Gemini 3.5 Flash为执行模型，综合得分超过Claude Opus 4.7驱动的Claude Code
- 初始基线方案的奖牌率达57.6%，是同类方案的2倍，仅需5次迭代即可达到66.7%的奖牌率

### 核心结论
长周期自主Agent任务的效率提升，不只是靠更强的基座模型或更深的搜索，更依赖对核心问题的显式建模与动态迭代
