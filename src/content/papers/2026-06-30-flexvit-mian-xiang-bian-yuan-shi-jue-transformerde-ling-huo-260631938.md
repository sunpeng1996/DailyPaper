---
title: 'FlexViT: A Flexible FPGA-based Accelerator for Edge Vision Transformers'
title_zh: FlexViT：面向边缘视觉Transformer的灵活FPGA加速器
authors:
- Hubert Dymarkowski
- Xingjian Fu
- Rappy Saha
- Jude Haris
- José Cano
affiliations:
- University of Glasgow
arxiv_id: '2606.31938'
url: https://arxiv.org/abs/2606.31938
pdf_url: https://arxiv.org/pdf/2606.31938
published: '2026-06-30'
collected: '2026-07-02'
category: Other
direction: 边缘ViT · FPGA推理加速
tags:
- FPGA
- Vision Transformer
- Edge AI
- INT8 Inference
- Model Acceleration
one_liner: 提出软硬件协同设计的边缘ViT FPGA推理加速器，较纯CPU最高获1.40倍端到端提速
practical_value: '- 端侧多模态电商推荐/搜图推荐场景可复用统一INT8 GEMM引擎设计，同时支撑卷积、全连接层计算，降低端侧算力开销

  - 端侧模型推理优化可参考深度优先分块策略，单趟完成累加消除片外partial sum传输，降低内存带宽占用

  - 异构模型边缘部署可借鉴动态数据流切换思路，根据层类型自适应选择输入/权重复用模式，提升推理效率'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
混合架构ViT同时包含卷积、全连接层，张量形状差异大，算力与内存开销高，资源受限边缘端部署难度大，现有FPGA加速方案灵活性不足。

### 方法关键点
1. 基于SECDA-TFLite框架采用软硬件协同设计，通过运行时im2col变换将两类层统一映射到高吞吐INT8 GEMM计算引擎；
2. 设计双模式数据流，支持运行时重配置计算阵列，动态切换输入/权重复用策略，适配不同层配置；
3. 提出深度优先分块策略，单趟完成累加，消除片外partial sum传输，降低内存带宽需求。

### 关键结果
在PYNQ-Z2 FPGA上验证，加速器执行层最高提速2.74x，端到端推理较纯CPU执行最高提速1.40x，代码已开源。
