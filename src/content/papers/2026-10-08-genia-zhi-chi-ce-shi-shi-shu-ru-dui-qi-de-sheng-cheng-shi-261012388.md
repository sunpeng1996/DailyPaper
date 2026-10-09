---
title: 'GenIA: Generative Reconstruction with Test-Time Input Alignment'
title_zh: GenIA：支持测试时输入对齐的生成式3D重建框架
authors:
- Stefano Esposito
- Naama Pearl
- Polina Karpikova
- Samuel Rota Bulò
- Lorenzo Porzi
- Peter Kontschieder
- Andreas Geiger
- Jonathon Luiten
affiliations:
- Tübingen AI Center, University of Tübingen
- Meta Reality Labs
arxiv_id: '2610.12388'
url: https://arxiv.org/abs/2610.12388
pdf_url: https://arxiv.org/pdf/2610.12388
published: '2026-10-08'
collected: '2026-10-09'
category: Other
direction: 生成式3D重建 · 测试时输入对齐
tags:
- 3D Reconstruction
- Test-Time Adaptation
- Generative Model
- Foundation Model
- Alignment
one_liner: 提出无需重训3D基础模型的测试时对齐框架，提升3D重建的姿态与外观一致性
practical_value: '- 测试时不重训大模型、仅通过轻量adapter+约束对齐输入的思路，可迁移到生成式推荐的测试时用户偏好对齐场景，大幅降低微调成本

  - 融合多观测输入加可见性偏置注意力的对齐方法，可复用在多行为序列用户兴趣建模、多模态召回的跨域特征对齐环节

  - 可微引导的去噪优化策略，可借鉴到生成式推荐的候选生成约束环节，提升生成结果与用户历史行为的匹配度'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有生成式3D基础模型补全观测外物体几何时，观测到的几何、外观、姿态还原度低，全量微调基础模型成本过高，难以适配多视图、动态输入等训练外场景。
### 方法关键点
1. 冻结SAM3D基础模型权重，测试时通过几何、光度约束对齐生成结果，无需重训；
2. 姿态优化：从观测几何推导平移、尺度参数，保留预训练旋转先验平衡生成效果与对齐度；
3. 外观对齐：去噪阶段引入可见性偏置注意力、跨观测融合、可微渲染引导，可选后处理阶段通过轻量decoder adapter微调外观隐向量、物体放置位置。
### 关键结果
在合成、真实基准上，单目、多视图、动态输入的姿态预测、3D重建效果均超过近期优化式、单帧图像转3D、视频转4D SOTA方法。
