---
title: Aggregate-then-Calibrate for Human-centered Assessment with Theoretical Guarantees
title_zh: 带理论保证的先聚合后校准以人为中心评估框架
authors:
- Zejun Xie
- Xintong Li
- Guang Wang
- Desheng Zhang
affiliations:
- Rutgers University
- Renmin University of China
- Florida State University
arxiv_id: '2608.02455'
url: https://arxiv.org/abs/2608.02455
pdf_url: https://arxiv.org/pdf/2608.02455
published: '2026-08-03'
collected: '2026-08-05'
category: Eval
direction: 人因评估 · 人机融合校准框架
tags:
- Human-Centered-Evaluation
- Rank-Aggregation
- Isotonic-Calibration
- Annotator-Reliability
- Label-Efficient
one_liner: 提出先聚合后校准两阶段框架，融合人工标注与模型评分，解决无真实标签的人因评估问题
practical_value: '- 推荐系统A/B测试、推荐结果人工评估场景，可直接复用AtC框架融合不同经验标注员的打分，校准模型排序分数，降低标注异质性带来的评估偏差

  - Agent任务无明确Ground Truth的评估场景（如客服Agent满意度、生成内容质量评估），可落地两阶段流程：先聚合多标注源的排序共识，再做保序投影校准模型输出，提升评估鲁棒性

  - 标注资源有限的电商搜索相关性评估场景，可引入标注者可靠性建模的排序聚合方法，降低对高成本专家标注的依赖'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
以人为中心的评估任务（如内容质量打分、服务体验评估）普遍缺乏可验证ground truth，纯人工评估受标注者专业度、评分尺度异质性影响偏差大，纯模型评估依赖不完美代理标签/不完整特征，效果受限。

### 方法关键点
提出两阶段Aggregate-then-Calibrate（AtC）框架：
1. 阶段1引入标注者可靠性建模，将异构的比较式标注聚合为共识排序
2. 阶段2通过保序投影将任意预测模型的分数校准到共识排序上，在保证序一致性的同时尽可能保留模型量化信息

### 关键结果
理论上证明异质性标注建模比同质性假设的共识估计效率更高，保序校准即使共识排序misspecified也有风险边界，AtC渐近优于纯模型评估；在半合成与真实数据集上，相比纯人工/纯模型评估，AtC准确率、鲁棒性均稳定提升。
