---
title: 'SiamJEPA: On the Role of Siamese Student Encoders in JEPA'
title_zh: SiamJEPA：探究联合嵌入预测架构中孪生学生编码器的作用
authors:
- Makoto Yamada
affiliations:
- Okinawa Institute of Science and Technology
arxiv_id: '2607.04044'
url: https://arxiv.org/abs/2607.04044
pdf_url: https://arxiv.org/pdf/2607.04044
published: '2026-07-03'
collected: '2026-07-09'
category: Training
direction: 自监督表征学习 · JEPA架构优化
tags:
- Self-Supervised Learning
- JEPA
- Siamese Network
- Representation Learning
- EMA Teacher
one_liner: 提出带EMA教师网络的孪生学生JEPA架构，提升低训练预算下自监督表征学习性能
practical_value: '- 电商/推荐场景做用户/商品表征自监督预训练时，可将单学生编码器替换为孪生结构加EMA教师，有限训练预算下即可获得更好的表征效果，降低训练成本

  - 孪生编码器作为正则项的思路可迁移到召回侧对比学习预训练，提升商品表征区分度，减少召回结果同质化问题

  - 训练初期收敛速度快的特性可用于快速迭代多模态商品表征模型，缩短新特征、新物料的模型上线周期'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有JEPA类自监督表征学习方法普遍采用单学生编码器，而更符合类脑表征学习逻辑的孪生学生编码器在JEPA中的作用尚未被系统探究，小训练预算下JEPA存在收敛慢、表征区分度不足的痛点。
### 方法关键点
提出SiamJEPA架构，核心为掩码孪生学生编码器搭配指数移动平均（EMA）教师网络，也可被视为类脑表征模型PhiNet的JEPA实现，孪生编码器天然作为JEPA训练目标的正则项。
### 关键结果
ImageNet线性探测任务中：训练早期收敛速度大幅提升；有限训练预算下性能稳定优于同配置单编码器JEPA变体；线性探测准确率高于需要更长训练周期的MAE，表征可分性显著提升。
