---
title: 'Toward Reliable RGB-D Semantic Segmentation: Handling Missing Modalities via
  Condition Dropout'
title_zh: 面向可靠RGB-D语义分割：基于条件Dropout解决模态缺失问题
authors:
- Xuchen Zhu
- Yajuan Wei
- Shuang Hao
- Jiwei Jiang
- Guanxiang Mao
- Fang Ren
affiliations:
- Xi'an University of Posts & Telecommunications
- Xi'an Jiaotong University
- Huazhong University of Science and Technology
- Beijing University of Posts and Telecommunications
arxiv_id: '2607.20326'
url: https://arxiv.org/abs/2607.20326
pdf_url: https://arxiv.org/pdf/2607.20326
published: '2026-07-22'
collected: '2026-07-23'
category: Other
direction: 多模态语义分割 · 模态缺失鲁棒性优化
tags:
- Semantic Segmentation
- Modality Robustness
- Dropout
- Multimodal
- Continued Training
one_liner: 提出条件Dropout（ConD）续训范式，提升RGB-D分割模型模态缺失场景鲁棒性同时保留全模态精度
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有RGB-D语义分割模型默认RGB、深度双模态始终可用，但实际场景中传感器故障、遮挡常导致单模态缺失，仅在全模态数据上训练的模型无法利用剩余有效模态信息，性能会出现严重下降。

### 方法关键点
提出Condition Dropout（ConD）轻量续训范式：1. 基于已预训练的全模态RGB-D模型，冻结原有编码器参数；2. 第二阶段随机模拟全模态、缺RGB、缺深度三种输入场景，新增零初始化特征注入的复制编码器单独训练，在优化鲁棒性的同时不损失原有全模态精度。

### 关键结果
在NYU-Depth V2、SUN RGB-D公开数据集上验证，ConD可大幅提升模态缺失场景下的分割性能，同时全模态输入时的分割精度还有小幅正向增益
