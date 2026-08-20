---
title: Frozen DINO Localizes Image Edits Without a Localizer
title_zh: 无需额外定位器：基于冻结DINO的图像编辑区域定位方法
authors:
- Zane Kumar
- Vishal Jain
- Bernhard Kainz
affiliations:
- St Paul’s School London
- Imperial College London
- FAU
arxiv_id: '2608.18968'
url: https://arxiv.org/abs/2608.18968
pdf_url: https://arxiv.org/pdf/2608.18968
published: '2026-08-19'
collected: '2026-08-20'
category: Multimodal
direction: 多模态 · 图像篡改区域定位
tags:
- DINO
- Image Forgery Detection
- Training-free
- Patch Token
- Localization
one_liner: 提出无训练TRAIL方法，基于冻结DINO的patch token漂移定位图像编辑区域
practical_value: '- 电商生成营销素材、商家上传商品图的篡改检测可直接复用TRAIL无训练方案，无需额外标注成本快速上线基础校验能力

  - 多模态召回排序场景中，可利用DINO 80%-94%深度层的patch token特征计算图像篡改分，过滤虚假违规商品图提升用户信任

  - 多模态特征工程优先选择保留全局上下文的提取方式，避免独立裁剪编码导致特征有效性下降'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有图像篡改检测仅能输出图像级伪造分数，无法定位编辑区域，有监督定位器标注成本高、跨场景泛化性差。
### 方法关键点
提出无训练TRAIL方案，对输入图像施加全局Haar扰动，计算扰动前后冻结DINO对应patch token的余弦漂移，直接生成编辑区域定位热力图，无需微调或额外标注。
### 关键结果
- CocoGlide测试集patch AUROC达0.903，仅比有监督Detective SAM低0.009；固定阈值Dice为0.619，逐图最优阈值下提升至0.790
- 零调整迁移到泊松图像插值场景，AUROC达0.855，泛化性优异
- 16款DINO家族模型验证最优定位特征来自归一化深度80%~94%的网络层；保留全局上下文比独立裁剪编码的AUROC高0.168
