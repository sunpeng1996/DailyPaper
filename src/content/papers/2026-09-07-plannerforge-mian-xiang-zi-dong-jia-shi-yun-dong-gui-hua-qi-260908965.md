---
title: 'PlannerForge: LLM Agents for Scenario-Based Testing of Motion Planners in
  Autonomous Driving'
title_zh: PlannerForge：面向自动驾驶运动规划器场景化测试的LLM Agent框架
authors:
- Yuan Gao
- Sebastian Müller
- Mattia Piccinini
- Marc Kaufeld
- Yuchen Zhang
- Finn Rasmus Schäfer
- Qunying Song
- Johannes Betz
affiliations:
- Technical University of Munich
- Munich Institute of Robotics and Machine Intelligence
- University College London
arxiv_id: '2609.08965'
url: https://arxiv.org/abs/2609.08965
pdf_url: https://arxiv.org/pdf/2609.08965
published: '2026-09-07'
collected: '2026-09-12'
category: Agent
direction: 自动驾驶 · LLM Agent 全流程测试框架
tags:
- LLM Agent
- Scenario Testing
- Pipeline Orchestration
- Autonomous Driving
- Framework
one_liner: 提出统一LLM Agent框架覆盖自动驾驶全流程场景化测试，新增增强与基准测试环节
practical_value: '- 多环节碎片化工具统一Agent调度的设计思路可复用，可用于搭建电商推荐/搜索全链路自动化评测框架，解决各环节工具割裂、数据不通的问题

  - 20-35B参数开源LLM可在多数任务对标商用API的结论可直接复用，业务侧Agent选型时可优先考虑该参数区间模型，大幅降低调用成本

  - 无领域微调仅通过流程编排与prompt优化提升任务效果的思路，可复用在电商冷启动场景效果评测、异常case自动化挖掘等场景，减少标注与微调成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
当前自动驾驶场景化测试全环节工具碎片化、各模块交互性弱，尚无统一LLM Agent框架覆盖完整测试流程。
### 方法关键点
1. 提出PlannerForge统一LLM Agent框架，覆盖场景生成、检索、修改、执行、评估全测试环节，额外新增ADS增强、ADS基准测试两个LLM增强阶段；
2. 支持10款开源/商用LLM接入，适配5种prompt条件，模块支持端到端串联调用。
### 关键结果数字
单任务最优得分区间0.88~1.00，20~35B参数开源LLM在多数任务上效果匹配商用API，Qwen3.6:35B在3/5任务上平替商用API；端到端串联可保留83%（商用）/78%（开源）种子查询；自然语言生成可执行场景占比193/200，优于SOTA的144/200；Top1场景检索准确率92.0%，优于BM25的67.5%；物理有效编辑率≥94%，优于SOTA的31%；无需领域微调即可将规划成功率从50.4%提升至70.2%，碰撞率从19.0%降至8.4%。
