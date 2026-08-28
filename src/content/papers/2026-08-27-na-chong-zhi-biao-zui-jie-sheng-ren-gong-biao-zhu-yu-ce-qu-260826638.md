---
title: Which Metrics Save the Most Human Annotation? Prediction-Powered Evaluation
  and Meta-Evaluation
title_zh: 哪种指标最节省人工标注：预测驱动的评估与元评估
authors:
- Mingqi Gao
- Anthony Sicilia
- Weiyan Shi
affiliations:
- Northeastern University
- West Virginia University
arxiv_id: '2608.26638'
url: https://arxiv.org/abs/2608.26638
pdf_url: https://arxiv.org/pdf/2608.26638
published: '2026-08-27'
collected: '2026-08-28'
category: Eval
direction: 评估方法优化 · 人工标注降本
tags:
- Evaluation
- Human Annotation
- Automatic Metrics
- Meta-Evaluation
- PPI
one_liner: 构建预测驱动评估框架与PPSR元指标，融合少量人工标注与自动评分实现无偏高效系统对比
practical_value: '- 推荐/广告系统AB测效果评估可复用该框架，用少量人工标注结合现有自动指标（如点击率、用户停留时长等统计值）获得无偏对比结果，大幅降低标注成本

  - 自研LLM-based评估指标时，可用PPSR元指标优先筛选能最大化节省标注成本的指标，替代传统相关性指标做选型

  - 生成式推荐/Agent回复质量评估场景，可直接适配参数/非参数版预测驱动评估流程，平衡评估准确性与标注成本'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
非可验证任务（如生成式推荐效果、Agent回复质量评估）中，人工标注可靠但成本高昂，自动指标可大规模扩展但普遍存在偏差，传统评估范式要么完全依赖人工要么直接替代人工，未找到二者高效结合的路径。
### 方法关键点
1. 基于预测驱动推理（PPI）构建预测驱动评估框架，融合极少量人工标注与大规模自动评分，输出可证明无偏的系统对比结果，同时实现参数、非参数两种落地流程，完成配对/非配对实验设计的效率权衡分析；
2. 提出PPSR元指标，量化自动指标在该框架下可节省的人工标注量，用于自动指标的选型与排序。
### 关键结果
在6个WMT数据集验证，PPSR相比现有系统级元指标，对自动指标的排序区分度提升显著，稳定性更强，可大幅压缩非可验证任务的人工标注成本。
