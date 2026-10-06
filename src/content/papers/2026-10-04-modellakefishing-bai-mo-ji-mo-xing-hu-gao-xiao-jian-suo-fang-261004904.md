---
title: 'ModelLakeFishing: Efficient Retrieval over Million-Scale Model Lakes'
title_zh: ModelLakeFishing：百万级模型湖高效检索方法
authors:
- Xiaoyang Liu
- Zhengyuan Dong
- Renée J. Miller
affiliations:
- University of Waterloo
arxiv_id: '2610.04904'
url: https://arxiv.org/abs/2610.04904
pdf_url: https://arxiv.org/pdf/2610.04904
published: '2026-10-04'
collected: '2026-10-06'
category: Other
direction: 大规模模型湖检索 · 图编码与向量索引优化
tags:
- Model Retrieval
- Graph Encoder
- HNSW
- Vector Index
- Efficient Retrieval
one_liner: 提出关系感知图编码+HNSW索引框架，实现百万级模型湖的毫秒级高效检索
practical_value: '- 大规模候选库（如商品库、广告创意库、Agent工具库）检索场景可复用「HNSW粗筛+轻量重排」两级架构，在精度损失不到7%的前提下将p95延迟压到1ms级，适配高吞吐推荐/广告/Agent工具调用的召回需求

  - 异构稀疏关联数据（如推荐场景的用户-物品-属性交互、Agent场景的工具-任务-效果关联）可通过关系感知图编码器生成可索引embedding，降低冷启动下的召回难度

  - 千万级候选集的检索任务无需全库打分，粗召阶段取Top1000候选再重排的策略平衡精度与效率，可直接迁移到广告/推荐/Agent工具的召回链路'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
公开模型湖存量达数百万级，全库打分检索适配目标任务的模型成本极高，且模型-数据集-任务的关联证据稀疏异构，传统方案无法兼顾精度与延迟。

### 方法关键点
1. 整合模型元数据、历史评估数据构建模型-数据集-任务异构图
2. 采用关系感知图编码器生成模型、查询的可索引embedding，基于HNSW构建向量索引
3. 推理阶段采用两级链路：HNSW粗召Top1000候选，再用训练侧任务先验做指标感知重排，输出Top10结果

### 关键结果
在300万+模型、24.7万+模型-数据集性能对的测试集上，gold@10达0.2968，保留全库打分基线93.47%的精度；预计算查询embedding前提下，中位数延迟0.747ms，p95延迟仅1.102ms
