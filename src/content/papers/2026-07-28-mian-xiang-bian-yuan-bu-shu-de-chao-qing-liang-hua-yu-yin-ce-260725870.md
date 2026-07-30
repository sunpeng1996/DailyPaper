---
title: 'VAD to the Bone: Ultra-Tiny Speech Activity Detection for Edge Deployment'
title_zh: 面向边缘部署的超轻量化语音活动检测模型kiloVAD
authors:
- Stephen Bauer
- Sheila Seidel
- Shanza Iftikhar
- Scott Veidenheimer
- Gorkem Ulkar
affiliations:
- Analog Devices, Inc., USA
- University of California, Los Angeles (UCLA), USA
arxiv_id: '2607.25870'
url: https://arxiv.org/abs/2607.25870
pdf_url: https://arxiv.org/pdf/2607.25870
published: '2026-07-28'
collected: '2026-07-30'
category: Other
direction: 边缘端语音模型轻量化部署优化
tags:
- VAD
- Edge Deployment
- Structured Pruning
- Quantization-Aware Training
- Knowledge Distillation
- CNN
one_liner: 提出仅2.1k参数的纯CNN边缘VAD模型，搭配新型训练策略精度超越同规模现有SOTA
practical_value: '- 端侧轻量化模型训练可复用「逐层结构化剪枝+自蒸馏+角度感知QAT」pipeline，比标准QAT精度高1-4%，适配低算力场景

  - 端侧部署优先选择纯CNN、标准特征输入的架构，避免依赖特殊算子，大幅提升跨硬件兼容性

  - 资源约束场景下可增加可调上下文/频谱参数配置项，灵活平衡精度与算力开销，适配不同硬件规格'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
边缘常在线语音系统对前端VAD的内存、延迟、算力要求极高，现有轻量化VAD依赖的可学习滤波器组、循环层、非因果后处理等组件硬件兼容性差，难以规模化部署。
### 方法关键点
1. 设计kiloVAD纯CNN架构，仅输入标准Mel特征，支持上下文/频谱参数可调，适配不同场景需求
2. 采用逐层结构化剪枝+自蒸馏训练策略，搭配自研角度量化感知训练（QAT），相比标准QAT精度提升1-4%
### 关键结果
因果推理条件下逐帧评估，kiloVAD仅2.1k参数、200ms上下文，在AVA-Speech数据集上AUC达0.850，成为当前可直接部署的因果VAD新SOTA。
