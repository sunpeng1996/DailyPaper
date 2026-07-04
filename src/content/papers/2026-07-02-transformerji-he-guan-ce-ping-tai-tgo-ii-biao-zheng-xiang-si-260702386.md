---
title: 'Transformer Geometry Observatory TGO-II: Representational Similarity Observatory'
title_zh: Transformer几何观测平台TGO-II：表征相似度观测工具
authors:
- Kaustubh Kapil
- Kishor P. Upla
affiliations:
- Department of Electronics Engineering, SVNIT
- Sardar Vallabhai National Institute of Technology (SVNIT), Surat, India
arxiv_id: '2607.02386'
url: https://arxiv.org/abs/2607.02386
pdf_url: https://arxiv.org/pdf/2607.02386
published: '2026-07-02'
collected: '2026-07-04'
category: Training
direction: Transformer训练表征演化分析
tags:
- Transformer
- Representation Learning
- Training Dynamics
- Model Analysis
- ViT
one_liner: 提出TGO-II表征几何分析框架，揭示Transformer训练过程内部表征演化规律
practical_value: '- 可复用CKA、SVCCA、TwoNN-ID等表征相似度分析方法，诊断LLM4Rec、生成式推荐模型的训练健康度，识别层冗余问题

  - 可借鉴「保留token强交互结构提升表征复杂度」的结论，优化推荐系统用户/物品序列Transformer的训练策略，避免过度解耦损失交互信息

  - 表征本征维度先增后稳的规律可用于指导LoRA微调推荐大模型时的维度选择与训练停止时机判断'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有Transformer相关研究多聚焦注意力机制优化与下游性能提升，对训练过程中内部表征的几何演化规律缺乏系统性分析，难以支撑模型架构与训练策略优化。
### 方法关键点
TGO-II表征几何分析框架集成CKA、SVCCA、TwoNN-ID、token协方差分析四类工具，针对ViT-Small/16的监督训练过程开展全周期观测。
### 关键结果
- 训练全程CKA、SVCCA指标持续下降，层间表征特化程度逐步提升；
- 表征本征维度先持续上升后稳定，表征流空间自由度逐步扩张后收敛；
- 训练全程token强交互结构始终存在，推翻「表征复杂度提升主要来自token逐步独立」的假设，证明表征复杂度与层特化同步出现，流形扩张无需token解耦。
