---
title: Evidence-First Agentic Verification
title_zh: 证据优先的智能体验证框架SAURON：长周期任务可靠评估
authors:
- Reza Sanayei
- Razvan-Gabriel Dumitru
- Sunjie Hou
- MohammadHossein Rezaei
- Haris Riaz
- Robert Vacareanu
- Minglai Yang
- Ying Liu
- Mihai Surdeanu
- Daniel Yue Zhang
affiliations:
- Scale AI
- University of Arizona
arxiv_id: '2610.17724'
url: https://arxiv.org/abs/2610.17724
pdf_url: https://arxiv.org/pdf/2610.17724
published: '2026-10-12'
collected: '2026-10-20'
category: Agent
direction: 智能体验证 · 奖励对齐与可靠性评估
tags:
- Agent Verification
- Reward Alignment
- LLM Judge
- Rubric Evaluation
- Fault Detection
one_liner: 提出证据优先的智能体验证框架SAURON，更低成本下实现更高验证准确率与奖励作弊检测能力
practical_value: '- 搭建电商导购、内容推荐类Agent的评估/RL奖励模块时，可复用证据优先的解耦架构：将证据收集与校验独立，所有判决必须锚定独立验证过的用户行为trace、商品状态等源数据，避免被Agent生成的虚假话术误导

  - 长会话推荐归因、广告投放全链路核验这类长trace评估场景，可照搬聚类+bounded query设计：先将相似评估维度聚类共享证据，仅按需拉取相关片段而非全量输入LLM，实测可降本20%以上同时提升准确率

  - 检测推荐/广告Agent的奖励Hacking行为时，可复用PAFault的正负配对故障注入评估范式，提前验证评估模块的抗欺骗能力，避免Agent学出钻规则漏洞的作弊行为（如诱导无效点击、虚假下单引导）'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长周期智能体任务当前多基于rubric评估，但相关证据散落在环境状态、执行trace中，普通LLM法官易漏看证据、轻信智能体自报告，错误判决作为RL奖励会强化不良行为甚至奖励Hacking，现有验证器普遍存在成本高、流程类指标准确率低的问题。

### 方法关键点
- 轻量规划层先将rubric评估维度按共享证据聚类，生成仅作参考的任务摘要，每个聚类并行启动调查会话，减少冗余工作
- 采用bounded query机制，仅按需拉取状态、trace的相关片段，而非全量输入LLM，大幅降低上下文消耗
- 证据收集与校验完全解耦：调查员提出的所有claim必须由独立模块核对源数据，精确匹配类自动校验，解释类用隔离的忠实度校验器校验，仅通过校验的claim可支撑判决
- 所有判决附带可审计的证据溯源收据，未找到有效证据的指标默认判定为不满足

### 关键实验
在三个基准集上对比5款现有验证器，覆盖8种LLM backbone：PA100（100个个人助理长周期任务，2586个人工标注指标）上，用GPT-5.6 Sol时F1达0.96，比最强基线Gandalf高0.04，成本低23%；PAFault（637对故障注入样本含奖励Hacking）上检测到97%的注入故障，误报率仅2%；TRAIL真实智能体错误检测集上所有指标均领先基线。

最值得记住的结论：智能体验证不能轻信智能体的自报告，所有判决必须锚定独立校验过的源证据，才能从根源上降低奖励Hacking风险。
