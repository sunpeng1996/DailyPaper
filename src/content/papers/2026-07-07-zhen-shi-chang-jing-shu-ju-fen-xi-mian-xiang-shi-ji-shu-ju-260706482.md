---
title: 'Data Analysis in the Wild: Benchmarking Large Language Models Against Real-World
  Data Complexities'
title_zh: 真实场景数据分析：面向实际数据复杂度的大模型基准测试
authors:
- So Hasegawa
- Shailaja Keyur Sampat
- Lei Liu
- Wei-Peng Chen
affiliations:
- Fujitsu Research of America
arxiv_id: '2607.06482'
url: https://arxiv.org/abs/2607.06482
pdf_url: https://arxiv.org/pdf/2607.06482
published: '2026-07-07'
collected: '2026-07-08'
category: Eval
direction: 大模型数据分析能力评测基准
tags:
- LLM
- Benchmark
- TableQA
- DataAnalysis
- Agent
one_liner: 推出基于政府公开数据的DataGovBench基准，覆盖表QA、表洞察两大真实数据分析任务
practical_value: '- 落地大模型数据分析Agent时，可参考DataGovBench的任务设计框架，拆解多表关联、外部知识融合、复杂查询的评估维度，避免仅测试小表简单查询的评估偏差

  - 搭建业务数据自动洞察系统（如用户行为、交易数据分析）时，可复用Table Insight任务的专家级洞察评估标准，判断输出内容的业务可用性

  - 当前带Agent框架的SOTA LLM在真实多表数据分析上仍存在显著性能gap，业务落地需优先做边界兜底，不盲目上线全自主数据分析Agent'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM数据分析基准多聚焦小表单表事实检索，忽略真实场景下大尺寸多表数据集、外部知识融合、探索性洞察挖掘的核心挑战，无法反映实际落地能力。
### 方法关键点
1. 推出基于政府公开数据的DataGovBench，覆盖真实数据分析的核心需求
2. 包含两大评测任务：Table QA（解决复杂可分解查询，输出文本/可视化结果）、Table Insight（评估探索性分析生成专家级发现的能力）
3. 统一测试了SOTA LLM带/不带Agent框架的性能表现
### 关键结果
所有被测SOTA模型无论是否搭载Agent框架，在两大任务上均存在显著性能缺口，当前LLM相关系统远未达到真实场景数据分析的落地要求。
