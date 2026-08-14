---
title: 'V-RAE: Rethinking Video Latent Spaces for Generation'
title_zh: V-RAE：面向视频生成的视频隐空间重构方法
authors:
- Minghui Guo
- Shengqiong Wu
- Hao Fei
affiliations:
- National University of Singapore
- University of Oxford
arxiv_id: '2608.13556'
url: https://arxiv.org/abs/2608.13556
pdf_url: https://arxiv.org/pdf/2608.13556
published: '2026-08-13'
collected: '2026-08-14'
category: Multimodal
direction: 多模态视频生成 · 隐空间自编码器优化
tags:
- Video Generation
- Autoencoder
- Latent Space
- Foundation Model
- Temporal Modeling
one_liner: 基于冻结视觉基础模型表征构建视频自编码器，大幅提升视频生成质量与收敛速度
practical_value: '- 电商短视频广告物料生成场景可复用「冻结视觉大模型+轻量时序池化」架构，在保留语义的前提下压缩视频特征，降低生成模型训练成本

  - 短视频生成效果评估可引入论文提出的tFVD时序一致性指标，相比单纯重建质量指标更能准确衡量生成内容的下游可用性

  - 多模态推荐的表征建模可参考「不追求像素级重建最优，优先保留高维语义」的思路，提升跨模态召回/排序的语义匹配精度'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有视频自编码器的隐空间主要面向像素级重建优化，高维语义组织能力弱，并非生成建模的最优选择，限制了下游生成任务的性能与效率。

### 方法关键点
提出V-RAE视频表征自编码器，基于冻结视觉基础模型的表征构建适配生成任务的紧凑隐空间；引入轻量时序池化模块去除时序冗余同时保留语义结构，搭配视频解码器从压缩特征中重建连续运动；提出tFVD时序一致性诊断指标，更可靠地衡量隐空间的下游生成效用。

### 关键结果
K600数据集上rFVD达2.13，优于所有参评的大规模预训练视频VAE；UCF101、K600数据集上gFVD分别达117.86、19.16，收敛速度最高提升6倍；隐空间保留的语义信息远高于传统视频tokenizer，Cityscapes数据集上的视频预测效果优于Wan 2.2 VAE。
