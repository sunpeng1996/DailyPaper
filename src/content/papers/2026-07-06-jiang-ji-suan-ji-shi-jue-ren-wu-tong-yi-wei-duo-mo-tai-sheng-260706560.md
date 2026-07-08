---
title: Vision as Unified Multimodal Generation
title_zh: 将计算机视觉任务统一为多模态生成范式
authors:
- Xiaoyang Han
- Jianhua Li
- Kewang Deng
- Zukai Chen
- Xuanke Shi
- Sihan Wang
- Boxuan Li
- Linyan Wang
- Siyi Xie
- Xin You
affiliations:
- SenseTime Research
- Nanyang Technological University
- The Chinese University of Hong Kong
- Peking University
- Shanghai Jiao Tong University
arxiv_id: '2607.06560'
url: https://arxiv.org/abs/2607.06560
pdf_url: https://arxiv.org/pdf/2607.06560
published: '2026-07-06'
collected: '2026-07-08'
category: Multimodal
direction: 多模态大模型 · 统一视觉任务范式
tags:
- Multimodal LLM
- Computer Vision
- Instruction Tuning
- Unified Foundation Model
- Visual Understanding
one_liner: 提出无需任务专属架构的统一多模态视觉模型SenseNova-Vision，性能匹配各细分视觉任务的专用SOTA系统
practical_value: '- 可复用「异构任务转统一生成空间样本」的思路，将多模态推荐的图文生成、多模态召回等子任务统一到同一基座训练，无需单独改造架构

  - 多模态电商Agent可直接接入开源SenseNova-Vision，一站式完成商品检测、OCR、属性识别、分割等视觉任务，降低多模型调度成本

  - 微调多模态基座时可复用「混入通用能力辅助数据」的技巧，避免垂域微调后通用能力灾难性遗忘，兼顾任务效果与通用交互能力'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
传统计算机视觉不同细分任务需独立设计专属架构与预测头，复用性差、落地成本高，难以无缝整合到通用基础模型中。
### 方法关键点
1. 提出统一范式：将所有异构视觉任务映射到多模态模型原生的文本、图像生成空间，仅通过自然语言指令+可选视觉提示指定任务、目标区域、解码规则，输出对应文本、图像或图文混合结果
2. 构建SenseNova-Vision Corpus，将各类CV标注统一转换为兼容生成空间的指令-响应对，覆盖文本、图像、混合输出三类目标
3. 基于现成预训练多模态基座微调，无额外任务专属模块，训练时混入辅助多模态数据保留通用能力
### 关键结果
单模型覆盖检测、OCR、分割、深度估计等10+视觉任务，在结构化感知、密集几何预测、多视图几何等任务上性能与专用SOTA持平；普通检测F1@mIoU达56.6%，密集检测F1@mIoU达52.9%
