---
title: 'Better Slots, Better Worlds: Representation Quality & Robustness in Object-Centric
  World Models'
title_zh: 目标中心世界模型表征质量与鲁棒性研究：槽质量决定规划效果上限
authors:
- Shukrullo Nazirjonov
- Sai Prasanna
- Anna Manasyan
- Georg Martius
affiliations:
- University of Tuebingen
- Max Planck Institute for Intelligent Systems
arxiv_id: '2608.12078'
url: https://arxiv.org/abs/2608.12078
pdf_url: https://arxiv.org/pdf/2608.12078
published: '2026-08-12'
collected: '2026-08-13'
category: Agent
direction: Agent 世界模型表征优化
tags:
- Object-Centric Representation
- World Model
- Slot Attention
- Robustness
- Model Predictive Control
one_liner: 通过对照实验明确目标中心世界模型槽质量与规划效果的关联及鲁棒性驱动因子
practical_value: '- 开发交互Agent时可优先用无监督指标FG-ARI、mBO筛选槽编码器质量，无需额外标注成本，达到阈值后即可停止优化避免冗余投入

  - 分布偏移场景下的Agent推理可优先选择绑定质量优的目标中心表征，搭配冻结预训练视觉特征进一步提升鲁棒性

  - 电商3D商品展示、直播商品理解任务可复用槽分解的归纳偏置，替代传统全局特征，降低背景、拍摄角度变化带来的识别误差'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有目标中心世界模型（OCWMs）默认使用给定槽编码器，仅开展分布内评估，无法明确目标中心归纳偏置对规划任务的实际增益，也未厘清OCWMs效果的核心驱动因子。
### 方法关键点
针对视觉模型预测控制场景，沿「目标中心表征质量」「分布偏移下泛化性」两个维度开展受控对照实验，对比OCWMs与场景中心模型的表现差异。
### 关键结果
1. 规划成功率与无监督槽质量指标FG-ARI、mBO正相关，高槽质量区间增益出现饱和；
2. 当槽绑定质量足够优时，原有OCWMs依赖的辅助本体感觉输入、掩码归纳偏置可完全移除，不影响效果；
3. 未知分布偏移场景下，优槽OCWMs鲁棒性优于端到端训练的场景中心LeWM，基于冻结预训练特征的DINO-WM鲁棒性与其相当，预训练特征是鲁棒性的核心贡献因子。
