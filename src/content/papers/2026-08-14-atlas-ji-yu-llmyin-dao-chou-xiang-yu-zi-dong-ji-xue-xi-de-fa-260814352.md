---
title: 'ATLAS: Discovering Agent Strategies through LLM-Guided Abstraction and Automata
  Learning'
title_zh: ATLAS：基于LLM引导抽象与自动机学习的Agent策略发现框架
authors:
- Ignacio D. Lopez-Miguel
- Andreas Happe
- Jürgen Cito
- Ezio Bartocci
- Bettina Könighofer
- Martin Tappler
affiliations:
- TU Wien
- TU Graz
arxiv_id: '2608.14352'
url: https://arxiv.org/abs/2608.14352
pdf_url: https://arxiv.org/pdf/2608.14352
published: '2026-08-14'
collected: '2026-08-17'
category: Agent
direction: Agent行为分析 · 策略挖掘
tags:
- AI Agents
- Automata Learning
- Explainable AI
- Knowledge Transfer
- LLM Abstraction
one_liner: 结合LLM语义抽象与自动机学习从Agent轨迹提取可解释行为模型并支持跨模型知识迁移
practical_value: '- 可复用LLM引导的轨迹抽象pipeline：将电商导购Agent、搜索推荐Agent的用户交互/工具调用原始轨迹，通过「批量分类→类别归一化→逐轨迹映射」三步转换为语义符号，解决原始轨迹噪声大、语义冗余问题，降低后续行为分析门槛

  - 自动机学习的行为模型可直接落地业务：用于挖掘电商Agent高转化路径、识别无效循环行为（如重复查询同个商品），也可部署为运行时监控器，检测Agent偏离预期的异常行为（如违规推荐违禁品）

  - 跨模型知识迁移思路可直接复用：用大模型跑复杂业务场景（如大促活动导购、复杂用户需求应答）得到轨迹，学习为行为模型后指导小模型执行，动态迁移模式可将小模型成功率从1.7%提升至38.3%，大幅降低推理成本

  - 可解释性提取方法可复用：通过DAG提取、top-k剪枝+强连通分量合并的方式，从复杂行为模型中压缩出核心成功路径，用于业务复盘、Agent策略迭代参考'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前LLM Agent决策过程黑盒化，现有评估仅聚焦任务成功率与单条执行轨迹，无法挖掘通用决策策略、识别隐性故障模式，也难以实现策略跨模型复用；高风险场景（如交易Agent、安全Agent）下缺乏可解释行为模型会导致风险不可控，因此亟需从历史轨迹中自动提取结构化的Agent行为策略。

### 方法关键点
- LLM驱动的轨迹抽象流水线：分三步完成原始轨迹的语义符号化，首先批量将<Agent动作,环境观测>对映射到初始语义标签，接着归一合并冗余标签得到稳定符号集，最后逐轨迹完成符号映射，内置重试机制修正LLM输出格式错误。
- 自动机行为建模：采用Alergia状态合并算法对抽象后的符号轨迹进行学习，生成带转移概率的Markov Chain（MC）模型，自动捕获Agent决策分支、循环行为、成功路径等核心模式，无需预设状态规则。
- 下游落地能力：支持两类核心应用，一是跨模型知识迁移，将大模型学到的MC策略通过4种模式注入小模型，动态模式实时跟踪MC状态为小模型输出单步执行指导；二是可解释模型提取，通过DAG提取、top-k剪枝+强连通分量合并两种方式压缩MC，得到轻量化核心策略路径。

### 关键实验结果
数据集为12台Linux漏洞靶机的渗透测试轨迹，每台靶机采集大模型（DeepSeek V4 Flash）20轮执行轨迹。对比不同迁移模式下小模型的任务成功率：ministral-14b基线成功率仅1.7%，动态迁移模式下提升至38.3%，覆盖6个靶机；Guided模式成功率达21.7%。可解释模型提取可将最高57个状态的原始MC压缩到7个状态，完整保留核心成功路径。

### 核心结论
Agent执行轨迹不是被动的日志产物，而是可转化为可复用、可分析的一阶工程化行为模型，是黑盒Agent治理的核心抓手。
