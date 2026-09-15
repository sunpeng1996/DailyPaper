---
title: 'Pick Your Poison: Learning to Select Poison Sets for Stronger LLM Backdoor
  Attacks'
title_zh: 投毒最优选择：面向更强LLM后门攻击的毒样本集选择方法
authors:
- Aashiq Muhamed
- Mona T. Diab
- Virginia Smith
- Andrew Ilyas
- Matthew Jagielski
affiliations:
- Carnegie Mellon University
- Anthropic
arxiv_id: '2609.15029'
url: https://arxiv.org/abs/2609.15029
pdf_url: https://arxiv.org/pdf/2609.15029
published: '2026-09-13'
collected: '2026-09-15'
category: LLM
direction: LLM安全 · 后门投毒攻击优化
tags:
- Backdoor Attack
- Poisoning Attack
- LLM Security
- Fine-tuning
- Set Optimization
one_liner: 提出SAILS毒样本集选择框架，同等投毒量下大幅提升LLM后门攻击成功率
practical_value: '- 针对业务定制LLM微调场景，可复用SAILS的评估逻辑排查训练数据中的高风险毒样本集，提前规避后门风险

  - 做LLM应用安全审计时，不要用随机采样毒集评估脆弱性，需用基于集优化的方法评估最坏攻击风险

  - Agent系统依赖第三方微调数据时，可参考本文的毒集优先级排序逻辑，过滤高风险候选训练样本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有LLM后门攻击评估默认随机采样固定数量毒样本，严重低估模型最坏脆弱性，相同模型、干净数据、投毒量下，攻击成功率波动区间达3%~80%。

### 方法关键点
将毒样本集选择形式化为有限oracle预算下的集合优化问题，SAILS框架逻辑为：先通过数百次微调+评估迭代训练集打分器，再对百万级候选集排序，仅审计少量候选短名单即可选出最优毒集。

### 关键结果数字
比最强影响力基线的域外攻击成功率平均高30个百分点，可从小规模微调迁移到全量微调，适配代码生成、Agent、仅API访问等多类后门场景。
