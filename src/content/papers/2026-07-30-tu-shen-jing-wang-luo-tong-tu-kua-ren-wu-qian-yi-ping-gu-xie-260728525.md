---
title: 'Same Graph Cross-Task Transfer in GNNs: Protocols and Predictors'
title_zh: 图神经网络同图跨任务迁移：评估协议与效果预测器
authors:
- Neelam Akula
- Surbhi Kumar
- Murat Kantarcioglu
- Baris Coskunuzer
affiliations:
- University of Texas at Dallas
- Virginia Polytechnic Institute and State University
arxiv_id: '2607.28525'
url: https://arxiv.org/abs/2607.28525
pdf_url: https://arxiv.org/pdf/2607.28525
published: '2026-07-30'
collected: '2026-08-01'
category: Eval
direction: GNN同图跨任务迁移 评估与规律总结
tags:
- GNN
- Cross-Task Transfer
- Node Classification
- Link Prediction
- Evaluation Protocol
one_liner: 提出无泄漏的同图NC-LP跨任务迁移评估协议，明确迁移方向性并给出效果预判方法
practical_value: '- 电商/社交等同质性高的GNN应用场景，可优先用节点分类（如用户/物品标签分类）预训练再迁移到链接预测（如交互召回）任务，收益稳定

  - 搭建GNN共享编码器同时支撑分类、预测双任务时，避免直接复用链接预测预训练参数到分类任务，仅分类效果未饱和时可尝试

  - 跨任务GNN效果验证时固定节点/边划分、排除评估边做消息传递、固定LP负采样，避免数据泄漏导致的效果虚高'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有GNN跨节点分类(NC)、链接预测(LP)的同图跨任务迁移评估存在划分不兼容、数据泄漏、负采样规则不统一等问题，得出的迁移结论可靠性低，缺乏可落地的跨任务迁移指导。
### 方法关键点
1. 提出无泄漏的标准化评估协议：固定节点与边划分，使用排除所有评估边的共享消息传递图，LP任务采用固定负采样规则；
2. 提出CoTask Score(CTS)衡量共享编码器同时支撑NC+LP双任务的综合效用，基于数据集统计量（尤其是同质性）预测迁移效果，指导机制选择。
### 关键结果
在GCN、GraphSAGE、GPS三类主流GNN骨干上验证：同质性图上NC→LP迁移稳定正向无负迁移；朴素复用LP预训练表示到NC任务易出现精度下降，仅当LP难度低、NC效果远未饱和时LP→NC迁移稳定正向；基于同质性等简单统计量即可准确预判跨任务迁移效果。
