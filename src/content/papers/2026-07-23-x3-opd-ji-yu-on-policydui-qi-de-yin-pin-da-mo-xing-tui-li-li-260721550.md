---
title: 'X$^3$-OPD: Distilling Reasoning into Large Audio-Language Models via On-Policy
  Alignment'
title_zh: X³-OPD：基于On-Policy对齐的音频大模型推理能力蒸馏
authors:
- Dongjie Fu
- Di Cao
- Xize Cheng
- Zihan Zhang
- Wenxu Jia
- Yifu Chen
- Shengpeng Ji
- Yu Zhang
- Tao Jin
affiliations:
- Tencent Hunyuan
- Zhejiang University
arxiv_id: '2607.21550'
url: https://arxiv.org/abs/2607.21550
pdf_url: https://arxiv.org/pdf/2607.21550
published: '2026-07-23'
collected: '2026-07-24'
category: LLM
direction: 多模态大模型 · 跨模态知识蒸馏
tags:
- Knowledge Distillation
- On-Policy Alignment
- Audio-Language Model
- Cross-Modal Transfer
- Chain-of-Thought
one_liner: 提出跨模态On-Policy蒸馏框架X³-OPD，将文本大模型的推理能力迁移至音频大模型
practical_value: '- 做语音交互类电商Agent（如直播语音导购、智能语音客服）时，可复用on-policy蒸馏范式，用文本大模型作为教师提升音频输入场景的推理能力

  - 跨模态蒸馏的token级guidance策略可迁移至多模态推荐模型训练，对齐图文/音视频模态特征与文本大模型的推理先验

  - 三层对称语料构建思路可复用，针对语音交互、直播音频等业务场景定制推理数据集，解决音频推理数据稀缺问题'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
大音频语言模型（LALMs）听觉感知能力已取得显著进展，但深度逻辑推理能力远落后于文本LLM，核心瓶颈是高质量音频推理数据稀缺，现有跨模态蒸馏无法覆盖非语言声学事件、韵律等无文本对应内容的推理需求。
### 方法关键点
1. 提出X³-OPD跨模态On-Policy蒸馏框架，以强文本大模型为教师，学生LALM基于自身声学感知生成推理轨迹，教师用匹配文本输入与验证答案提供token级引导；
2. 构建三层对称语料库，覆盖文本推理转语音、复杂声学场景音频事件推理、含副语言线索的口语对话推理三类场景。
### 关键结果
在MMSU、MMAU、BIG Bench Audio、MMAR等基准上大幅提升音频相关推理与CoT质量，同时域偏移场景下基本保留模型原有能力。
