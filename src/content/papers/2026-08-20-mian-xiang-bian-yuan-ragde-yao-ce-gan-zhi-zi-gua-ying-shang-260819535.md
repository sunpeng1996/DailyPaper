---
title: 'From Retrieved Context to Runtime Control: Adaptive Compression for Edge-based
  RAG'
title_zh: 面向边缘RAG的遥测感知自适应上下文压缩方法
authors:
- Zlatan Feric
- Amir Taherin
- Yanzhi Wang
- David Kaeli
affiliations:
- Northeastern University
arxiv_id: '2608.19535'
url: https://arxiv.org/abs/2608.19535
pdf_url: https://arxiv.org/pdf/2608.19535
published: '2026-08-20'
collected: '2026-08-21'
category: RAG
direction: 边缘RAG · 运行时自适应压缩
tags:
- Edge-RAG
- Context Compression
- Runtime Optimization
- Energy Efficient Inference
- LLM Inference
one_liner: 基于边缘SoC实时遥测动态调整RAG上下文压缩率，平衡推理能耗、延迟与回答质量
practical_value: '- 端侧部署RAG类智能导购/客服Agent时，可参考0.3的安全压缩率阈值，在几乎不损失回答质量的前提下最高降低48.2%的SoC能耗，适配移动端/边缘设备算力限制

  - 不要固定压缩率，可根据当前设备的温度、内存占用、任务负载动态开关压缩功能：轻量任务/小模型场景跳过压缩避免额外开销，大模型长上下文场景开启0.3压缩率

  - RAG系统成本核算要算全链路开销，不能只看生成阶段的加速，要把压缩/重排等前置阶段的算力开销纳入收益评估'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有边缘RAG的上下文压缩多采用固定预算，忽略了边缘SoC的实时负载、资源限制，以及压缩本身的算力开销，要么过度压缩损失回答质量，要么压缩收益被自身开销抵消，无法兼顾能效与回答正确性。

### 方法关键点
- 提出遥测感知的自适应压缩框架，基于边缘SoC的实时温度、延迟、能耗、内存占用等信号，动态决策是否开启压缩及压缩率
- 采用LLMLingua-2作为硬压缩方案，仅压缩检索到的上下文片段，保留系统提示、少样本示例等固定内容不压缩，无需修改生成器接口
- 定义净收益指标：压缩后生成阶段的资源节省减去压缩自身的算力开销，作为压缩决策的核心依据

### 关键实验结果
在NVIDIA Jetson AGX Thor平台测试Llama 1B/3B/8B、Qwen 1.5B/3B/7B模型，使用Natural Questions、HotpotQA数据集，对比无压缩基线：
1. 7B-8B大模型场景下，生成阶段占单查询latency的90%、GPU能耗的91%，是边缘RAG的主要成本项
2. 压缩率0.3为安全阈值，该配置下F1值波动小于±0.05（几乎无质量损失），最高降低GPU能耗53.2%、SoC总能耗48.2%、延迟32.6%
3. 压缩率0.9的轻度压缩会带来1%-13%的额外能耗损失，因为压缩开销无法被少量token减少的收益覆盖

**最值得记住的一句话**：边缘RAG的上下文压缩不是固定预处理步骤，而是需要结合任务负载、设备状态动态决策的运行时资源调度旋钮。
