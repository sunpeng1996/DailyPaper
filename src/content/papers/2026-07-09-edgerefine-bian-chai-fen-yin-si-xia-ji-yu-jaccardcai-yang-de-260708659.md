---
title: 'EdgeRefine: Privacy-Utility Balance for Graphs via Jaccard Sampling under
  Edge Differential Privacy'
title_zh: EdgeRefine：边差分隐私下基于Jaccard采样的图隐私效用平衡框架
authors:
- Wenxiu Ding
- Muzhi Liu
- Zheng Yan
- Mingjun Wang
- Yifan Zhao
- Qiao Liu
affiliations:
- Xidian University
- State Key Laboratory of Integrated Services Networks, Xidian University
- School of Cyber Engineering, Xidian University
arxiv_id: '2607.08659'
url: https://arxiv.org/abs/2607.08659
pdf_url: https://arxiv.org/pdf/2607.08659
published: '2026-07-09'
collected: '2026-07-11'
category: Other
direction: 隐私保护图学习 · 边差分隐私优化
tags:
- Differential Privacy
- Graph Neural Network
- Privacy Preserving
- Jaccard Sampling
- Edge Privacy
one_liner: 提出基于Jaccard采样的边差分隐私框架EdgeRefine，大幅优化图学习的隐私-效用平衡
practical_value: '- 电商用户行为/社交图、商品关联图隐私合规场景，可复用Jaccard相似性预排序筛除低置信度噪边的思路，在满足差分隐私要求前提下最小化GNN效果损失

  - 差分隐私落地时可替代全局统一加噪方案，借鉴按边置信度分桶采样、用隐私预算ε动态调整真假边保留比例的策略

  - 稀疏用户行为图场景可复用固定总边数采样的trick，避免加噪后图结构过度畸变导致GNN召回/排序效果暴跌'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
GNN在图结构数据学习上效果优异，但传统边差分隐私方案通过全局邻接矩阵加噪实现隐私保护，存在隐私强度提升则图效用大幅下降的问题，隐私-效用平衡难题阻碍隐私敏感场景的图学习落地。
### 方法关键点
EdgeRefine是本地差分隐私框架：首先用Jaccard相似度计算边存在概率并排序，移除低置信度噪边；再用隐私预算ε动态确定真假边保留比例，按概率排名分采样；最后用采样率k控制总边数，保证最终图的稀疏性和可靠性。
### 关键结果
隐私预算ε=2.5时，节点分类任务较SOTA基线提升17.8%（GAT+ACM数据集）、19.7%（GCN+Cora数据集）；图分类任务较无噪基线仅平均掉点5%准确率；抗图重建攻击时，相对绝对误差平均达1.962（Cora）、1.472（AMAP），隐私鲁棒性优异。
