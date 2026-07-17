---
title: 'AlphaWiSE: Adaptive Weight Interpolation for Continual Multimodal Representation
  Learning'
title_zh: AlphaWiSE：面向持续多模态表征学习的自适应权重插值方法
authors:
- Sarthak Jain
- Qiran Hu
- Zhen Zhu
- Yaoyao Liu
affiliations:
- University of Illinois Urbana-Champaign
- Google DeepMind
arxiv_id: '2607.15094'
url: https://arxiv.org/abs/2607.15094
pdf_url: https://arxiv.org/pdf/2607.15094
published: '2026-07-16'
collected: '2026-07-17'
category: Multimodal
direction: 持续多模态表征 · 跨模态检索优化
tags:
- Continual Learning
- Multimodal Representation
- Cross-Modal Retrieval
- Weight Interpolation
- CLIP
one_liner: 提出无额外推理开销的后验权重插值方法，解决多模态持续学习的跨模态对齐遗忘问题
practical_value: '- 多模态检索/商品跨模态召回场景做增量更新时，可复用AlphaWiSE后验权重插值策略，无需修改模型结构，无额外推理开销，适配线上低延迟要求

  - 仅需在小样本exemplar记忆集上拟合每层共享的标量插值系数，即可平衡旧任务稳定性与新任务可塑性，无需存储多checkpoint做推理，降低部署成本

  - 跨模态搜索迭代时可直接套用该方法，缓解旧类目跨模态对齐效果退化问题，减少全量重训的时间与计算成本'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
CLIP等多模态模型进行持续增量学习时，参数更新会破坏前期习得的跨模态对齐关系，传统持续学习方法输出的单checkpoint无法兼顾不同检索方向的稳定性-可塑性trade-off，还易带来额外推理开销。
### 方法关键点
提出AlphaWiSE后验权重空间插值方案，直接组合两个冻结的源checkpoint；对每个匹配的参数张量，仅拟合1个全张量共享的标量插值系数，系数在小样本exemplar记忆集上训练，最终生成的插值checkpoint与原模型结构、参数量完全一致。
### 关键结果
在音频-图像-文本跨模态检索任务上，相比主流持续学习基线，在所有检索方向和评估指标上均获得一致性能提升，无额外推理延迟。
