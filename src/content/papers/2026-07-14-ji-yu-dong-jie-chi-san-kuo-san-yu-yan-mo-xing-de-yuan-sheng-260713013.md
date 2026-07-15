---
title: Audio-Native Speech Recognition with a Frozen Discrete-Diffusion Language Model
title_zh: 基于冻结离散扩散语言模型的原生音频语音识别方法
authors:
- Harsha Vardhan Khurdula
- Abhinav Kumar Singh
- Yoeven D Khemlani
- Vineet Agarwal
arxiv_id: '2607.13013'
url: https://arxiv.org/abs/2607.13013
pdf_url: https://arxiv.org/pdf/2607.13013
published: '2026-07-14'
collected: '2026-07-15'
category: LLM
direction: LLM多模态 · 离散扩散语音识别
tags:
- Diffusion LLM
- MoE
- LoRA
- Speech Recognition
- Multimodal
one_liner: 基于冻结26B MoE离散扩散LLM实现并行语音识别，仅训练0.16%参数达LibriSpeech 6.6% WER
practical_value: '- 大模型跨模态迁移时可采用「冻结主干+轻量Projector+LoRA」的低参微调范式，仅训练千分级参数即可适配新模态，大幅降低训练成本

  - 跨模态微调出现梯度对齐死锁时，可在冻结输出头处加CTC loss打通梯度通路，快速解决模态grounding失效问题

  - 离散扩散模型做生成任务可实现固定步数并行解码，不受生成长度影响，可复用在长文案/多轮对话生成场景提升推理速度'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
当前ASR主流为自回归逐token解码，推理速度随序列长度线性上升，离散扩散LLM可并行迭代优化全序列，有望解决该痛点但存在跨模态对齐难问题。

### 方法关键点
1. 主干采用冻结的26B参数MoE离散扩散模型DiffusionGemma，搭配冻结Whisper编码器提取声学特征；
2. 仅训练轻量投影层+LoRA适配器，总参数量仅42M，占主干的0.16%；
3. 针对原生训练目标梯度无法有效传导到投影层的问题，在冻结输出头引入CTC loss打通梯度通路，解决模态对齐死锁。

### 关键结果
LibriSpeech test-clean数据集WER达6.6%；仅需8步并行解码，推理速度不受语音长度影响；单适配器支持6种语言，在英/印/普通话上均验证有效。
