---
title: Automated Background Swapping for Robustness against Spurious Backgrounds
title_zh: 面向伪背景干扰的自动背景替换图像分类鲁棒性提升方案
authors:
- Cesar Roder
- Kajetan Schweighofer
affiliations:
- Johannes Kepler University Linz, Austria
- Cognizant AI Lab, USA
arxiv_id: '2606.32018'
url: https://arxiv.org/abs/2606.32018
pdf_url: https://arxiv.org/pdf/2606.32018
published: '2026-06-30'
collected: '2026-07-01'
category: Other
direction: 图像分类鲁棒性 · 数据增广
tags:
- Data Augmentation
- Spurious Correlation
- Image Classification
- Model Robustness
- Background Inpainting
one_liner: 自动背景替换增广框架，仅需少量标注即可降低分类器对伪背景关联的依赖
practical_value: '- 电商商品图分类/识别场景可复用前景背景拆分+背景替换的增广思路，降低分类器对商品拍摄布景、场地等背景的伪关联依赖，提升跨场景识别准确率

  - 仅需数百个patch级标注即可完成增广网络训练的思路，可迁移到标注成本高的电商垂类图像识别任务，大幅降低标注开销

  - 针对训练集完全不存在反伪关联样本的场景依然有效的结论，可参考优化小样本垂类分类任务的泛化能力'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
深度神经网络分类器易学习训练数据中的非因果伪关联特征，推理阶段伪关联断裂时会出现灾难性性能下降；CV场景中大量伪关联来自图像背景，现有优化方法在训练集完全无反伪关联样本时效果不佳。

### 方法关键点
AutoBackSwap自动背景替换框架流程为：1）训练二级网络实现图像前景、背景解耦；2）通过图像补全生成完整合成背景；3）交叉组合不同前景与合成背景生成增广训练数据。仅需数百个样本的patch级标注即可完成二级网络训练，支持全量训练集自动增广。

### 关键结果
在多个存在背景伪关联的图像分类任务上性能持续优于SOTA方法；即使训练集中完全不存在打破伪关联的样本，仍可实现显著的鲁棒性提升。
