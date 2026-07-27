---
title: 'dRAE: Representation Autoencoder with Hyper-Spherical Codes'
title_zh: dRAE：采用超球面编码的表征自编码器
authors:
- Tianren Ma
- Lin Long
- Chuyan Chen
- Mu Zhang
- Junbo Zhao
- Tong Zhang
- Qixiang Ye
affiliations:
- University of Chinese Academy of Sciences
- Zhejiang University
- Peking University
- Ant Group
arxiv_id: '2607.22148'
url: https://arxiv.org/abs/2607.22148
pdf_url: https://arxiv.org/pdf/2607.22148
published: '2026-07-24'
collected: '2026-07-27'
category: Multimodal
direction: 多模态表征 · 高维特征离散量化
tags:
- Vector Quantization
- Codebook Collapse
- Visual Tokenizer
- Multimodal
- Autoencoder
one_liner: 提出超球面量化HSQ解决高维表征离散化码本坍塌，兼顾语义保真与重建性能
practical_value: '- 高维用户/物品表征离散化可复用HSQ思路：用余弦相似度做码本路由替代欧氏距离，解决大码本下的坍塌问题，提升Semantic
  ID的语义区分度

  - 量化损失函数设计可迁移：码本更新用角度损失保证语义对齐，保留欧氏距离的commitment损失保留特征幅值信息，平衡语义保真与下游任务性能

  - 多模态电商内容（图文/短视频）的统一tokenizer可参考dRAE架构：无需复杂多阶段训练，单阶段端到端训练即可同时支撑内容理解与生成任务，降低多模态系统维护成本'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
现有高维视觉表征离散化方法（如VQ）存在严重码本坍塌问题，码本规模超过16K后性能不再提升，无法支撑统一多模态理解与生成任务需求；根源是欧氏距离量化目标与预训练表征空间的各向异性几何结构不匹配，特征幅值主导码本分配而非语义方向，同时直接丢弃幅值又会大幅降低重建性能。

### 方法关键点
- 超球面量化（HSQ）：码本路由阶段用余弦相似度替代欧氏距离，仅基于特征方向（语义信息）分配码本，避免幅值干扰
- 损失解耦设计：码本更新采用角度损失约束语义对齐，commitment损失保留欧氏距离约束，兼顾特征幅值信息保证重建性能
- dRAE架构：采用冻结预训练视觉基础模型作为编码器，ViT作为解码器，单阶段端到端训练，无需额外抗坍塌trick或课程学习

### 关键实验
在ImageNet、多模态理解基准、文本生成图像基准上对比VQRAE等基线：1）码本规模最高支持131072，码本利用率达100%，无坍塌问题；2）131K码本下图像重建rFID低至0.42，PSNR达24.52，优于同参数VQRAE；3）多模态理解任务MMBench得分达81.5，超出VQRAE13.9分；4）文本生成图像仅用12M训练数据，DPG-Bench得分达80.58，接近用超1B数据训练的DALL-E 3的83.5。

> 高维预训练表征的语义信息主要存在于向量方向，量化时对齐几何结构比盲目增加抗坍塌trick更能提升码本利用率与任务性能
