---
title: 'InterConRank: Joint Node Centrality in Interconnected Heterogeneous Networks'
title_zh: InterConRank：互联异构网络下的联合节点中心性排序算法
authors:
- Hao Ren
- Jiaojiao Jiang
affiliations:
- University of New South Wales
arxiv_id: '2611.34763'
url: https://arxiv.org/abs/2611.34763
pdf_url: https://arxiv.org/pdf/2611.34763
published: '2026-11-25'
collected: '2026-11-27'
category: RecSys
direction: 异构网络 · 节点中心性排序
tags:
- Heterogeneous Network
- Node Centrality
- Graph Ranking
- Multilayer Network
- Iterative Update
one_liner: 提出支持跨层得分传播的互联异构网络节点中心性算法InterConRank，在学术网络排序任务上性能最优
practical_value: '- 电商场景可复用跨层迭代更新逻辑，融合用户行为层、商品关系层、供应链层的多维度信号计算商品/商家全局重要性，用于冷启动排序、推荐池初选

  - 不同类型边分别归一化的策略可直接复用，避免点击/收藏/关注/供应关系等不同边规模差异带来的得分偏置

  - 算法收敛性已被理论证明，落地到图排序任务时无需额外做收敛性验证，降低工程成本'
score: 7
source: arxiv-cs.AI
depth: abstract
---

## 动机
现有异构网络中心性算法仅支持单链路或双群体排序，无法适配多层互联场景下节点跨层邻居的位置会影响自身重要性的需求，例如供应商排名需参考其生产组件的产品网络地位。
## 方法关键点
1. 支持自定义有向依赖关系定义各层得分的输入来源，适配任意多层异构网络的联合排序需求；
2. 对不同类型边分别做归一化，多层节点得分同步迭代更新，得分可单次迭代跨层流入后，下次迭代沿层内链路传播；
3. 严格证明了迭代更新过程的收敛性，无落地时的收敛性风险。
## 关键结果
在4个学术网络数据集上测试，针对协作层节点排序，InterConRank与h-index、总引用量的排序相关性均为所有对比方法最高。
