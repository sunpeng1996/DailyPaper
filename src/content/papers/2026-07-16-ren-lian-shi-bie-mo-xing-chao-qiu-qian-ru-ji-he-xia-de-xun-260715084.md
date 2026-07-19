---
title: Quantifying Training Membership Information in the Hyperspherical Embedding
  Geometry of Face Recognition Models
title_zh: 人脸识别模型超球嵌入几何下的训练成员信息量化
authors:
- Ünsal Öztürk
- Sébastien Marcel
affiliations:
- Idiap Research Institute
- Université de Lausanne (UNIL)
arxiv_id: '2607.15084'
url: https://arxiv.org/abs/2607.15084
pdf_url: https://arxiv.org/pdf/2607.15084
published: '2026-07-16'
collected: '2026-07-19'
category: Other
direction: 人脸识别 · 成员推断隐私分析
tags:
- FaceRecognition
- MembershipInference
- EmbeddingGeometry
- PrivacyAnalysis
- ModelSecurity
one_liner: 基于180组人脸识别模型实验量化训练成员与非成员嵌入几何差异及各训练因素影响权重
practical_value: '- 可复用超球嵌入簇几何统计特征，用于检测推荐系统用户/物品嵌入是否泄露训练集成员隐私

  - 需降低训练集隐私泄露风险时，优先扩充训练ID规模（而非更换backbone/损失函数），可单调降低成员识别信号

  - 做隐私泄露评估时需优先使用同域held-out数据，跨域基准会放大成员信号导致高估泄露风险'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
人脸识别模型通过角间隔损失将训练身份的嵌入在单位超球上聚类，仅作用于训练身份的损失会导致非训练身份嵌入簇的几何特性存在差异，该差异的量化方法及影响因素尚不明确，直接关系到训练数据的隐私泄露风险。
### 方法关键点
基于因子控制实验训练180组不同配置的IResNet人脸识别模型，覆盖backbone规模、损失头、训练时长、训练身份数4类核心变量，从簇几何维度提取4种统计特征，在9个基准上评估成员/非成员的可分性。
### 关键结果数字
训练身份数对成员/非成员可分性的影响远高于backbone和损失头；同域基准下，训练身份数越多，成员识别信号单调下降；跨域基准会显著高估成员信号强度；4种特征融合的分类器相比最优单特征可挖掘更多隐藏的成员信息
