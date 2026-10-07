---
title: 'SquidAgent: Parallelize Wisely, Coordinate Efficiently'
title_zh: SquidAgent：多Agent系统的成本感知自适应并行调度框架
authors:
- Yexiong Lin
- Shanshan Ye
- Yu Yao
- Zhen Fang
- Bo Han
- Tongliang Liu
affiliations:
- The University of Sydney
- Mohamed bin Zayed University of Artificial Intelligence
- University of Technology Sydney
- Hong Kong Baptist University
arxiv_id: '2610.08647'
url: https://arxiv.org/abs/2610.08647
pdf_url: https://arxiv.org/pdf/2610.08647
published: '2026-10-06'
collected: '2026-10-07'
category: Agent
direction: 多Agent协作 · 自适应并行调度
tags:
- Multi-Agent
- Parallel Scheduling
- LLM Agent
- Cost-Aware
- Orchestration
one_liner: 提出基于输出token的成本感知多Agent并行调度框架，消除冗余开销实现2倍以上效率提升
practical_value: '- 电商场景下批量生成商品文案、活动页、详情页等多Agent任务，可复用「输出token预估成本」的调度逻辑，代替不稳定的耗时预估，大幅提升调度决策可靠性

  - 多Agent并行执行前先输出统一公约块（如文案风格、规格参数命名规范、页面组件格式），可降低后续内容对齐返工成本，直接适用于电商多角色Agent协同生产内容的场景

  - 工程上可直接复用「worker fork orchestrator会话上下文」的设计，消除worker重复理解全局任务要求的冗余开销，无需复杂改造即可优化现有多Agent工作流'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有多Agent系统盲目追求并行反而经常比单Agent执行更慢，核心是忽略了并行带来的两个隐性成本：一是worker重复理解orchestrator已完成的规划、上下文的重探索成本，二是独立生成结果不一致的对齐成本，始终缺乏可落地的并行价值判定标准。
### 方法关键点
- 放弃LLM预估误差极大的耗时指标，改用输出token作为成本度量，LLM对生成内容的token数预估准确度远高于耗时，且固定模型下token生成速率稳定，可直接作为耗时代理
- 提出拓扑层粒度的并行判定准则：仅当层内所有子任务串行总token数 >（最长子任务token数 + 层对齐成本token数）* 安全边际α时，才执行并行，避免预估误差导致的负收益
- 工程侧双重优化：worker直接fork orchestrator的会话上下文，将重探索成本压缩至接近0；并行执行前生成统一公约块（如命名规则、格式要求），将对齐成本从事后返工转为可预估的前置成本
### 关键结果
在9个涵盖代码生成、长文档创作、结构化规划的任务上，对比Claude Code、AgentConductor等7个基线：SquidAgent相对Claude Code实现2.6×平均wall-time加速、2.2×平均吞吐量提升，相对最强多Agent基线吞吐量提升2.0×，同时输出质量得分达98.2%，为所有方法最高。
### 核心结论
多Agent并行不是越快越好，只有当并行节省的成本超过额外的协调开销时，才能带来实际收益
