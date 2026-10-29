---
title: 'What Victims Take Away: Attack Reuse and Defense Revision after Prompt-Injection
  Attacks'
title_zh: Prompt Injection攻击后受害方的攻击复用行为与防御优化研究
authors:
- Zihan Chen
- Lei Nico Zheng
- Di Zhu
affiliations:
- Stevens Institute of Technology
- University of Massachusetts Boston
arxiv_id: '2610.36422'
url: https://arxiv.org/abs/2610.36422
pdf_url: https://arxiv.org/pdf/2610.36422
published: '2026-10-27'
collected: '2026-10-29'
category: LLM
direction: LLM安全 · Prompt Injection攻防
tags:
- Prompt Injection
- LLM Security
- Social Learning
- Attack Reuse
- Defense Revision
one_liner: 基于56万+攻击记录量化揭示LLM Prompt Injection攻击后受害方的攻击复用与防御迭代规律
practical_value: '- 搭建电商导购/客服Agent等LLM应用的攻击告警系统时，仅向运营人员披露攻击技术特征，不要暴露完整攻击payload，避免被恶意复用

  - LLM应用防御规则迭代时，针对曾攻破自身的同家族攻击特征做定向过滤，可降低20%+的同类型攻击成功率

  - 监控LLM系统攻击日志时，可重点标记已被成功利用的payload的传播特征，提前拦截批量复用的已知攻击'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 动机
现有LLM系统通常向运营方披露完整的Prompt Injection攻击明文日志用于修复防御，但明文payload存在被受害方复用攻击其他系统的风险，此前缺乏相关行为规律的量化研究。
### 方法关键点
基于Tensor Trust在线LLM攻防游戏的563349条全量攻击记录，对比受害方收到的攻击与同期同圈层未触达的匹配攻击的复用率，结合社会学习理论分析行为逻辑。
### 关键结果数字
- 攻破自身防御的攻击1周内被受害方复用率达10.0%，是未触达匹配攻击复用率（0.03%）的300+倍
- 受害方修复防御后，同家族攻击的成功率相对其他防御者下降24.5个百分点
- 成功的劫持攻击中23.2%来自攻击者此前收到的攻击文本，仅披露攻击技术而非完整payload可大幅降低复用风险
