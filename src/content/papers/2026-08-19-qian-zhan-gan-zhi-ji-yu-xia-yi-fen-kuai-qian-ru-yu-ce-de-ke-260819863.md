---
title: 'Listening Forward: Next Patch Embedding Prediction Enables Scalable Audio
  Learners'
title_zh: 前瞻感知：基于下一分块嵌入预测的可扩展音频学习器
authors:
- Umberto Cappellazzo
- Xubo Liu
- Stavros Petridis
- Maja Pantic
affiliations:
- Imperial College London
- University of Surrey
arxiv_id: '2608.19863'
url: https://arxiv.org/abs/2608.19863
pdf_url: https://arxiv.org/pdf/2608.19863
published: '2026-08-19'
collected: '2026-08-21'
category: Training
direction: 自监督学习 · 音频表征预训练
tags:
- SSL
- Autoregressive Prediction
- Audio Representation
- Causal Transformer
- Pre-training
one_liner: 提出极简自监督音频预训练框架NAPE，仅靠因果掩码与梯度停止实现多任务SOTA性能
practical_value: '- 时序类数据（如用户行为序列、音频交互信号）表征预训练可参考NAPE的极简设计思路，砍掉冗余的解码器、tokenizer、师生架构等组件，大幅降低工程落地复杂度

  - 自监督预训练时可复用「因果掩码+stop-gradient仅预测下一块嵌入」的监督信号设计，无需额外正则损失即可有效提升表征质量

  - 搭建多模态生成式推荐/Agent多模态交互理解能力时，可直接复用NAPE预训练的音频编码器，降低音频特征抽取的标注成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
当前音频自监督预训练依赖复杂训练流程才能取得有竞争力的效果，而NLP、CV领域已验证仅通过自回归预测下一个元素的极简范式即可学到优质数据分布表征，音频天然的时序结构与该范式高度适配。

### 方法关键点
NAPE自监督框架基于因果Transformer对log-mel声谱图做自回归预训练，仅用因果掩码+stop-gradient作为唯一训练信号，设计极度精简，无需重建解码器、声学tokenizer、师生架构、辅助正则损失等冗余组件。

### 关键结果
在6个音频/语音基准任务上微调性能达到SOTA，随编码器尺寸扩容性能稳定线性提升，线性探测表现优异，无显式监督下即可生成结构化注意力模式。
