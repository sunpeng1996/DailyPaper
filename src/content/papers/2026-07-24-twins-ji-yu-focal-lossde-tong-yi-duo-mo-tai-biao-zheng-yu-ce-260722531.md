---
title: 'Twins: Learn to Predict Unified Representations with Focal Loss'
title_zh: Twins：基于Focal Loss的统一多模态表征预测学习方法
authors:
- Kaixiong Gong
- Xin Cai
- Bin Lin
- Hao Wang
- Yunlong Lin
- Mingzhe Zheng
- Bohao Li
- Jian-Wei Zhang
- Miles Yang
- Zhao Zhong
affiliations:
- The Chinese University of Hong Kong
- Tencent Hunyuan
- City University of Hong Kong
- Xiamen University
- The Chinese University of Hong Kong, Shenzhen
arxiv_id: '2607.22531'
url: https://arxiv.org/abs/2607.22531
pdf_url: https://arxiv.org/pdf/2607.22531
published: '2026-07-24'
collected: '2026-07-27'
category: Multimodal
direction: 多模态统一表征 · 生成理解对齐
tags:
- Multimodal Representation
- Focal Loss
- Diffusion Transformer
- Flow Matching
- Tokenization
one_liner: 提出通道拼接ViT与VAE特征的统一连续表征，搭配Focal回归损失解决多模态建模优化失衡
practical_value: '- 电商商品图生成、素材自动化等多模态生成场景可复用ViT+VAE通道拼接方案，不增加注意力开销的前提下同时兼顾语义理解与生成质量

  - 多任务联合建模遇到优化倾斜问题时，可借鉴Focal回归损失思路，给误差大的任务分支/特征维度加权，平衡不同分布特征的拟合效果

  - 无需依赖离散codebook的连续统一表征方案，可降低多模态RAG系统的索引存储与检索复杂度，适配电商商品图语义检索场景'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有多模态连续表征方案拆分语义理解（ViT）与生成（VAE）两套独立特征，存在隐空间不匹配问题；直接拼接两类特征用Diffusion Transformer建模时会出现优化失衡，ViT拟合效果好但VAE分布匹配度差，根源来自频率偏差、固有维度差异、条件对齐/独立不确定性三类异质性问题。
### 方法关键点
1. 提出Twins统一连续token空间，将同token网格下的ViT与VAE特征按通道拼接，序列长度不变，无额外注意力开销；
2. 适配Flow Matching任务的Focal回归目标，对VAE维度中误差大的样本加权，平衡两类特征的优化效果。
### 关键结果
ImageNet无分类器自由引导场景下，比朴素MSE损失gFID最高提升10.57；多模态理解基准表现具备竞争力，重建保真度显著提升，有效缩小了理解与生成导向表征的差距。
