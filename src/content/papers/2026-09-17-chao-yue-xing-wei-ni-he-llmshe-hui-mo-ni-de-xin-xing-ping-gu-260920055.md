---
title: 'What People Almost Did: Evaluating LLM Social Simulations Beyond Behavioral
  Fit'
title_zh: 超越行为拟合：LLM社会模拟的新型评估指标研究
authors:
- JaeWon Kim
- Angie Boggust
affiliations:
- University of Washington
- MIT CSAIL
arxiv_id: '2609.20055'
url: https://arxiv.org/abs/2609.20055
pdf_url: https://arxiv.org/pdf/2609.20055
published: '2026-09-17'
collected: '2026-09-18'
category: Agent
direction: Agent 社会模拟评估指标优化
tags:
- LLM Agent
- Social Simulation
- Evaluation Metric
- Reasoning Trace
- Behavioral Fit
one_liner: 新增表征充足性评估指标，衡量LLM社会模拟行为背后推理过程的人群与场景保真度
practical_value: '- 做电商/广告用户行为仿真Agent时，不能仅评估行为匹配度，新增「场景-推理-行为」三元组校验，区分「用户没看到商品」「对商品不感兴趣」等相同行为的不同决策原因，避免策略误判

  - 可复用推理trace采集校验思路，在运营策略、用户增长仿真场景下，先验证Agent对用户决策逻辑的还原度，再跑大规模干预仿真，降低真实实验的成本与伦理风险

  - 推荐冷启动场景的用户persona模拟可引入表征充足性评估，确保模拟用户的决策逻辑符合目标人群特征，提升冷启动召回/排序的准确率'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 动机
当前LLM社会模拟仅以行为拟合为核心评估目标，仅能还原用户「做了什么」，无法支撑行为归因、干预效果仿真等需要明确行为背后决策逻辑的场景；相同行为可能对应完全不同的决策原因，仅靠行为拟合无法保障仿真结果的有效性。

### 方法关键点
新评估目标为**表征充足性（representational adequacy）**，核心逻辑是通过挖掘LLM推理trace，校验仿真输出的「场景-推理-行为」三元组是否与真实人群、真实场景的决策逻辑一致；同时明确该指标与可解释性、对齐指标的边界差异，给出集成到现有仿真研究的落地路径。

### 核心结论
该指标可有效弥补行为拟合评估的盲区，大幅提升LLM社会仿真在策略验证、行为归因场景的可信度，其量化测量方法目前仍为开放研究问题。
