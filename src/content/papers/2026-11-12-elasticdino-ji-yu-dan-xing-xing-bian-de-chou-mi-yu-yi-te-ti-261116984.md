---
title: 'ElasticDino: Dense Semantic Features Using Elastic Deformations'
title_zh: ElasticDino：基于弹性形变的稠密语义特征提取方法
authors:
- Ulysse Mizrahi
- Sean Zaretzky
- Dov Danon
- Amit H. Bermano
affiliations:
- Tel Aviv University
arxiv_id: '2611.16984'
url: https://arxiv.org/abs/2611.16984
pdf_url: https://arxiv.org/pdf/2611.16984
published: '2026-11-12'
collected: '2026-11-14'
category: Multimodal
direction: 多模态视觉特征 · 轻量适配器优化
tags:
- ViT
- Adapter
- Dense Feature
- Semantic Extraction
- Deformation
one_liner: 提出轻量适配器ElasticDino，消除ViT空间伪影，高效生成高分辨率像素对齐语义特征
practical_value: '- 电商多模态搜推场景可直接将ElasticDino接入现有DINOv2等预训练ViT backbone，无需重训大模型即可获得像素对齐的高分辨率商品图特征，用于商品细粒度属性识别、同款匹配、前景分割等任务，降本提效

  - 跨通道伪影一致性校正、空间形变避免平滑偏差的思路，可迁移到文本/多模态特征上采样任务，提升细粒度特征质量

  - 无真值场景下用下游多任务线性头引导通用特征训练的范式，适合业务缺标注的场景，避免任务特定语义泄漏，方便多任务复用同一份特征'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
ViT自注意力的二次复杂度严重限制输出特征分辨率，且会引入空间伪影，现有上采样方法普遍存在平滑偏差，无法保留尖锐语义，难以适配语义分割、深度估计等稠密预测任务。
### 方法关键点
1. 核心观察到ViT输出的空间伪影在通道维度存在一致性，基于空间形变设计轻量适配器架构，无额外自注意力开销，可高效生成像素对齐的高分辨率特征图
2. 无特征真值情况下，采用语义分割、深度估计等多个下游稠密任务的线性预测头引导形变过程，不会向通用特征注入任务特定语义，保证特征通用性
3. 基于形变的上采样方式可严格保留语义锐度，彻底避免传统上采样的平滑偏差问题
### 关键结果
在多个主流稠密视觉任务基准上精度超越现有SOTA方法，同时计算性能更优
