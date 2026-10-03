---
title: Does Native 3D Texture Generation Necessarily Require 3D Assets for Training?
title_zh: 原生3D纹理生成是否必须使用3D资产进行训练？
authors:
- Jiangshan Wang
- Zeqiang Lai
- Jiayi Guo
- Xin Yang
- Xin Huang
- Jiarui Chen
- Ziheng Ouyang
- Chunchao Guo
- Xiangyu Yue
affiliations:
- MMLab, CUHK
- Tencent Hunyuan
- Tsinghua University
- Fudan University
- Nankai University
arxiv_id: '2609.34621'
url: https://arxiv.org/abs/2609.34621
pdf_url: https://arxiv.org/pdf/2609.34621
published: '2026-09-27'
collected: '2026-10-03'
category: Other
direction: 3D纹理生成 · 无3D资产训练范式
tags:
- 3D_Texture_Generation
- 2D_to_3D
- Zero_3D_Asset_Training
- VAE
- DiT
one_liner: 提出无需3D资产、仅用2D图像训练的高保真原生3D纹理生成框架Tex-Zero
practical_value: '- 电商3D商品/虚拟场馆素材生产可直接复用该思路，仅用现有2D商品图/场景图生成高保真3D纹理，无需采购昂贵的3D资产，大幅降低3D内容建模成本

  - 数据构造范式可迁移：保留任务核心信息、人工构造辅助信息的思路，可复用在各类多模态生成任务中降低训练数据获取成本

  - 条件输入与训练数据的表征gap对齐手段，可迁移到生成式推荐、多模态内容生成等跨域训练场景提升效果'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
原生3D纹理生成此前普遍依赖大规模高质量3D资产训练，3D资产采集成本高、获取难度大，严重制约技术落地规模化。
### 方法关键点
1. 核心观察：3D纹理训练仅需高保真细粒度颜色信息，几何信息可人工构造，无需从真实3D资产获取；
2. 将2D图像转为3D空间平面，通过patch级随机旋转聚合构造复杂几何结构，把海量2D图像转化为可用3D训练样本；
3. 先后训练仅使用构造样本的Tex-Zero VAE与Tex-Zero DiT，将多视角条件2D图同样转为3D平面并经VAE编码，缩小表征gap提升生成质量。
### 关键结果
仅用2D图像训练的Tex-Zero可生成带细粒度细节的高保真3D纹理，训练阶段从未见过真实3D资产也能高质量重建真实3D资产。
