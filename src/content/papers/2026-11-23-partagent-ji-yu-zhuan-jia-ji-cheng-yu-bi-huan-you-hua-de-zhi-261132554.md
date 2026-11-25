---
title: 'PartAgent: Agentic 3D Part Segmentation via Expert Integration and Closed-Loop
  Refinement'
title_zh: PartAgent：基于专家集成与闭环优化的智能体3D部件分割
authors:
- Yang Cao
- Zhe Zhu
- Yiheng Zhang
- Zhengqiang Zhang
- Haoyuan Li
- Le Wan
- Dan Xu
affiliations:
- Hong Kong University of Science and Technology
- Tencent
- Hong Kong Polytechnic University
- Sun Yat-sen University
arxiv_id: '2611.32554'
url: https://arxiv.org/abs/2611.32554
pdf_url: https://arxiv.org/pdf/2611.32554
published: '2026-11-23'
collected: '2026-11-25'
category: Other
direction: 3D视觉理解 · Agent多专家融合
tags:
- Agent
- 3D Segmentation
- Expert Fusion
- Closed-loop Refinement
- Training-free
one_liner: 提出免训练的多专家融合Agent框架做3D部件分割，性能大幅超越现有SOTA
practical_value: '- 异构专家能力融合的免训练Agent架构思路，可迁移至多模态推荐场景下多模型能力的低成本集成

  - 观测驱动的闭环迭代优化逻辑，可复用在推荐bad case自动订正、生成式推荐结果校验优化链路

  - 3D部件分割能力可直接用于电商3D商品的细粒度部件打标，支撑部件级检索与个性化推荐'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
3D部件分割需同时结合几何结构与语义上下文推理，现有预训练3D专家可输出空间对齐的区域候选，2D专家可提供部件识别的语义线索，但缺乏高效融合异构能力的框架，难以同时生成准确分割结果并实现渐进式优化。
### 方法关键点
1. 免训练Agent框架PartAgent包含两个核心模块：①结构-语义专家集成模块，通过image-to-surface对应关系，融合3D专家区域候选与2D专家多视图语义证据，构造多粒度组合部件分区；②观测驱动的闭环分区优化模块，基于当前分区及支撑证据选择检查、证据修复、组合、重选等动作，验证变更后用更新状态指导后续决策。
### 关键结果
- PartObjaverse-Tiny-WT数据集mIoU达68.41，超最优基线8.53个点
- 3DCoMPaT200、PartNeXt、PartNetE、PartObjaverse-Tiny四个数据集平均mIoU达69.36，超最优基线平均7.28个点，全数据集取得SOTA
