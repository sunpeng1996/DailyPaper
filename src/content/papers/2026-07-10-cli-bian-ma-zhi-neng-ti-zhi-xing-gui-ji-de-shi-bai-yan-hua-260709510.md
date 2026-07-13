---
title: 'Failure as a Process: An Anatomy of CLI Coding Agent Trajectories'
title_zh: CLI 编码智能体执行轨迹的失败演化过程解剖
authors:
- Xiangxin Zhao
- Han Li
- Shuaiting Li
- Tianyi Zhao
- Earl T. Barr
- Federica Sarro
- He Ye
affiliations:
- University College London
- Nanjing University
arxiv_id: '2607.09510'
url: https://arxiv.org/abs/2607.09510
pdf_url: https://arxiv.org/pdf/2607.09510
published: '2026-07-10'
collected: '2026-07-13'
category: Agent
direction: Agent 行为分析 · 失败轨迹实证研究
tags:
- LLM Agent
- Failure Analysis
- CLI Coding Agent
- Empirical Study
- Trajectory Analysis
one_liner: 首次将CLI编码Agent失败视为时序过程，开展大规模实证研究并产出14项普适性发现
practical_value: '- 可复用三阶段错误拆解框架（`t_err`/`t_lock`/`t_obs`）搭建Agent执行轨迹监控系统，在` t_lock`之前的修复窗口介入拦截异常，可降低电商运营、推荐系统调优等场景下Agent的无效执行开销

  - 优先优化Epistemic认知类错误，尤其是虚假假设问题：给Agent增加关键假设校验步骤，比如调用推荐API、操作电商后台前先校验环境、权限、入参是否符合预期，可降低50%以上的故障率

  - 给Agent设置修复时长阈值：当修复尝试超过5步（成功修复中位数）时触发重新诊断，避免无效修错浪费资源；同时增加独立的结果校验模块，防范Agent伪造成功的情况

  - 选型Agent系统时需同时评估基座模型和Scaffold的组合效果，二者对最终成功率的影响均显著，不要仅盲目升级大模型而忽略Scaffold的场景适配'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有LLM编码Agent失败研究均将失败视为静态最终结果，未覆盖CLI终端场景下失败从产生、演化到不可恢复的完整时序过程，无法为早期干预、提升Agent可靠性提供有效指导，而CLI是当前工业级编码Agent的核心执行环境，其可靠性问题直接影响落地效果。

### 方法关键点
- 提出面向过程的失败分析框架，将失败轨迹拆解为3个关键时间节点：决定性错误出现`t_err`、失败不可恢复锁定`t_lock`、错误首次可观测`t_obs`，衍生修复窗口、观测延迟两个核心度量
- 采集3款主流Agent Scaffold（OpenHands、MiniSWE、Terminus2）+7款前沿大模型在Terminal-Bench上的3843条原始轨迹，过滤得到1794条有效样本（覆盖63000+执行步骤），采用Claude Opus预标注+双人人工校验的标注流程，标注一致性Cohen's κ达0.78~0.94
- 从错误发生时机、根因分类、恢复行为、跨系统一致性4个维度开展量化分析

### 关键结果
- 决定性错误中位数出现在第7步，修复窗口中位数仅1步，可观测信号平均滞后10步，28%的失败全程无任何显性信号
- 57.9%的失败为Epistemic认知类错误（误用已有信息），其中虚假假设占30.7%是第一大失败诱因，仅32.8%为能力不足导致的失败
- 失败后仅18%的Agent会立即终止，剩余82%会持续无效执行，其中错误诊断导致的无效修复占39%的计算浪费；71%的成功轨迹也会出现错误，但是可在中位数5步内完成修复
- 跨21种模型+Scaffold组合，认知类错误始终是首要失败原因，占比达44%~80%

> 最值得记住的结论：编码Agent失败的核心诱因不是能力不足，而是对已有信息的误用，提前校验关键假设的收益远高于后期修复。
