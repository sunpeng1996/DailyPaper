---
title: 'LeVJEPA: Efficient & Scalable Video Pretraining without the Heuristics'
title_zh: LeVJEPA：无需启发式规则的高效可扩展视频预训练
authors:
- Lukas Kuhn
- Lucas Maes
- Giuseppe Serra
- Quentin Le Lidec
- Yann LeCun
- Randall Balestriero
- Florian Buettner
affiliations:
- German Cancer Research Center
- Mila
- Brown University
- New York University
- Advanced Machine Intelligence (AMI Labs)
arxiv_id: '2608.27395'
url: https://arxiv.org/abs/2608.27395
pdf_url: https://arxiv.org/pdf/2608.27395
published: '2026-08-27'
collected: '2026-08-28'
category: Training
direction: 视频自监督预训练 · 无坍塌表征约束
tags:
- Video Pretraining
- Self-supervised Learning
- JEPA
- Representation Learning
- Computational Efficiency
one_liner: 提出基于LeJEPA无坍塌目标的视频预训练框架LeVJEPA，大幅降低算力开销同时提升多场景下游精度
practical_value: '- 短视频推荐场景可复用SIGReg正则约束，替换现有自监督训练的EMA、停止梯度等复杂设计，简化预训练pipeline同时降低算力消耗

  - 多模态内容理解任务可借鉴随机token dropping策略，在降低预训练计算量的同时反而提升下游分类/召回任务精度

  - 时序视频理解场景可复用块因果注意力设计，不需要额外架构不对称约束即可学习时序表征，适合短视频流实时理解需求'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有视频自监督预训练要么依赖EMA编码器、停止梯度等架构不对称设计防表征坍塌，要么通过像素空间掩码重建规避坍塌，算力开销极高，落地门槛高。
### 方法关键点
基于LeJEPA无坍塌目标训练单编码器，架构仅保留编码器+投影器，搭配SIGReg正则从理论上保证表征不坍塌，仅需1个超参数；支持随机token dropping降低训练所需token量，可无缝适配块因果注意力学习时序表征。
### 关键结果
同等训练轮次下，预训练算力比V-JEPA 2低5.6~20.8倍，精度持平或更优；同等FLOPs下，ImageNet-1K精度领先最强视频基线7.6个点；与同算力DINOv2相比，运动相关任务精度接近翻倍，外观任务精度相当。
