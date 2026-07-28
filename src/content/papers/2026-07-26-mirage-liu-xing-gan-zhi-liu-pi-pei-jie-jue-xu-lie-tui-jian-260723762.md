---
title: 'Escaping the Euclidean Void: Manifold-Informed Flow Matching for Sequential
  Recommendation'
title_zh: MIRAGE：流形感知流匹配解决序列推荐欧氏空间空洞问题
authors:
- Dengzhao Fang
- Jingtong Gao
- Yu Li
- Xiangyu Zhao
- Yi Chang
affiliations:
- 吉林大学
- 香港城市大学
arxiv_id: '2607.23762'
url: https://arxiv.org/abs/2607.23762
pdf_url: https://arxiv.org/pdf/2607.23762
published: '2026-07-26'
collected: '2026-07-28'
category: GenRec
direction: 生成式推荐 · 流匹配序列推荐优化
tags:
- Flow Matching
- Sequential Recommendation
- Generative Recommendation
- Manifold Regularization
- Long-tail Recommendation
one_liner: 训练时引入共现图拓扑正则修正嵌入空间，零推理开销提升流匹配序列推荐效果
practical_value: '- 做流匹配/扩散类生成式推荐时，可复用「训练时加共现图拓扑正则、推理完全弃用」的设计，既提升效果又不增加推理延迟

  - 可复用抛物型时间调制权重 `4t(1-t)`，仅在生成路径的中间段施加正则，避免破坏噪声源和目标item的表征

  - 长尾商品推荐场景可直接复用锚定目标商品共现邻域的思路，用高曝关联商品的表征补全长尾商品的几何支撑

  - 可根据数据集稀疏度选择锚定策略：稠密场景用单最近邻硬锚定，稀疏场景用加权质心软锚定'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
流匹配类生成式序列推荐默认欧氏空间的直线路径全程有语义支撑，但实际item表征稀疏分布，路径中间段往往落在无有效语义的「欧氏空洞」，导致生成结果漂移；现有方法仅优化路径传输效率，未解决路径的语义有效性问题，长尾商品因监督信号少，该问题更加突出。

### 方法关键点
- 核心框架MIRAGE保留流匹配的直线概率路径，仅训练时用物品共现图作为语义流形代理，正则化调整嵌入空间几何结构，推理阶段无任何图相关开销
- 拓扑正则设计：对路径中间插值状态，锚定目标item的共现邻域，可选硬锚定（拉向最近邻）或软锚定（拉向邻域加权质心），拉近插值态与邻域表征的距离
- 时间调制策略：用抛物型权重 `4t(1-t)` 控制正则强度，t=0（噪声源）和t=1（目标item）处正则为0，仅在路径中间段施加约束，避免破坏边界表征
- 训练目标结合流匹配目标恢复、全库排序、历史重建、拓扑正则四项，推理支持1步生成，无额外计算开销

### 关键结果
在四个Amazon公开数据集（Beauty、Sports、Toys、CDs）上对比传统序列推荐（SASRec、LightGCN等）、扩散类推荐（DiffuRec等）、流匹配类推荐（FMRec、FAVE等），相比最优基线FMRec，H@20最高提升11.69%，长尾商品H@20最高提升17.5%；1步推理延迟低于同类流匹配模型，精度随推理步数增加无明显波动。

最值得记住的一句话：生成式推荐的优化不能只看路径传输效率，更要确保路径全程的语义支撑，训练时的拓扑正则可以在零推理开销的前提下同时提升整体效果和长尾表现。
