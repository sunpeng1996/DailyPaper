---
title: 'LACToS: Local Anomaly Detection via Conditional Typicality of Superpixels'
title_zh: LACToS：基于超像素条件典型性的局部异常检测方法
authors:
- Jihoon Hong
- Alireza Kheirandish
- Rohan Sanda
- Sara Fridovich-Keil
affiliations:
- Georgia Institute of Technology
- Stanford University
- Cohere
arxiv_id: '2610.31538'
url: https://arxiv.org/abs/2610.31538
pdf_url: https://arxiv.org/pdf/2610.31538
published: '2026-10-22'
collected: '2026-10-25'
category: Other
direction: 局部异常检测 · 跨场景图像识别
tags:
- Anomaly Detection
- OOD Detection
- Superpixel
- Diffusion Model
- Computer Vision
one_liner: 针对多模态内分布场景局部OOD检测性能退化问题，提出基于超像素典型性的鲁棒检测方法
practical_value: '- 电商商品主图质检/违规内容识别场景，可复用超像素分块策略替代逐像素检测，降低推理算力开销

  - 跨品类商品瑕疵检测场景，可借鉴多模态内分布下的OOD典型性估计思路，减少单场景标注训练成本

  - 少样本类目缺陷识别需求下，可复用仅用正常样本预训练扩散模型的方案，适配小样本业务场景'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有局部OOD检测方法多针对工业缺陷检测场景设计，在内分布为多模态的泛化场景下性能下降明显，无法适配跨领域检测需求。
### 方法关键点
基于统计典型性设计LACToS方案，核心优化两点：1）将像素分组为超像素降低计算粒度；2）引入高效代理指标估计条件典型性，仅需在正常分布图像上预训练的扩散模型即可完成推理，无需针对目标场景做专项微调。
### 关键结果
在医学影像、人脸异常检测、X光安检三类跨场景基准测试中，鲁棒性显著优于现有SOTA方法，代码已完全开源可直接复用。
