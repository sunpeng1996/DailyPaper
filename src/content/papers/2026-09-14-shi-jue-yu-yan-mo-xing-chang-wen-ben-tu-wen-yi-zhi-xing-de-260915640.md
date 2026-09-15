---
title: Human-Grounded Calibration for Long-Text Image-Text Congruence in Vision-Language
  Models
title_zh: 视觉语言模型长文本图文一致性的人本位校准方法
authors:
- Alessandro Gambetti
- Qiwei Han
affiliations:
- Universidade NOVA de Lisboa, NOVA School of Science and Technology
- Universidade NOVA de Lisboa, Nova School of Business and Economics
arxiv_id: '2609.15640'
url: https://arxiv.org/abs/2609.15640
pdf_url: https://arxiv.org/pdf/2609.15640
published: '2026-09-14'
collected: '2026-09-15'
category: Multimodal
direction: 多模态图文匹配 · 得分校准
tags:
- Vision-Language Model
- Score Calibration
- Image-Text Matching
- Multimodal Retrieval
- Human-grounded Evaluation
one_liner: 提出轻量校准层Congruency Score，实现可解释、对齐人判的长文本图文一致性打分
practical_value: '- 电商商品主图与长描述/详情页合规校验可直接复用CS轻量校准层，无需微调多模态大模型，大幅降低落地成本

  - 多模态召回/排序场景可参考三目标权衡思路，同步平衡检索精度、人感一致性、阈值适配性三类核心业务需求

  - 多模态打分校准场景可优先尝试后验校准方案，在保留与人判对齐效果的前提下避免损失检索性能'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
双编码器多模态模型的原始相似度得分受模态gap影响，无法直接作为长文本与图像的一致性校准指标，既难对齐人类判断，也无法适配阈值化的业务规则。

### 方法关键点
1. 提出轻量无训练的校准层Congruency Score（CS），将原始图文相似度映射为有界的一致性得分；
2. 系统性对比后验校准、投影类校准两类方案的效果trade-off。

### 关键结果数字
1. 投影校准降低模态质心距离的操作无法统一提升图文检索性能；
2. 直接后验校准与人判相关性最高，投影类校准可降低阈值斜率/截距失真，但会损失10%~15%的检索精度与人判相关性；
3. 明确长文本图文一致性打分需同时权衡检索性能、人判对齐度、阈值校准三个独立优化目标。
