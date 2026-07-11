---
title: Secure Decentralized Federated Learning via Gossip and Virtual Voting
title_zh: 基于八卦协议与虚拟投票的安全去中心化联邦学习框架
authors:
- Amirhossein Taherpour
- Xiaodong Wang
arxiv_id: '2607.08651'
url: https://arxiv.org/abs/2607.08651
pdf_url: https://arxiv.org/pdf/2607.08651
published: '2026-07-09'
collected: '2026-07-11'
category: Training
direction: 去中心化联邦学习 · 训练安全优化
tags:
- Federated-Learning
- Gossip-Protocol
- DAG
- Byzantine-Fault-Tolerance
- Virtual-Voting
one_liner: 提出gspDAG-FL无中心安全联邦学习框架，降协调开销同时提升拜占庭节点鲁棒性
practical_value: '- 跨机构联合训练推荐/广告模型（如电商与品牌方联邦建模）时，可复用gspDAG-FL的无中心协调架构，避免单点信任风险与数据泄露隐患

  - 联邦训练存在恶意/惰性参与方时，可直接套用其聚合前三重校验机制，提升异常节点检测率，保证最终模型质量

  - 大规模联邦训练集群可借鉴基于gossip历史的虚拟投票共识方案，替换现有全局同步逻辑，降低协调开销、提升训练吞吐量'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有去中心化联邦学习（DFL）的gossip类方案缺乏来源最终性，对拜占庭/惰性参与方鲁棒性差；账本辅助FL虽提升可审计性，但引入的全局协调成本抵消了DFL的本地化优势。
### 方法关键点
1. 提出gspDAG-FL安全DFL框架，直接复用模型分发的gossip历史实现共识：节点仅和邻居交换模型payload，全节点收集事件证书、接收方背书的gossip证明，构建拓扑DAG后运行Hashgraph式虚拟投票生成全节点证书，最终性针对模型来源元组而非本地参数状态。
2. 聚合前配置payload校验、接受证明校验、私有语义审计三重校验机制，形式化证明了控制面安全性、条件活性与时变混合场景下的收敛性。
### 关键结果数字
100节点规模下，学习效果接近基于校验的账本FL，协调瓶颈显著降低、吞吐量提升；混合拜占庭/惰性节点场景下，无效来源检测率保持较高水平，在MNIST分类、PTB语言建模任务上均达标
