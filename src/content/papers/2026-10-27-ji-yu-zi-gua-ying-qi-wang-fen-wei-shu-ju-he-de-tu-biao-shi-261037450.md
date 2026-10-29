---
title: Graph Representation Learning via Adaptive Expectile Aggregation
title_zh: 基于自适应期望分位数聚合的图表示学习
authors:
- Tianyi Zhu
- Wei Lan
affiliations:
- Colorado State University
- Southwestern University of Finance and Economics
arxiv_id: '2610.37450'
url: https://arxiv.org/abs/2610.37450
pdf_url: https://arxiv.org/pdf/2610.37450
published: '2026-10-27'
collected: '2026-10-29'
category: Other
direction: 图神经网络 · 邻域聚合优化
tags:
- GNN
- Graph Representation Learning
- Neighborhood Aggregation
- Heterophilic Graph
- Robust Learning
one_liner: 提出可学习期望分位数聚合的ExpectileGCN，解决GNN均值聚合在异配图下信息捕捉不足问题
practical_value: '- 电商推荐用户/物品异构图建模场景，可替换现有GNN均值聚合算子为Expectile聚合，适配用户兴趣跳变、跨类别关联的异配场景，提升召回/排序特征表征质量

  - 面对用户行为特征噪声、社交关系/物品关联结构扰动场景，可引入该自适应聚合方法提升图模型鲁棒性，减少预测bad case

  - 可借鉴sigmoid平滑+固定点迭代的可微近似实现思路，将其他非可微分位类统计算子引入端到端训练的推荐模型'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
传统GNN依赖均值邻域聚合生成节点表征，无法捕捉与分类相关的邻域分布信息，尤其在异配图（关联节点类别差异大）场景下性能衰减严重，且对特征噪声、结构扰动的鲁棒性较差，无法适配复杂现实图数据。

### 方法关键点
1. 提出ExpectileGCN自适应聚合框架，引入可学习的期望分位数水平，聚合算子可在最小值、均值、最大值模式间连续自适应调整，均值聚合是其特殊情况，可覆盖更多邻域信息分布模式；
2. 基于sigmoid平滑与固定点迭代实现期望分位数聚合的可微近似，支持模型端到端优化；
3. 理论层面证明了模型稳定性、直推式泛化边界，以及异配邻域场景下相比均值聚合的分类优势可稳定存在。

### 关键结果
在同配、异配基准图数据集上分类性能显著优于均值聚合基线GNN，特征损坏、结构扰动场景下预测鲁棒性提升明显。
