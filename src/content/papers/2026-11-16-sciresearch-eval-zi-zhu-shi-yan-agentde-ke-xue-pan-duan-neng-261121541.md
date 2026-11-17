---
title: 'SciResearch-Eval: Evaluating Scientific Judgment in Autonomous Experimental
  Agents'
title_zh: SciResearch-Eval：自主实验Agent的科学判断能力评估基准
authors:
- Brian T. Weston
- Alondra Torres Contreras
- Aldair E. Gongora
affiliations:
- Lawrence Livermore National Laboratory
arxiv_id: '2611.21541'
url: https://arxiv.org/abs/2611.21541
pdf_url: https://arxiv.org/pdf/2611.21541
published: '2026-11-16'
collected: '2026-11-17'
category: Agent
direction: 自主实验Agent · 能力评估基准
tags:
- Agent
- Benchmark
- LLM Agent
- Evaluation
- Autonomous Experiment
one_liner: 首个整合自主实验设计、缺陷模拟器、校准区间评分的科学Agent交互式评估基准
practical_value: '- 做Agent能力评估时，可复用「加入刻意缺陷的模拟环境+置信区间校准评分」的范式，避免只测最终结果正确性，覆盖鲁棒性评估

  - 电商决策/导购类Agent落地时，强制要求输出决策逻辑+置信区间，比单纯扩大置信范围可提升1.6~2.5倍的区间得分

  - Agent推理成本优化可参考token-效果trade-off结论：高效果模型默认token消耗是普通模型的6倍，同token约束下效果会下滑，可根据业务容忍度选推理参数'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有科学Agent评估多仅校验最终结果正确性，未覆盖存在缺陷工具、自主设计实验、置信度校准等真实场景下的核心科学判断能力。
### 方法关键点
搭建SciResearch-Eval交互式基准，以材料热属性测量任务为载体，要求Agent自主设计实验、使用存在物理缺陷的热传导模拟器输出带95%置信区间的结果，基于真值做校准评分。
### 关键结果数字
9款模型在93项任务2511次episode测试中，普通模型置信区间真值覆盖率仅20%~62%，GPT-6 Astra达94%、Claude Fable 5.2达99%；要求Agent明确输出实验策略可将区间评分提升1.6~2.5倍；高算力模式下Claude 5.5 Opus效果提升超10倍，但推理成本是默认模式的13~31倍；Fable 5.2默认效果是Astra的1.9倍，但token消耗高6倍，同token约束下效果不及Astra。
