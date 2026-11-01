---
title: Leveraging Recourse and Size Bounds for OnlineKnapsack with Removable Items
title_zh: 结合回溯与尺寸边界的可移除物品在线背包问题优化
authors:
- Dimitris Fotakis
- Laurent Gourvès
- Aris Pagourtzis
- Panagiotis Patsilinakos
affiliations:
- National Technical University of Athens
- Archimedes, Athena Research Center
- Université Paris-Dauphine (PSL)
- CNRS
- LAMSADE
arxiv_id: '2610.40290'
url: https://arxiv.org/abs/2610.40290
pdf_url: https://arxiv.org/pdf/2610.40290
published: '2026-10-29'
collected: '2026-11-01'
category: Other
direction: 在线背包算法 · 竞争比优化
tags:
- Online Knapsack
- Competitive Ratio
- Recourse
- Adaptive Algorithm
- Removable Items
one_liner: 给出可移除物品在线背包带回溯与尺寸边界的紧竞争比，提出无需预知尺寸上限的自适应算法
practical_value: '- 实时广告预算控量、召回池动态截断场景可复用「可移除+有限次回溯」决策范式，替代硬截断规则提升资源利用率

  - 物品尺寸/价值分布不明确的动态调度场景可借鉴自适应算法思路，无需预训练分布也能获得稳定性能保障

  - 流计算场景下的资源分配可参考给出的竞争比上下界做最坏情况性能预估，规避极端劣化风险'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
在线无权重背包是流资源分配的核心基础问题，传统不可撤销决策模式下无法获得有效竞争比，仅支持已接受物品移除的现有优化方案提升空间有限，无法满足高动态资源调度需求。
### 方法关键点
融合两类已有的模型扩展能力：① 已知物品尺寸上限（边界感知）；② 可重新插入之前拒绝的物品（回溯），严格推导三类能力（移除+边界感知+回溯）结合下的竞争比上下界；进一步提出自适应在线算法，无需预先知道物品尺寸上限即可获得与边界感知模型可比的性能保障。
### 关键结果
当物品尺寸上限约束较宽松、仅需少量回溯次数时，竞争比大幅优于仅支持物品移除的现有最优在线背包算法；自适应算法性能与预先知道尺寸上限的边界感知模型的保障水平相当。
