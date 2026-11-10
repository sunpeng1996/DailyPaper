---
title: 'THEATRON: A Benchmark for Evaluating Persona Persistence in Long-Horizon LLM
  Decision-Making'
title_zh: THEATRON：长序列LLM决策中人物设定持续性评测基准
authors:
- Yuyan Wang
- Yuechen Jiang
- Zhiwei Liu
- Jimin Huang
- Sophia Ananiadou
affiliations:
- The University of Manchester
- The Fin AI
- ELLIS Manchester
arxiv_id: '2611.11487'
url: https://arxiv.org/abs/2611.11487
pdf_url: https://arxiv.org/pdf/2611.11487
published: '2026-11-08'
collected: '2026-11-10'
category: Agent
direction: Agent 长周期决策人设一致性评测
tags:
- LLM Agent
- Persona Persistence
- Long-Horizon Decision
- Benchmark
- Evaluation
one_liner: 提出金融场景可控基准，评估不同人设注入方法下LLM长周期决策的人设持续性
practical_value: '- 做个性化Agent人设对齐时，需在单轮语义一致性之外，增加长序列轨迹的组内稳定性、组间区分度双维度评估，规避人设漂移或行为跳变问题

  - 电商用户行为模拟、数字人前置AB测试可复用该框架：固定外部环境+人设注入+轨迹层指标，缩小线下模拟与线上真实行为的gap

  - 纯prompt注入人设（Zero-Shot/One-Shot/CoT）仅能改变行为分布，无法解决长周期人设漂移，业务需搭配持久化用户偏好向量保障一致性

  - 若出现Agent行为可解释但不符合人设的情况，需排查两种失效模式：刻板动作坍缩、噪声策略跳变'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM人设评测多聚焦单轮对话的语义表达一致性，无法验证长序列决策场景下人设是否能持续指导行为，而个性化Agent、用户数字孪生等落地场景均依赖人设的长期行为稳定性，高stake决策场景下人设漂移会直接导致业务受损。
### 方法关键点
- 构建金融场景可控基准THEATRON，覆盖3支股票102个交易日的行情、新闻、公告数据，设定过度自信、损失厌恶、羊群效应3种典型行为金融学人设
- 任务为固定人设+每日行情+账户反馈的序列决策任务，动作空间为BUY/HOLD/SELL，每步动作会影响后续账户状态输入
- 提出三维度评估框架：组内稳定性、组间区分度、动作多样性，可排除刻板动作坍缩导致的假阳性区分
### 关键结果
- 测试4款主流LLM、3种人设注入方法，人设注入相对无角色基线可产生22.5~96.5pp的行为偏移，跨人设区分度是组内方差的1.21~12.93倍
- 高区分度不代表人设稳定：32%的高区分度场景来自刻板动作坍缩，剩余场景中同一人设的累计收益标准差最高达21.95%，存在严重策略跳变
- One-Shot、CoT、小样本SFT均无法系统性解决上述失效问题
### 核心结论
LLM人设注入仅能产生可观测的行为差异，无法保证长周期下形成上下文感知的稳定人设决策策略，仅用区分度指标评估人设一致性会产生严重假阳性
