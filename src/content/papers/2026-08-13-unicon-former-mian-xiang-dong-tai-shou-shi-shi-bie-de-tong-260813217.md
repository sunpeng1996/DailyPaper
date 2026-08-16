---
title: 'UniCon-Former: Unified Convolution Transformer is All You Need for Hand Gesture
  Recognition'
title_zh: UniCon-Former：面向动态手势识别的统一卷积Transformer架构
authors:
- Mallika Garg
- Debashis Ghosh
- Pyari Mohan Pradhan
affiliations:
- Indian Institute of Technology Kharagpur
- Indian Institute of Technology Roorkee
arxiv_id: '2608.13217'
url: https://arxiv.org/abs/2608.13217
pdf_url: https://arxiv.org/pdf/2608.13217
published: '2026-08-13'
collected: '2026-08-16'
category: Other
direction: 计算机视觉 · 卷积Transformer融合优化
tags:
- Transformer
- CNN
- Multiscale Feature
- Lightweight Model
- Gesture Recognition
one_liner: 融合CNN局部特征与Transformer全局建模能力，提出轻量高效的动态手势识别SOTA架构
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 4
source: arxiv-cs.HC
depth: abstract
---

### 动机
CNN虽能高效提取局部特征，但受限于感受野，全局上下文建模能力弱；Transformer通过自注意力可捕捉全局依赖，但存在冗余度高、计算开销大的问题，动态手势识别任务需同时兼顾局部纹理特征与全局时空依赖，现有方案难以平衡效果与推理效率。
### 方法关键点
1. 提出统一卷积Transformer架构UniCon-Former，同时融合CNN的局部特征提取能力与Transformer的全局建模能力；
2. 每个Transformer阶段前置卷积投影层，对输入向量降维，在单阶段内构建金字塔结构，支持多尺度、高分辨率特征学习的同时降低计算资源消耗。
### 关键结果
在NVGesture、Briareo两个公开动态手势识别数据集上取得SOTA效果，相比原生Transformer参数量与MACs（乘加运算量）显著更低。
