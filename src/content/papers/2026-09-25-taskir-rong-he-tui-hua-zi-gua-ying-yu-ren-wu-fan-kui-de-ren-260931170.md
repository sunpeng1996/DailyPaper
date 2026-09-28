---
title: 'TaskIR: Task-Driven Image Restoration via Degradation Adaptation and Task
  Feedback'
title_zh: TaskIR：融合退化自适应与任务反馈的任务驱动图像修复框架
authors:
- Yanjie Tu
- Qingsen Yan
- Axi Niu
- Wenxuan Cai
- Tao Hu
- Wei Dong
- Haokui Zhang
affiliations:
- Northwestern Polytechnical University
- Shenzhen Research Institute of Northwestern Polytechnical University
- Xi'an University of Architecture and Technology
arxiv_id: '2609.31170'
url: https://arxiv.org/abs/2609.31170
pdf_url: https://arxiv.org/pdf/2609.31170
published: '2026-09-25'
collected: '2026-09-28'
category: Multimodal
direction: 多模态预处理 · 图像修复优化
tags:
- Image Restoration
- Degradation Adaptation
- Transformer
- Task Feedback
- Multimodal Preprocessing
one_liner: 提出双阶段自适应图像修复框架，适配多类退化同时提升修复质量与下游任务性能
practical_value: '- 电商商品图/UGC内容图预处理可复用双阶段架构：先基于退化特征做自适应修复，再结合下游搜推任务的特征反馈做选择性修正，避免过度修复影响语义特征

  - 可借鉴Degradation Representation Module(DRM)设计，自动识别不同场景下的图像退化类型，动态调整修复策略，无需为单类退化单独训练模型

  - 多模态推荐/搜推的图像特征预处理场景，可复用Selective Task Feedback Refinement(STFR)思路，仅修正会影响下游任务语义识别的局部特征，降低计算开销'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有任务驱动图像修复方法大多仅适配单种退化类型，无法应对真实场景中模糊、低光、噪点等多样化退化，修复不充分残留的伪影会破坏对象边界、语义线索，拉低下游视觉任务性能。
### 方法关键点
提出双阶段TaskIR统一框架：
1. 第一阶段通过Degradation Representation Module(DRM)提取退化表征，驱动Degradation-Guided Transformer Block(DGTB)动态调整特征变换，实现自适应修复
2. 第二阶段先通过Task-to-Restoration Feedback Generation(TRFG)模块建模当前修复结果与任务要求的表征差异，将异构任务特征转换为修复反馈，再通过Selective Task Feedback Refinement(STFR)模块评估反馈相关性，仅选择性优化未达标区域的修复特征，避免干扰已修复完好的内容
### 关键结果数字
在多类退化场景、多类下游视觉任务上，修复质量与下游任务表现均达到SOTA水平
