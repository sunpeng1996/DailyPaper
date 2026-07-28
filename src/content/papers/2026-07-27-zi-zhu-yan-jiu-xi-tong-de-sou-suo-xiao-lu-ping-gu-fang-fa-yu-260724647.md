---
title: Efficiency Matters in Autonomous Research
title_zh: 《自主研究系统的搜索效率评估方法与自适应优化框架》
authors:
- Haiqian Yang
- Yuan Cao
affiliations:
- MIT
arxiv_id: '2607.24647'
url: https://arxiv.org/abs/2607.24647
pdf_url: https://arxiv.org/pdf/2607.24647
published: '2026-07-27'
collected: '2026-07-28'
category: Agent
direction: Agent 自主研究效率优化
tags:
- Autonomous Research
- Search Efficiency
- Portfolio Bandit
- Pareto Frontier
- Dynamic Resource Allocation
one_liner: 提出自主研究系统搜索效率评估指标，以及动态预算分配的流体搜索算法，性能接近单任务最优Oracle
practical_value: '- 推荐/广告系统的候选集搜索、超参调优场景可复用Pareto frontier AUC评估指标，同时平衡最终效果和资源消耗，避免为了微小效果提升浪费大量算力

  - 多搜索策略（如召回、排序阶段的多路并行策略）可借鉴fluid search的portfolio bandit动态分配机制，根据实时效果动态分配流量/算力给最优策略，降低整体预算消耗

  - 电商Agent做货品选品、营销策略自动探索时，可参考该框架区分最终效果和搜索效率两个维度，在试错成本高的场景（如线下营销实验）优先选择高搜索效率的方案'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
当前自主研究（AR）系统仅以最终结果质量评估性能，完全忽略搜索过程效率；当AR落地到物理实验、真实业务等验证成本高的场景时，低搜索效率会带来极高的预算浪费，现有评估体系无法覆盖该需求。
### 方法关键点
1. 新增Pareto frontier AUC作为搜索效率评估指标，与最终结果质量并列作为双评估维度；
2. 对比爬山、束搜索、树搜索、进化搜索四类常见搜索算法在12个系统优化任务上的表现，发现无单一算法能在所有任务上保持效率最优；
3. 推出fluid search自适应搜索框架，用portfolio bandit动态将固定评估预算分配给多个并行搜索进程，自动适配任务最优搜索策略。
### 关键结果
在12个测试任务上，fluid search的整体搜索效率达到最高，性能接近预先知道每个任务最优搜索结构的单任务Oracle；最终效果最优的方法和搜索效率最优的方法是两个独立维度，部分最终效果最优的方法消耗的评估预算是高效方法的数倍。
