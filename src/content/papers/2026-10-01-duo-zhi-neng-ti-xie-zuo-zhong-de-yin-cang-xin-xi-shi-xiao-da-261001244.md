---
title: 'Right Answers, Wrong States: Hidden Information Failures in Multi-Agent Collaboration'
title_zh: 多智能体协作中的隐藏信息失效：正确答案背后的错误共享状态
authors:
- Herun Wan
- Jiaying Wu
- Minnan Luo
- Zihan Ma
- Fanxiao Li
- Nancy F. Chen
- Min-Yen Kan
affiliations:
- Xi'an Jiaotong University
- National University of Singapore
- Yunnan University
- Agency for Science, Technology and Research (A*STAR), Singapore
arxiv_id: '2610.01244'
url: https://arxiv.org/abs/2610.01244
pdf_url: https://arxiv.org/pdf/2610.01244
published: '2026-10-01'
collected: '2026-10-02'
category: MultiAgent
direction: 多智能体协作 · 共享状态可靠性优化
tags:
- Multi-Agent
- Shared State
- Collaboration Reliability
- Benchmark
- Information Failure
one_liner: 提出OFFQUERY基准检测多Agent隐藏信息失效，REGROUND框架大幅提升共享状态可靠性
practical_value: '- 电商/广告多Agent业务系统（如智能导购、投放决策）不要仅评估当前任务准确率，需增加共享状态校验环节，避免历史错误信息在后续任务中引发故障

  - 可复用REGROUND三阶流程：先做冲突引导的证据校验识别不可靠信息源，再做原子事实粒度的状态重构，最后基于可信状态推理，适配分布式信息输入的决策场景

  - 多源异构信息融合场景（如多渠道用户行为、商品信息、运营规则融合的推荐决策）可参考「先校验私域证据、再引入共享上下文」的顺序，避免被污染的共享信息误导决策

  - 评估多Agent系统可参考OFFQUERY三层评估逻辑：证据校验准确率、共享状态保真度、当前任务准确率，全链路定位系统缺陷'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有多Agent系统仅以当前任务准确率作为评估指标，无法发现「当前答案正确但共享信息状态已被污染」的off-query失效问题，这类隐藏错误会在后续复用共享状态的任务中触发严重故障，尤其在高风险场景下隐患极高，缺乏针对性的评估基准和解决方案。

### 方法关键点
- 提出OFFQUERY基准，覆盖医疗、灾难响应两个高风险领域，拆分三层评估指标：T1证据校验（识别不可靠信息源）、T2共享状态重构（还原可信全局信息）、T3当前任务解决（回答当前查询）
- 提出REGROUND协作框架，分三阶段：1）冲突引导的证据校验，仅用Agent私有证据迭代识别不可靠信息源；2）证据驱动的状态重构，将共享上下文拆分为原子事实，保留经可信源验证的事实、移除错误信息；3）基于重构的可信状态完成当前任务推理

### 关键实验
在7个模型（GPT、Gemini、Qwen全系列）、3个测试场景下验证：标准多Agent协作平均T3准确率达64.7%，但T1仅14.3%、T2仅43.1%；REGROUND相对提升T1达309.0%、T2达82.9%、T3达17.6%；43%的当前任务正确但共享状态被污染的案例，在后续更宽范围的任务中会出现决策错误。

**最值得记住的一句话**：多智能体系统的可靠性不能仅看当前答案正确率，必须将协作后留存的共享信息状态作为核心可靠性指标。
