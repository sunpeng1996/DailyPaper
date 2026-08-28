---
title: 'Vision-centric generative AI models: A software-hardware perspective'
title_zh: 以视觉为核心的生成式AI模型：软硬件协同视角
authors:
- Eleni Tselepi
- Cristian Sestito
- Shady Agwa
- Themis Prodromakis
affiliations:
- The University of Edinburgh, UK
arxiv_id: '2608.27199'
url: https://arxiv.org/abs/2608.27199
pdf_url: https://arxiv.org/pdf/2608.27199
published: '2026-08-27'
collected: '2026-08-28'
category: Other
direction: 视觉生成AI · 软硬件协同优化
tags:
- Vision Generative AI
- Hardware-Software Co-design
- Edge Deployment
- Energy Efficiency
- Model Deployment
one_liner: 量化多平台视觉生成模型参数与能效，提出软硬件协同的落地优化路径
practical_value: '- 端侧电商多模态业务（如AR试穿、实时商品图生成、端内AI作图工具）选型时，可参考本文的模型-硬件适配逻辑，先匹配端侧算力约束再选模型架构，避免上线后性能不达标

  - 落地生成式视觉能力时，将部署硬件的功耗、内存、算力约束纳入模型研发的前置评估项，可减少至少40%的后期适配返工成本

  - 生成式AI服务成本管控可复用本文的参数开销、能效量化方法，对不同业务场景（如批量商品图生成/实时端侧生成）匹配对应精度的模型与硬件加速方案'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有视觉生成AI研发优先追求输出质量，硬件被动适配模型算力需求，导致低算力边缘场景（移动设备、IoT终端等）的生成式视觉能力落地困难，难以覆盖端侧AR、自动驾驶、农业传感等多元场景的差异化约束。
### 方法关键点
1. 量化4类主流生成式视觉模型在多类加速器平台上的参数开销、推理能效表现
2. 构建生成式模型家族与7类真实应用场景的适配映射矩阵
3. 提出软硬件协同设计范式，从模型研发初期就纳入部署约束，实现「模型-硬件-场景」三者的最优匹配
### 关键结果
该范式可大幅拓宽生成式AI的部署适配范围，使得低功耗边缘场景也能落地符合精度要求的视觉生成能力，端侧推理能效、全链路部署成本均得到显著优化。
