---
title: 'CASA: Content-Acoustic Speaking Assessment with Speech Encoder and Large Language
  Model'
title_zh: CASA：结合语音编码器与大语言模型的内容-声学口语评估
authors:
- Nhan Phan
- Ilona Lähteenmäki
- Anna von Zansen
- Olli-Pekka Pauna
- Yaroslav Getman
- Tamás Grósz
- Mikko Kurimo
affiliations:
- Aalto University
- University of Helsinki
- Walton Institute
arxiv_id: '2608.13101'
url: https://arxiv.org/abs/2608.13101
pdf_url: https://arxiv.org/pdf/2608.13101
published: '2026-08-13'
collected: '2026-08-14'
category: Eval
direction: 多模态大模型 · 口语能力自动评估
tags:
- LLM
- Multimodal
- Whisper
- Automatic Assessment
- Speech Encoder
one_liner: 结合Whisper与Qwen3.5-2B构建轻量可解释口语评估框架CASA，性能SOTA且推理参数量减半
practical_value: '- 多模态内容评估任务可借鉴声学+内容特征拆分思路，单独验证各模态贡献提升可解释性，可直接复用在电商直播/短视频语音质量、主播话术合规评估场景

  - 大模型落地优先尝试小参数量基座（如2B级）+少量领域手工特征的组合，可在保证效果的同时大幅降低推理成本

  - 领域评估任务可复用「通用架构+数据集适配」的设计思路，无需修改模型结构即可跨场景迁移，降低多业务落地开发成本'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有自动口语评估（ASA）的多模态大模型方案缺少声学、内容特征的贡献度分析，可解释性差、性能稳定性未知，且参数量大推理成本高。
### 方法关键点
提出CASA架构，融合Whisper-medium语音编码器与Qwen3.5-2B小参数量大模型，显式拆分语音表达（声学）与内容语义两类特征，仅引入3个人工构造的流畅度特征，架构通用无需修改即可适配其他ASA数据集。
### 关键结果数字
在Speak & Improve Corpus 2025数据集上RMSE达0.358，超过此前SOTA效果，推理参数量仅为原有SOTA方案的约50%；通过消融实验验证了声学、内容特征的互补作用，同时验证了LLM可实现无训练的内容校验。
