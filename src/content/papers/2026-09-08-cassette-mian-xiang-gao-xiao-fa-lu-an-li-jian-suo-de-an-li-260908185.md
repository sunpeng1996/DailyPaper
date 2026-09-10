---
title: 'Cassette: Case-to-Case Structural Distillation for Efficient Legal Case Retrieval'
title_zh: Cassette：面向高效法律案例检索的案例间结构蒸馏框架
authors:
- Yanran Tang
- Ruihong Qiu
- Hongzhi Yin
- Xue Li
- Zi Huang
affiliations:
- School of EECS, The University of Queensland, Brisbane, Australia
arxiv_id: '2609.08185'
url: https://arxiv.org/abs/2609.08185
pdf_url: https://arxiv.org/pdf/2609.08185
published: '2026-09-08'
collected: '2026-09-10'
category: RecSys
direction: 检索效率优化 · 知识蒸馏
tags:
- Knowledge Distillation
- Dual Encoder
- GNN
- Efficient Retrieval
- Ranking Distillation
one_liner: 通过排序与特征匹配双目标蒸馏，将重检索器知识迁移到轻量双编码器，实现法律案例检索精度效率平衡
practical_value: '- 可复用异构双编码器设计：查询侧用轻量MLP做在线推理，候选侧用GNN做离线预计算，适配电商大规模商品/内容检索的低延迟要求

  - 双目标蒸馏范式可直接迁移：采用排序损失+特征匹配损失的蒸馏策略，可将召回/排序链路的重模型知识迁移到上线轻量模型，平衡精度与速度

  - 大规模候选集场景下，可参考本方法替换O(n²)的在线相似度计算逻辑，将离线预计算的图结构知识蒸馏进encoder，实现量级级延迟降低'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
原有基于案例间图结构的法律案例检索方法推理复杂度达O(n²)，大规模候选集下延迟极高：1.5k候选集上单query检索耗时超500ms，5.5万候选集下耗时超3500秒，完全无法落地。
### 方法关键点
提出Cassette蒸馏框架，设计排序+特征匹配双蒸馏目标，将训练好的重型教师检索器的结构知识迁移到轻量混合双编码器学生模型；其中查询编码器采用MLP适配在线低延迟推理，候选编码器采用GNN做离线预计算，彻底避免在线构图与两两相似度计算开销。
### 关键结果
在3个公开基准数据集上检索精度优于普通双编码器基线，推理延迟较原有CaseLink基线降低4个数量级，达到大规模检索场景的落地延迟要求。
