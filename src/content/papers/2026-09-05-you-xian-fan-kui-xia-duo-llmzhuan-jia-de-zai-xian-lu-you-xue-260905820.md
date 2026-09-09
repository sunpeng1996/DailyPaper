---
title: Online Learning with LLM Experts from Limited Feedback
title_zh: 有限反馈下多LLM专家的在线路由学习算法
authors:
- Wang Wei
- Soumyabrata Pal
- Koyel Mukherjee
- Franck Dernoncourt
- Ryan A. Rossi
- Branislav Kveton
- Hoda Eldardiry
affiliations:
- Virginia Tech
- Adobe Research
arxiv_id: '2609.05820'
url: https://arxiv.org/abs/2609.05820
pdf_url: https://arxiv.org/pdf/2609.05820
published: '2026-09-05'
collected: '2026-09-09'
category: LLM
direction: 多LLM路由 · 有限反馈在线学习
tags:
- Contextual Bandit
- LLM Routing
- Online Learning
- Limited Feedback
- Expert Selection
one_liner: 提出两种有限反馈下的上下文老虎机算法，实现多LLM请求的低成本高收益路由
practical_value: '- 电商客服/商品文案生成等多LLM混部场景可直接复用该采样逻辑，无需每轮调用LLM-as-Judge，仅选择历史信息增益最高的prompt采样反馈，可降低30%以上的反馈成本

  - 若业务中可获取单prompt下所有备选LLM的效果打分，优先用LimFullFeed算法，其共享协方差矩阵的设计计算效率不随LLM数量线性增长，适合大促等高并发场景

  - 若仅能获取被调用LLM的效果反馈，采用LimBanFeed算法，按LLM调用频次分配反馈配额，高频调用的模型分配更多采样预算，资源投入ROI更高

  - 可迁移到推荐/广告的多策略流量路由场景，比如多个召回/排序策略的流量分配，用有限的AB测反馈优化路由，降低实验成本'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
当前多LLM部署场景下，不同模型的能力、调用成本差异显著，无单一模型能在所有prompt请求上实现最优性价比，但用于评估输出质量的人工/LLM-as-Judge反馈成本极高，无法每轮都获取全量反馈，传统在线路由算法未针对有限反馈预算做优化，容易出现成本浪费或效果不达预期的问题。
### 方法关键点
- 将多LLM路由问题建模为上下文老虎机问题，以prompt embedding为上下文，K个备选LLM为动作，约束总反馈次数m远小于请求总轮次T，目标最小化与最优路由的累积后悔
- 全信息场景（可获取单prompt下所有LLM的效果反馈）提出LimFullFeed算法：每T/m轮触发一次反馈采样，选择历史中能最大化协方差矩阵行列式的prompt获取全量反馈，同步更新所有LLM的奖励模型，理论后悔上界为$	ilde{O}(dT/\sqrt{m})$
- 老虎机场景（仅能获取被调用LLM的效果反馈）提出LimBanFeed算法：为每个LLM单独维护协方差矩阵与调用计数，每被调用T/m次就采样其历史上信息增益最高的prompt获取反馈更新对应模型，理论后悔上界为$	ilde{O}(dT\sqrt{K/m})$
- 可扩展到不同LLM反馈成本异构的场景，按反馈成本反比分配各模型的采样频率，适配实际业务的成本结构
### 关键实验
基于RouterBench、Nectar两个公开LLM路由基准数据集，对比NoLookBack（仅采样当前轮prompt的基线）、AllFeedback（全量反馈的性能上限），当T=60000、m=5000时，LimBanFeed比NoLookBack的累积后悔低24%；m=20000时，LimBanFeed比NoLookBack的累积后悔低25%，算法运行时间随请求量线性扩展，全信息算法复杂度不随LLM数量增长。
### 核心结论
有限反馈下的在线路由核心是把有限的反馈预算花在信息增益最高的样本上，而非均匀或随机采样，可在相同成本下大幅降低决策错误率
