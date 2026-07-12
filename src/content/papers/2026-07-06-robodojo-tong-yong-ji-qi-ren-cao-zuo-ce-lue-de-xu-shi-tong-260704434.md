---
title: 'RoboDojo: A Unified Sim-and-Real Benchmark for Comprehensive Evaluation of
  Generalist Robot Manipulation Policies'
title_zh: RoboDojo：通用机器人操作策略的虚实统一综合评测基准
authors:
- Tianxing Chen
- Yue Chen
- Zixuan Li
- Junyuan Tang
- Kailun Su
- Haoran Lu
- Weijie Wan
- Baijun Chen
- Songling Liu
- Haowen Yan
affiliations:
- MMLab@HKU
- UC Berkeley
- THU
- PKU
- Stanford
arxiv_id: '2607.04434'
url: https://arxiv.org/abs/2607.04434
pdf_url: https://arxiv.org/pdf/2607.04434
published: '2026-07-06'
collected: '2026-07-12'
category: Eval
direction: 具身AI · 机器人操作策略评测
tags:
- Embodied AI
- Benchmark
- Sim-to-Real
- Evaluation
- Robot Manipulation
one_liner: 推出覆盖42个仿真+18个真实任务的通用机器人操作策略虚实统一评测基准及配套工具链
practical_value: '- 多维度+虚实结合的评测框架设计思路可迁移，可用于电商具身导购Agent、多场景推荐策略的能力评估，避免单一环境评测的结果偏差

  - 一次集成多环境跑测的XPolicyLab框架思路可复用，可降低推荐/Agent策略跨电商不同业务场景做AB测试的适配成本

  - 标准化评测协议（统一硬件/场景重置/流程）的设计思路，可用于大模型/Agent在复杂真实电商业务场景的效果复现性评测'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
通用机器人操作策略迭代速度快，但现有评测基准普遍存在能力覆盖窄、仅支持单一环境（仿真/真实）运行的缺陷：仿真评测忽略真实物理部署挑战，真实世界评测成本高、流程难复现。
### 方法关键点
1. 构建RoboDojo基准，包含42个仿真任务、18个真实世界任务，覆盖泛化性、记忆、操作精度、长序列执行、开放词汇指令跟随5个核心评测维度
2. 基于Isaac Sim实现异构并行仿真支持规模化评测，配套RoboDojo-RealEval可复现真实评测系统，支持云远程访问、标准化硬件/场景重置/评测协议
3. 配套XPolicyLab框架，支持策略一次集成即可在虚实两类环境低适配完成跑测
### 关键结果
已完成30个主流策略的全基准评测，公开了持续更新的公共leaderboard，输出了当前主流通用机器人操作策略的性能系统分析报告。
