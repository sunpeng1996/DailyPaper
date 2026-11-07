---
title: Message-passing graph persistence
title_zh: 消息传递图持久性（MGP）拓扑描述符
authors:
- Jorge Luiz Franco
- Arthur Queiroz Moura
- Moacir Ponti
- Amauri Souza
affiliations:
- University of São Paulo (ICMC)
- Avra
- Mercado Libre
- Federal Institute of Ceará (IFCE)
arxiv_id: '2611.06801'
url: https://arxiv.org/abs/2611.06801
pdf_url: https://arxiv.org/pdf/2611.06801
published: '2026-11-04'
collected: '2026-11-07'
category: Other
direction: GNN表达增强 · 拓扑特征学习
tags:
- GNN
- Persistent Homology
- Topological Data Analysis
- Message Passing
- Graph Representation
one_liner: 将消息传递融入图过滤流程，提出表达能力优于现有PH描述符的MGP拓扑特征
practical_value: '- 电商用户行为图谱、社交关系图谱类推荐场景，可引入MGP拓扑特征补充传统GNN的表征能力，提升规则图、高密度子图的区分度

  - 图分类类业务（如用户风险分层、商品关联图谱聚类）可直接复用MGP「过滤步嵌入更新+拓扑事件绑定」的流程，替换原有PH特征计算逻辑

  - 现有GNN召回/排序模块可轻量接入MGP特征作为侧输入，无需重构原模型架构即可获得拓扑信息增益'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
传统消息传递GNN表达能力受1-WL测试上界限制，无法区分规则图等简单结构；现有持久同调（PH）拓扑特征计算与表征学习流程解耦，无法端到端优化。

### 方法关键点
提出MGP拓扑描述符族，将消息传递嵌入图过滤全流程：
1. 每步过滤基于当前子图更新节点嵌入，与持久性事件绑定
2. 节点嵌入直接决定持久性计算中连通分量的代表
3. 理论证明MGP满足图同构不变性，表达能力严格优于所扩展的PH基描述符

### 关键结果
在表达能力基准、多个图分类与回归数据集上，MGP在绝大多数任务上优于其他PH基描述符。
