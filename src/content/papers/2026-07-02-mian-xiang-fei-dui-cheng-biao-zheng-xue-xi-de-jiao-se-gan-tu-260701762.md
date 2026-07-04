---
title: Role-Aware Neural Convex Divergence Heads for Asymmetric Representation Learning
title_zh: 面向非对称表征学习的角色感知神经凸散度头
authors:
- He Huang
- Lu Shen
- Yunfeng Huang
- Li Qi
affiliations:
- Chongqing Technology and Business University, School of Mathematics and Statistics
- Chongqing Key Laboratory of Statistical Intelligent Computing and Monitoring, Chongqing
  Technology and Business University
- Chongqing Technology and Business University, School of Food Science
- TU Dortmund University, Faculty of Electrical Engineering and Information Technology
arxiv_id: '2607.01762'
url: https://arxiv.org/abs/2607.01762
pdf_url: https://arxiv.org/pdf/2607.01762
published: '2026-07-02'
collected: '2026-07-04'
category: Other
direction: 非对称表征学习 · 可插拔距离模块
tags:
- Asymmetric Representation Learning
- Bregman Divergence
- Input-Convex Neural Network
- Role-aware Projection
- Metric Learning
one_liner: 提出带源/目标角色投影的可插拔凸散度模块，结构化建模非对称表征学习中的有向关系
practical_value: '- 针对电商推荐中用户→物品、上级类目→下级类目、搜索query→匹配文档等有向关系匹配任务，可将该模块作为可插拔距离头替换现有cosine/欧氏距离，提升方向匹配准确率

  - 涉及类目层级构建、商品蕴含关系（平替/升级款等）建模的场景，可复用角色投影+ICNN Bregman散度的结构，获得可解释的非对称匹配得分

  - 大规模固定特征的召回排序场景不建议使用该模块，专用对称或双曲基线的排序精度表现更优'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有对称距离度量（cosine、欧氏、马氏距离）无法适配词汇蕴含、层级结构、有向链接这类非对称表征学习任务，通用神经打分器虽可建模方向性但几何结构约束缺失，可解释性差。
### 方法关键点
1. 提出角色感知神经凸散度头，先对源、目标角色表征做独立投影，再在投影空间计算输入凸神经网络（ICNN）建模的Bregman散度，输出非负结构化得分
2. 理论证明该模块的投影空间恒等性、源角色凸性、方向间隙可分解性、Hessian局部曲率可解释性
### 关键结果
- 语义、本体基准测试中，相比普通ICNN-Bregman头，角色投影在10次随机种子实验中持续提升方向准确率，同时保持零观测负散度率
- 大规模固定特征的引文预测场景下，专用对称或双曲基线的排序精度更优
