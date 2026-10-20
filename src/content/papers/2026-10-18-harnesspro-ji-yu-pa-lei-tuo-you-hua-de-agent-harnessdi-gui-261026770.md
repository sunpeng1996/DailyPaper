---
title: 'HarnessPro: Recursive Harness Self-Improvement with Pareto Optimization for
  Performance-Cost Trade-offs'
title_zh: HarnessPro：基于帕累托优化的Agent Harness递归自提升框架
authors:
- Zhuoshi Pan
- ZhiYuan Feng
- Yukuo Cen
- Honglin Lin
- Junru Lu
- Zhongxia Chen
- Shuo Yang
- H. Vicky Zhao
- Jie Tang
affiliations:
- Tsinghua University
- Z.AI Co., Ltd.
- Shanghai Jiao Tong University
- University of Warwick
- Kuaishou Technology
arxiv_id: '2610.26770'
url: https://arxiv.org/abs/2610.26770
pdf_url: https://arxiv.org/pdf/2610.26770
published: '2026-10-18'
collected: '2026-10-20'
category: Agent
direction: Agent 性能成本权衡优化
tags:
- Agent Harness
- Pareto Optimization
- Recursive Self-Improvement
- Cost Efficiency
- Multi-Agent
one_liner: 无标注场景下递归优化Agent Harness，输出三种性能-成本权衡的部署版本
practical_value: '- Agent落地可复用三档位版本输出思路：用帕累托加权距离选择成本优先/平衡/性能优先三个版本的Harness，适配电商不同流量场景（大促用高性能版、平日用低成本版）的成本约束

  - 优化Agent运行成本可复用动态预算管控trick：根据任务难度动态分配推理算力、工具调用上限，配合runtime hook拦截冗余操作，可直接用于导购Agent、query理解Agent等场景降低token消耗

  - 无标注评估Agent可复用测试合成方案：不用LLM直接判分，改为LLM先生成固定测试用例再执行验证，可将失败召回率提升41.6pp，适合业务迭代Agent时标注不足的场景

  - 迭代Harness可复用DPP核心集采样方法：仅用10个左右多样性高的核心任务做迭代，不用全量数据，大幅降低迭代试错成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent Harness递归自提升方法仅追求性能提升，往往伴随token消耗、 latency大幅上涨，不符合业务部署的成本约束；且多数方案依赖标注数据或官方测试集，落地门槛高，亟需无标注下同时优化性能和成本的方案。

### 方法关键点
- 多Agent协作迭代架构：轨迹分析Agent诊断执行失败原因和冗余开销，演化规划Agent分成本优先/平衡/性能优先三个方向输出改进方案，编辑Agent生成可执行候选Harness，测试合成Agent生成固定测试用例实现无标注评估
- 帕累托筛选机制：先过滤性能低于初始版本、被帕累托占优的候选，再用归一化加权平方距离选择三个档位的代表性Harness进入下一轮迭代
- 无标注评估优化：用LLM生成固定测试用例替代直接LLM判分，失败召回率从41.7%提升至83.3%，评估偏差大幅降低

### 关键实验
在Terminal-Bench 2、SWE-Bench Pro、ProgramBench三个基准测试，对比RHO等基线：
- 采用GPT-5.5+Codex时，heavy版相比RHO平均pass率提升2.0pp，单任务成本降低26.1%；Terminal-Bench 2上pass率提升4.5pp，成本降低33.9%
- medium版性能与RHO相当，成本最高降低53.0%；lite版性能优于原始Harness，成本最高降低57.4%
- 收益跨基座通用，GLM-5.2+Claude Code上也有一致的性能成本双提升效果

最值得记住的结论：性能和成本不是必然互斥，通过消除可避免的冗余开销、动态分配算力，完全可以实现性能提升的同时成本下降
