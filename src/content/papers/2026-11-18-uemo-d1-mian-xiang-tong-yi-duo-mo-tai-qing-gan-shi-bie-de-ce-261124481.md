---
title: 'UEmo-D1: An Efficient and Calibrated Decision Model for Unified Multimodal
  Emotion Recognition'
title_zh: UEmo-D1：面向统一多模态情感识别的高效校准决策模型
authors:
- Daiqing Wu
- Junqiao Wang
- Chengyang Fang
- Runhao Zeng
- Fei Ma
- Sicheng Zhao
affiliations:
- Tsinghua University
- Jiangxi University of Finance and Economics
- Shenzhen MSU-BIT University
- Guangming Laboratory
arxiv_id: '2611.24481'
url: https://arxiv.org/abs/2611.24481
pdf_url: https://arxiv.org/pdf/2611.24481
published: '2026-11-18'
collected: '2026-11-21'
category: Multimodal
direction: 多模态情感识别 · 统一决策建模
tags:
- Multimodal Emotion Recognition
- MLLM
- Decision Model
- Low Latency
- Confidence Calibration
one_liner: 提出首个多模态情感识别决策模型UEmo-D1及百万级配套数据集，兼顾性能、低延迟与置信度校准
practical_value: '- 电商直播/短视频/评论的多模态情感识别场景，可借鉴「指令引导+直接输出概率分布」的决策范式，相比生成式MLLM推理大幅降延迟，满足高吞吐在线业务要求

  - 多任务多模态分类建模可复用其统一训练策略，兼顾跨任务泛化性与置信度校准，降低下游业务bad case率

  - 低资源多模态任务可参考其跨任务数据集构建逻辑，减少重复标注成本，提升小样本下模型表现'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有多模态情感识别（MER）的两类主流范式（任务专用模型、MLLM类方法）无法同时兼顾跨任务泛化、高效决策、支持多合理解读三个类人情感理解核心能力，难以适配实际业务的复杂需求。
### 方法
提出统一决策框架，在自然语言指令引导下将多模态输入直接映射到候选选项的概率分布，落地为首个MER专用决策模型UEmo-D1；同步构建UEmo-Data数据集，包含97.7万训练样本、覆盖6类MER任务共41个评估子集，支撑联合训练与系统评测。
### 结果
3B参数的UEmo-D1精度优于现有7B/8B级MER专用大模型，推理延迟最高降低95%以上，同时置信度校准表现优异；实验明确了训练策略、数据构成对模型三类核心能力的影响规律，为统一MER建模提供落地参考。
