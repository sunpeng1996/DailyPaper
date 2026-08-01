---
title: 'MixFrag: Fragility-Guided Mixed-Precision Post-Training Quantization for Vision
  Transformers'
title_zh: MixFrag：面向视觉Transformer的脆弱性引导混合精度训练后量化框架
authors:
- Md. Mehrab Hossain Opi
- Robiul Islam Ryad
- Md. Umar Faruk
affiliations:
- Khulna University of Engineering & Technology (KUET)
arxiv_id: '2607.28589'
url: https://arxiv.org/abs/2607.28589
pdf_url: https://arxiv.org/pdf/2607.28589
published: '2026-07-30'
collected: '2026-08-01'
category: Training
direction: Transformer 混合精度训练后量化优化
tags:
- PTQ
- VisionTransformer
- MixedPrecision
- Quantization
- KL-divergence
- MCKP
one_liner: 基于组件量化脆弱性评估与多选择背包比特分配，实现ViT高效混合精度训练后量化
practical_value: '- 多模态推荐/搜索场景的ViT类视觉特征提取模型部署，可直接复用MixFrag混合精度PTQ方案，在显存/算力约束下降低推理延迟

  - 组件级量化敏感度评估思路可迁移到LLM/推荐大模型量化工作，用小校准集测KL散度判断各层量化损失，避免一刀切的统一比特分配

  - 比特分配阶段的多选择背包问题（MCKP）建模可复用，在给定算力/延迟预算下自适应分配各模块精度，平衡效果和推理性能'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有ViT训练后量化（PTQ）普遍采用全局统一比特位宽，忽略不同组件对量化的敏感度异质性，导致精度分配效率低，难以在资源约束下兼顾推理性能和任务效果。
### 方法关键点
1. 量化脆弱性指标通过小校准集计算全精度与单组件量化输出的KL散度，评估各Transformer组件的量化敏感度
2. 将比特分配建模为多选择背包问题（MCKP），在目标比特预算约束下实现层级自适应精度分配
### 关键结果
- ImageNet-1K分类任务上多个ViT架构均取得有竞争力的混合精度量化效果
- COCO检测/分割任务上领先现有SOTA混合精度PTQ方法，MP3/MP3场景下最高提升9.6 AP
- 脆弱性指标与最优比特分配高度相关，验证了方案合理性
