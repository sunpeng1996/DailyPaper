---
title: 'From RGB Generation to Dense Field Readout: Pixel-Space Dense Prediction with
  Text-to-Image Models'
title_zh: 从RGB生成到密集场读取：基于文生图模型的像素空间密集预测
authors:
- Zanyi Wang
- Xin Lin
- Haodong Li
- Dengyang Jiang
- Yijiang Li
- Pengtao Xie
affiliations:
- UCSD
- HKUST
arxiv_id: '2607.06553'
url: https://arxiv.org/abs/2607.06553
pdf_url: https://arxiv.org/pdf/2607.06553
published: '2026-07-07'
collected: '2026-07-09'
category: Multimodal
direction: 多模态感知 · 文生图模型复用优化
tags:
- DiT
- Text-to-Image
- Dense Prediction
- LoRA
- Multimodal Perception
one_liner: 提出ReChannel框架，复用预训练DiT空间结构，裁剪冗余模块，用极少量参数实现高效SOTA密集预测
practical_value: '- 预训练大模型复用时可针对下游任务特性裁剪冗余模块，该研究丢弃VAE解码器大幅降本提效的思路，可直接迁移到电商商品主体分割、属性识别等多模态内容理解场景，裁剪扩散类预训练模型的冗余结构

  - 冻结大模型主干+仅加极少量轻量头+LoRA适配的范式，仅33K参数就能实现SOTA效果，可复用在电商商品图深度估计、瑕疵检测等多类视觉任务，大幅降低微调成本

  - 预训练生成模型的空间token对齐特性可直接作为感知任务特征基座，无需将感知任务转成生成任务，推理速度提升2.48倍的结论可复用在直播内容理解、AR试穿等高实时性场景的视觉链路'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有基于文生图预训练模型的密集预测方案将任务转化为目标生成，需走完整VAE编解码链路，冗余度高，不符合密集预测仅需同图像平面像素级正确任务原生场的需求，推理效率、精度都有优化空间。
### 方法关键点
提出ReChannel框架，保留DiT输入所需的VAE编码器，丢弃目标侧VAE解码器；冻结DiT主干仅用任务专属LoRA适配，新增仅33K参数的共享token局部线性头，直接将每个DiT输出token映射为对应像素块的任务原生值，无空间混合计算。
### 关键结果数字
在6类密集预测任务、10+基准上测试，在无trimap抠图、KITTI深度估计、指代分割任务上达到新SOTA，法线、显著性、姿态估计任务保持竞争力；同等4B参数设置下，精度更高，推理速度比生成+隐空间解码的方案快2.48倍。
