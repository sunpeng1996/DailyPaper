---
title: 'Content is What Remains: Invariant Speech Tokenization from Parallel Utterances'
title_zh: 基于并行语音提取不变特征的离散语音分词方法
authors:
- Laurin Wagner
- Bernhard Thallinger
- Miroslav Stankovic
- Mario Zusag
affiliations:
- nyra labs, Austria
arxiv_id: '2607.19033'
url: https://arxiv.org/abs/2607.19033
pdf_url: https://arxiv.org/pdf/2607.19033
published: '2026-07-21'
collected: '2026-07-23'
category: Other
direction: 语音语义表示 · 不变性分词
tags:
- speech-tokenization
- self-supervised-learning
- semantic-representation
- invariance-learning
- audio-processing
one_liner: 提出PINT并行不变语音分词方案，过滤非语言噪声生成高一致性语义语音token
practical_value: '- 多模态交互Agent的语音输入模块可复用PINT对齐损失思路，过滤说话人、环境噪声干扰，提升语音语义理解准确率

  - 语音搜索场景下，可采用PINT生成的高一致性语义token做query召回，降低无关声学特征对搜索匹配的干扰

  - 短视频/音频内容推荐场景，可基于PINT提取的纯语义特征做内容表征，提升跨说话人/跨环境的内容匹配精度'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有基于HuBERT等SSL模型的离散语音分词方法会泄露说话人、韵律、信道等非语言信息，导致token熵过高，无法精准提取纯语义信息，拖累后续语音生成、多模态推理等任务效果。

### 方法关键点
提出PINT（Parallel INvariant Tokenization）方案，核心假设为多说话人在不同环境下说相同内容时，唯一共享的因子就是语言语义；基于该思路对SSL编码器做微调，引入并行语音和数据增强的对齐损失，蒸馏不同样本间共享的语义残差，将相同文本对应到一致的token序列，同时保留帧级时间对齐能力，可直接作为音频编码的语义目标。

### 关键结果数字
相比基线方案，说话人探测准确率相对下降98.7%（从93.1%降至1.2%），ABX错误率降低42%，LM困惑度降低27-30%
