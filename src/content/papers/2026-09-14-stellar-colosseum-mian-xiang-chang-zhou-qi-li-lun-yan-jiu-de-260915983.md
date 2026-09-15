---
title: 'Stellar Colosseum: A Many-Agent Harness for Long-Horizon Research in Mathematics
  and Theoretical Computer Science'
title_zh: Stellar Colosseum：面向长周期理论研究的多Agent编排框架
authors:
- Honghao Lin
- David P. Woodruff
- Yuan Deng
- Jieming Mao
- Song Zuo
- Vahab Mirrokni
affiliations:
- Google Research
- Carnegie Mellon University
arxiv_id: '2609.15983'
url: https://arxiv.org/abs/2609.15983
pdf_url: https://arxiv.org/pdf/2609.15983
published: '2026-09-14'
collected: '2026-09-15'
category: MultiAgent
direction: 多智体协作 · 长周期推理任务编排
tags:
- MultiAgent
- Long-Horizon Reasoning
- Theorem Proving
- Agent Orchestration
- Falsification
one_liner: 提出多Agent编排框架，通过分层核验与树状聚合支撑长周期数学与理论CS研究任务
practical_value: '- 多Agent任务编排可复用其分层流程：先策略探索→就绪校验→子问题拆分并行求解→全局校验，适配电商大促 campaign 策划、复杂推荐链路优化等长周期决策任务

  - 树状随机采样聚合+定向falsification方案可直接迁移到LLM生成内容校验场景：比如广告文案、商品详情页生成的多候选打分融合，保留有效内容同时过滤缺陷

  - 跨任务共享知识目录设计可复用在推荐系统的用户/物品全局信息维护：避免多Agent重复探索相同路径，降低推理成本，尤其适配多轮交互Agent导购场景'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
LLM在短推理任务上表现出色，但长周期研究类任务依赖连续多轮相互依赖的决策，现有方案易出现误差累积、有效中间结果丢失、全局一致性差等问题，无法支撑复杂长任务的自动探索与迭代。

### 方法关键点
- 分层工作流：分为策略探索、就绪门控、任务拆分、子问题并行求解、全局校验5个阶段，失败任务可定向回到局部修改或重新探索，无需全链路重跑
- 单阶段内部采用「多候选生成→定向falsification找缺陷→重叠随机采样树聚合」范式，聚合过程保留候选的缺陷反馈，避免有效信息丢失
- 全局维护共享知识目录，存储已验证结论、失败路径、参考资料、观测结论，跨轮次复用中间结果减少重复计算

### 关键结果
- 在TCS-Bench（300道FOCS/STOC/SODA顶会衍生的定理证明题）上，搭配Gemini 3.1 Pro + 3.7 Flash的跨模型选择方案准确率达71.0%，超过GPT-5.6 Pro的68.0% baseline
- 在222道难度1530~4599的Codeforces竞赛题上，搭配Gemini 3.1 Pro+执行反馈的方案解决218道，性能评分达4263，比无执行反馈版本高345分
- 已助力产出5篇理论CS顶会级别的新研究成果，可独立复现Erdős单位距离猜想反证的核心架构

> 最值得记住：长周期复杂任务的核心不是单次推理能力的提升，而是通过合理的多Agent编排保留中间有效信息、控制误差传播、定向分配算力
