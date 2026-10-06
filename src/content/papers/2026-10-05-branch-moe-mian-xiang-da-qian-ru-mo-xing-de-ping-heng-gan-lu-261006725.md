---
title: 'BRANCH-MoE: Balance-Aware Tree Routing for Large Embedding Models'
title_zh: BRANCH-MoE：面向大嵌入模型的平衡感知树路由算法
authors:
- Gang Fu
- Adel Javanmard
- MohammadHossein Bateni
- Vahab Mirrokni
affiliations:
- Google Research
- University of Southern California
arxiv_id: '2610.06725'
url: https://arxiv.org/abs/2610.06725
pdf_url: https://arxiv.org/pdf/2610.06725
published: '2026-10-05'
collected: '2026-10-06'
category: Training
direction: MoE树路由 · 负载均衡与通信效率优化
tags:
- MoE
- Tree Routing
- Load Balancing
- Communication Locality
- Embedding Model
one_liner: 提出无辅助平衡损失的树结构MoE路由，兼顾任务效果、负载均衡与通信locality
practical_value: '- 电商推荐/广告场景的大规模MoE排序、召回模型可直接替换原有flat路由，无需调试辅助平衡损失超参，降低训练复杂度的同时保证效果不下降

  - 树路由天然自带的前缀locality可直接用于部署优化，将同一子树的专家部署到同GPU/同物理机，可降低12%+的跨设备通信开销，适配大参数MoE的低延迟推理需求

  - 基于EMA锚定决策边界的均衡分配思路可迁移到多召回源流量分配、多Agent任务调度等需要动态均衡流量的业务场景，无需额外规则即可维持分配公平性'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
传统MoE的flat路由存在三大痛点：一是专家负载不均衡，需额外引入辅助平衡损失或动态偏置控制器，提升了训练调参复杂度；二是专家索引无拓扑语义，无法结合硬件拓扑优化跨设备通信；三是易出现路由坍塌，部分专家长期接收不到足够样本，收敛速度慢。在电商/广告场景的大规模嵌入类MoE模型中，上述问题会显著推高训练与推理部署成本。
### 方法关键点
- 将E个专家部署在深度为log₂E的二叉树叶子节点，每个内部节点通过线性或浅层MLP计算输入的分支分数
- 每个内部节点用EMA维护到达该节点的流量加权平均分数作为锚点，分支概率以锚点为中心计算，无需额外辅助平衡损失即可避免子树饥饿
- 路由路径天然形成专家的结构化二进制地址，同前缀的专家属于同一子树，可直接匹配硬件部署拓扑优化通信
### 关键实验结果
在Criteo CTR预测、Forest Covertype等4个数据集上与Switch、DeepSeek-V3、Skywork等主流路由方案对比：
1. 任务效果与最优baseline持平，在Forest Covertype数据集上取得最低的held-out损失
2. 无需辅助损失即可维持均衡的专家负载，UCI数据集上同token选中的专家归一化树距离为0.710~0.718，比随机配对低12~13%，而所有flat路由的该指标仅比随机低最多3.5%
### 核心结论
结构化路由可以在不损失任务效果、不增加训练辅助损失的前提下，同时实现负载均衡与通信效率优化，是大规模MoE落地的高性价比方案
