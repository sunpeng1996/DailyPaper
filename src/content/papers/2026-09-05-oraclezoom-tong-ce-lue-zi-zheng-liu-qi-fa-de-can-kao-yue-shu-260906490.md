---
title: 'OracleZoom: On-Policy Self-Distillation Inspired Reference-Constrained Recursive
  Image Super Resolution'
title_zh: OracleZoom：同策略自蒸馏启发的参考约束递归图像超分方法
authors:
- Shubhashis Roy Dipta
- Sourajit Saha
- Shaswati Saha
- Nobin Sarwar
affiliations:
- University of Maryland, Baltimore County
arxiv_id: '2609.06490'
url: https://arxiv.org/abs/2609.06490
pdf_url: https://arxiv.org/pdf/2609.06490
published: '2026-09-05'
collected: '2026-09-10'
category: Multimodal
direction: 多模态图像生成 · 递归超分辨率优化
tags:
- Image Super Resolution
- Self-Distillation
- On-Policy Training
- Generative Vision
- EMA Regularization
one_liner: 提出同策略自蒸馏启发的参考约束递归超分框架，解决深层放大无标注、幻觉严重问题
practical_value: '- 电商商品图极端放大场景可复用该框架，用最后一张有标注图做约束减少超分幻觉，提升商品图高清化效果

  - 多模态生成任务无标注迭代生成场景，可借鉴KL约束预训练隐空间先验+EMA一致性的训练trick，降低生成漂移

  - 递归式生成任务（如多轮生成、增量放大）可复用同策略自蒸馏思路，用生成轨迹做训练数据解决标注不足问题'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
递归超分可通过重复迭代实现极端图像放大，但放大倍率提升时所需Ground Truth分辨率几何级增长，深层放大阶段无标注监督，易出现严重幻觉，现有方案效果受限。
### 方法关键点
1. 借鉴同策略自蒸馏思路，以最后可用的Ground Truth作为跨监督边界的参考约束，基于模型自身递归生成的轨迹完成训练
2. 用直接+跨尺度监督约束可验证内容，无参考质量目标引导未确定的细粒度细节生成
3. 引入KL约束的预训练隐空间先验限制生成漂移，EMA一致性机制稳定监督边界的训练过程
### 关键结果
在7个数据集上达到SOTA超分效果，平均CLIPIQA得分0.713，深层放大阶段增益更显著，幻觉水平降低2-5倍
