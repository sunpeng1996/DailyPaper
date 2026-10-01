---
title: 'Conversational Capture: A Trajectory-Level Framework for Evaluating Generative
  Engine Optimization in Multi-turn Human-Agent Interaction'
title_zh: 面向多轮人智交互生成引擎优化的轨迹级评估框架
authors:
- Junwei Yu
- Jieyu Zhou
- Mufeng Yang
- Yepeng Ding
- Hiroyuki Sato
affiliations:
- The University of Tokyo
- UniConvo Inc.
- University of Tsukuba
- Hiroshima University
- National Institute of Informatics
arxiv_id: '2609.40069'
url: https://arxiv.org/abs/2609.40069
pdf_url: https://arxiv.org/pdf/2609.40069
published: '2026-09-30'
collected: '2026-10-01'
category: Eval
direction: 多轮人智交互 · GEO评估
tags:
- GEO
- Multi-turn Interaction
- RAG
- Evaluation
- Conversational Search
one_liner: 提出轨迹级GEO评估框架，修正单轮评估忽略多轮人智交互闭环的偏差
practical_value: '- 电商导购Agent、多轮对话式推荐的内容优化效果评估可复用轨迹级增益分解方案，拆分机器历史依赖、用户行为漂移两类贡献，避免单轮评估误判优质优化策略

  - 优化RAG导购/搜索系统时，可复用捕获系数κ、复合比ρ两个指标衡量内容的长期曝光增益，优先优化能在对话早期获得高曝光的内容，利用路径依赖放大收益

  - 对话式搜索/推荐的防内容操纵设计可借鉴文中三类缓解方案：每轮检索重接地降低历史依赖、强制单轮来源多样性、来源引用溯源，降低早期bias的复利放大效应'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有GEO评估仅采用单轮静态指标，忽略多轮人智交互的闭环特性：Agent回复会改变用户认知进而调整后续query，检索也会依赖历史对话上下文，早期曝光的内容可获得复利式额外增益，单轮评估完全无法捕捉该部分收益，甚至会错误排序GEO优化策略。
### 方法关键点
- 定义对话捕获现象，拆分两类独立捕获通道：机器侧M1（历史依赖的检索/生成偏差，无需用户模型即可测量）、用户侧M2（用户受回复引导产生的query漂移偏差）
- 构建轨迹级评估指标体系：累计会话可见度CCV、轨迹增益拆分为直接项（单轮增益线性累加）与反馈项（闭环带来的额外增益，可进一步拆分M1、M2贡献）、捕获系数κ、复合比ρ、单轮/轨迹排名一致性Kendall τ
- 基于Pólya瓮强化过程理论证明：反馈项在单轮评估中恒为0，GEO累计增益随对话长度超线性增长，早期曝光优势存在强路径依赖
### 关键结果
仿真实验T=10轮时，轨迹总增益2.68，其中直接项仅1.20，反馈项达1.48（M1贡献0.85，M2贡献0.63），复合比ρ=2.23，单轮评估低估收益超1倍；5类GEO方法的单轮与轨迹排名Kendall τ仅0.4，单轮排名第一的方法轨迹排名仅第三，90%随机方法集存在单轮/轨迹排名不一致问题。
### 核心结论
多轮交互场景下GEO收益不是单轮曝光的线性累加，而是依赖路径的复利增长，早期1单位曝光优势最终可带来2倍以上的累计收益。
