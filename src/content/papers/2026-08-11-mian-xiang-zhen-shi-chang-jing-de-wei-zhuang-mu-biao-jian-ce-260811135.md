---
title: Is There Really a Camouflaged Object? Towards Realistic Camouflaged Object
  Detection
title_zh: 面向真实场景的伪装目标检测基准OPC16K与OPCNet网络
authors:
- Huafeng Chen
- Yueming Lyu
- Chenyang Si
- Wende Tan
- Liucheng Guo
- Caifeng Shan
affiliations:
- Nanjing University
- Imperial College London
arxiv_id: '2608.11135'
url: https://arxiv.org/abs/2608.11135
pdf_url: https://arxiv.org/pdf/2608.11135
published: '2026-08-11'
collected: '2026-08-12'
category: Other
direction: 开放世界伪装目标检测
tags:
- Camouflaged Object Detection
- Open-world Benchmark
- Existence Reasoning
- Feature Refinement
- False Positive Reduction
one_liner: 构建含纯背景/非伪装目标的16K真实COD基准，提出存在感知检测网络降低误报
practical_value: '- 开放场景识别类任务可借鉴「目标存在判断+下游识别/分割」联合优化思路，比如电商图搜、内容审核场景，可大幅降低纯背景、非目标类样本的误报率

  - 构建业务评估基准时可参考负样本分层设计，纳入纯背景、非目标类等真实场景常见负样本，避免线下评估虚高、上线后泛化性差的问题

  - 可复用存在感知特征精修思路，用目标存在预测的结果约束下游任务的特征学习，提升特征对不同场景的适配性'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有伪装目标检测（COD）均基于封闭世界假设，默认输入一定包含伪装目标，忽略真实场景中纯背景、非伪装目标的普遍情况，部署时会出现严重的误报问题。
### 方法关键点
1. 构建OPC16K大规模真实COD基准，包含16245张来自14个来源的图像，分为伪装目标、纯背景、非伪装目标三类，支持分割质量+负样本拒识的综合评估
2. 提出OPCNet，将COD从纯分割任务重构为目标定位+伪装存在推理联合任务，包含分层存在推理模块区分三类场景、相似度感知伪装关系建模捕捉前后景伪装线索、存在感知特征精修模块用存在预测结果约束分割特征
### 关键结果
在OPC16K基准上性能领先，负样本误报显著降低，同时保持高精度的伪装目标分割效果
