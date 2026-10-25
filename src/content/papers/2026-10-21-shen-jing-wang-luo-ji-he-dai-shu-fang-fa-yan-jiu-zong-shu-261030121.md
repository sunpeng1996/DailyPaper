---
title: 'Geometric Algebra for Neural Networks: A Survey'
title_zh: 神经网络几何代数方法研究综述
authors:
- Tao Zhong
- Kaison Fong
- Keqin Wang
- Christine Allen-Blanchette
affiliations:
- Princeton University
- Stanford University
arxiv_id: '2610.30121'
url: https://arxiv.org/abs/2610.30121
pdf_url: https://arxiv.org/pdf/2610.30121
published: '2026-10-21'
collected: '2026-10-25'
category: Other
direction: 几何代数神经网络技术综述
tags:
- Geometric Algebra
- Equivariant Neural Network
- Geometric Deep Learning
- Multivector Representation
- Survey
one_liner: 系统梳理几何代数神经网络的架构、特性与适用场景，提供选型指南与失效模式分析
practical_value: '- 若业务涉及AR/VR商品展示、3D商品推荐等带明确几何对称的场景，可评估GA神经网络，利用其内置等变性降低特征工程成本

  - 通用推荐、用户行为建模、文本语义处理等无显式几何对称的场景不建议尝试GA架构，其效果/效率优势无实证支撑

  - 引入GA架构前可参考文中代数选型指南，提前规避训练不稳定、部署开销高的已知失效模式'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
当前几何深度学习领域等变架构选型缺乏统一参考，几何代数（GA）类神经网络的适用边界、性能优劣没有系统性梳理，从业者难以判断落地价值。
### 方法关键点
系统梳理GA神经网络的核心组件、等变特性、主流应用领域、实证表现与工程化工具链；提供代数选型决策指南，头对头对比GA与其他等变架构的效果，完整覆盖训练病理、部署约束、性能上限三类失效模式分析。
### 关键结果
仅在存在显式几何对称、异构几何实体的场景下，GA架构有明确优势；通用场景下其参数效率、可解释性、稠密预测能力的优势缺乏一致实证，效果不优于调优后的非GA等变基线。
