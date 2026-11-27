---
title: 'Reading, Not Adapting: Unlocking Frozen Visual Knowledge for AI-Generated
  Image Detection'
title_zh: 无需适配：读取冻结视觉知识实现AI生成图像检测
authors:
- Yuncheng Guo
- Ying Dong
- Xiaodong Gu
affiliations:
- Department of Electronic Engineering, Fudan University
arxiv_id: '2611.34719'
url: https://arxiv.org/abs/2611.34719
pdf_url: https://arxiv.org/pdf/2611.34719
published: '2026-11-24'
collected: '2026-11-27'
category: Other
direction: AI生成内容检测 · 冻结基座知识读取
tags:
- AIGC Detection
- Frozen Foundation Model
- Mixture-of-Transformers
- Multi-view Fusion
- Knowledge Readout
one_liner: 提出仅3074个可训练参数的ReMoT框架，冻结视觉基座读取多视图知识实现SOTA级AI生成图像检测
practical_value: '- 冻结大基座仅新增极少量可训练参数做特征读取的思路，可迁移到电商AIGC商品图、营销素材的合规检测场景，大幅降低训练推理成本

  - RGB+小波多视图特征融合+分阶段联合注意力方案，可复用在多模态推荐的跨模态特征交互模块，提升不同模态特征互补性

  - 跨Transformer层逐步读取特征不回写的设计，可借鉴到GenRec/RAG的特征蒸馏场景，避免破坏预训练基座的泛化性'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有AI生成图像检测方案通常微调视觉基座适配任务，反而会损害模型跨未知生成器的泛化性；传统线性探针仅能利用最后一层RGB特征，多 cue 检测器又存在泛化性下降、异构特征融合难、缺乏中间层跨视图交互的问题。
### 方法关键点
提出ReMoT框架，全程冻结视觉基座，参考MoE设计从空间对齐的RGB和小波双视图读取互补知识；采用分阶段联合注意力实现可控的局部/全局跨视图交互，通过可学习融合查询跨Transformer层逐步读取互补证据且不回写参数，仅需3074个可训练参数。
### 关键结果
在8个基准测试集上平均准确率达91.2%，为所有参评方法中整体平均精度最高的方案，验证了结构化知识读取相对于基座微调的显著优势。
