---
title: Rethinking Successive Rejects Algorithms
title_zh: 最优臂识别场景下连续淘汰（SR）算法的改进研究
authors:
- Mohamed Khair
- Junpei Komiyama
affiliations:
- Mohamed bin Zayed University of Artificial Intelligence
- RIKEN AIP
arxiv_id: '2610.22051'
url: https://arxiv.org/abs/2610.22051
pdf_url: https://arxiv.org/pdf/2610.22051
published: '2026-10-15'
collected: '2026-10-17'
category: RecSys
direction: 多臂老虎机 · 最优臂识别算法优化
tags:
- Multi-Armed Bandit
- Best-Arm Identification
- Successive Rejects
- Online Learning
- Cold Start
one_liner: 优化连续淘汰算法的阶段调度，提出H1-SR，逼近最优自适应臂识别算法的归一化速率
practical_value: '- 电商冷启动选品/广告素材最优筛选场景，可直接替换原有SR算法为H1-SR，固定采样预算下提升最优臂识别准确率

  - 流量分配、小流量测试选最优方案时，参考H1-SR的阶段调度设计，避免过早淘汰潜力选项的损失

  - 线上资源有限的快速实验场景，可复用其归一化误差指数优化思路设计采样节奏，平衡探索成本和准确率'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
固定预算最优臂识别场景中，原连续淘汰（SR）算法采用预设阶段长度，被认为自适应能力有限，但实际性能可媲美SOTA自适应采样算法，存在进一步优化空间。
### 方法关键点
将SR的阶段调度设计转化为归一化误差指数优化问题，提出H1-balanced SR（H1-SR），为确定性等计数调度类SR算法中的最优方案。
### 关键结果数字
同方差高斯臂场景下，H1-SR在任意臂数K≥2时，归一化速率至少达到所有自适应算法最优值的11/12，K趋于无穷时逼近比收敛到$1-O(1/\log K)$，远优于原SR的1/4收敛上限；10组合成数据+2组真实基准数据集实验显示，多数场景下H1-SR性能显著优于原SR，同时验证了过早激进淘汰潜力臂会带来额外性能损失。
