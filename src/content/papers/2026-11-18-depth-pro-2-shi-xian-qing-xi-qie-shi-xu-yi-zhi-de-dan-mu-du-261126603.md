---
title: 'Depth Pro 2: Sharp and Temporally Consistent Metric Monocular Depth'
title_zh: Depth Pro 2：实现清晰且时序一致的单目度量深度估计
authors:
- Peiyun Hu
- Marko Mihajlovic
- Lyndon Duong
- Lahav Lipson
- Wei Dong
- Amaël Delaunoy
- Stephan R. Richter
- Vladlen Koltun
affiliations:
- Apple
arxiv_id: '2611.26603'
url: https://arxiv.org/abs/2611.26603
pdf_url: https://arxiv.org/pdf/2611.26603
published: '2026-11-18'
collected: '2026-11-21'
category: Other
direction: 单目深度估计 · 跨场景统一建模
tags:
- Monocular Depth Estimation
- Metric Depth
- Temporal Consistency
- Boundary Sharpness
- Unified Architecture
one_liner: 提出统一处理图像与视频的单目深度估计网络，兼顾边界清晰度与时间一致性，多维度性能超现有SOTA
practical_value: '- 当两类互补方法存在固有性能trade-off时，可尝试用统一可扩展架构同时适配两类输入/任务，避免单独优化的偏科问题

  - 多维度指标优化时可优先瞄准帕累托前沿，输出不同算力档位的模型族适配不同落地场景的资源约束'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有单目深度估计方法存在难以调和的性能trade-off：单帧方法输出的深度图边界清晰度高，但逐帧独立处理导致时间一致性差；多帧方法依赖时序关联保证一致性，但输出分辨率低、边界细节模糊，无法同时满足高清场景下的多维度性能要求。
### 方法关键点
1. 设计单一可扩展的端到端网络，支持同时处理单张图像与视频输入，无需针对两类场景单独训练模型
2. 直接输出与输入同分辨率的度量深度图，无需额外降采样、上采样后处理步骤
### 关键结果
在度量精度、边界清晰度、时间一致性、推理速度四个核心维度上全面超越此前SOTA方法，开源的多档位模型族在性能-速度曲线上定义了新的帕累托前沿。
