---
title: Can Vision-Language Models Reason about AI Edits in Images?
title_zh: 视觉语言模型能否对图像中的AI编辑进行推理？
authors:
- Darsha Udayanga
- Pin-Yu Chen
- Payel Das
- Qiang Ji
affiliations:
- Rensselaer Polytechnic Institute
- IBM Research
arxiv_id: '2607.28464'
url: https://arxiv.org/abs/2607.28464
pdf_url: https://arxiv.org/pdf/2607.28464
published: '2026-07-30'
collected: '2026-08-01'
category: Reasoning
direction: 多模态大模型 · AIGC篡改检测推理
tags:
- VLM
- GRPO
- Reinforcement Learning
- AIGC Detection
- Multimodal Reasoning
one_liner: 基于GRPO强化学习训练VLM，弱监督下实现AI篡改图像的推理、检测与像素级定位
practical_value: '- 电商场景AIGC商品图合规校验（如虚假P图识别）可复用GRPO弱监督训练VLM的思路，无需标注大量推理过程数据，大幅降低标注成本

  - 多模态内容理解任务可参考「VLM输出推理链引导下游轻量分割/分类模型」的架构，平衡大模型推理能力与线上部署性能开销

  - 多步骤联合任务（如识别+定位）的评估可借鉴eff-IoU统一指标的设计思路，解决多指标分开评估难对齐的问题'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
AI生成篡改的图像识别难度持续提升，传统篡改检测分类器无解释性、泛化能力弱；现有基于VLM的方案依赖带推理标注的监督微调，标注成本高，未充分利用VLM固有推理能力。
### 方法关键点
1. 采用GRPO强化学习框架训练VLM，仅用准确率、格式两类简单reward，无需显式推理过程标注，引导VLM先输出结构化推理链再给出篡改判定结果
2. 用VLM输出的推理结果引导轻量分割模型，生成像素级篡改定位掩码
3. 提出eff-IoU统一指标，联合评估检测与定位效果
### 关键结果
在多套公开图像篡改数据集上，性能与SOTA伪造图像检测器相当，所需监督信号强度大幅降低
