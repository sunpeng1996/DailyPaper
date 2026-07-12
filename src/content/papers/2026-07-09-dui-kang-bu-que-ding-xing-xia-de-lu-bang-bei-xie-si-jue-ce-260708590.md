---
title: Robust Bayesian Decision Making under Adversarial Uncertainty
title_zh: 对抗不确定性下的鲁棒贝叶斯决策方法研究
authors:
- Haripriya Harikumar
- Sammie Katt
- Yasir Zubayr Barlas
- Samuel Kaski
affiliations:
- The University of Manchester, UK
- ELLIS Institute Finland
- Aalto University, Finland
arxiv_id: '2607.08590'
url: https://arxiv.org/abs/2607.08590
pdf_url: https://arxiv.org/pdf/2607.08590
published: '2026-07-09'
collected: '2026-07-12'
category: Other
direction: 鲁棒决策 · 贝叶斯实验设计
tags:
- Bayesian Decision Theory
- Adversarial Robustness
- Experimental Design
- Active Learning
- Decision Stability
one_liner: 提出对抗不确定性下的鲁棒贝叶斯实验设计准则，优先保障决策稳定性而非名义最优
practical_value: '- 推荐/广告排序场景可借鉴鲁棒决策思路，将用户环境变化、作弊刷量等对抗扰动纳入排序优化目标，避免输出高置信但脆弱的排序结果，降低线上业务波动

  - 做推荐模型主动学习标注样本选择时，可优先选择能提升决策稳定性的样本，而非仅选择提升模型精度的样本，提升全场景排序效果的鲁棒性

  - Agent 做动态决策（如大促流量调度、广告预算分配）时，可引入最坏情况扰动建模，提升极端业务场景下的决策可靠性'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有决策感知实验设计、主动学习方法默认模型设定准确、最优决策可在真实扰动下保持稳定，但实际场景中大量未建模隐效应会大幅改变决策最优性，引发误导性结论。
### 方法关键点
将可预期的最坏情况非预期效应建模为对抗变量波动，基于贝叶斯决策理论形式化该场景下的对抗鲁棒最优决策，推导有理论支撑的贝叶斯实验设计准则，明确以决策稳定性而非名义最优为优化目标。
### 关键结果
在合成数据集、真实科学数据集上的实验表明，传统决策感知设计方法会快速收敛到高置信但脆弱的决策，本方法产出的决策在对抗波动下的稳定性与可靠性提升显著，完全规避了高置信错误决策问题。
