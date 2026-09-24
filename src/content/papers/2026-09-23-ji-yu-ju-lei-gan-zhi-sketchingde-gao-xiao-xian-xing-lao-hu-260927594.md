---
title: Efficient Linear Bandits via Cluster-Aware Sketching
title_zh: 基于聚类感知Sketching的高效线性老虎机算法
authors:
- Hantao Yang
- Hong Xie
- Defu Lian
affiliations:
- University of Science and Technology of China
arxiv_id: '2609.27594'
url: https://arxiv.org/abs/2609.27594
pdf_url: https://arxiv.org/pdf/2609.27594
published: '2026-09-23'
collected: '2026-09-24'
category: RecSys
direction: 在线学习 · 线性老虎机效率优化
tags:
- Linear Bandit
- Online Learning
- Clustering
- Matrix Sketching
- Computational Efficiency
one_liner: 提出聚类感知CS-LB线性老虎机算法，解决高维场景传统sketching的regret退化问题，平衡计算效率与效果
practical_value: '- 高维特征下的LinUCB/汤普森采样在线服务优化，可参考先对arm特征做聚类再做低维sketch降维，把每轮更新复杂度从O(d²)降到O(l²d)，大幅提升高维场景推理速度

  - 避免传统固定sketch方法的regret退化问题，可借鉴聚类内保留全协方差信息的设计，在降维同时保证在线探索的效果稳定性

  - 多臂场景下的簇切换机制可直接复用，给每个簇分配哨兵项做漂移检测，适配用户兴趣/广告池动态变化的电商场景'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
高维有限arm场景下，传统线性老虎机（如LinUCB）每轮更新复杂度达O(d²)，特征维度升高时计算成本不可接受；基于固定大小matrix sketching的降维方法在数据谱尾较重、sketch尺寸选择不当时会出现线性regret，无法保证收敛。
### 方法关键点
1. 引入聚类机制，提出CS-LB算法，每个簇内保留完整协方差信息，避免谱尾敏感问题，保证亚线性regret收敛；
2. 为每个簇分配哨兵项实现动态簇切换，适配arm分布变化；
3. 引入可调sketch尺寸l<d，将每轮更新复杂度降至O(l²d)。
### 关键结果
合成数据集实验显示，相比传统sketch类方法，CS-LB在regret仅提升2%-8%的前提下，每轮更新速度提升3-7倍，稳定实现效率与效果的最优权衡。
