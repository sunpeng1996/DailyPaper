---
title: 'Surrogate Quality Score: A Novel Composite Performance Metric for Model Selection'
title_zh: 替代质量得分：面向模型选择的新型复合性能指标
authors:
- Maaz Ahmad
- Iftekhar A. Karimi
affiliations:
- Department of Chemical & Biomolecular Engineering, National University of Singapore
arxiv_id: '2611.08937'
url: https://arxiv.org/abs/2611.08937
pdf_url: https://arxiv.org/pdf/2611.08937
published: '2026-11-06'
collected: '2026-11-09'
category: Eval
direction: 模型选择 · 评估指标设计
tags:
- Model Selection
- Evaluation Metric
- Accuracy-Complexity Tradeoff
- Composite Metric
one_liner: 提出兼顾预测精度与模型复杂度的可调节复合指标SQS，支撑系统化客观模型选择
practical_value: '- 推荐/排序模型选型时可参考SQS的加权乘积思路，平衡精度、推理时延、参数量等多维度指标，避免仅靠AUC选模型导致的线上性能退化

  - 内置的可调节权重参数可对接业务需求，大促低时延场景拉高复杂度权重，长期效果优先场景拉高精度权重

  - 归一化多维度指标后做乘积融合的方案，可直接复用为多目标排序的融合层逻辑，实现比线性加权更灵活的trade-off控制'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
当前ML模型选择多优先关注离线预测精度，忽略模型复杂度、推理成本等和业务落地强相关的属性，缺乏标准化的多维度融合选型方法，无法灵活适配不同场景的精度-成本权衡需求。
### 方法关键点
1. 提出复合评估指标Surrogate Quality Score（SQS），对归一化后的预测精度、模型复杂度两项核心指标做加权乘积融合，输出单值的模型整体质量得分，降低选型决策难度；
2. 内置用户可自定义的权重参数，支持显性控制精度与复杂度的trade-off权重，可直接对接业务偏好与部署约束。
### 关键结果
通过多组示例验证SQS选型的合理性，相比单一精度指标选型，可在精度损失小于3%的前提下，将模型参数量/推理时延降低35%以上，适配不同场景的落地需求。
