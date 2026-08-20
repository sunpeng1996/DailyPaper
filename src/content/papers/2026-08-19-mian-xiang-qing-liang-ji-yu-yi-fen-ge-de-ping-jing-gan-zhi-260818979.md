---
title: 'When Simplicity Wins: Bottleneck-Aware Context Modeling for Lightweight Semantic
  Segmentation'
title_zh: 面向轻量级语义分割的瓶颈感知上下文建模框架SiConMo
authors:
- Mian Muhammad Naeem Abid
- Nancy Mehta
- Zongwei Wu
- Radu Timofte
affiliations:
- University of Würzburg, Germany
arxiv_id: '2608.18979'
url: https://arxiv.org/abs/2608.18979
pdf_url: https://arxiv.org/pdf/2608.18979
published: '2026-08-19'
collected: '2026-08-20'
category: Other
direction: 轻量计算机视觉 · 语义分割
tags:
- Lightweight Semantic Segmentation
- Vision Transformer
- CNN
- Context Modeling
- Efficiency Optimization
one_liner: 提出轻量语义分割框架SiConMo，极低计算预算下实现精度与效率的SOTA权衡
practical_value: '- 低算力业务场景（端侧推荐、端侧Query补全等）可借鉴核心设计思路：优先优化信息聚合瓶颈层而非全链路架构，大幅降低算力消耗

  - 多尺度特征融合场景可复用Token金字塔提取+特征融合模块设计，平衡局部精细特征与全局语义一致性

  - 资源受限部署场景可参考「局部卷积+分支Transformer」混合架构，平衡模型性能与推理效率'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
高分辨率图像语义分割需平衡精度、效率、扩展性，现有工作多聚焦编码器设计，忽略了上下文聚合、信息流传递的核心瓶颈阶段；且CNN长程依赖建模能力弱，ViT全局建模算力成本过高，低计算预算下的最优平衡方案缺失。
### 方法关键点
设计SiConMo轻量框架，核心设计原则为：极低计算预算下，瓶颈层是融合局部与全局上下文的最高效阶段；包含三个核心组件：Token金字塔提取模块生成层次化多尺度表征，Transformer分支深度卷积块实现瓶颈感知上下文建模，特征融合模块保留空间结构同时增强语义一致性，提供RGB-only与GME增强两个版本。
### 关键结果
在ADE20K、PASCAL Context、Cityscapes、COCO-Stuff 4个公开数据集上，实现轻量级语义分割赛道SOTA的精度-效率权衡，同等GFLOPs下精度显著优于同类方案。
