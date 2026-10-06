---
title: Quality-Aware Cross-Model Computation Reuse
title_zh: 质量感知的跨模型计算复用技术
authors:
- Jin Cheng
- Xiangxiang Dai
- Maoli Liu
- Ziyi Han
- Zhuohua Li
- John C. S. Lui
affiliations:
- The Chinese University of Hong Kong
- Xi’an University of Electronic Science and Technology
arxiv_id: '2610.05285'
url: https://arxiv.org/abs/2610.05285
pdf_url: https://arxiv.org/pdf/2610.05285
published: '2026-10-04'
collected: '2026-10-06'
category: LLM
direction: LLM 跨模型计算复用调度优化
tags:
- ComputationReuse
- LLMServing
- OnlineScheduling
- OnlineLearning
- RegretAnalysis
one_liner: 提出QARS质量感知复用调度算法，优化跨模型计算复用的在线决策
practical_value: '- 多LLM串联的推荐/Agent服务中，可复用QARS的跨模型中间结果调度逻辑，在可控质量损失下降低推理时延与算力成本

  - 在线调度决策可借鉴其乐观估计+质量感知停止规则的设计，平衡决策准确度与计算开销，适配延迟反馈场景

  - 多模型服务的成本优化可直接复用其regret分析框架，量化调度策略的长期收益'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有跨模型计算复用研究侧重工程落地，缺乏决策优化的理论支撑，面临两大核心挑战：一是复用对不同模型任务的质量影响不确定，二是多任务共享可复用结果的调度高度耦合，即使质量已知也属于NP难问题，不符合现有方法的前提假设。
### 方法关键点
将跨模型计算复用建模为在线决策问题，提出QARS算法：① 针对质量不确定性，从延迟反馈中学习任务相关的复用质量，用乐观估计引导决策；② 针对耦合调度，联合决策可复用结果制备与任务复用分配，根据剩余质量不确定性自适应调整调度精度；③ 引入质量感知停止规则，实现$O(√T)$的regret上界。
### 关键结果
相比最强基线调度策略，计算与质量损失的综合成本最高降低18.0%，平均regret降低63.9%
