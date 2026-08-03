---
title: Learning to Trace Seiberg Dualities
title_zh: 学习追踪Seiberg对偶性
authors:
- Jonathan J. Heckman
- Shani Meynet
- Alessandro Mininno
- Gary Shiu
affiliations:
- University of Pennsylvania Department of Physics and Astronomy
- University of Pennsylvania Department of Mathematics
- University of Wisconsin–Madison Department of Physics
arxiv_id: '2607.28628'
url: https://arxiv.org/abs/2607.28628
pdf_url: https://arxiv.org/pdf/2607.28628
published: '2026-07-30'
collected: '2026-08-03'
category: Other
direction: 理论物理 · AI对偶性判定
tags:
- Transformer
- MLP
- Pathfinding
- Theoretical Physics
- Graph Matching
one_liner: 用Transformer、MLP结合寻路算法实现优于传统确定性算法的Seiberg对偶性判定
practical_value: '- 核心为理论物理领域学术研究，无直接适配电商/推荐/Agent业务的可落地方案

  - 仅「神经网络+传统启发式算法融合提效」的思路可参考复杂匹配类问题优化'
score: 3
source: arxiv-cs.LG
depth: abstract
---

### 动机
物理系统对偶性是验证微观与涌现现象的核心依据，但即使已知全部规则，判定两个系统是否对偶的计算复杂度极高，传统确定性算法效率低下，缺乏自动化的高效判定方案。
### 方法关键点
1. 将超对称箭袋规范理论的Seiberg对偶性判定转化为箭袋结构突变匹配问题，属于「学习解结」类任务的变体；
2. 对比Transformer、MLP等不同网络架构的对偶性追踪效果，额外融合成熟的寻路算法（类比箭袋结构的「谷歌地图」）优化搜索策略。
### 关键结果数字
针对节点数约10的小规模箭袋，Transformer与MLP架构的表现均优于传统确定性算法；融合寻路算法后，搜索策略的效率与准确率获得进一步提升，该类对偶性判定任务可作为前沿AI模型在理论物理场景的基准测试集。
