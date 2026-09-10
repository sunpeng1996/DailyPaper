---
title: View-Structured Conformal Prediction for 3D Gaussian Splatting
title_zh: 面向3D高斯泼溅的视图结构化共形预测方法
authors:
- Junzheng Chu
- Bin Pan
- Zhenwei Shi
affiliations:
- Nankai University
- Beihang University
arxiv_id: '2609.10307'
url: https://arxiv.org/abs/2609.10307
pdf_url: https://arxiv.org/pdf/2609.10307
published: '2026-09-09'
collected: '2026-09-10'
category: Other
direction: 3D高斯泼溅 · 共形预测不确定性校准
tags:
- 3D Gaussian Splatting
- Conformal Prediction
- Uncertainty Estimation
- Novel View Synthesis
- Real-time Rendering
one_liner: 提出视图结构化共形预测VSCP，为3DGS新视图渲染提供可证覆盖保证，降低推理开销
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
3D Gaussian Splatting（3DGS）可实时生成新视图，但现有不确定性热图无法为渲染结果提供可量化的预测覆盖保证，逐像素校准的视图级覆盖度远低于预设目标。
### 方法关键点
提出View-Structured Conformal Prediction（VSCP）：将预校准尺度拆解为渲染器输出的空间形状项与可迁移的视图难度因子，预测形状项所需的最小视图级乘数；基于留存视图分位数的View-CP校准策略，可保障跨场景迁移下的有限样本有效性。
### 关键结果
13个真实场景90%覆盖目标下，像素池化校准视图级覆盖仅61.4%，View-CP可达91.7~92.0%；相同覆盖度下VSCP较恒定尺度宽度降低22.1%，性能媲美10模型集成效果但仅需单模型、4次光栅化，较单模型基线3DGS-U指标提升4.7个点；跨场景迁移下宽度较恒定尺度节省20.7%，RTX 4090上推理速度达216~280FPS。
