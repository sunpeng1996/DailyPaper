---
title: 'SPEARBench: A Benchmark for Naturalness Evaluation in Streaming Speech-to-Speech
  Language Models'
title_zh: SPEARBench：流式语音转语音大模型自然度评估基准
authors:
- Thomas Thebaud
- Yuzhe Wang
- Hao Zhang
- Sathvik Manikantan Napa Ugandhar
- Ashish Hallur
- Georgi Tinchev
- Venkatesh Ravichandran
- Laureano Moro-Velazquez
affiliations:
- Johns Hopkins University
- Amazon Inc.
arxiv_id: '2607.05365'
url: https://arxiv.org/abs/2607.05365
pdf_url: https://arxiv.org/pdf/2607.05365
published: '2026-07-06'
collected: '2026-07-08'
category: Eval
direction: 语音大模型 · 对话自然度评估
tags:
- Speech-to-Speech
- Benchmark
- Naturalness Evaluation
- Streaming LLM
- Conversational AI
one_liner: 提出覆盖8维度对话自然度的流式语音转语音大模型专用评估基准SPEARBench
practical_value: '- 开发电商语音客服、语音导购类Agent时，可直接复用该基准的多维度评估框架，替代单一ASR准确率评估，更贴合用户真实感知

  - 流式语音交互系统上线前验收，可参考其「受控对话Prompt+人类回答基线」的评估范式，提升测试结果的业务相关性

  - 服务多地域方言用户的语音交互产品，可重点对齐基准中的方言保留、人际姿态适配指标，优化下沉市场用户体验'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有流式语音转语音大模型的标准语音、文本评估基准仅关注信号、文本准确率，无法覆盖对话场景下时序、轮次、情绪、方言适配等维度的交互自然度，难以衡量真实场景的用户感知质量。
### 方法关键点
1. 基于Seamless Interaction语料构建受控问答对话prompt，内置人类原始回答作为参照基线
2. 设计8维度多模态评估协议，覆盖响应时延、打断容忍度、语音质量、ASR鲁棒性、语言方言一致性、情绪自然度、人际姿态适配、可解释分布基线
### 关键结果
当前主流流式S2S模型已实现高信号质量、低ASR错误，但在时延控制、对话重叠处理、方言保留、情绪适配、人际姿态动态5个维度上与人类对话表现存在显著差距。
