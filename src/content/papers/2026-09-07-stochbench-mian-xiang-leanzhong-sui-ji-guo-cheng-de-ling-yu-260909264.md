---
title: 'StochBench: A Domain-Specific Benchmark for Stochastic Processes in Lean'
title_zh: StochBench：面向Lean中随机过程的领域专用基准
authors:
- Idan Davidovich
- Debargha Ganguly
- Vikash Singh
- Vipin Chaudhary
affiliations:
- Case Western Reserve University
arxiv_id: '2609.09264'
url: https://arxiv.org/abs/2609.09264
pdf_url: https://arxiv.org/pdf/2609.09264
published: '2026-09-07'
collected: '2026-09-13'
category: Eval
direction: LLM定理证明领域专用评测基准
tags:
- Benchmark
- Theorem Proving
- Stochastic Process
- Lean4
- LLM Agent
one_liner: 推出含450道研究生难度随机过程题的Lean4基准StochBench，测试Opus4.8智能体证明率达34.9%
practical_value: '- 构建垂直领域评测集时可参考「优先领域深度而非跨域广度，标注多抽象层级样本」的设计思路

  - 评估Agent复杂推理能力时，可复用「单任务超时限制+可验证输出正确性」的标准化评测范式

  - 开发涉及定价、库存优化等数理推理的电商Agent时，可借用该基准测试底座LLM的随机过程推理能力'
score: 3
source: huggingface-daily
depth: abstract
---

### 动机
现有LLM形式化定理证明基准多取自IMO、Putnam等竞赛数学，样本量小，无法准确反映模型在垂直领域应用场景下的真实能力，随机过程领域相关评测资源在Mathlib中严重缺失。
### 方法关键点
推出StochBench适配Lean 4形式化验证环境，包含450道不同抽象层级的研究生难度随机过程题目，每道匹配对应自然语言源，覆盖有限/可数马尔可夫链、更新过程、随机游走、鞅、随机微积分、布朗运动等10余个子领域。
### 关键结果
基于Opus 4.8的Agent在单题15分钟时限约束下，证明率达34.9%（157/450），基准兼具领域代表性与高挑战性，可有效支撑垂直领域定理证明Agent的能力评测。
