---
title: 'Objects as Addresses: Instance Binding in Vision Transformer Attention'
title_zh: 《对象即地址：视觉Transformer注意力中的实例绑定机制》
authors:
- Khalil Sabri
- Guillaume-Alexandre Bilodeau
- Nicolas Saunier
- Wassim Bouachir
affiliations:
- Polytechnique Montréal
- Université TÉLUQ
arxiv_id: '2611.17240'
url: https://arxiv.org/abs/2611.17240
pdf_url: https://arxiv.org/pdf/2611.17240
published: '2026-11-12'
collected: '2026-11-14'
category: Other
direction: ViT自注意力机制 · 视觉实例绑定
tags:
- Vision Transformer
- Self-Attention
- Instance Binding
- Attention Routing
- DINOv2
one_liner: 揭示预训练ViT通过注意力路由的共享地址机制实现视觉对象实例的绑定与区分
practical_value: '- 多模态商品搜推的同实例聚合任务，可借鉴注意力地址思路，用特定头的query-key关系做实例聚类，避免同类别不同SKU被误合并

  - 多模态ViT特征优化场景，可优先选用注意力路由特征而非最终层输出做实例区分，实测FG-ARI指标提升超112%

  - 多模态Agent的视觉感知模块，可通过编辑指定注意力头的query分量快速切换关注的实例目标，无需全模型微调'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
预训练ViT已被证实具备类人的视觉对象绑定能力，但自注意力实现实例区分的底层运行机制尚未明确，传统基于最终层特征的实例聚类方法容易合并同类别不同实例。
### 方法关键点
针对8款不同架构的预训练ViT做机制拆解，对比注意力路由、token内容、value相似度、残差表示的实例区分能力，提出「注意力地址」概念：同一对象的所有patch在指定注意力头内会指向共同的注意力查询区域，相同类别不同实例会分配独立可迁移的地址。
### 关键结果
基于指定头query分量的patch分组方法在同类别实例分离任务上FG-ARI达到0.615，相比传统最终层特征聚类的0.289提升112%；编辑指定头的query分量可直接重定向注意力地址到其他实例，无需全模型调整。
