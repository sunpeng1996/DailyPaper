---
title: 'Stateless Language Agents: Scaling Long-Horizon Automated Research'
title_zh: 无状态语言Agent：支撑长周期自动化研究的可扩展架构
authors:
- Qizheng Zhang
- Changxiu Ji
- Isaac Sun
- Yuetai Li
- Shubhangi Upasani
- Sherry Ruan
- Boyuan Ma
- Fenglu Hong
- Vamsidhar Kamanuru
- Yoonho Lee
affiliations:
- Stanford University
- Carnegie Mellon University
- University of Washington
- SambaNova Systems, Inc.
- UC Berkeley
arxiv_id: '2610.07625'
url: https://arxiv.org/abs/2610.07625
pdf_url: https://arxiv.org/pdf/2610.07625
published: '2026-10-05'
collected: '2026-10-12'
category: Agent
direction: 长周期无状态Agent 自动化搜索优化
tags:
- LLM-Agent
- Stateless-Agent
- Long-Horizon
- AutoResearch
- Multi-Agent
one_liner: 提出无状态语言Agent架构，将全局状态从Agent会话剥离，长周期搜索token效率最高提升14.5倍
practical_value: '- 长周期Agent迭代任务（如广告素材自动优化、推荐策略自动调优、大促选品挖掘）可直接借鉴SLA的状态与会话分离设计，由调度器统一管理所有历史实验数据，每次Agent调用按需重建上下文，既避免context
  rot，又能降低80%以上的token消耗

  - 多Agent协作场景可复用SLA的低开销协调架构：用轻量全局Advisor分配任务，Worker仅获取任务相关局部上下文，Advisor token占比不到0.6%，协调成本远低于现有共享内存/多Agent会话同步方案，还能避免Worker重复劳动

  - 长周期自动优化类任务的评估需拉长观测周期，论文中SLA在25%预算时效果劣于基线，全预算时全面反超，做A/B test自动选优、推荐特征挖掘等任务时不要过早淘汰潜力方案

  - 需并行加速的Agent任务可按任务类型选择Worker数量，SLA中15个Worker相比单Worker可将耗时降低6.6~7.3倍，长周期任务下质量损失可忽略，适合业务端有明确量化目标的自动迭代场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有长周期LLM Agent自动化搜索系统存在三大痛点：一是Agent携带全量会话历史导致token消耗飙升，还会出现context rot导致性能退化；二是多Agent并行时重复探索严重，大量token空耗无有效产出；三是短周期评估容易误判方案潜力，无法衡量长周期下的持续迭代能力，现有依赖Agent自身维护状态的设计无法支撑十亿token级的长周期任务。
### 方法关键点
- 核心设计原则：状态与会话完全分离，全局研究状态（候选方案、评估结果、实验记录）统一由harness存储，所有Agent无状态，每次调用都重建全新上下文，不继承过往会话
- 角色分工：全局Advisor每次调用时仅获取harness生成的结构化全局实验摘要，输出各Worker的具体实验任务；Worker仅获取当前任务相关的局部上下文，无法访问全局历史或其他Worker的工作空间
- 协调机制：Advisor基于全局证据动态分配实验方向，避免Worker重复劳动，所有有效结果统一存入全局状态用于下一轮上下文重建
### 关键结果
在三类长周期任务（软件工程、内核优化、算法设计）最高10亿token预算下，对比EvoX、CORAL、SwarmResearch三类基线：
1. 全预算下所有任务效果均超过基线，内核优化任务达基线同等效果仅需67.9M token，较基线减少93.1%
2. FrontierSWE任务25%预算时效果落后基线，100%预算时平均超出基线4.95分
3. Advisor仅消耗0.24~0.51%的总token，协调成本可忽略
### 核心结论
长周期Agent系统的核心优化方向是把状态管理从Agent会话中剥离，用显式的上下文重建和任务分配替代隐式的会话历史传递，可同时提升效果与资源效率
