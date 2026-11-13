---
title: 'CoLFA: Collaboration-Guided Lightweight Failure Attribution for LLM-Based
  Multi-Agent Systems'
title_zh: 协作引导的LLM多智能体系统轻量级故障归因框架CoLFA
authors:
- Yufei Luo
- Yuchen Ling
- Chunrong Fang
affiliations:
- Nanjing University
arxiv_id: '2611.14980'
url: https://arxiv.org/abs/2611.14980
pdf_url: https://arxiv.org/pdf/2611.14980
published: '2026-11-11'
collected: '2026-11-13'
category: MultiAgent
direction: 多智能体系统 · 故障归因优化
tags:
- MultiAgent
- FailureAttribution
- TokenEfficiency
- LLMDebugging
- RCA
one_liner: 利用多智能体协作线索组织归因输入，兼顾故障定位精度与token成本
practical_value: '- 电商/广告多Agent系统（智能客服群、选品Agent、投放Agent）的故障排查可复用倒推式步骤筛选逻辑，从失败结果出发仅关联任务交接、内容复用的上下游步骤，无需全量拉取长日志，大幅降低归因的token开销

  - 多Agent交互日志的上下文组织可复用跨引用内容组织方案，重复内容用引用代替，既保留溯源链路又减少输入冗余，适配长会话Agent系统的日志分析场景

  - 故障归因场景无需盲目喂全量trace给LLM，「协作线索筛选关键步骤+全链路概览拼接」的范式可直接复用到自建Agent可观测系统，同时提升准确率与降本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM多Agent系统在复杂长周期任务落地越来越广泛，失败执行的故障归因需要定位最早的决定性错误步骤和责任Agent，用于系统调试与迭代。但多Agent分工交互导致步骤交错、内容冗余，现有方法要么全量分析trace精度低，要么多轮排查token成本极高，难以平衡精度与开销，无法适配工业级长链路Agent系统的归因需求。

### 方法关键点
- **Handoff-Guided Step Expansion**：从最终失败结果倒推，基于任务交接记录、跨步骤特有内容匹配关联上下游执行步骤，划分为输出步骤、生产步骤、供给步骤三类，仅保留相关步骤作为归因候选，过滤无关历史记录
- **Cross-Referenced Content Organization**：候选步骤的详细记录用内容引用、步骤引用代替重复文本，同时补充全链路执行概览，既保留各步骤的独立执行上下文，又支持跨步骤对比校验，大幅减少输入冗余

### 关键实验
在Who&When、LongRCA两个公开多Agent故障归因基准测试，覆盖平均8.7~156步的不同长度trace，基于DeepSeek-V4.1-Flash、GLM-5.3-Flash、Claude Sonnet 5.5三个骨干模型，对比10个现有基线：
- 相比各场景下精度最高的基线，定位准确率提升1.84%~3.26%，token消耗降低66%~90%，单正确归因的token成本（CoP）最高下降74%
- 最长trace分组下，CoP比最低基线低75%~83%，长链路场景优势更突出

### 最值得记住的一句话
多Agent的协作过程本身就是故障溯源的最佳线索，不需要依赖复杂的推理链或全量日志输入，基于协作线索组织归因输入就能实现精度和成本的双重优化。
