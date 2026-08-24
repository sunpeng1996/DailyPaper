---
title: 'UniSpace: Unified Visual Representation and Scalable Multimodal Modeling'
title_zh: UniSpace：统一视觉表示与可扩展多模态建模
authors:
- Jinbo Yan
- Limeng Qiao
- Jie Qin
- Junyan He
- Feize Wu
- Guanglu Wan
affiliations:
- Meituan
arxiv_id: '2608.08676'
url: https://arxiv.org/abs/2608.08676
pdf_url: https://arxiv.org/pdf/2608.08676
published: '2026-08-08'
collected: '2026-08-24'
category: Multimodal
direction: 多模态统一表示 · 预训练ViT优化
tags:
- ViT
- MoE
- Multimodal Representation
- Image Generation
- Image Editing
one_liner: 通过Patch重参数化改造预训练ViT，构建8B MoE多模态模型UniSpace，实现统一的多模态理解、生成与编辑
practical_value: '- 电商商品图生成/编辑场景可复用Patch Reparameterization方案，无需单独VAE路径，降低多模态生成模型部署成本

  - 跨模态商品检索、商品理解场景可直接复用UniSpace的统一视觉表示，同时兼顾语义理解与细粒度视觉特征提取需求

  - 多模态大模型迭代可参考8B MoE架构选型，平衡多任务性能与推理成本'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
当前语义视觉编码器的最终token会丢弃细粒度视觉细节，像素重建效果差，无法同时支撑多模态理解、图像生成/编辑等对重建能力要求不同的任务。
### 方法关键点
1. 证明冻结的语义ViT Transformer块本身具备保留视觉细节的能力，性能瓶颈来自原始patch参数化过度偏向语义抽象；
2. 提出Patch Reparameterization，保留原语义通路的同时新增重建感知的patch embedding，为冻结ViT块注入细粒度视觉信息；
3. 基于该统一表示搭建8B MoE架构UniSpace，无需独立VAE通路即可在同一空间完成理解、生成、编辑全链路任务。
### 关键结果数字
在ImgEdit、DPG、OneIG-Bench中英文榜单上均超越SenseNova-U1、Bagel等基线，其中OneIG-Bench(CN)得分达4.28，较基线最高提升1.07分。
