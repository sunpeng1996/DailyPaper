---
title: 'SGN: A Similarity-based Generative Network for Data Generation under Distribution
  Shift'
title_zh: SGN：分布偏移场景下基于相似度的生成式数据增强框架
authors:
- Jiaqi Zhu
- Xincheng Chen
- Yuncheng Wu
- Zhaojing Luo
- Beng Chin Ooi
affiliations:
- National University of Singapore
- Renmin University of China
- Beijing Institute of Technology
- Zhejiang University
arxiv_id: '2607.18072'
url: https://arxiv.org/abs/2607.18072
pdf_url: https://arxiv.org/pdf/2607.18072
published: '2026-07-20'
collected: '2026-07-22'
category: Training
direction: 生成式数据增强 · 分布偏移适配
tags:
- Generative Model
- Distribution Shift
- Data Augmentation
- Latent Space
- Encoder-Decoder
one_liner: 提出一次训练可跨域复用的SGN生成框架，无需参数更新即可适配分布偏移的目标域数据增强
practical_value: '- 电商跨域/新品冷启动场景可复用该架构：源域预训练生成模型，目标域仅需少量标注样本即可生成符合目标域分布的训练数据，无需微调模型，大幅降低冷启动数据成本

  - 可迁移相似度约束的隐空间构建思路：用标签诱导的pairwise相似度约束隐空间结构，保障生成样本的类别/属性一致性，适合电商场景下带属性约束的用户/商品样本生成

  - 可直接用于推荐系统新域/新品类的训练样本扩充，缓解分布偏移下小样本训练的过拟合问题，提升跨域推荐模型的泛化性'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
源域训练的生成模型输出样本与分布偏移的目标域对齐度低，无法有效支撑目标域数据增强；传统域适配方案需额外优化及域专属参数，复用性差、落地成本高。

### 方法关键点
1. 提出一次训练可跨域复用的SGN框架，适配新目标域时无需更新参数；
2. 基于编码器-解码器架构，学习标签诱导的成对相似度约束的结构化隐空间，同时保留样本重构信息；
3. 生成阶段仅需输入目标域少量带标注代表性样本，在隐空间完成编码组合后输出，既继承目标域特性又保障类别一致性；
4. 理论证明了所提相似度结构的可实现性及隐空间维度要求。

### 关键结果
在图像、表格两类公开数据集上，均验证了源到目标分布偏移场景下SGN做目标引导数据增强的效果显著优于基线方案。
