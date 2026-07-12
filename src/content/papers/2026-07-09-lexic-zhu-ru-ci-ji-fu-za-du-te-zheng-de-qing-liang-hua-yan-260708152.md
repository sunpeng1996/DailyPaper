---
title: 'LEXIC: Lightweight Eye-tracking eXtension via Injected Complexity'
title_zh: LEXIC：注入词级复杂度特征的轻量化眼动追踪扩展方案
authors:
- Sumin Lee
- Kyeonghun Kim
- Subeen Lee
- Jiwon Yang
- Tien Nguyen
- Ken Ying-Kai Liao
- Nam-Joon Kim
affiliations:
- Seoul National University
- OUTTA
- NVIDIA
arxiv_id: '2607.08152'
url: https://arxiv.org/abs/2607.08152
pdf_url: https://arxiv.org/pdf/2607.08152
published: '2026-07-09'
collected: '2026-07-12'
category: Other
direction: 眼动认知预测 · 轻量特征注入
tags:
- Eye-tracking
- Lightweight Feature Injection
- Out-of-distribution Generalization
- CNN
- AUROC Optimization
one_liner: 为无大模型的纯眼动阅读理解预测模型注入词级难度特征，提升跨场景泛化性能
practical_value: '- 做用户行为特征增强时，可借鉴预计算静态特征直接拼接输入的轻量方案，无需引入大模型即可获得稳定效果增益

  - 跨分布泛化场景优先选择直接拼接的特征注入方式，残差校准方案容易因训练域拟合度高导致跨用户/跨场景迁移效果下降

  - 小样本/低资源任务可采用K种子集成+多折训练的验证方式，提升效果统计显著性，降低实验随机性干扰'
score: 4
source: arxiv-cs.HC
depth: abstract
---

### 动机
眼动预测阅读理解任务存在明显效果鸿沟：融合文本的预训练语言模型方案AUROC达56~63%，但纯眼动无语言模型方案效果接近随机，亟需低成本提优方案。
### 方法关键点
基于AhnCNN基线设计2种预计算词级难度特征（GPT-2 surprisal、词频、词长）注入机制：
1. LEXIC-Concat：直接将难度特征与眼动输入拼接
2. LEXIC-Res：通过小头预测典型读者眼动反应，将实际反应与预测值的偏差输入编码器做残差校准
训练时采用K=5种子集成+10折交叉验证。
### 关键结果
- Unseen Text场景下两种方案均获得1.8~2.2pp AUROC增益（Wilcoxon p≤0.065）
- LEXIC-Concat在Unseen Reader场景额外提升2.9pp AUROC（p=0.010）
- LEXIC-Res在Unseen Reader场景仅提升1.8pp（p=0.19），因校准头过度拟合训练域读者，跨分布迁移性差
