---
title: 'Video-MME-Logical: A Controlled Diagnostic Benchmark for Video Temporal-Logical
  Reasoning'
title_zh: Video-MME-Logical：视频时间逻辑推理可控诊断基准
authors:
- Hohin Kwan
- Hongyu Li
- Ray Zhang
- Manyuan Zhang
- Xianghao Kong
- Anyi Rao
- Jiahao Xie
- Si Liu
affiliations:
- HKUST
- Beihang University
- CUHK
arxiv_id: '2606.27828'
url: https://arxiv.org/abs/2606.27828
pdf_url: https://arxiv.org/pdf/2606.27828
published: '2026-06-25'
collected: '2026-06-30'
category: Eval
direction: 多模态视频推理 基准评测
tags:
- Multimodal LLM
- Temporal Reasoning
- Benchmark
- Video Understanding
- Diagnostic Evaluation
one_liner: 构建可控制难度的视频时间逻辑推理诊断基准，揭示当前SOTA MLLM的推理能力缺口
practical_value: '- 构建商品短视频/直播场景多模态推荐的能力评测基准时，可参考该工作分离核心能力、控制干扰变量的方法，避免任务混杂导致能力误判

  - 面向直播/短视频时序用户行为建模时，可参考该工作划分的5类时间逻辑操作，拆解复杂时序建模目标

  - 评测多模态大模型能力时，除最终答案外，可增加中间推理路径验证，更精准定位模型缺陷'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有MLLM视频推理评测混杂了场景复杂度、静态识别、无控时间变异等干扰因素，无法单独分离评测视频时间逻辑推理能力，该能力要求模型随帧状态变化维护、更新、组合视觉证据，是动态视频理解的核心能力。

### 方法关键点
构建可控基准Video-MME-Logical，围绕状态跟踪、顺序计数、时间排序、动态空间、结构组合5类时间逻辑操作，生成25个细粒度任务类别；可通过改变时间范围、推理复杂度控制任务难度，同时支持中间推理状态诊断，可验证模型推理路径是否正确，不只评测最终答案。

### 关键结果
测试多个SOTA MLLM发现，时间逻辑推理存在显著人机性能缺口，缺口随推理复杂度提升快速扩大；即便在50万生成样本上做监督微调，仍无法补齐推理缺口，该基准可作为该方向研究的可扩展测试平台。
