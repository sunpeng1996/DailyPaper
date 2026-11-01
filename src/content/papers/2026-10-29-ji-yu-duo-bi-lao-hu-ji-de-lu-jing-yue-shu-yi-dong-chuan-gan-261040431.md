---
title: Adaptive search with path-constrained mobile sensors using multi-arm bandits
title_zh: 基于多臂老虎机的路径约束移动传感器自适应搜索方法
authors:
- Abraham P. Vinod
- Parth K. Thaker
- Gautam Dasarathy
- Stefano Di Cairano
affiliations:
- Mitsubishi Electric Research Laboratories
- Arizona State University
arxiv_id: '2610.40431'
url: https://arxiv.org/abs/2610.40431
pdf_url: https://arxiv.org/pdf/2610.40431
published: '2026-10-29'
collected: '2026-11-01'
category: MultiAgent
direction: 多智能体路径规划 · 多臂老虎机优化
tags:
- Multi-Armed Bandits
- Multi-Agent
- Path Planning
- Active Sensing
- Graph Theory
one_liner: 将路径约束移动传感器的自适应搜索转化为多臂老虎机问题，提出带理论保证的分配与路径覆盖方案
practical_value: '- 多Agent资源约束调度场景可复用路径约束下的低基数路径覆盖构造方法，大幅降低决策空间复杂度，提升调度效率

  - 带硬约束的序贯决策问题可参考「预生成约束可行集→转化为多臂老虎机问题」的建模思路，直接复用多臂老虎机领域成熟的理论收敛保证

  - 动态资源分配类任务可借鉴置信界驱动的自适应分配策略，在平衡探索与利用的同时满足能量、路径等物理约束'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
针对能量受限、需避障、需返回充电站的移动传感器团队的感兴趣区域检测需求，现有方案未同时兼顾路径硬约束与序贯决策的探索利用平衡，普遍缺乏可落地的理论收敛保证。
### 方法关键点
1. 将主动路径选择问题建模为多臂老虎机问题，基于已采集数据计算置信界，实现迭代式自适应路径分配；
2. 提出基于图的低基数路径覆盖构造方法，在满足团队所有物理约束的前提下大幅压缩决策空间。
### 关键结果
推导得到检测所有感兴趣区域、标记所有节点所需时间的非渐近上界，在广泛问题实例中该上界与算法无关的下界仅相差常数因子；仿真验证了路径冗余度提升、团队规模扩大均可有效降低搜索耗时。
