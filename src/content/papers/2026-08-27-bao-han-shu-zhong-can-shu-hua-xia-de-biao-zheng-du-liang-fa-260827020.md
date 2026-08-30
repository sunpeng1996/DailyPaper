---
title: Representation Measurements Under Function-Preserving Reparameterizations
title_zh: 保函数重参数化下的表征度量方法有效性研究
authors:
- Abdullah Karasan
affiliations:
- University of Maryland, Baltimore County
arxiv_id: '2608.27020'
url: https://arxiv.org/abs/2608.27020
pdf_url: https://arxiv.org/pdf/2608.27020
published: '2026-08-27'
collected: '2026-08-30'
category: LLM
direction: 大语言模型表征度量 重参数不变性研究
tags:
- Representation Measurement
- Function-Preserving Reparameterization
- Parallel Analysis
- LLM
- Orthogonal Invariance
one_liner: 验证列置换并行分析不满足保函数重参数不变性，提出正交不变比较器实现稳定表征度量
practical_value: '- 做LoRA秩选择、表征降维时避免使用列置换并行分析选维度，防止基变换导致结果不稳定浪费调优成本

  - 估算用户/Item语义表征秩、设计表征相似度度量时，优先选择正交不变的度量方法，保障不同重参数下结果一致性

  - 做RAG检索表征压缩、语义召回低秩优化时，先验证度量方法的重参数不变性，减少无效超参实验'
score: 4
source: arxiv-stat.ML
depth: abstract
---

### 动机
LLM隐层坐标不由输入输出函数唯一决定，基于表征的度量需对保函数的基变换重参数保持不变性，现有广泛使用的列置换并行分析的度量有效性未经过该性质验证。
### 方法关键点
1. 理论证明列置换并行分析违反保函数重参数不变性，且数据内部参考流程无法同时满足坐标边缘保留、正交等变、去跨坐标协方差三个约束
2. 对比测试列置换并行分析、独立种子并行分析、正交不变比较器得分三类方法的稳定性与区分能力
### 关键结果
跨5个模型、3个检索域、75种变换的实验中，列置换并行分析的组件计数中位数差异达0.79，固定阈值决策差异中位数为0.26；1200组仅中心化对照实验中1141组组件计数因参考分布变化而改变，而正交不变比较器得分数值稳定，且保留同等水平的跨集区分能力。
