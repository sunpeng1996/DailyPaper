---
title: 'C$^{2}$R: Cross-sample Consistency Regularization Mitigates Feature Splitting
  and Absorption in Sparse Autoencoders'
title_zh: C²R：跨样本一致性正则缓解稀疏自编码器的特征分裂与吸收
authors:
- Haoran Jin
- Xiting Wang
- Shijie Ren
- Hong Xie
- Defu Lian
affiliations:
- University of Science and Technology of China
- State Key Laboratory of Cognitive Intelligence
- Gaoling School of Artificial Intelligence, Renmin University of China
arxiv_id: '2606.30609'
url: https://arxiv.org/abs/2606.30609
pdf_url: https://arxiv.org/pdf/2606.30609
published: '2026-06-29'
collected: '2026-06-30'
category: Training
direction: 稀疏自编码器训练 · 正则化优化
tags:
- SAE
- Regularization
- LLM Interpretability
- Feature Learning
- Training Optimization
one_liner: 提出跨样本一致性正则C²R，解决稀疏自编码器特征分裂与吸收问题，提升隐语义可靠性
practical_value: '- 电商/推荐场景下用SAE做用户/物品稀疏语义特征提取时，可引入C²R正则减少语义特征碎片化，提升召回、排序模块的特征一致性

  - 搭建RAG语义召回模块时，用C²R优化的SAE处理query、doc的embedding，降低同一语义映射到多隐向量的问题，提升召回准确率

  - 做LLM Agent可解释性分析时，用C²R优化的SAE拆解模型激活层，可得到更可靠的原子语义特征，辅助Agent决策链路归因'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
Sparse Autoencoders (SAEs) 是LLM可解释性分析的主流工具，可将模型激活值拆解为人类可理解的稀疏特征，但在大字典规模下存在两大痛点：① 特征分裂：同一连贯语义概念被碎片化映射到多个非原子隐向量；② 特征吸收：通用特征中混入大量任意例外，二者共同导致隐语义可靠性大幅下降，根源是单样本优化缺少跨样本隐向量分配约束，同一概念会被不一致地分配到多个冗余/干扰隐向量。

### 方法关键点
提出C²R（Cross-sample Consistency Regularization）正则策略，在batch维度惩罚方向相似的隐向量共激活，强制同一语义特征在跨样本时始终映射到统一隐向量。

### 关键结果
对比现有主流SAE约束（ℓ1、TopK、Batch TopK、Matryoshka、Ort等），C²R是唯一同时从理论上解决特征分裂、吸收问题，且100%保留重建精度的方案，无模型性能损耗。
