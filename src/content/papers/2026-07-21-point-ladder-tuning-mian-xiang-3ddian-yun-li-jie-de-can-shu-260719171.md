---
title: 'Point Ladder Tuning: Parameter-Efficient Hierarchical Adaptation for 3D Point
  Cloud Understanding'
title_zh: Point Ladder Tuning：面向3D点云理解的参数高效分层适配方法
authors:
- Junlin Chang
- Longhao Zou
- Rui Li
affiliations:
- Beihang University
- Pengcheng Laboratory
arxiv_id: '2607.19171'
url: https://arxiv.org/abs/2607.19171
pdf_url: https://arxiv.org/pdf/2607.19171
published: '2026-07-21'
collected: '2026-07-23'
category: Other
direction: 3D点云理解 · 参数高效微调
tags:
- PEFT
- 3D Point Cloud
- Hierarchical Adaptation
- Dynamic Prompt
- Parameter Efficient Training
one_liner: 提出感知局部性的PEFT框架PLT，仅用极低可训练参数超越3D点云理解现有微调基线
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
预训练3D点云backbone全量微调计算与内存开销极高；现有PEFT方法仅作用于下采样后的粗粒度全局token，无法恢复不可逆丢失的多尺度局部几何信息，适配效果存在瓶颈。
### 方法关键点
提出locality-aware PEFT框架PLT，冻结backbone前提下做分层实例级适配：1）Hierarchical Ladder Network直接从原始点构建多分辨率局部特征金字塔；2）Local-Global Fusion对齐融合局部金字塔与backbone中间层语义；3）Dynamic Prompt Generator生成实例感知多尺度prompt调控冻结backbone；稠密预测任务新增轻量分割头上采样融合特征优化细结构。
### 关键结果
分类任务仅用2.71%可训练参数达SOTA，稠密预测用7.69%参数达SOTA，适配PointGPT-L大模型仅需0.36%可训练参数，性能全面优于现有PEFT基线
