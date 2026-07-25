---
title: 'DINOde: Continuous Vision-Text Alignment for Open-Vocabulary Semantic Segmentation'
title_zh: DINOde：面向开放词汇语义分割的连续视觉-文本对齐方法
authors:
- Sung-Hoon Yoon
- Hoyong Kwon
- Changgyoon Oh
- Kuk-Jin Yoon
affiliations:
- Multimodal Intelligence and Perception Lab., DGIST, Republic of Korea
- Visual Intelligence Lab., KAIST, Republic of Korea
arxiv_id: '2607.21371'
url: https://arxiv.org/abs/2607.21371
pdf_url: https://arxiv.org/pdf/2607.21371
published: '2026-07-23'
collected: '2026-07-25'
category: Multimodal
direction: 多模态对齐 · 开放词汇语义分割
tags:
- Multimodal Alignment
- Open-Vocabulary Segmentation
- ODE
- DINOv3
- CLIP
one_liner: 提出基于ODE的DINOde框架，连续对齐CLIP文本嵌入与DINO视觉流形，实现SOTA开放词汇语义分割
practical_value: '- 连续ODE轨迹优化的跨模态对齐方法可迁移到电商图文检索、多模态商品召回场景，替代传统离散MLP投影，避免特征流形纠缠，提升匹配准确率

  - Velocity Tangent Projection约束速度场到切空间的trick，可复用在多模态特征对齐任务中，保留特征空间超球面几何性质，提升跨模态检索/匹配的鲁棒性

  - 语义文本流+全局上下文流的双模块互补优化架构，可用于多模态推荐的特征对齐层，同时优化侧文本特征与主内容图像全局表征，降低跨模态gap'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
开放词汇语义分割（OVSS）依赖文本语义实现预定义类别外的物体分割，自监督DINOv3可输出强结构化视觉表征，但原生缺乏文本对齐能力，无法直接落地OVSS；传统离散MLP投影对齐易引发特征流形纠缠，鲁棒性不足。

### 方法关键点
- 基于ODE构建连续对齐框架，将跨模态对齐过程建模为连续演化轨迹，规避离散投影的流形纠缠问题
- 双互补流模块：Semantic Text Flow（STF）通过ODE轨迹将CLIP文本嵌入向DINO视觉流形演化，Global Context Flow（GCF）逐步优化DINO CLS token承载的全局图像表征
- 新增Velocity Tangent Projection机制，将学习到的速度场约束到切空间，保留特征空间的超球面几何结构

### 关键结果
在多个OVSS基准测试集上表现稳定优于现有方案，达到SOTA性能
