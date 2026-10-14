---
title: 'PhyProbe: Rethinking Physical Consistency Evaluation in Generated Videos'
title_zh: PhyProbe：重新思考生成视频的物理一致性评估
authors:
- Max Ku
- Jiaojiao Fan
- Zekun Hao
- Francesco Ferroni
- Heng Wang
- Wenhu Chen
- Ming-Yu Liu
- Prithvijit Chattopadhyay
affiliations:
- NVIDIA
- University of Waterloo
- Vector Institute
arxiv_id: '2609.38377'
url: https://arxiv.org/abs/2609.38377
pdf_url: https://arxiv.org/pdf/2609.38377
published: '2026-09-28'
collected: '2026-10-14'
category: Eval
direction: 生成内容质量评估 · 物理一致性检测
tags:
- VideoGeneration
- Evaluation
- SpatioTemporalEncoder
- Alignment
- PhysicalConsistency
one_liner: 基于冻结预训练时空编码器与多目标训练，实现生成视频物理一致性鲁棒评估
practical_value: '- 多源异构监督（排序/标量/锚点）的统一训练范式，可迁移到电商AI商拍视频、生成式商品文案的质量评估任务，解决标注数据类型不统一的问题

  - 冻结大模型+轻量打分头的架构，可低成本复用到业务侧各类生成内容的合规/质量打分，无需全量微调大模型，节省训练成本

  - 锚点校准方法可将不同来源的评分统一映射到稳定[0,1]区间，解决业务侧多模型打分结果不可比、对齐成本高的问题

  - 物理一致性违规与人类整体偏好强相关的结论，可简化生成式内容质检流程，无需单独设计多维度繁杂的质检标签'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有生成视频物理一致性评估存在两类缺陷：基于现成VL模型的方案对物理动态感知能力弱，基于人工标注微调的评估器易过拟合数据集特征、泛化性差；且现有监督源仅能提供相对排序或绝对分数中的一类，无法同时满足两类评估需求。
### 方法关键点
采用冻结的预训练时空编码器提取特征，搭配轻量打分头输出物理一致性违规分数；训练时使用统一目标融合三类任务：成对样本排序、带噪标量标注回归、锚点校准，适配异构监督源。
### 关键结果
在无对应关系、生成-生成样本对等现有方法性能退化严重的场景下，性能显著优于SOTA；与人类判断相关性优异，打分稳定落在[0,1]区间；未用通用偏好标注训练，在人类偏好基准上仍具备竞争力
