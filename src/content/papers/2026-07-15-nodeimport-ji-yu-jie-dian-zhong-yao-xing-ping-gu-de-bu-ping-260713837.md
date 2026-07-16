---
title: 'NodeImport: Imbalanced Node Classification with Node Importance Assessment'
title_zh: NodeImport：基于节点重要性评估的不平衡节点分类方法
authors:
- Nan Chen
- Zemin Liu
- Bryan Hooi
- Bingsheng He
- Jun Hu
- Jia Chen
affiliations:
- Johns Hopkins University
- Zhejiang University
- National University of Singapore
- Grabtaxi Holdings Pte Ltd
arxiv_id: '2607.13837'
url: https://arxiv.org/abs/2607.13837
pdf_url: https://arxiv.org/pdf/2607.13837
published: '2026-07-15'
collected: '2026-07-16'
category: Other
direction: 图不平衡节点分类 · 节点重要性评估
tags:
- GNN
- Imbalanced Classification
- Node Importance
- Graph Learning
- Meta-Set
one_liner: 提出基于平衡元集的节点重要性评估框架，缓解图节点分类的类别不平衡问题
practical_value: '- 电商用户/商品图建模场景（如社交关系图、商品关联图）遇到类别不平衡（如小众商品、低活用户分类）时，可复用该框架的节点筛选逻辑，提升小众样本识别准确率

  - 框架将合成样本生成与过滤流程解耦的设计，可直接迁移到推荐系统长尾样本增强场景，兼容现有各类样本生成方法

  - 平衡元集的构建策略，可复用在推荐系统评估集构造环节，提升A/B实验指标的置信度'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现实图节点分类场景普遍存在类别不平衡问题，传统GNN易过拟合多数类、对少数类表征不足，现有基于类别大小加权/合成少数类节点的方案无法有效解决该问题。
### 方法关键点
1. 利用平衡元集评估节点重要性，仅保留能在无偏场景下提升模型性能的训练节点，训练全流程支持细粒度动态节点筛选；
2. 理论推导节点重要性直接计算公式，降低计算开销，同时提供明确的节点筛选阈值；
3. 解耦合成节点生成与过滤流程，兼容各类节点生成方法，同时设计贴合全局特征分布的元集构建策略，保障各类别鲁棒表示。
### 关键结果
在多个基准数据集、主流GNN架构上验证，效果优于所有SOTA基线，可有效缓解类别不平衡带来的性能偏差
