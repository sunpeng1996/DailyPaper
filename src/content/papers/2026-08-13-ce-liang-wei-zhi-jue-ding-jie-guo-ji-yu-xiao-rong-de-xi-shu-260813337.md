---
title: 'Where You Measure Decides What You Measure: Position Selection in Ablation-Based
  SAE Evaluation'
title_zh: 测量位置决定结果：基于消融的稀疏自编码器评估中的位置选择
authors:
- Valentin Noël
affiliations:
- Devoteam
arxiv_id: '2608.13337'
url: https://arxiv.org/abs/2608.13337
pdf_url: https://arxiv.org/pdf/2608.13337
published: '2026-08-13'
collected: '2026-08-14'
category: Eval
direction: LLM可解释性 · SAE评估协议优化
tags:
- Sparse Autoencoder
- Ablation Study
- Evaluation Protocol
- LLM Interpretability
- Causal Analysis
one_liner: 揭示基于消融的SAE评估默认位置选择的偏差，给出跨论文可比的标准化评估协议
practical_value: '- 做LLM4Rec、Agent的SAE可解释性分析时，不要默认在latent激活最强的token位置测量消融效果，需固定统一测量位置避免结果偏差

  - 跨团队/跨版本对比SAE效果时，必须明确标注测量位置，否则结果不具备可比性，可直接复用论文给出的1行修正代码

  - 做LLM可解释性相关的算法迭代时，不要盲目增加语料规模消除评估偏差，该问题随语料规模扩大反而更严重，优先修正位置选择逻辑'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
基于消融的SAE评估是当前LLM可解释性的核心方法，但行业默认选择latent激活最强的token作为测量位置，该选择由被评估的字典自动决定、几乎不被公开报告，会导致跨模型/跨字典的评估结果不可比。
### 方法关键点
对同初始化、仅训练拟合策略不同的6个SAE做对照实验，匹配decoder相似的latent，分别在默认位置和统一固定位置测量评估方差；同时测试16倍范围的语料规模对偏差的影响。
### 关键结果数字
默认位置选择带来的评估方差占比达7.6%、11.9%，固定测量位置后方差降至接近0；语料规模扩大16倍时，字典间测量位置的一致性反而下降，偏差随规模增大更严重，仅需1行代码即可修正评估逻辑。
