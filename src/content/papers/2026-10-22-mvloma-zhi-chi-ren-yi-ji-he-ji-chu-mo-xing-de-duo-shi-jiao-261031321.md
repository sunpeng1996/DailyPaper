---
title: 'MVLoMa: Multi-View Local Feature Matching with Any Geometry Foundation Model'
title_zh: MVLoMa：支持任意几何基础模型的多视角局部特征匹配
authors:
- Xinyang Lu
- Shengzhe Wei
- Sheng Tang
- Weiqi Zhang
- Juntong Fang
- Zesong Li
affiliations:
- Kosmo Research
- 哈尔滨工业大学航天学院
- 清华大学软件学院
arxiv_id: '2610.31321'
url: https://arxiv.org/abs/2610.31321
pdf_url: https://arxiv.org/pdf/2610.31321
published: '2026-10-22'
collected: '2026-10-24'
category: Other
direction: 多视角几何 · 局部特征匹配
tags:
- Multi-view Geometry
- Local Feature Matching
- Foundation Model
- Star Graph
- Relative Pose Estimation
one_liner: 提出星图架构多视角局部特征匹配器，复用参考图计算，融合多视角几何线索，兼顾精度与速度
practical_value: '- 一对多匹配任务可复用中心侧计算逻辑，降低重复推理开销，可迁移到多用户对同候选集的批量打分场景

  - 多源互补上下文信息注入基础特征描述子的思路，可用于多模态推荐的特征融合模块设计

  - 引入领域硬约束作为负样本监督信号的方法，可优化推荐召回/排序模型的损失函数设计'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有局部特征匹配多为成对设计，在参考图匹配多邻图的场景下，重复计算参考侧特征，且无法利用多视角互补几何信息，推理效率低、精度存在上限。
### 方法关键点
1. 提出星图架构多视角匹配器MVLoMa，基于冻结的任意几何基础模型联合编码星型结构内所有图像，将跨视角几何上下文注入局部描述子；
2. 单前向传播即可完成中心图与所有邻图的匹配，包含逐视角自注意力、中心-邻域双向交叉注意力；
3. 监督侧仅采用深度有效、相互可见的密集变换生成正样本，显式惩罚违反极线几何的高置信度匹配。
### 关键结果
在HyperSim、ScanNet++等4个数据集的25视角星图任务上，三个阈值下的相对位姿AUC均达最优（58.65/85.41/90.99）；推理速度比逐对顺序计算快2.2倍，可兼容4种不同的冻结几何编码器。
