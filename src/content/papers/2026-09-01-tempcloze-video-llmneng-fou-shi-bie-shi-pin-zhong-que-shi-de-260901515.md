---
title: 'TempCloze: Can Video-LLMs Identify the Missing Middle?'
title_zh: TempCloze：Video-LLM能否识别视频中缺失的中间片段？
authors:
- Wenqi Pei
- Henry Hengyuan Zhao
- Yilai Liu
- Jiahao Meng
- Han Chen
- Ziyu Wang
- Hongyang Du
affiliations:
- The University of Hong Kong
- National University of Singapore
- Peking University
arxiv_id: '2609.01515'
url: https://arxiv.org/abs/2609.01515
pdf_url: https://arxiv.org/pdf/2609.01515
published: '2026-09-01'
collected: '2026-09-03'
category: Eval
direction: Video-LLM 时序推理能力评估
tags:
- Video-LLM
- Temporal Reasoning
- Benchmark
- Evaluation
- Cloze Task
one_liner: 构建消除语言捷径的视频完形基准TempCloze，测Video-LLM时序推理并定位时序对齐为核心瓶颈
practical_value: '- 做短视频/直播内容的多模态时序检索/生成评估时，可复用「同源干扰项+屏蔽语言/外观捷径」的构造方法，避免评估结果虚高

  - 涉及时序内容理解的多模态推荐/Agent场景，可参考语义/对齐/进展三维度拆解模型能力瓶颈，针对性做模块优化

  - 测试多模态大模型时序能力时，需控制候选顺序、帧密度、可见跨度等干扰参数，保证测试结果可信度'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有Video-LLM时序推理基准依赖语言交互形式，模型可通过选项措辞、答案关联、语言先验等捷径取巧，导致评估结果无法反映真实视觉时序推理能力。
### 方法关键点
1. 提出TempCloze视频完形基准：给定视频首尾片段，要求模型从4个候选中选出正确的缺失中间片段，覆盖1521条经过滤的长镜头、第一视角视频；
2. 从三个维度构造同源干扰项：语义（事件是否合理）、对齐（发生时机是否正确）、进展（演变过程是否连贯），同时通过共享场景/物体消除外观提示，最大程度规避语言捷径。
### 关键结果
测试10款闭源、21款开源Video-LLM发现，时序对齐是核心瓶颈：模型可识别合理语义内容、判断局部事件进展，但跨片段时序匹配能力较差；额外验证了候选顺序、帧密度、可见跨度、测试时缩放等参数会显著影响模型表现。
