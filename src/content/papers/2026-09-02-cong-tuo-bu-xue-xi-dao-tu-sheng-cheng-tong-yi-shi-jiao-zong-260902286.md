---
title: 'From topology learning to graph generation: A unifying perspective'
title_zh: 从拓扑学习到图生成：统一视角综述
authors:
- Xiaowen Dong
- Hoi-To Wai
- Siheng Chen
- Laura Toni
- Dorina Thanou
affiliations:
- University of Oxford
- The Chinese University of Hong Kong
- Shanghai Jiao Tong University
- University College London
- EPFL
arxiv_id: '2609.02286'
url: https://arxiv.org/abs/2609.02286
pdf_url: https://arxiv.org/pdf/2609.02286
published: '2026-09-02'
collected: '2026-09-05'
category: Other
direction: 图学习 · 拓扑推理与生成统一框架
tags:
- Graph_Learning
- Graph_Topology_Learning
- Graph_Generation
- Unified_Framework
- Survey
one_liner: 构建统一框架关联图拓扑学习与图生成任务，梳理范式优缺并指明跨方向融合研究路径
practical_value: '- 做用户/商品异构图构建时可参考两类图学习范式选型：单图拓扑学习适合静态用户-物品关联挖掘，图生成适合冷启动场景的未知关系补全

  - 可复用跨范式融合思路做序列推荐的用户行为图建模：先用拓扑学习挖掘现有行为关联结构，再用生成式方法预测未来交互图提升长周期推荐准确率

  - 图结构未知的推荐场景（如新品冷启动）可借鉴统一框架的逆问题建模思路，从交互数据端到端同时学习图结构与推荐模型，减少人工特征工程'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
图结构学习是信号处理与机器学习领域的基础任务，现有研究长期分为两个独立方向：一是从观测数据推理单张图的拓扑结构，二是从已有图实例学习生成分布以采样新图，两类任务的关联与范式差异缺乏系统性梳理。
### 方法关键点
将两类任务统一建模为图数据通用生成过程的逆问题，搭建统一分析框架，系统性梳理两类方向下的主流方法体系，对比不同范式的适用场景、性能优势与局限性，明确跨方向的融合创新点。
### 关键结果
完成了图拓扑学习与图生成两大领域的跨范式打通，给出了多个未解决的研究方向与融合切入点，为跨领域图建模的算法设计提供了系统性参考。
