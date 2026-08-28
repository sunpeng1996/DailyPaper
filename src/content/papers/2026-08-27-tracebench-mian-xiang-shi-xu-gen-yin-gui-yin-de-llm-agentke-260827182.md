---
title: 'TraceBench: Controlled Evaluation of LLM Agents for Time-Series Root-Cause
  Attribution'
title_zh: TraceBench：面向时序根因归因的LLM Agent可控评测基准
authors:
- Tommaso Bendinelli
- Artur Dox
- Christian Holz
affiliations:
- ETH Zürich
- CSEM SA
- Independent Researcher
arxiv_id: '2608.27182'
url: https://arxiv.org/abs/2608.27182
pdf_url: https://arxiv.org/pdf/2608.27182
published: '2026-08-27'
collected: '2026-08-28'
category: Eval
direction: Agent评测 · 时序根因归因基准
tags:
- LLM Agent
- Benchmark
- Root Cause Attribution
- Time Series
- Evaluation
one_liner: 提出模拟生成式可控基准TraceBench，系统评测时序根因归因场景下的LLM Agent性能
practical_value: '- 垂直场景Agent评测可复用「模拟生成可控任务集」的思路，解决电商流量异动根因分析等场景真实样本标注难、变量不可控的问题，降低预验证成本

  - 时序分析类Agent的工具链优先做数值查询/统计能力，无需优先投入可视化解析开发，后者对根因判断增益极低

  - 根因归因类Agent任务若不需要可解释执行逻辑，可直接让Agent输出结论，强制要求输出可执行推理脚本会显著降低准确率'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
LLM Agent已被广泛应用于真实系统时序观测的异常检测与根因分析，但当前缺乏可控条件下的系统性评测方案，无法量化不同设计对Agent性能的影响。
### 方法关键点
构建基于仿真的TraceBench可控根因归因任务生成框架：通过模拟物理动力系统生成时序观测，要求Agent判断仿真过程中是否修改了系统参数、以及被修改的具体参数；基于3个可解释机械系统生成任务集，控制实验变量系统性评测4款LLM Agent的表现。
### 关键结果
- 给Agent注入领域上下文可带来显著性能提升
- Agent时序数据探索主要依赖数值控制台输出，可视化能力几乎无增益
- 要求Agent输出逐样本映射根因标签的Python脚本时，性能显著低于直接输出预测的模式
所有数据集、Agent轨迹、实验结果、排行榜已开源。
