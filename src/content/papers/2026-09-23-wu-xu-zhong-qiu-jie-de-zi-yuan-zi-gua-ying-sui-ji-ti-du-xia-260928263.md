---
title: Resource-Adaptive Stochastic Gradient Descent for Online Linear Programming
  without Re-solving
title_zh: 无需重求解的资源自适应随机梯度下降在线线性规划算法
authors:
- Jiameng Lyu
affiliations:
- Fudan University
arxiv_id: '2609.28263'
url: https://arxiv.org/abs/2609.28263
pdf_url: https://arxiv.org/pdf/2609.28263
published: '2026-09-23'
collected: '2026-09-24'
category: Other
direction: 在线资源分配 · 在线线性规划优化
tags:
- Online-Linear-Programming
- Stochastic-Gradient-Descent
- Resource-Allocation
- Regret-Optimization
- Online-Optimization
one_liner: 提出无需LP重求解的RASGD算法，在线线性规划下实现最优O(logT) regret，单步仅O(m)开销
practical_value: '- 在线广告预算分配、LLM推理Token/算力配额分配、推荐系统流量调控等资源受限在线决策场景，可直接替换原有定期LP重求解逻辑，RASGD单步O(m)运算性能比逐次重求解高4个数量级，regret仅高20%-30%

  - 动态步长设计可复用：早期步长随时间递减保证收敛，后期步长随剩余周期反比提升匹配库存动态速度，适配大促、流量峰值等短周期资源分配场景

  - 每步用当前剩余资源更新对偶价格，无需存储历史请求数据，适配高吞吐、低延迟要求的在线生产系统，可支持亿级日请求规模的决策需求'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
大规模在线资源分配（如LLM推理算力调度、在线广告预算分配、搜索推荐流量调控）的核心抽象是在线线性规划（OLP），传统逐次重求解LP的方法在亿级请求规模下延迟、算力开销过高，现有一阶方法要么regret过高、要么需要强分布假设限制落地。
### 方法关键点
- 提出RASGD框架：每步仅用当前请求、剩余库存更新资源对偶价格，无需求解任何LP或样本平均优化问题，单步运算、内存开销均为O(m)（m为资源维度）
- 双向步长设计：前期步长随时间递减保证价格学习收敛，中期后步长随剩余周期数反比提升，匹配库存动态变化速度，避免资源耗尽或闲置
- 路径可行性保障：每步决策先校验剩余资源是否满足请求消耗，从机制上避免资源超支
### 关键实验
对比6种现有OLP算法，覆盖单/多资源、不同资源覆盖率、周期长度T最高20000的场景：
- Regret表现接近逐次重求解LP的最优基线Li-Ye A3，T=5000时多资源混合覆盖率场景下RASGD regret为27.43，仅比Li-Ye A3的21.74高26%
- 运行效率比逐次重求解LP高4个数量级以上，T=5000、10资源场景下RASGD单流耗时仅0.262ms，远低于Li-Ye A3的18184ms
- 消融实验证明实时资源反馈、后期步长上调两个设计分别可降低43%、45%的regret
### 核心结论
资源受限在线决策场景下，结合实时资源反馈与动态匹配的步长设计，一阶方法即可达到接近重求解的决策质量，同时满足高吞吐低延迟的生产要求
