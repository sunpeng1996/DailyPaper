---
title: 'SERPO: Self-Evolving Rubric Policy Optimization for Open-Ended Test-Time Reinforcement
  Learning'
title_zh: SERPO：面向开放式生成的自进化评分规则强化学习优化框架
authors:
- Jianze Wang
- Kunwang Zheng
- Ying Liu
- Yu Cao
- Qilong Zhang
- Jinlong Chen
- Hua Yang
- Qianglong Chen
affiliations:
- Huazhong University of Science and Technology
- University of Science and Technology of China
- Alibaba Group
arxiv_id: '2607.26873'
url: https://arxiv.org/abs/2607.26873
pdf_url: https://arxiv.org/pdf/2607.26873
published: '2026-07-29'
collected: '2026-07-30'
category: Training
direction: 大模型测试时自进化 · 无标注RL优化
tags:
- Test-Time RL
- Rubric Evolution
- Self-Evolution
- Open-Ended Generation
- GRPO
one_liner: 提出无需外部标注的响应-评分规则-策略三元闭环测试时强化学习框架，适配开放式生成任务
practical_value: '- 做生成式推荐/Agent开放式回复优化时，可复用G-N-B三档响应归档+动态rubric的闭环设计，无需额外标注即可在线迭代模型效果

  - 做LLM自对齐时，可借鉴概率式判决打分方案，将判决token的logprob转换为连续奖励信号，避免硬判决带来的GRPO优势收缩问题

  - 跨场景迁移落地可参考：仅在目标场景少量query上做30 epoch的SERPO迭代，即可获得最高8%的跨场景效果提升，远低于全量SFT成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有测试时强化学习（TTRL）依赖多数投票构造伪标签，仅适配有标准答案的闭域任务，无法适配开放式生成场景——这类场景响应无统一标准答案，投票易奖励共性遗漏、拒掉有效异构回复，且现有方法依赖外部奖励模型/标注，无法满足部署后无标注自进化需求。
### 方法关键点
- 三元闭环设计：维护每个query对应的Good-Normal-Bad（G-N-B）三档响应归档、query专属动态rubric池、共享策略参数，三者协同迭代
- 概率化奖励接口：提取判决token的logprob转换为0-1连续的准则满足概率，再根据准则极性对齐为统一分数，保留判决置信度差异
- 动态rubric进化：每次迭代从G-N-B响应差异中挖掘新的评分准则，保留能区分三档响应的高效用准则，淘汰低区分度规则
- 策略优化：基于更新后的rubric计算奖励，用GRPO更新策略参数，新的响应再刷新归档和rubric，形成闭环
### 关键实验
在Qwen3-4B、Qwen3.5-9B两个模型上验证，覆盖2个域内基准（HealthBench、ResearchQA）、4个OOD基准，对比投票类TTRL、静态rubric等基线：域内效果最高提升20.63/20.31个点，6个基准的平均提升最高达8.06个点，且进化后的策略支持跨基准迁移和持续进化。
### 核心结论
无外部标注的开放式生成任务自进化，靠的不是多数投票的共识，而是动态演化的、能区分响应质量差异的评分准则。
