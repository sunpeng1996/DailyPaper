---
title: 'PhysCount: Do MLLMs Count Visual Appearances or Physical Entities?'
title_zh: PhysCount：多模态大语言模型是统计视觉表象还是物理实体？
authors:
- Lidong Lu
- Jiaxin Lv
- Liangrui Dong
- Xinyi Mao
- Lidong Zou
- Zhenquan Li
- Tong Lu
- Guo Chen
affiliations:
- Nanjing University
- NVIDIA
arxiv_id: '2610.40530'
url: https://arxiv.org/abs/2610.40530
pdf_url: https://arxiv.org/pdf/2610.40530
published: '2026-10-29'
collected: '2026-10-31'
category: Eval
direction: 多模态大模型认知能力测评
tags:
- MLLM
- Benchmark
- Visual Reasoning
- Evaluation
- Physical Perception
one_liner: 构建测评基准PhysCount，衡量多模态大模型区分视觉表象与物理实体的计数能力
practical_value: '- 多模态商品识别、AR实景导购Agent场景，可复用同实体多表象映射标注框架，避免将镜像/反射的同一商品识别为多个SKU

  - 多模态搜索/内容推荐场景，推理阶段将关联问题联合作答可显著提升实体识别准确率，可优化prompt引入关联推理约束

  - 实体级多模态任务无需盲目采用超高清图像输入，高分辨率对认知能力增益有限，可平衡输入分辨率与推理成本'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有视觉计数基准未区分「统计视觉表象」和「统计物理实体」两类任务，无法衡量MLLM对物理世界的真实认知能力，单实体以直接呈现、反射、隔玻璃等多表象出现时的识别缺陷未被充分验证。

### 方法关键点
构建PhysCount测评基准，包含546张真实世界图像、4595个人工标注问题，分为651个特定目标组，标注同实体的不同表象及观察模式，设计4类问题分别测试表象枚举、物理实体枚举、成像相关计数、表象-实体对应能力，以单组全对率和各问题族准确率作为核心指标。

### 关键结果数字
测试40款MLLM，表象计数准确率远高于实体关联推理能力；最强模型的全组正确率仅13.36%；单实体多表象、跨观察模式时性能显著下降；高分辨率图像仅提升视觉证据获取能力，对全组正确率增益有限，相关问题联合作答可大幅提升性能。
