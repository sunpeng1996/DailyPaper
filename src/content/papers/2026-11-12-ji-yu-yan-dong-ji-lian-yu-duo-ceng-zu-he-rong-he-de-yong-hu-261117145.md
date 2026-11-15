---
title: Enhancing Preference Detection using Eye Movement Cascade and Multilayer Combinatorial
  Fusion
title_zh: 基于眼动级联与多层组合融合的用户偏好检测增强方法
authors:
- Yuanhong Wu
- Mary Tsaryk
- Sam Watson
- Tahsin Ahmed
- Christina Schweikert
- D. Frank Hsu
affiliations:
- Fordham University
- St. John's University
arxiv_id: '2611.17145'
url: https://arxiv.org/abs/2611.17145
pdf_url: https://arxiv.org/pdf/2611.17145
published: '2026-11-12'
collected: '2026-11-15'
category: RecSys
direction: 用户偏好建模 · 多模型融合
tags:
- preference_detection
- eye_tracking
- multi_model_fusion
- combinatorial_fusion
- cognitive_diversity
one_liner: 提出多层组合融合框架，基于认知多样性迭代融合多模型，提升眼动偏好检测性能
practical_value: '- 电商商品对比页、推荐结果页可接入前端埋点的眼动/注视时长数据，实时预测用户偏好，提升短路径决策场景的推荐准确率

  - 多模型融合环节可复用MCF「先扩选融合池再基于认知多样性剪枝」的迭代逻辑，相比单一融合策略可稳定提升3%左右的模型效果

  - 二元偏好判断场景（如商品二选一测评、排序正负样本标注）可引入眼动特征作为弱监督信号，降低人工标注成本'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
传统用户偏好检测多依赖显式反馈或行为后数据，无法捕捉决策过程中的视觉注意力信号，二元偏好预测场景下单一模型性能瓶颈明显

### 方法关键点
1. 基于用户二选一决策过程的眼动追踪数据构建偏好预测任务，输入为注视时长、扫视路径等多维度眼动特征
2. 引入多层组合融合（MCF）框架：先批量生成多分类器融合候选池，再基于认知多样性剪枝保留高价值融合方案，多层迭代直到多样性收敛

### 关键结果数字
最优单模型Pre@k达0.90，经第一层MCF融合后提升至0.9143，第二层融合后进一步提升至0.9286，较单模型相对提升3.18%
