---
title: 'VisionMX: Unlocking Microscaling Post-Training Quantization for Vision Models'
title_zh: VisionMX：面向视觉模型的微缩放训练后量化优化方法
authors:
- Elad Dror Cohen
- Ofir Gordon
- Lior Dikstein
- Idan Achituve
- Hai Victor Habi
affiliations:
- Arm AI Research (AAIR), Arm Ltd
arxiv_id: '2610.03218'
url: https://arxiv.org/abs/2610.03218
pdf_url: https://arxiv.org/pdf/2610.03218
published: '2026-10-02'
collected: '2026-10-05'
category: Training
direction: 视觉模型微缩放训练后量化优化
tags:
- Post-Training Quantization
- Microscaling
- Vision Model
- Model Compression
- Inference Optimization
one_liner: 针对视觉模型微缩放训练后量化的三类误差，提出VisionMX方案实现精度与推理效率的平衡
practical_value: '- 多模态推荐/商品图像检索场景可复用该量化方案，端侧/边缘端部署视觉模型时，可在几乎无精度损失的前提下降低内存占用与推理延迟

  - 针对非负激活的可折叠仿射校正 trick 可直接迁移到各类CV类模型的低精度量化流程中，无需额外修改推理链路

  - 小卷积权重张量的有界舍入优化方法可复用在移动端商品实拍质检、图像分类等端侧AI任务的模型压缩环节'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
微缩放（MX）格式是硬件原生支持的低精度推理/训练方案，可大幅降低模型存储与计算开销，但现有MX量化在视觉模型上精度损失严重，三类误差是核心瓶颈：块尺度表示误差、小卷积权重张量与非均匀元素网格对齐差、非负激活对有符号编码利用率低。
### 方法关键点
VisionMX训练后MX量化框架包含两个核心优化：1）针对权重做有界舍入优化，适配小卷积张量的量化分布；2）针对激活加入可折叠仿射校正，提升非负激活的有符号编码利用率，校正算子可折叠入现有计算图无需额外推理开销。
### 关键结果
在图像分类、目标检测、语义分割、低光照增强四类CV任务上验证，效果优于直接MX转换与现有PTQ基线，对MX转换最敏感的架构精度恢复幅度最高。
