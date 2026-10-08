---
title: 'Distilling Graph Geometry: Knowledge Gap from GNNs to MLPs'
title_zh: 图几何蒸馏：弥补GNN到MLP知识蒸馏的知识缺口
authors:
- Zhewei Chen
- Hao Zhu
- Jiaojiao Jiang
- Ahad N. Zehmakan
affiliations:
- Australian National University
- Data61, CSIRO
- University of New South Wales
arxiv_id: '2610.10520'
url: https://arxiv.org/abs/2610.10520
pdf_url: https://arxiv.org/pdf/2610.10520
published: '2026-10-07'
collected: '2026-10-08'
category: Training
direction: GNN到MLP知识蒸馏 · 无图推理优化
tags:
- Knowledge Distillation
- GNN
- MLP
- Graph Geometry
- Ollivier-Ricci Curvature
one_liner: 基于Ollivier-Ricci曲率的G²MLP蒸馏框架，无图推理MLP保留GNN教师精度与图几何特征
practical_value: '- 电商用户/商品关联图场景可复用该曲率引导的蒸馏思路，将GNN/Graph Transformer的图结构知识蒸馏到MLP，推理无需加载图结构，大幅降低召回/排序链路延迟

  - 针对用户行为图可按稀疏/稠密区域分层优化：稀疏区重点对齐保留GNN高能量特征，稠密区过滤冗余伪特征，提升蒸馏后MLP泛化性

  - 蒸馏时可同时做预测层+表征层双对齐，按曲率分配监督权重，训练开销低，部署侧无需改动MLP架构，可适配分类、链接预测等多任务'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有GNN-to-MLP蒸馏仅迁移节点预测结果或做置信度重加权，未指定学生模型需保留的教师图诱导几何特征，引发两类谱失效：稀疏图下学生谱欠拟合，丢失边界区域高能量教师特征；稠密图下谱过拟合，保留教师聚合后已坍缩的伪特征，高延迟GNN难以落地低延迟场景难度高。
### 方法关键点
基于能量加权的师生对齐目标，引入Ollivier-Ricci曲率定位两类谱误差的集中区域，据此动态分配预测层与表征层的监督权重，训练得到G²MLP，推理阶段为标准MLP，无需访问图结构。
### 关键结果
节点分类基准上G²MLP相对无图蒸馏基线精度稳定提升，师生秩差在稀疏/稠密图场景均显著降低，无需改动架构即可适配Graph Transformer教师模型与链接预测任务
