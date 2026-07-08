---
title: Speaker-Disentangled Chunk-Wise Regression for Syllabic Tokenization
title_zh: 面向音节分词的说话人解耦分块回归方法
authors:
- Ryota Komatsu
- Kota Kawakita
- Takuma Okamoto
- Takahiro Shinozaki
affiliations:
- Institute of Science Tokyo
- National Institute of Information and Communications Technology
arxiv_id: '2607.04064'
url: https://arxiv.org/abs/2607.04064
pdf_url: https://arxiv.org/pdf/2607.04064
published: '2026-07-04'
collected: '2026-07-08'
category: Other
direction: 语音自监督学习 · 音节分词
tags:
- Speech Tokenization
- Self-supervised Learning
- Speaker Disentanglement
- HuBERT
- Speech LM
one_liner: 提出说话人解耦的分块回归音节分词方案，消除说话人特征干扰，提升语音LM语义理解效果
practical_value: '- 多模态电商场景下处理用户语音查询时，可借鉴说话人特征解耦思路，消弭不同用户发音差异对语义识别的干扰，提升query理解准确率

  - 做自监督模型师生蒸馏时，可复用固定长度分块回归的损失设计，替代全局utterance级交叉熵，降低无关特征噪声对蒸馏效果的影响

  - 搭建语音交互类电商导购Agent时，可采用本文优化的音节token替代传统音素token，提升语音语义理解的准确率'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有无监督音节分词方案基于预训练HuBERT做师生蒸馏，采用utterance级交叉熵训练时，模型会拟合说话人身份而非语言内容，导致产出的音节token纯度低，拖累下游语音LM性能。
### 方法关键点
1. 给学生侧输入的语音表征引入说话人特征扰动
2. 在固定长度分块内做回归，将扰动后的学生表征对齐干净的教师侧目标，替代全局交叉熵损失，实现说话人特征与语言内容解耦
### 关键结果
- 音节边界检测、音节段聚类任务达到SOTA
- 基于该方法产出的音节token训练的语音LM，相比音素级SpiRit-LM，句法与语义理解相对提升7%
