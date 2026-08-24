---
title: 'Tydra: An Efficient Hybrid Model for Tabular Data'
title_zh: Tydra：面向表格数据的高效混合模型
authors:
- Mieszko Komisarczyk
- Saurabh Mathur
- Maurice Kraus
- Sriraam Natarajan
- Kristian Kersting
affiliations:
- Technical University of Darmstadt
- The University of Texas at Dallas
- Hessian Center for Artificial Intelligence (hessian.ai)
- German Research Center for AI (DFKI)
arxiv_id: '2608.21199'
url: https://arxiv.org/abs/2608.21199
pdf_url: https://arxiv.org/pdf/2608.21199
published: '2026-08-21'
collected: '2026-08-24'
category: Other
direction: 表格基础模型 · 混合架构效率优化
tags:
- Tabular Foundation Model
- SSM
- Transformer
- Hybrid Architecture
- Inference Optimization
one_liner: 提出交替堆叠Attention与SSM层的混合架构，平衡表格预测任务的精度与推理效率
practical_value: '- 电商/推荐场景的用户行为、物品属性等表格类预测任务，可复用Attention+SSM混合堆叠架构思路，在精度损失可控的前提下降低推理时延，适配高QPS线上场景

  - 落地大模型处理表格特征时，可参考该混合架构替代纯Transformer方案，降低长上下文下的计算开销，适合低算力本地部署需求

  - 性能调优时可参考本工作的精度-效率平衡思路，无需盲目堆叠大参数量SSM模型，混合架构可在更小参数下实现更优综合表现'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
纯Transformer架构的表格基础模型（如TabPFN）预测精度高，但推理成本随上下文长度呈二次增长，无法适配低算力本地部署场景；纯SSM架构的表格模型（如Hydra）推理效率高，但精度表现不足，两者无法兼顾性能与成本。
### 方法关键点
提出混合架构Tydra，交替堆叠Transformer Attention层与SSM层，结合Attention的精准关联建模能力与SSM的亚线性推理效率优势，适配表格数据的上下文学习任务。
### 关键结果数字
在30个OpenML数据集上，相比TabPFN推理时延降低30%，同时保留绝大多数预测精度；性能远超参数量约10倍的Hydra模型，且推理速度更快。
