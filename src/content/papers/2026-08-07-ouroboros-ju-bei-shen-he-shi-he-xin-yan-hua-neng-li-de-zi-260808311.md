---
title: 'Ouroboros: A Self-Developing Frontier Coding Agent with Reviewed Core Evolution'
title_zh: Ouroboros：具备审核式核心演化能力的自成长前沿编程Agent
authors:
- Anton Razzhigaev
- Andrei Gritsaev
- Andrei Kaznacheev
- Nikita Dragunov
- Roman Yampolskiy
- Andrei Kuznetsov
affiliations:
- Lomonosov Moscow State University
- Skolkovo Institute of Science and Technology
- Joi Lab
- FusionBrain Lab at Artificial Intelligence Research Institute
arxiv_id: '2608.08311'
url: https://arxiv.org/abs/2608.08311
pdf_url: https://arxiv.org/pdf/2608.08311
published: '2026-08-07'
collected: '2026-08-11'
category: Agent
direction: 自进化编程Agent架构与安全管控
tags:
- Self-Evolving Agent
- Coding Agent
- Agent Safety
- SOTA
- Autonomous Improvement
one_liner: 提出带双演化模式与安全护栏的自迭代Agent框架，在多个编程基准上达SOTA
practical_value: '- 自迭代架构可复用：双演化模式（主动自优化+任务经验驱动优化）+ 审核式提交链路，可直接迁移到电商运营Agent、推荐策略调优Agent的自迭代模块，避免盲目修改导致线上故障

  - 安全护栏设计可落地：独立supervisor层、不可篡改运行宪法、操作权限分级、外部预算管控的设计，完美适配生产环境Agent的风险管控，解决业务Agent自迭代的安全顾虑

  - 多渠道状态统一方案：多入口消息统一落序日志+分场景摘要投射，可复用在电商全渠道客服Agent、用户触达Agent的状态管理，避免多端响应不一致

  - 经验沉淀机制可迁移：错误类持久化+根因修复映射模式，可适配推荐系统badcase自动修复链路，从单次badcase处理升级为同类问题根因解决'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有长周期Agent的执行harness在设计完成后就固定，随着基础模型能力提升，harness对Agent最终性能的影响占比越来越高，固定框架严重限制了Agent能力的持续提升；同时自迭代Agent的安全管控、可审计性问题缺乏成熟落地方案。

### 方法关键点
- 架构拆分：独立不可变的启动监督层 + 可迭代的Agent版本仓库，所有核心代码、prompt、工具、逻辑的变更都走版本控制+审核提交链路
- 双演化模式：① 递归自由演化：Agent主动将自身优化作为任务，完成后自动调度下一轮迭代；② 经验驱动演化：从常规任务执行、用户反馈、错误日志中提取问题，经审核后合并到核心框架
- 安全管控机制：内置不可篡改的运行宪法、多模型评审阈值、提交前后diff指纹校验、独立操作员紧急停止通道、外部预算管控，确保自迭代过程中护栏不失效

### 关键实验
在Terminal-Bench 2.1、OSWorld-Verified、CL-Bench三个核心基准上达到SOTA：Opus 5版本在Terminal-Bench 2.1得分86.74%（超基线2.94pct），OSWorld-Verified得分90.69%（超基线0.5pct），Sonnet 4.6版本在CL-Bench得分0.2301（超基线0.0341）；161天的线上部署实例Hope累计处理22万+公开消息，完成1085次自修改提交，Agent自主提交占比94.2%。

### 核心洞见
自迭代Agent的核心不是无约束的自我修改，而是在明确、不可逾越的安全护栏下，将单次任务经验转化为全系统的持久能力提升。
