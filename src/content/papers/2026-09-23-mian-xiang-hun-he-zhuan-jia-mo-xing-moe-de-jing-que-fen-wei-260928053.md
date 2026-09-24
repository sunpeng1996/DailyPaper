---
title: Exact Quantile Balancing and Load-Error Injection for Mixture-of-Experts
title_zh: 面向混合专家模型（MoE）的精确分位数均衡与负载误差注入方法
authors:
- Pit Neitemeier
- Jiaze Li
- Alessio Serra
- Philipp Scholl
- Sohir Maskey
affiliations:
- Aleph Alpha
arxiv_id: '2609.28053'
url: https://arxiv.org/abs/2609.28053
pdf_url: https://arxiv.org/pdf/2609.28053
published: '2026-09-23'
collected: '2026-09-24'
category: Training
direction: MoE训练 · 负载均衡优化
tags:
- MoE
- Load Balancing
- Distributed Training
- Quantile Balancing
- Router Optimization
one_liner: 提出精确分位数均衡EQB与负载误差注入LEI，双维度优化MoE全局与局部负载均衡及训练表现
practical_value: '- 业务侧训练垂域MoE大模型（如电商商品生成、推荐文案生成用MoE基座）时，可直接复用EQB的双256桶all-reduce方案，替代现有近似分位数均衡方法，仅增加极低通信开销即可提升全局负载均衡度，减少专家闲置

  - 可将LEI替换现有GShard辅助损失做局部负载均衡，其无专家耦合的梯度注入逻辑修正效率更高，能在不损失模型效果的前提下降低微批次负载偏斜，提升专家并行执行效率

  - LEI的tanh缩放残差技巧可直接复用，解决负载均衡梯度注入导致的注意力logit不稳定问题，避免训练过程崩溃，减少调参成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
MoE模型通过稀疏路由提升参数容量的核心前提是负载均衡：全局（优化器步长内）均衡避免专家长期闲置，局部（微批次内）均衡提升专家并行执行效率。现有分布式Quantile Balancing（QB）依赖近似全局分位数误差大，GShard辅助损失通过归一化路由概率传递负载误差，存在专家耦合、修正信号与硬路由匹配度低的问题，无法同时满足双维度均衡需求。
### 方法关键点
- **Exact Quantile Balancing（EQB）**：适配BF16精度做两次8位基数选择，通过两次256桶all-reduce聚合全局计数，无需传输token级数据即可得到精确全局批次分位数，通信量仅为全量直方图方案的1/128，与token数量无关。
- **Load-Error Injection（LEI）**：将每个专家的局部负载误差直接注入路由得分梯度，用非归一化路由得分做Straight-Through估计的代理，避免专家耦合，仅调整对应专家的路由梯度；额外通过tanh缩放残差bound梯度大小，避免注意力logit不稳定。
### 关键实验
在7.5B参数MoE（256个专家，单token激活6个）上训练，对比基线为秩平均QB、EQB+GShard损失：
1. 100B token训练下，EQB比秩平均QB全局MaxVio降低19.4%，局部MaxVio降低9.8%；
2. 加LEI后局部MaxVio进一步降低到3.49，比GShard损失方案低25.9%，多任务平均精度相当；
3. 500B token训练下，LEI将局部MaxVio从5.14降到4.15，平均精度从48.25%提升到48.56%。
### 核心结论
MoE负载均衡需要全局偏置控制与局部梯度修正互补配合，精确全局分位数+直接负载误差注入的组合，能以极低通信成本实现更优的均衡效果与训练稳定性
