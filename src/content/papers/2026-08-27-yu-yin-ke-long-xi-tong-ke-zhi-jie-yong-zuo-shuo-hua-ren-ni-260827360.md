---
title: Your Voice Cloning System is Secretly a Voice Anonymizer
title_zh: 语音克隆系统可直接用作说话人匿名化工具
authors:
- Romolo Muletta
- Felix Matthias Saaro
- Mark Cieliebak
- Jan Deriu
affiliations:
- Centre for Artificial Intelligence ZHAW School of Engineering
arxiv_id: '2608.27360'
url: https://arxiv.org/abs/2608.27360
pdf_url: https://arxiv.org/pdf/2608.27360
published: '2026-08-27'
collected: '2026-08-28'
category: Other
direction: 预训练语音模型跨任务复用 · 说话人匿名化
tags:
- Voice Anonymization
- XTTSv2
- Cross-task Transfer
- Multilingual Speech
- Zero-shot Adaptation
one_liner: 复用预训练XTTSv2语音克隆模型无需重训实现跨语种说话人匿名化，效果优于专用基线
practical_value: '- 电商/语音交互Agent场景下用户语音数据脱敏可直接复用该方案，无需重训现有预训练语音克隆模型，大幅降低研发成本

  - 跨境多语种业务的语音数据匿名化可直接适配，无需针对每个语种单独训练专属模型

  - 构建语音类用户反馈数据集时，可复用其迭代优化策略平衡隐私保护与语音内容可懂度，降低信息损耗'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
说话人匿名化需在隐藏说话人身份特征的同时保留语音内容、韵律与质量，现有专用方案泛化性差，多语种适配成本高，且需从零训练。

### 方法关键点
1. 复用预训练多语种XTTSv2语音克隆模型，利用其韵律结构与说话人身份独立解耦的特性，以伪说话人为条件做语音转换，无需重训
2. 引入迭代优化策略，最大化说话人不相似度与语音可懂度的调和平均，平衡隐私性与实用性

### 关键结果
在CommonVoice、多语种LibriSpeech的7个欧洲语种上测试，隐私性接近最优（EER≈0.49），可懂度达到业界竞争水平，语音质量显著优于专用匿名化基线，无需语种专属训练。
