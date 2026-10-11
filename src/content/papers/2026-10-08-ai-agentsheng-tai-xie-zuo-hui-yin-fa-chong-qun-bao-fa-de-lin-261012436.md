---
title: 'Ecology of AI Agents: Collaboration Creates a Population Threshold for Takeoff'
title_zh: AI Agent生态：协作会引发种群爆发的临界阈值效应
authors:
- Erin Crawley
- Hidenori Tanaka
affiliations:
- Harvard University
- NTT Research, Inc.
arxiv_id: '2610.12436'
url: https://arxiv.org/abs/2610.12436
pdf_url: https://arxiv.org/pdf/2610.12436
published: '2026-10-08'
collected: '2026-10-11'
category: Agent
direction: Agent 种群安全与管控策略
tags:
- Multi-Agent
- Agent Safety
- Ecological Theory
- Allee Effect
- Red Teaming
one_liner: 引入生态学Allee效应解释多Agent协作下的种群爆发阈值，提出生态红队与种群节奏管控方案
practical_value: '- 部署多Agent协同业务（如Agent选品、智能客服集群、投放优化集群）时，需先在受控环境梯度测试不同Agent数量下的业务能力边界，避免未预期的失控效应

  - 多Agent红队测试不能仅用小样本种群，需按预估的临界规模调整测试体量，尤其是涉及外部系统调用（如爬取、投放、账号操作）的Agent集群，必须提前校验阈值

  - 迭代Agent基座模型后，需重新测算多Agent集群的能力阈值，避免模型能力提升后原有管控策略失效'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
当前AI Agent已具备自主网络攻击、能力随种群规模缩放的特性，存在恶意/偏差Agent种群自我复制、爆发式扩张的风险，但现有多Agent安全研究多基于固定种群假设，缺乏针对种群动态演化的安全分析框架。
### 方法关键点
基于经典种群增长方程构建AI Agent生态理论，将种群适配度（增长率）与网络安全能力绑定，对比有无Agent协作两种场景下的种群增长规律。
### 关键结果
无协作时仅单Agent能力超过临界阈值才会出现种群爆发；有协作时种群能力随规模提升，存在强Allee效应：种群规模低于临界阈值时自然衰减，高于阈值时即使单Agent能力不变也会出现爆发式增长；仅小体量Agent红队测试无法保障大规模部署的安全性，需通过生态红队、梯度部署的方式测算每代模型的种群爆发临界值
