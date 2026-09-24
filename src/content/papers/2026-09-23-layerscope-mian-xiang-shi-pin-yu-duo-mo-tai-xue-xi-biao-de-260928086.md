---
title: 'LAYERSCOPE: A Layerwise Characterization of Video and Multimodal Learned Representations'
title_zh: LAYERSCOPE：面向视频与多模态学习表征的逐层分析框架
authors:
- Sandra Arcos-Holzinger
- Debashish Chakraborty
- Rohita Mocharla
- Will Walden
- Andrew Yates
- Reno Kriz
- Sarah M. Erfani
- James Bailey
- Vishal M. Patel
- Sanjeev Khudanpur
affiliations:
- Johns Hopkins University
- Human Language Technology Center of Excellence
- Johns Hopkins Applied Physics Lab
- University of Melbourne
- Monash University
arxiv_id: '2609.28086'
url: https://arxiv.org/abs/2609.28086
pdf_url: https://arxiv.org/pdf/2609.28086
published: '2026-09-23'
collected: '2026-09-24'
category: Multimodal
direction: 多模态表征 · 无标注逐层分析
tags:
- Multimodal Representation
- Layerwise Analysis
- Video Understanding
- Unsupervised Evaluation
- Representation Learning
one_liner: 提出无标注逐层分析框架LAYERSCOPE，可跨模型跨层对比视频/多模态表征无需任务标签
practical_value: '- 电商多模态检索/推荐场景可复用框架思路，无需标注即可对比不同预训练多模态模型的各层表征质量，降低下游任务选型成本

  - 做召回/表征层优化时可优先测试中间层表征而非默认最终层，实测可提升分类、聚类、检索类任务表现

  - 不同任务选层参考：分类/聚类优先用RankMe指标选最优层，跨模态检索优先用配对感知类指标评估表征效果'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有多模态/视频模型表征评估依赖大量标注数据、任务特定评测流程，计算成本高；且默认仅用最终层输出，无法知晓各层表征的实际业务价值。
### 方法关键点
提出无标注逐层分析框架LAYERSCOPE，基于局部、全局、分布、对应关系四类几何指标，无需任务标签即可实现单模型内部跨层、不同模型之间的表征结构对比。
### 关键结果数字
在7款不同架构模型、MVEB/MVEB+的分类/聚类/文本到视频检索任务上验证：1）中间层表征效果可超过最终层/默认输出；2）无单一几何指标可通用预测下游性能：RankMe对分类/聚类任务选层效果最优，配对感知指标对检索任务解释度优于单独分布距离，LID和性能的关联随任务变化。
