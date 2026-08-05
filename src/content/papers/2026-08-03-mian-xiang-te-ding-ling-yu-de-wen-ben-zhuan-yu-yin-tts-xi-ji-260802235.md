---
title: 'Domain-Specific Evaluation of Text-to-Speech Systems: A Multi-Metric Benchmarking
  Study'
title_zh: 面向特定领域的文本转语音（TTS）系统多指标基准评估研究
authors:
- Ali Jafar
- Amal Sarmad
- Shifa Yousaf
- Maryam Bashir
affiliations:
- FAST School of Computing, National University of Computer and Emerging Sciences
  (FAST-NUCES)
arxiv_id: '2608.02235'
url: https://arxiv.org/abs/2608.02235
pdf_url: https://arxiv.org/pdf/2608.02235
published: '2026-08-03'
collected: '2026-08-05'
category: Eval
direction: 低资源语音合成 · TTS跨领域基准评估
tags:
- TTS
- Evaluation Benchmark
- Low-resource Language
- Multi-metric Evaluation
- Domain-specific Evaluation
one_liner: 提出融合主客观协议的跨领域低资源语言TTS多指标评估框架，公开全套可执行评估工具
practical_value: '- 电商语音客服、商品介绍TTS选型时，可复用该框架主客观结合的评估方案，针对正式/口语/情感/叙事4类场景分别测试选择适配模型

  - 小语种跨境电商语音内容生成团队，可直接复用其开源的评估脚本与Colab工具，快速完成低资源语言TTS效果验收

  - 针对电商情感播报、直播口播等细分TTS需求，可参考其领域性能差异结论，优先对情感类TTS做专项优化'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有TTS评估方法缺乏跨多领域同时覆盖感知质量、说话人相似度、声学保真度的统一体系，低资源语言相关评估方案尤其缺失。
### 方法关键点
提出可复现的多指标基准框架，融合主观（MUSHRA听测、ABX判别测试）+客观（Resemblyzer说话人相似度打分、MCD、F0 RMSE声学分析）两类评估协议，以低资源语言为测试案例覆盖正式、会话、叙事、情感4个语音领域，对4个SOTA TTS系统开展960组音频对的测试。
### 关键结果数字
不同领域TTS性能差异显著，情感语音合成难度最高（平均MCD 12.03dB，F0 RMSE 889音分），会话语音的声学保真度整体最优，全套评估工具已开源。
