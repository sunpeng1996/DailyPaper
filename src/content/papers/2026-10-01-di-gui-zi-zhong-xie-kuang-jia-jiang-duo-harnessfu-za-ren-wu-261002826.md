---
title: Scaling Trajectories for Complex Tasks through Recursive Self-Rewrite
title_zh: 递归自重写框架：将多harness复杂任务成功轨迹转化为通用能力
authors:
- Zongxia Li
- Yucheng Shi
- Zhongzhi Li
- Junyao Yang
- Ruhan Wang
- Chengsong Huang
- Fuxiao Liu
- Haitao Mi
- Jordan Boyd-Graber
- LeoweiLiang
affiliations:
- Tencent HY LLM Frontier
- University of Maryland, College Park
- University of Georgia
- National University of Singapore
- Indiana University
arxiv_id: '2610.02826'
url: https://arxiv.org/abs/2610.02826
pdf_url: https://arxiv.org/pdf/2610.02826
published: '2026-10-01'
collected: '2026-10-05'
category: Agent
direction: Agent 自提升 · 轨迹蒸馏
tags:
- RSR
- Agent Self-Improvement
- Trajectory Rewriting
- Multi-Harness
- SFT
one_liner: 提出递归自重写RSR框架，将多harness成功轨迹转化为通用harness下的训练样本提升模型复杂任务表现
practical_value: '- 多harness采集轨迹思路可复用：电商Agent解决商品运营、用户复杂问题时，可同时部署工具增强、反思循环、状态管控三类harness采集成功路径，比单harness任务覆盖量提升30%以上

  - RSR轨迹蒸馏流程可直接迁移：先将带外部干预的业务成功轨迹提取为无信息泄漏的执行手册（runbook），再让Agent在通用生产环境下重新执行生成无偏训练样本，避免直接SFT引入的分布偏移

  - Agent SFT优先使用重写后的标准化轨迹：比直接用原始采集轨迹的任务pass@3最高提升20个百分点，还能避免模型学习到循环、死胡同类异常行为'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
复杂任务的成功轨迹是Agent自提升的核心监督信号，但不同harness（执行控制框架）下采集的轨迹包含大量专属控制逻辑、人工干预、任务专属提示，直接用于SFT会带来严重分布偏移，模型推理时无对应harness支持就会失效，现有方法无法高效将多harness的互补成功经验转化为模型通用能力。

### 方法关键点
- 多harness互补采集：同时用3种特性互补的harness（通用交互Terminus2、状态管控StateM、结果引导反思RSRT）执行任务，收集覆盖更多领域的成功轨迹，充分挖掘单模型的潜力
- 三模块递归自重写：Planner将原始轨迹提炼为仅包含关键步骤、检查点、容错策略的runbook；Critic筛查runbook的答案泄漏、harness专属信息，不合格的返回Planner重写；Executor基于合格runbook在通用harness的全新沙箱中重新执行，过滤带泄漏的样本后得到无偏新轨迹
- 全流程用同一基座模型完成，无需额外人工标注

### 关键实验
基座采用Qwen-3.8-27B，采集3K左右终端任务的2001条原始成功轨迹，经RSR重写后扩展为11094条高质量训练样本。对比原始基座、直接用原始轨迹SFT的基线，RSR训练后pass@3在Terminal-Bench2从57.0%提升到74.2%，Terminal-Bench4从1.5%提升到9.1%，自构建的Terminal-Bench Hard从39.0%提升到63.0%，所有指标均大幅优于直接SFT。

> 最值得记住的话：不同harness不仅是推理阶段提升Agent表现的工具，更是挖掘多样化成功经验、实现模型自提升的优质数据来源。
