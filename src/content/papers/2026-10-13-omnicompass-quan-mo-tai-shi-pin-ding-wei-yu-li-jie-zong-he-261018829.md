---
title: 'OmniCompass: A Holistic Benchmark for Omni-Modal Video Grounding and Understanding'
title_zh: OmniCompass：全模态视频定位与理解综合评测基准
authors:
- Xuyang Liu
- Shihao Wang
- Xinyu Wei
- Minghan Li
- Zeqing Wang
- Zuhao Yang
- Zichen Wen
- Lei Zhang
affiliations:
- The Hong Kong Polytechnic University
- OPPO Research Institute
- Colorado School of Mines
- Nanyang Technological University
- Shanghai Jiao Tong University
arxiv_id: '2610.18829'
url: https://arxiv.org/abs/2610.18829
pdf_url: https://arxiv.org/pdf/2610.18829
published: '2026-10-13'
collected: '2026-10-17'
category: Eval
direction: 多模态大模型 · 视频理解评测
tags:
- MLLM
- Video Understanding
- Multimodal Benchmark
- Temporal Grounding
- Spatial Grounding
- QA
one_liner: 推出覆盖双轨三任务的全模态视频理解基准OmniCompass，完成50款MLLM能力评测
practical_value: '- 短视频带货场景多模态理解能力评测，可复用「时空定位+QA」三层任务设计，覆盖用户找商品位置、出现时间、属性信息的全链路需求

  - 多模态召回/排序模型离线评估可参考双设置对照思路，对比纯文本query、文本+商品图query下的模型表现一致性，降低跨模态匹配幻觉

  - 电商内容审核类Agent的能力验证，可借鉴该基准的多轮人工校验标注流程，提升评测数据集的可靠性'
score: 7
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有多模态大模型（MLLM）视频理解评测覆盖维度不全，无法系统性诊断全模态视频理解能力短板

### 方法关键点
推出OmniCompass基准，分两个评测赛道：OmniCompass-VL针对视觉-语言任务，OmniCompass-AV针对音视频联合理解任务；每个赛道覆盖temporal grounding（TG）、spatial grounding（SG）、QA三类互补任务，QA覆盖多类感知、推理维度；数据集含820条视频2460条VL实例、240条视频720条AV实例，覆盖不同时长，支持纯文本、文本+图两种对照输入设置，所有样本经多轮人工标注校验

### 关键结果数字
对50款MLLM评测显示，开源模型整体落后于闭源模型，音视频联合理解差距尤为明显；即使头部模型也难以实现精准时空定位，不同输入设置下的预测一致性较差
