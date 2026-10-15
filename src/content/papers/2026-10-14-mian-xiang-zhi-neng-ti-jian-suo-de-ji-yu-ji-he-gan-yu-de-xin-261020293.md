---
title: 'CASI: Credit Assignment via Set Intervention for Agentic Retrieval'
title_zh: 面向智能体检索的基于集合干预的信用分配方法CASI
authors:
- Xinyi Cheng
- Tianfu Zhang
- Jiwen Li
- Xuesen Zhang
- Shihao Yu
- Pengfei Zhu
- Renhuan
- Heda Wang
affiliations:
- Xiaohongshu Inc.
arxiv_id: '2610.20293'
url: https://arxiv.org/abs/2610.20293
pdf_url: https://arxiv.org/pdf/2610.20293
published: '2026-10-14'
collected: '2026-10-15'
category: Agent
direction: Agent 多检索动作信用分配优化
tags:
- Credit Assignment
- Agentic Retrieval
- Reinforcement Learning
- Sponsored Search
- Shapley Value
one_liner: 提出基于快照集合干预的多检索动作信用分配方法CASI，在赞助搜索场景获3.51%广告主价值提升
practical_value: '- 电商/搜索多query并行召回场景，可复用「缓存单query召回结果+固定下游快照+枚举子集计算Shapley值」的归因方案，避免重复调用检索/拍卖链路，大幅降低细粒度信用分配的计算成本

  - 多动作联合输出的RL训练流程中，可引入有界零和优势塑形方法调整单动作梯度，既保留全局集合奖励的优化方向，又能修正动作间的相对梯度信号，解决广播奖励的归因模糊问题

  - 赞助搜索query改写优化场景，可直接参考该方法的落地效果：训练后的策略仅做推理替换，即可获得3.51%的广告主价值、5.08%的广告花费提升，ROI明确'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前基于LLM的智能检索系统普遍为单输入生成多个并行检索动作（如多维度query改写），下游仅返回整个动作集合的全局奖励，传统广播式奖励分配无法区分集合内不同动作的真实贡献，更无法覆盖动作间的冗余、竞争等 coalition 依赖效应，导致RL训练的检索策略效果受限。

### 方法关键点
- 快照式集合干预：对每个生成的动作集合仅做1次LLM生成和检索，缓存每个动作的召回结果，固定下游排序/拍卖链路的静态快照，仅通过组合不同子集的召回结果评估子集收益，无额外检索/排序开销
- Shapley值信用聚合：枚举所有子集的收益后，用Shapley权重聚合每个动作在不同上下文 coalition 下的边际贡献，得到集合内每个动作的独立信用
- 有界零和优势塑形：将单动作信用中心化、归一化后投影到零和有界空间，与全局集合优势结合得到每个动作的最终优势，保证全局优化目标不变的前提下调整单动作梯度

### 关键结果
实验在5动作并行的赞助搜索场景开展：离线1200条请求全子集拍卖重放显示，CASI与重放Shapley参考值的中位数余弦相似度达0.424，比Singleton方法高0.036；held-out集上CASI训练策略的平均重放价值达66.70，较Singleton高11.7，较SFT基线高6.38；7天10%流量线上A/B测试，CASI策略较生产基线获得3.51%的广告主价值提升、5.08%的搜索广告花费提升。

> 最值得记住：当多个检索动作存在明显的依赖、冗余效应时，快照集合干预的细粒度信用分配能以可接受成本获得显著业务收益
