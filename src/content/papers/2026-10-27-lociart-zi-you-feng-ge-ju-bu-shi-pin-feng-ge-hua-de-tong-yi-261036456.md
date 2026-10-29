---
title: 'LociArt: A Unified Paradigm for Free-Style Local Video Stylization'
title_zh: LociArt：自由风格局部视频风格化的统一范式
authors:
- Yuxuan Chen
- Feng Xie
- Jiagao Hu
- Fuhao Li
- Zepeng Wang
- Fei Wang
- Daiguo Zhou
affiliations:
- MiLM Plus, Xiaomi Inc.
- Xi’an University of Electronic Science and Technology
arxiv_id: '2610.36456'
url: https://arxiv.org/abs/2610.36456
pdf_url: https://arxiv.org/pdf/2610.36456
published: '2026-10-27'
collected: '2026-10-29'
category: Multimodal
direction: 多模态 · 可控视频风格化
tags:
- Video Stylization
- Generative Refinement Network
- Controllable Generation
- Dataset
- Evaluation
one_liner: 提出支持多区域任意风格控制的局部视频风格化范式、数据集及评测基准
practical_value: '- 极坐标风格感知掩码设计可直接复用在电商短视频/直播特效生产场景，实现指定商品/人物区域的精准风格化，保留其他区域内容不变

  - 自动化配对数据集构建流水线（全局风格化+对象移除+抠图合成）可迁移用于业务场景自定义风格特效的训练数据集生产，大幅降低标注成本

  - SPS区域风格质量评估方案可用于短视频特效、商品展示视频生成效果的自动化评测，替代部分人工标注'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有视频风格化方案多针对全场景转换，局部艺术编辑难以同时满足精准区域-风格关联、空间控制、时序一致性三大需求，且缺乏标准化数据集与评测基准。
### 方法关键点
1. 核心GRNStyle模块基于Generative Refinement Networks (GRN)，引入极坐标风格感知掩码，将风格ID编码为选定区域内的等范数方向，实现风格与区域的精准绑定；
2. 采用表征-几何联合条件控制，融合掩码编码特征与原始掩码空间信息，兼顾时空上下文与几何控制精度；
3. 搭建自动化样本生成流水线，构建含10万对样本的LociArt-100K数据集，配套覆盖168个场景的评测基准与Style Prototype Similarity (SPS)区域风格质量评测指标。
### 关键结果
仅在单区域单风格配对数据上训练的GRNStyle，区域风格质量、空间控制效果优于现有方法，同时保持优异时序一致性，可零样本支持多区域同/异风格联合编辑。
