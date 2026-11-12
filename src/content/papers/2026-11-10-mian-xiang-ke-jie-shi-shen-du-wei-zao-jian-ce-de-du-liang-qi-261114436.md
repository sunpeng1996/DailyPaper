---
title: Metric-Aligned Group Relative Policy Optimization for Explainable Deepfake
  Detection
title_zh: 面向可解释深度伪造检测的度量对齐组相对策略优化方法
authors:
- Luka Dragar
- Peter Peer
- Vitomir Štruc
- Borut Batagelj
affiliations:
- University of Ljubljana
arxiv_id: '2611.14436'
url: https://arxiv.org/abs/2611.14436
pdf_url: https://arxiv.org/pdf/2611.14436
published: '2026-11-10'
collected: '2026-11-12'
category: Other
direction: 可解释深度伪造检测 · 大模型对齐优化
tags:
- Deepfake Detection
- GRPO
- Multimodal LLM
- Explanation Generation
- Metric Alignment
one_liner: 提出解耦预测-解释深度伪造检测pipeline，用度量对齐GRPO优化解释生成，获挑战赛专项指标第一
practical_value: '- 解耦「硬分类+归因解释」的pipeline可迁移到电商违规内容审核、虚假广告识别场景，先做确定性分类再生成面向普通用户的解释，避免多模态模型的分类幻觉

  - 用度量对齐的GRPO做生成任务的指标对齐优化思路，可复用到推荐理由生成、广告文案生成场景，直接对齐业务指标（如文案点击率、理由转化率）做RLHF替代，降低标注成本

  - 长解释转短摘要的双大模型串联结构，可迁移到商品评价摘要、客服话术生成场景，无需二次调用多模态模型，降低推理成本'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有深度伪造检测器仅输出真假分类结果，实际落地场景需要可解释的视觉证据支撑决策；联合训练的多模态模型易出现幻觉，常为篡改图像生成符合真实属性的错误描述。

### 方法关键点
1. 采用解耦的预测-解释pipeline，先用DINOv3-MAC+SigLIP2/DINOv2视觉基础模型集成做图像真假分类
2. 基于分类结果输入Qwen3-VL-8B，生成依赖视觉证据的决策条件解释
3. 针对假图调用第二个无图像输入的Qwen3-VL-8B，将长解释压缩为普通用户易懂的短摘要
4. 引入度量对齐的GRPO，对两个解释生成模型直接对齐挑战赛评价指标做优化

### 关键结果
相同实验条件下，GRPO将复杂BERTScore-F1从0.686提升至0.712，同时显著提升实体、证据F1等grounding指标；提交方案在ACM MM2026可解释深度伪造检测挑战赛中，复杂BERTScore-F1排名第一，总排名第七
