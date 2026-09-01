---
title: 'The Edge Spectrum of Choice-Derived Item Graphs: Strong and Weak Edges Encode
  Different Relations in Collaborative Filtering'
title_zh: 选择衍生物品图的边谱：协同过滤中强弱边编码差异化关系
authors:
- Keigo Sakurai
- Takahiro Ogawa
- Miki Haseyama
affiliations:
- Hokkaido University
arxiv_id: '2608.29578'
url: https://arxiv.org/abs/2608.29578
pdf_url: https://arxiv.org/pdf/2608.29578
published: '2026-08-30'
collected: '2026-09-01'
category: RecSys
direction: 图协同过滤 · 物品关系建模
tags:
- Graph-CF
- Collaborative-Filtering
- Choice-Model
- Item-Item-Graph
- Recommendation-System
one_liner: 揭示选择衍生物品图强弱边语义异质性，给出可落地的诊断协议与边感知优化算子
practical_value: '- 别将物品图的邻居截断$k$仅当稀疏超参调，对基于曝光/选择模型构建的物品图，$k$是语义开关，建议先跑论文给出的4步诊断协议，判断是否存在边谱效应再选截断值

  - 不要盲目迷信选择模型的「更丰富信号」，直接用MNL选择模型的转移权重做正平滑图CF效果普遍不如共点击图，核心原因是强边对应同曝光池的竞争关系，和BPR梯度方向冲突

  - 要复用选择衍生物品图的话，不要做全局符号翻转或在loss层加margin修正，最优方案是按边权分强弱区间，强边做负平滑、弱边要么正平滑要么直接丢弃，可取得超过共点击图的效果

  - 图CF优化的核心收益不在物品图构造侧，本实验中不同物品图算子的NDCG@10差异不到0.01，远小于训练框架、超参带来的0.04+增益，不要在物品图构造上过度投入'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
图协同过滤默认物品图边权越高代表置信度更高的同类关系，邻居截断$k$仅作为稀疏化超参调整；但基于选择模型（用于建模同曝光池物品竞争）构建的物品图是否符合该假设此前未被验证，实际业务中直接替换选择衍生算子往往达不到预期收益，缺乏明确的问题诊断与优化路径。
### 方法关键点
- 控制变量对比4种物品侧传播算子：LightGCN默认的$S^\top S$、共点击图、共曝光图、MNL选择模型衍生的替代图，固定训练、评估、超参等所有其他配置
- 理论证明：选择衍生图的强边对应同曝光池的点击-未点击竞争对，正平滑会缩小二者得分差，与BPR梯度方向完全相反，而共点击图天然不存在该冲突
- 提出4步可落地诊断协议，可提前判断选择衍生图是否存在边谱效应、是否影响业务指标；进一步设计边权感知算子，按边权划分为强弱区间，分别适配不同符号的平滑系数
### 关键实验
在MIND、EB-NeRD两个公开新闻推荐数据集上验证：
- 直接替换选择衍生算子的效果比共点击图低0.005~0.008 NDCG@10，4种算子的效果差距小于0.01，远小于LightGCN到LightGCN++的0.04+增益
- 全局符号翻转、损失层加竞争margin等统一修正方案均失效，边权感知算子在EB-NeRD上超过共点击图0.0027 NDCG@10，完全匹配理论预测

选择衍生物品图的邻居截断$k$是语义开关，而非单纯的稀疏化超参。
