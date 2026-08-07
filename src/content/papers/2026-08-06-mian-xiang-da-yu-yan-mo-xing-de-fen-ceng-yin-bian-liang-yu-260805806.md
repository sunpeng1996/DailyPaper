---
title: Hierarchical Latent Prediction for Language Models
title_zh: 面向大语言模型的分层隐变量预训练方法
authors:
- Chang Shi
- Tim Pearce
- Manan Tomar
- Siddhartha Sen
- John Langford
affiliations:
- University of Texas at Austin
- Microsoft Research
arxiv_id: '2608.05806'
url: https://arxiv.org/abs/2608.05806
pdf_url: https://arxiv.org/pdf/2608.05806
published: '2026-08-06'
collected: '2026-08-07'
category: LLM
direction: LLM预训练 · 分层隐空间自监督目标
tags:
- LLM-Pretraining
- Next-Token-Prediction
- Latent-Space
- Speculative-Decoding
- Long-Horizon-Reasoning
one_liner: 提出分层隐变量预训练目标HiLP，推理无额外开销，提升长程推理与投机解码效率
practical_value: '- 预训练加辅助目标、推理全丢弃的架构思路，可迁移到电商LLM4Rec模型的语义表征训练，加兴趣预测辅助loss不影响线上推理
  latency

  - 分层隐空间多尺度监督的思路，可用于用户行为序列建模，减少长序列兴趣建模的误差累积，提升长周期兴趣召回准确率

  - glu_cross特征融合方式比直接concat参数量减少65%、速度更快效果更好，多模态/多特征融合的推荐模块可直接替换现有concat方案降本提效

  - HiLP提升投机解码效率的特性，可直接用于电商导购Agent、客服大模型线上部署，降低推理延迟提升并发'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
标准Next-Token Prediction (NTP)预训练的teacher-forcing范式存在训练推理不一致的暴露偏差问题，多步预测、单尺度隐空间预测等优化方案要么预测horizon有限，要么多步展开误差累积严重，无法有效建模语言的多层级结构和长程依赖。

### 方法关键点
- 新增滑动窗口注意力（SWA）模块，将Transformer输出的低层隐状态聚合为更高层级的抽象隐状态，建模多粒度时序结构
- 联合优化5类损失：标准NTP损失、低层隐状态转移一致性损失、KL散度约束、高层抽象隐状态k步预测损失、结合双层级隐状态的组合NTP损失，所有隐空间预测目标均添加stop-gradient避免梯度干扰
- 推理阶段仅保留原始Transformer主干和标准NTP头，所有辅助模块全部丢弃，无任何架构overhead

### 关键实验
1B参数模型在100B token上预训练，对比baseline为标准NTP、MTP、NextLat：HumanEval pass@1达11.33%，比NextLat高0.75pp，比NTP高2.56pp；代码场景下投机解码平均每步接受token数达3.41，比NextLat高0.15；训练阶段仅损失35%吞吐量，推理速度和基线完全一致。

训练阶段设计的多层级辅助监督信号只要梯度隔离合理，完全可以做到推理零开销，同时提升模型长程能力和推理效率。
