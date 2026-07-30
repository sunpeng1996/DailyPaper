---
title: Lottery Tickets Are Not Deployment Tickets
title_zh: 彩票票稀疏子网络无法直接替代稠密模型上线部署
authors:
- Bum Jun Kim
affiliations:
- The University of Tokyo
arxiv_id: '2607.27031'
url: https://arxiv.org/abs/2607.27031
pdf_url: https://arxiv.org/pdf/2607.27031
published: '2026-07-29'
collected: '2026-07-30'
category: Eval
direction: 模型稀疏化 · 部署兼容性评估
tags:
- lottery-ticket
- model-sparsification
- model-compression
- deployment-compatibility
- model-evaluation
one_liner: 验证精度匹配的稀疏彩票票子网络与原稠密模型行为不兼容，无法直接上线替换
practical_value: '- 线上推荐/广告模型做剪枝、稀疏化压缩时，不能仅验证离线精度，需新增决策边界兼容性、下游策略 churn 率专项校验，避免上线后下游阈值逻辑失效

  - 若计划将现有稠密模型替换为同精度稀疏版本，需提前预估7%~10%的决策波动，预留下游逻辑重调、重验证资源，不要假设可无缝切换

  - 依赖固定阈值做召回/排序/审核决策的业务链路，稀疏模型的置信度偏移会导致阈值附近样本波动大，需先完成针对性阈值校准再上线'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
过往稀疏化、彩票票相关研究仅关注精度对齐，未考虑实际部署场景中已有下游决策逻辑固定的前提，研究结论矛盾，缺乏落地参考价值。
### 方法关键点
提出行为兼容距离指标，覆盖校准度、OOD响应、类别级可靠性、表征差异、下游策略决策5个维度的非精度相关偏差，在多数据集、多backbone架构下验证精度匹配的稀疏模型与稠密原模型的行为差异。
### 关键结果数字
- 精度匹配的稀疏模型仍存在显著行为差异，部分场景下抗噪精度更低
- 固定阈值决策场景中，彩票票替换会导致7%~10%的接受/审核决策变更，触发下游逻辑重配置成本，无法实现无缝替换
- 理论证明即使Top-1预测完全一致，决策边界附近的置信度小偏移也会产生大量路由 churn
