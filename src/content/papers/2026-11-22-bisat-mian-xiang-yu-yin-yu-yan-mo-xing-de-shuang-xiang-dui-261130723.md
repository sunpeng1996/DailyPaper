---
title: 'BiSAT: Bidirectionally Aligned Semantic-Acoustic Tokenization for Speech Language
  Models'
title_zh: BiSAT：面向语音语言模型的双向对齐语义-声学Token化方法
authors:
- Y. Lu
- L. Wang
- S. Okada
arxiv_id: '2611.30723'
url: https://arxiv.org/abs/2611.30723
pdf_url: https://arxiv.org/pdf/2611.30723
published: '2026-11-22'
collected: '2026-11-27'
category: LLM
direction: 语音大模型 · Token化优化
tags:
- Speech LLM
- Tokenization
- Zero-shot TTS
- Flow Matching
- Autoregressive LM
one_liner: 提出双分支共享索引的语音Token化框架，无需固定语义教师，适配零样本TTS等语音LM任务
practical_value: '- 多模态Agent的语音交互模块可借鉴双分支共享索引设计，平衡语义理解与音色/韵律等声学特征保留，提升语音交互自然度

  - 电商零样本语音广告生成、智能客服语音回复场景可复用BiSAT-TTS架构，用更少训练数据达到S级TTS效果，降低冷启动成本

  - 语音类用户反馈（如直播评论语音、客服咨询语音）的语义理解任务可适配BiSAT tokenizer，兼顾声学情绪特征与语义内容提取，提升用户偏好建模准确率'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有语音LM的tokenizer存在明显短板：语义增强型易丢失音色、韵律等声学细节，声学导向型保留的冗余声学波动会提升语言建模难度；现有统一tokenizer将两类特征压缩到单特征空间易产生目标干扰，且大多依赖冻结语义教师模型对齐，灵活性差。

### 方法关键点
提出BiSAT统一tokenization框架，设置独立的声学、语义双分支，通过共享索引机制对齐：双分支各配独立编码器、码本、解码器，每帧用共享索引最小化双分支联合量化误差，无需固定语义教师，可输出单离散码流的同时在独立空间学习两类表征；基于该框架搭建BiSAT-TTS零样本TTS系统，结合自回归文本-语音LM与条件流匹配声学解码器。

### 关键结果
BiSAT生成的码流可同时保留完整语义与声学信息，域内外语音适配性优异；BiSAT-TTS仅用更少训练数据就达到与SOTA语音LM类TTS模型相当的效果，码表表征互补性强，支持基于码的强化学习奖励建模。
