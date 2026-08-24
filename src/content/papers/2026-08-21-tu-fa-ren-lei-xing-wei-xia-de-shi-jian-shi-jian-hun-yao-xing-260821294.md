---
title: Event-Time Confounding Under Bursty Human Dynamics
title_zh: 《突发人类行为下的事件时间混淆：行为日志事件窗口偏误研究》
authors:
- Michael Iannelli
- Alan Ai
affiliations:
- Scrunch AI
arxiv_id: '2608.21294'
url: https://arxiv.org/abs/2608.21294
pdf_url: https://arxiv.org/pdf/2608.21294
published: '2026-08-21'
collected: '2026-08-24'
category: Eval
direction: 用户行为分析 · 因果偏误校验
tags:
- Causal Inference
- Event Study
- Log Analysis
- Bias Detection
- User Behavior
one_liner: 揭示行为日志事件研究将任务延续误判为事件效果的偏误，给出诊断方案与轻量审计工具
practical_value: '- 做推荐点击/AI助手唤起/商品页访问等事件的效果评估时，不能默认事后活动增长就是事件效果，需先排除用户正处于任务周期的干扰

  - 效果验证可复用论文提出的安静时刻基线法：选择用户无前置活动的触发时段做分析，可大幅降低内生时间零点带来的偏误

  - 可直接接入开源burstcheck工具，对现有AB实验、事件研究的结果做偏误审计，避免误判策略效果'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 动机
过往数字行为研究常以用户主动触发事件（点击推荐、打开AI助手、访问商品页等）为时间零点，将事后活动增长直接归为事件效果，存在内生时间零点的因果混淆风险。
### 方法关键点
1. 分析跨端用户行为日志，验证AI、购物、新闻等多场景事件前均存在前置活动高峰，零点后活动增长可能是任务延续而非事件响应；
2. 采用无因果效应的null timestamp做对照，证明单端事件窗口无法脱离额外假设区分真实效果与偏误，用户固定效应、粗粒度活动匹配均无法消解该用户内时变混淆；
3. 形式化定义episode-selection偏误，配套输出诊断协议、公开基准与轻量burstcheck审计工具。
### 关键结果
严格符合前置活动与洗脱标准的AI响应中，null timestamp事后搜索活动是用户内安慰剂组的3.42倍，真实事件为4.32倍；活跃时段null timestamp可复现56%的超额活动，安静时段该值降至-0.04，无偏误。
