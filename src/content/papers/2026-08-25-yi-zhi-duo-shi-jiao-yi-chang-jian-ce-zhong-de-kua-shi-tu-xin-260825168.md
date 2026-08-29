---
title: See More, Detect Less? Taming Information Leakage in Multi-View Anomaly Detection
title_zh: 抑制多视角异常检测中的跨视图信息泄露
authors:
- Shang-Fu Chen
- Kuan-Chuan Peng
- Jhih-Ciang Wu
- Wen-Huang Cheng
- Kai-Lung Hua
affiliations:
- National Taiwan University
- Mitsubishi Electric Research Laboratories (MERL)
- National Taiwan Normal University
- VinUniversity
- National Taiwan University of Science and Technology
arxiv_id: '2608.25168'
url: https://arxiv.org/abs/2608.25168
pdf_url: https://arxiv.org/pdf/2608.25168
published: '2026-08-25'
collected: '2026-08-29'
category: Other
direction: 多视角视觉异常检测 · 信息泄露抑制
tags:
- Multi-View
- Anomaly Detection
- Attention Mechanism
- Vision Foundation Model
- Information Leakage
one_liner: GLAD全局-局部注意力框架通过显式信息约束解决多视角异常检测的跨视图信息泄露问题
practical_value: '- 多源特征/多模态融合场景可复用token级门控+可学习权重的设计思路，避免核心信号被其他源的冗余/冲突信息淹没

  - 重构类任务（如生成式推荐内容生成、电商站内异常内容识别）做特征融合时，不要直接叠加残差，可采用替换原表征的方案保留任务依赖的差异gap

  - 跨源/跨视图融合模块可参考MMA的线性复杂度设计，在大流量推理场景下控制算力开销'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
基于重构的多视角异常检测任务中，朴素跨视图融合会导致正常视角的信息泄露到解码器，完美重构异常区域，抹平检测依赖的重构差，导致性能退化。
### 方法关键点
1. GLAD全局-局部注意力驱动框架首次结合视觉基础模型特征与全局+局部跨视图融合策略，显式约束流向解码器的信息量
2. 局部融合采用Multi-view Merging Attention（MMA）模块，线性复杂度为O(N)，自带可学习视角重要性权重和token级门控，支持每个视角选择性融合其他视角的细粒度信息
3. 全局融合采用Object-Guided Attention（OGA）模块，聚合所有视图的class token得到对象级统一表征，经温度缩放sigmoid门控后直接替换原patch表征（而非叠加残差），避免重构差被抵消
### 关键结果
在Real-IAD、MANTA-Tiny两个公开数据集上，GLAD在样本级、图像级、像素级全维度指标上均超过现有SOTA方法
