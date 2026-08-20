---
title: Learning-State-Aware Dynamic Generative Data Augmentation on Small-Scale Datasets
title_zh: 小样本数据集下感知学习状态的动态生成式数据增强方法
authors:
- Ting Xiang
- Chenxi Deng
- Jinhui Zhao
- Bingting Jiang
- Ke Zhang
- Changjian Chen
- Zhuo Tang
affiliations:
- Hunan University
arxiv_id: '2608.18907'
url: https://arxiv.org/abs/2608.18907
pdf_url: https://arxiv.org/pdf/2608.18907
published: '2026-08-19'
collected: '2026-08-20'
category: Training
direction: 小样本训练 · 生成式数据增强
tags:
- Data Augmentation
- Diffusion Model
- Few-shot Learning
- Dynamic Augmentation
- Image Classification
one_liner: 提出感知样本学习状态的动态生成式数据增强方法，解耦区域增强平衡生成多样性与类别语义
practical_value: '- 电商长尾类目商品识别、小众用户兴趣建模等小样本场景，可复用「基于单样本损失及损失下降率判定学习状态、动态匹配增强强度」的策略，避免无效增强。

  - 生成式数据增强场景可借鉴「解耦核心语义区域/无关区域分别处理」的思路，比如生成电商商品素材时保留商品核心特征不变、仅对背景等无关区域做多样化生成，兼顾多样性和语义准确性。

  - 下游训练任务与生成增强模块联动的框架可迁移到推荐系统小流量场景样本扩充，基于模型当前学习效果动态调整生成样本的分布，提升训练效率。'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
小样本图像分类受训练数据稀缺限制，现有生成式数据增强（GDA）普遍存在两大问题：一是策略与下游任务无关，无法匹配模型实际训练需求；二是动态增强方法难以精准控制单样本增强强度，无法平衡生成多样性与类别语义一致性，性能提升有限。
### 方法关键点
1. 为每个训练样本构建基于当前损失、损失下降率的学习状态表征，映射得到样本专属的增强强度，实现按需增强；
2. 提出解耦增强与扩散融合策略：对类别相关核心区域做强度可控的变换，对类别无关区域生成多样化内容，逐步融合两类区域，兼顾多样性与语义保真。
### 关键结果
在9个公开数据集上验证，相比现有SOTA动态GDA方法，6个自然图像数据集平均分类精度提升4.5%，3个医学图像数据集平均精度提升2.5%。
