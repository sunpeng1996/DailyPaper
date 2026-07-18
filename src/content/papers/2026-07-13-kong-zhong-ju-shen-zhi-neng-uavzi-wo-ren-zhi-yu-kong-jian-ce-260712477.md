---
title: 'Self in Space: Benchmarking Self-Awareness and Spatial Cognition in UAV Embodied
  Intelligence'
title_zh: 空中具身智能：UAV自我认知与空间认知评测基准SIS-Bench
authors:
- Zhishan Zou
- Guoyan Sun
- Zhiwei Wei
- Jiancheng Pan
- Yujie Li
- Mugen Peng
- Wenjia Xu
affiliations:
- Beijing University of Posts and Telecommunications
- Hunan Normal University
- Tsinghua University
arxiv_id: '2607.12477'
url: https://arxiv.org/abs/2607.12477
pdf_url: https://arxiv.org/pdf/2607.12477
published: '2026-07-13'
collected: '2026-07-18'
category: Agent
direction: 具身Agent · 认知能力评测与优化
tags:
- Embodied Agent
- UAV
- MLLM
- Benchmark
- Spatial Cognition
- Self-Awareness
one_liner: 提出UAV具身智能评测基准SIS-Bench，验证运动感知表示可提升自我与空间认知效果
practical_value: '- 做具身导购Agent/AR探店Agent时，可参考空间+自我双维度、感知-记忆-推理三层架构搭建能力评测体系，覆盖全链路能力

  - 优化移动端/可移动Agent环境感知能力时，可复用光流+视觉特征融合的运动感知表示方法，提升动态场景状态建模效果

  - 构建行业Agent评测集时，可参考任务条件驱动+专家校验的构造pipeline，保证评测样本的场景真实性和标注准确性'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
当前UAV具身智能依赖MLLM处理复杂真实场景，需同时建模环境空间和Agent自身状态，但现有方案和评测均以环境为中心，仅聚焦空间认知任务，缺乏对Agent自我意识的显式评估。
### 方法关键点
1. 搭建SIS-Bench评测基准，沿「空间/自我」双维度、「感知/记忆/推理」三层认知层级设计评测框架
2. 基于1646条真实UAV视频，经任务驱动构造+专家校验流程，生成覆盖13项任务的4856条标注问答对
3. 提出光流与视觉特征融合的运动感知表示方法，显式建模Agent自身运动动态
### 关键结果
现有MLLM在动态Agent中心任务上存在显著短板，空间认知与自我认知能力失衡，认知层级越高性能衰减越明显；引入运动感知表示后，感知、记忆类任务性能平均提升7~12%，可直接泛化到下游UAV决策任务。
