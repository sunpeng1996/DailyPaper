---
title: 'EDiS: Edge Disjoint Subgraph Sparsification Framework for Graph Neural Networks'
title_zh: EDiS：面向图神经网络的边不相交子图稀疏化框架
authors:
- Sai Karthik Navuluru
- Siddhartha Shankar Das
- Franck Dernoncourt
- S M Ferdous
- Ryan A. Rossi
- Nesreen K. Ahmed
- Baris Coskunuzer
- Alex Pothen
- Lakshman Tamil
- Mahantesh M Halappanavar
affiliations:
- University of Texas at Dallas
- Pacific Northwest National Laboratory
- Adobe Research
- University of North Carolina at Charlotte
- Purdue University
arxiv_id: '2610.09059'
url: https://arxiv.org/abs/2610.09059
pdf_url: https://arxiv.org/pdf/2610.09059
published: '2026-10-05'
collected: '2026-10-10'
category: Training
direction: GNN训练优化 · 大规模图稀疏化
tags:
- GNN
- Graph Sparsification
- Training Efficiency
- Subgraph Sampling
- Edge Pruning
one_liner: 解耦结构提取与逐epoch构图的GNN边不相交子图稀疏化框架，性能优于17种基线
practical_value: '- 电商用户-物品交互图GNN训练可复用EDiS的「一次性分解+逐epoch重构图」范式，避免每轮采样的高额开销，降低大规模图训练成本

  - 边预算紧张的场景（如低算力端GNN推理/小batch训练），优先采用边不相交子图分解+组合的方案，既能保证拓扑动态性又能保留高价值边

  - 交互图稀疏化时可复用基于特征打分的最大得分覆盖森林规则，优先保高价值交互边的同时维持稀疏性，平衡效果与效率'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
GNN训练中稀疏化可显著降低计算量，但传统方案要么复用固定稀疏拓扑限制模型拟合效果，要么每轮重采样带来高额额外开销，效果与效率难以平衡。
### 方法关键点
EDiS框架将图稀疏化解耦为两个独立阶段：1）一次性将原图分解为可缓存的边不相交子图，分解时默认采用特征打分+连续最大得分覆盖森林规则，也支持自定义边选择逻辑；2）逐epoch直接用缓存的子图组合出满足边预算约束的训练图，无需重复提取结构，同时保证每轮训练的拓扑动态性。
### 关键结果数字
在19个同配/异配/大规模节点分类基准上，同等边预算下对比17种基线，EDiS取得最高平均准确率/ROC-AUC，平均排名、与最优结果的差距均为所有方法最低，边预算越紧张性能优势越明显。
