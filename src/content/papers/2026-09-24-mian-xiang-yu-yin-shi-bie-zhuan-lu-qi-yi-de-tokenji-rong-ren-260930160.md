---
title: A Training Criterion with Token-Level Tolerance to Transcription Ambiguity
  for Automatic Speech Recognition
title_zh: 面向语音识别转录歧义的Token级容忍训练准则
authors:
- Saurabh Kumar
- Diptiman Mohanta
- Prasanta Kumar Ghosh
affiliations:
- Indian Institute of Science (IISc), Bangalore, India
arxiv_id: '2609.30160'
url: https://arxiv.org/abs/2609.30160
pdf_url: https://arxiv.org/pdf/2609.30160
published: '2026-09-24'
collected: '2026-09-25'
category: Other
direction: 语音识别 · 弱监督训练优化
tags:
- ASR
- CTC
- Weakly Supervised Learning
- Token-level Alignment
- WER Optimization
- Alignment Tolerance
one_liner: 提出token级容错的CTC训练准则，结合熵调度策略，相对CTC平均降低9.45% WER
practical_value: '- 电商语音搜索Query的ASR模块可借鉴token级wildcard容错设计，降低转录标注成本，提升口语化Query识别准确率

  - 预测熵驱动的权重调度思路可复用在带噪声的用户行为标签（如点击、收藏）建模任务，无需依赖固定训练轮数调参

  - 粗+细粒度混合容错路径的设计思路，可迁移到语义匹配、item标签纠错、用户评论情感识别等任务，兼顾监督信号利用率和噪声鲁棒性'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
传统ASR CTC训练默认参考转录为唯一正确标签，未考虑发音、拼写变体等标注歧义，原有词级OTC容错粒度过粗，跳过单个不支持token即丢失整词监督信号。
### 方法关键点
1. 将OTC的wildcard弧从词级下探到token粒度，仅跳过歧义token，保留同词其余token的监督信号
2. 混合token级+词级弧作为互补容错路径
3. 用预测熵索引的调度替代epoch索引的wildcard权重松弛，降低对训练轮数的依赖
### 关键结果
在19种语言、3个语料库的25个任务上全面优于CTC，混合方案平均相对WER降低9.45%；标注验证实验显示模型更倾向在有争议字符上触发wildcard跳过，精准匹配局部转录歧义。
