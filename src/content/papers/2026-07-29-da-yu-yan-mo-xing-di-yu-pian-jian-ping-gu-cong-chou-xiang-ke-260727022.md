---
title: Evaluating Regional Bias in LLMs From Abstract Stereotype to Concrete Social
  Decision-Making
title_zh: 大语言模型地域偏见评估：从抽象刻板印象到具体社会决策
authors:
- Jiayuan Di
- Haoyi Yang
- Yufei Luo
- Jiahui Qu
- Yiming Wang
affiliations:
- East China University of Science and Technology
- Mohamed bin Zayed University of Artificial Intelligence
- Beijing University of Posts and Telecommunications
- The London School of Economics and Political Science
- Shanghai Jiao Tong University
arxiv_id: '2607.27022'
url: https://arxiv.org/abs/2607.27022
pdf_url: https://arxiv.org/pdf/2607.27022
published: '2026-07-29'
collected: '2026-07-31'
category: Eval
direction: LLM公平性 · 地域偏见全链路评估
tags:
- LLM Bias
- Evaluation Framework
- Stereotype Detection
- Fairness
- Regional Bias
one_liner: 提出S2D评估框架，覆盖中国34个省级行政区，系统量化LLM从抽象刻板印象到决策的地域偏见
practical_value: '- 本地化推荐、招聘类Agent落地前，可复用S2D的「双维度刻板印象+多场景决策」评估范式，检测模型地域偏见，避免差异化对待不同地域用户

  - 电商本地化运营文案生成、用户分层策略迭代前，可参考该框架的跨语种prompt一致性验证方法，确保多语言版本策略公平性

  - 地域相关的召回排序模型迭代时，可参考研究中偏见与经济发展指标的关联结论，针对性校准低发展地区流量权重，降低马太效应'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM地域偏见研究多单独评估刻板印象或决策表现，未明确两者关联结构与实际影响，而LLM广泛应用于教育、招聘、信息服务等场景，地域偏见会导致差异化对待不同地域用户，存在公平性风险。

### 方法关键点
提出Stereotypes-to-Decisions（S2D）全链路评估框架，覆盖中国34个省级行政区，从两层维度评估：1）抽象刻板印象：按Warmth（友好可信）、Competence（能力智力）评分；2）具体决策：覆盖教育、职业、社交三类场景的配对选择任务，共测试6款主流LLM。

### 关键结果
不同LLM的地域偏见结果一致性较高，尤其是Competence评分和职业场景决策；偏见模式与区域经济、数字发展指标强相关，存在单维度高低分化的类人刻板印象；中英文prompt下偏见表现基本稳定，地域偏见具备普遍性、系统性和高影响性。
