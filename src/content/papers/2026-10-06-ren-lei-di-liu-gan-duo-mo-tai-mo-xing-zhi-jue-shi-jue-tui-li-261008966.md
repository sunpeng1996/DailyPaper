---
title: 'Humanity''s Sixth Sense: Benchmarking Intuitive Visual Reasoning in Multimodal
  Models'
title_zh: “人类第六感”：多模态模型直觉视觉推理能力基准测试
authors:
- Xingang Guo
- Jing Gu
- Brian Jang
- Renxiong Wang
- Utkarsh Tyagi
- Daniel Quigley
- Steven Li
- David Yan
- Daniel Yue Zhang
- Darvin Yi
affiliations:
- ScaleAI
- Elorian
- University of California, Santa Cruz
arxiv_id: '2610.08966'
url: https://arxiv.org/abs/2610.08966
pdf_url: https://arxiv.org/pdf/2610.08966
published: '2026-10-06'
collected: '2026-10-10'
category: Eval
direction: 多模态大模型 · 直觉推理能力评测
tags:
- Multimodal-LLM
- Visual-Reasoning
- Benchmark
- Intuitive-Reasoning
- Model-Evaluation
one_liner: 提出HSS多模态直觉视觉推理基准，实测25款前沿模型表现远低于人类水平
practical_value: '- 搭建多模态导购Agent时可引入HSS的测试维度，验证模型对商品场景隐含信息（如空间适配、社交属性）的推理能力，减少导购错误

  - 电商内容理解模块可参考HSS的四层推理分类（时间/空间/社交/抽象）构建标注体系，提升商品隐含信息的挖掘精度

  - 多模态召回排序模块可针对性优化HSS暴露出的直觉推理短板，提升场景化推荐的匹配准确率'
score: 7
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有多模态基准要么聚焦专家级专业分析，要么仅测试底层感知能力，缺失对人类日常使用的直觉视觉推理（隐式时空/社交/抽象信息推断）能力的评测，无法对齐MLLM落地人类场景的能力要求。
### 方法关键点
提出HSS直觉视觉推理基准，覆盖图像、视频输入，构建结构化分类体系，每条测试用例搭配人工编写的prompt，探测模型对人类一眼就能推断的隐式信息的理解能力。
### 关键结果数字
人类在HSS基准上准确率达93.1%，最强模型GPT-6-astra最高仅达53.6%；引入动态视觉操作的Agent架构可缩小但无法抹平与人类的性能差距，25款主流多模态模型表现均远低于人类。
