---
title: 'When Personality Meets Quantization: A Layer-wise MBTI Analysis of Quantized
  LLMs'
title_zh: 量化大语言模型的逐层MBTI人格特性分析
authors:
- Yao Fu
- Lijia Huang
- Xiaomin Li
- Runchao Li
- Yu Yin
- Kenneth A. Loparo
affiliations:
- Case Western Reserve University
- Northeastern University
- Microsoft Research
arxiv_id: '2608.25977'
url: https://arxiv.org/abs/2608.25977
pdf_url: https://arxiv.org/pdf/2608.25977
published: '2026-08-26'
collected: '2026-08-27'
category: LLM
direction: 大语言模型 · 量化与人格评估
tags:
- LLM Quantization
- MBTI
- Personality Analysis
- Layer-wise Analysis
- Inference Decoding
one_liner: 首次系统分析多精度量化LLM的MBTI人格特性，揭示人格是层依赖的涌现决策过程
practical_value: '- 部署端侧Agent/电商智能客服时，4-bit量化（GPTQ/AWQ）可保留基础人格稳定性，显存占用降低75%的同时不会大幅影响用户感知的对话温度，可优先选用

  - 可控调整LLM人格时，优先选择和模型固有主导人格（如主流开源模型的ENFJ）接近的设定，可大幅降低prompt工程成本，提升稳定性

  - 极端2-bit量化会破坏人格一致性，仅适合无交互属性的离线任务，不建议用于多轮对话、导购客服等对用户情绪感知要求高的场景

  - 人格类任务的决策主要在模型上层生成，做个性化对齐时可只微调上层参数，无需全量微调，降低训练成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM大量应用于电商客服、陪伴Agent等交互场景，人格特性直接决定用户信任、留存与情感体验，但现有研究仅评估全精度模型的输出层人格，忽略了工业界广泛部署的量化LLM的人格表现，也未揭示人格在模型内部的生成逻辑，无法指导低资源场景下的人格可控部署。
### 方法关键点
- 覆盖LLaMA3.1、Mistral、Qwen2.5等主流开源模型，测试FP16、4-bit（GPTQ/AWQ）、极端2-bit（AQLM系列）三类量化精度
- 设计两类评估范式：无条件prompt探测模型固有性格，人格条件prompt评估人格可控性，将MBTI测试转化为单token分类任务消除采样噪声
- 提出UALD解码方法，通过层间熵、置信度差指标追踪人格决策的逐层演化过程，量化推理策略对人格漂移的影响
### 关键结果
- 所有模型的主导人格均为ENFJ，4-bit量化保留90%以上的人格一致性，2-bit量化的人格可控性下降40%以上，跨精度一致性仅为55%
- 人格决策在模型上层（约后1/3层）才收敛，早期/中层熵值高、决策模糊
- 与模型固有人格一致的prompt可将解码导致的人格漂移率降低80%
### 核心结论
LLM的人格不是静态属性，而是受量化、prompt、解码策略共同影响的层依赖涌现决策过程
