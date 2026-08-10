---
title: 'Aftab: A Comprehensive Benchmark of CNN Encoders and Advanced Value Functions
  in Parallelized Q-Networks'
title_zh: 《Aftab：并行Q网络下CNN编码器与先进值函数的全面基准测试》
authors:
- Taha Shieenavaz
- Shabnam Zareshahraki
- Loris Nanni
affiliations:
- Department of Information Engineering, University of Padua, Italy
arxiv_id: '2608.07335'
url: https://arxiv.org/abs/2608.07335
pdf_url: https://arxiv.org/pdf/2608.07335
published: '2026-08-07'
collected: '2026-08-10'
category: Training
direction: 强化学习训练 · 无缓存并行Q网络架构优化
tags:
- Reinforcement Learning
- CNN
- Q-Learning
- Parallel Training
- Benchmark
one_liner: 系统评测并行Q网络的CNN架构与值函数优化方案，提出低内存高性能RL架构Aftab
practical_value: '- 交互式推荐/动态定价等RL业务场景可复用无回放缓存PQN方案，大幅降低训练内存开销

  - 多模态推荐的视觉特征编码器选型，可直接参考本文8种CNN拓扑的参数效率对比结论

  - 广告出价/流量分配等OOD泛化要求高的场景，可借鉴Hadamax编码+分布/集成Q头优化思路'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
无回放缓存的并行Q网络（PQN）训练范式内存效率高，但视觉编码器的表征能力、参数效率优化空间尚未被系统探索，缺少成熟的架构参考。
### 方法关键点
1. 系统评测8种不同CNN拓扑在严格参数约束下的样本效率，筛选最优编码器结构；
2. 集成Hadamax编码、分布Q/集成Q/决斗Q头等扩展，优化表征与值估计精度；
3. 覆盖Atari-57、Procgen Hard两类基准完成多维度性能验证。
### 关键结果
Atari-57基准上IQM人类归一化得分达6.479，较标准PQN基线的提升概率为0.86；Procgen Hard非稳态OOD场景下IQM得分0.418，较基线0.382提升9.4%，同时完全保留无缓存并行训练的低内存优势。
