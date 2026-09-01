---
title: Which LLM for Which Work? Budgeted Model Allocation under Uncertain Evaluation
title_zh: 固定预算下存在评估不确定性的LLM任务分配优化方法
authors:
- Hamed Khosravi
- Xiaoming Huo
affiliations:
- Georgia Institute of Technology
arxiv_id: '2608.29560'
url: https://arxiv.org/abs/2608.29560
pdf_url: https://arxiv.org/pdf/2608.29560
published: '2026-08-30'
collected: '2026-09-01'
category: LLM
direction: LLM部署 · 预算约束下任务分配
tags:
- LLM Routing
- Budget Optimization
- Causal Inference
- Active Experimentation
- Robust Optimization
one_liner: 提出CASE主动实验框架，在评估不确定性下低成本确定最优LLM-任务分配方案
practical_value: '- LLM多任务调度场景可复用CASE的两次求解校验逻辑：先基于当前估计解多重选择背包，再构造最不利效果表重解，结果一致则无需额外评估，大幅降低评测成本，适合电商客服、商品文案生成、用户咨询应答等多LLM负载的降本场景

  - 评估存在不可消弭的偏差时（如LLM打分偏好、用户点击与真实满意度的Gap），无需追求完全准确的效果估计，仅需验证当前最优分配在所有合理效果区间内仍为最优即可，可复用该思路优化推荐系统多策略/多模型的流量分配

  - 主动评估仅需聚焦两次求解结果不一致的模型-任务对，无需全量评测，适合业务侧LLM选型、推荐策略调优的小流量实验设计，可降低70%以上的实验成本

  - 预算越紧张，分配方案对效果评估偏差的容忍度越高，低预算场景下可适当降低评测频率，优先保障核心任务的模型分配'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
企业LLM部署需在固定预算下给不同任务分配合适的模型，但模型在各任务上的真实效果存在两类难以消除的偏差：一是生产日志中模型被分配的请求难度不同导致的选择偏差，二是代理指标（如LLM打分、点击）和业务真实目标的测量偏差，现有方法无法同时解决两类偏差下的最优分配问题，且盲目增加评测投入也无法消除测量偏差。

### 方法关键点
- 放弃精确估计模型-任务效果表，转而验证当前分配是否在所有符合观测证据的合理效果区间内均为最优，仅需两次多重选择背包求解即可完成校验：第一次基于当前修正后的效果表求解最优分配，第二次构造对当前分配最不利的效果表（选中模型效果取区间下限，其余取上限）再求解，若两次结果一致则分配确定，不一致则识别出争议的模型-任务对。
- 提出CASE（causal active sequential experimentation）框架，仅主动对争议对做随机评测，修正选择偏差后重复校验，直到分配确定或评测预算耗尽。

### 关键实验
在KuaiRand生产日志、LLMRouterBench等数据集上测试，相比直接信任生产日志的方案，CASE在35%评测预算下将目标价值损失降低10.8%，移除了32%的信任日志带来的损失；真实场景下测量偏差远大于选择偏差，仅0.5%的场景下现有证据足够确定最优分配，更好的效果质量信息比同数据下的分配优化多带来32%的收益。

最值得记住的一句话：LLM任务分配的核心约束是可信的效果评估数据，而非分配优化算法本身。
