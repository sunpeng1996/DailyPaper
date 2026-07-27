---
title: Differentiable Logic Gate Networks for Low-Latency EEG Classification on Edge
  Devices
title_zh: 面向边缘设备低延迟EEG分类的可微逻辑门网络
authors:
- Shyamal Y. Dharia
- Stephen D. Smith
- Camilo E. Valderrama
affiliations:
- The University of Winnipeg
- University of Manitoba
- University of Calgary
arxiv_id: '2607.18149'
url: https://arxiv.org/abs/2607.18149
pdf_url: https://arxiv.org/pdf/2607.18149
published: '2026-07-19'
collected: '2026-07-27'
category: Other
direction: 边缘端低延迟AI 可微逻辑门网络架构
tags:
- Diff-Logic
- Edge AI
- Low Latency Inference
- Boolean Circuit
- EEG Classification
one_liner: 提出可微逻辑门网络，编译为纯布尔电路，大幅降低边缘设备EEG分类延迟与内存占用
practical_value: '- 端侧智能推荐/个性化推送场景可借鉴Diff-Logic思路，将端侧小模型编译为布尔电路，用位运算替代浮点计算，大幅降低端侧延迟和内存占用

  - 大模型边缘轻量化优化可参考该方案的硬件原生适配思路，在可接受精度损失范围内，优先选择适配CPU位运算的模型架构，提升推理效率

  - 模型扩缩容场景可参考该方案的恒定延迟特性设计，避免参数量提升带来的推理延迟线性上涨，适配不同复杂度的业务需求'
score: 3
source: huggingface-daily
depth: abstract
---

### 动机
边缘设备实时EEG分类受传统神经网络浮点运算瓶颈限制，延迟和内存占用过高，无法满足便携脑机接口设备部署要求。
### 方法关键点
1. 提出可微逻辑门网络（Diff-Logic）作为硬件原生替代方案，可将模型直接编译为纯布尔电路，通过CPU位运算执行推理，无需浮点计算
2. 覆盖4个EEG数据集、2类任务（二分类痴呆检测、三分类情绪识别）、4个参数量级（50k~500k），与同参数量MLP、BNN做等参对照实验
### 关键结果数字
- 痴呆检测任务Macro F1达80.2%，超出同参MLP基线6.8%
- 7W功率Jetson Orin Nano单核部署时，较MLP延迟低2.3倍、模型体积小14倍
- 模型规模扩大10倍时推理延迟几乎恒定，最大参数量级下推理速度较MLP最高快2.9倍
