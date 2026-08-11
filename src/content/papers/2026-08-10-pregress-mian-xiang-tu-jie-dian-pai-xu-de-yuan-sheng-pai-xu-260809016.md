---
title: 'PreGress: Ranking-Native Pre-training and Prompting for Graph Node Ranking'
title_zh: PreGress：面向图节点排序的原生排序预训练与提示微调框架
authors:
- Lujie Ban
- Jiasheng shi
- Yingli Zhou
- Kaiwen Xue
- Daiyin Wang
- Xubin Li
- Shuanghua Li
- Chenhao Ma
affiliations:
- 香港中文大学（深圳）数据科学学院
- 华为技术有限公司GTS
arxiv_id: '2608.09016'
url: https://arxiv.org/abs/2608.09016
pdf_url: https://arxiv.org/pdf/2608.09016
published: '2026-08-10'
collected: '2026-08-11'
category: RecSys
direction: 图推荐 · 节点排序预训练与提示微调
tags:
- GraphRanking
- Pre-training
- Prompt Tuning
- GNN
- Recommendation
one_liner: 提出首个图节点排序原生预训练+轻量提示框架，一次预训练适配多类排序任务性能优于基线
practical_value: '- 电商用户/商品图排序场景可复用其无监督预训练策略：用易获取的度中心性预测+节点属性重建做预训练，无需额外标注成本

  - 多排序任务复用同一预训练图backbone时，可参考其任务级轻量prompt设计：通用排序任务用可学习向量prompt，结构匹配类任务用轻量GNN生成prompt，仅调少量参数即可适配新任务，训练成本降低99%以上

  - 解决GNN过平滑问题可借鉴k-hop ego network提取+子图GNN的架构设计，保留节点局部结构信息的同时避免表示坍缩，适配排序任务对细粒度区分度的要求

  - 推荐召回的节点排序优化可参考其预训练损失设计：将MSE回归与listwise KL散度结合，同时校准绝对分值与相对排序，提升NDCG等排序指标'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有图节点排序方法要么传统计算复杂度高，要么单任务定制GNN需重训，通用图预训练目标与排序任务错配、迁移效果差，适配多类排序需求成本极高，尤其电商/推荐场景大量用户、商品图排序任务亟需高效可迁移的方案。

### 方法关键点
- 预训练阶段：采用无标注易获取的度中心性预测+节点属性重建多任务目标，度预测用MSE+listwise KL联合损失兼顾分值校准与排序一致性，属性重建用InfoNCE损失优化特征表达
- 架构设计：提取k-hop ego network构造节点局部子图，基于子图GNN编码，避免深层GNN过平滑问题，保留节点细粒度结构特征
- 下游适配：冻结预训练backbone，针对不同任务设计轻量prompt：中心度预测用可学习向量加性prompt，子图计数类结构任务用轻量GNN编码模式图生成prompt，仅调prompt与投影头即可完成适配

### 关键实验
在6个公开图数据集+Yelp2018、MovieLens-100K两个推荐基准上测试，对比传统排序器、监督GNN、预训练微调/提示微调基线：介数中心性预测任务NDCG@10平均领先第二名15%以上，局部子图计数任务NDCG@10平均领先12%；Yelp2018推荐任务性能与SOTA SimGCL差距小于0.3%，训练参数减少99.9%，训练速度提升39.1倍。

### 核心结论
图预训练目标与下游排序任务的输出空间、语义对齐程度直接决定迁移效果，节点级原生排序预训练+轻量提示的范式，能以极低的适配成本实现接近定制模型的排序效果。
