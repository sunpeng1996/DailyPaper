---
title: 'Vera: Identity-Faithful Human Subject-to-Video Generation'
title_zh: Vera：保身份一致性的人物主体到视频生成框架
authors:
- Yulong Xu
- Xinyue Liu
- Shujuan Li
- huafeng shi
- Yan Zhou
- Jiwen Liu
- Xintao Wang
- Yu Shen Liu
- Huaibo Huang
affiliations:
- Kuaishou Technology
- Institute of Automation, Chinese Academy of Sciences
- Tsinghua University
arxiv_id: '2607.20247'
url: https://arxiv.org/abs/2607.20247
pdf_url: https://arxiv.org/pdf/2607.20247
published: '2026-07-22'
collected: '2026-07-23'
category: Multimodal
direction: 多模态生成 · 人物主体视频生成
tags:
- Video Generation
- Diffusion Transformer
- Identity Consistency
- Multimodal Generation
one_liner: 提出面向单/多人的保身份主体到视频生成框架Vera，配套数据集与两个身份优化模块
practical_value: '- 电商数字人广告、商品展示短视频生成场景可复用IFMS+RALA模块，解决跨帧身份漂移、多人同框身份混淆问题

  - 搭建行业专属主体生成数据集时可参考跨clip人物级检索的对齐逻辑，低成本构造百万级身份对齐的图像-视频对

  - 数字人广告成片生产流水线可集成Vera框架，大幅降低后期身份修正的人力成本，提升内容生产效率'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有主体到视频（S2V）生成方案的通用主体一致性无法满足以人为中心的生成需求，视频全局一致但身份关键细节跨帧/跨姿态漂移，多人场景下身份-角色绑定错误、属性互换、过度照搬参考图特征等问题突出，无法适配数字人、广告内容生成等落地场景。
### 方法关键点
1. 构造百万级身份对齐的人物图像-视频数据集，通过跨clip人物级检索提供明确的身份对应关系与多样化参考
2. 提出Identity-Focal Masked Supervision（IFMS）：通过空间聚焦的监督强化身份感知学习，减少无关伪影干扰
3. 提出Reference-Aware Layer-wise Attention（RALA）：在DiT backbone中调控视频token与参考身份特征的交互，保留稳定身份锚点，优化分层身份读出
### 关键结果
实验验证Vera可提升人物身份一致性、多人主体绑定准确率、动作自然度，显著降低身份混淆、过度复制参考图像的问题。
