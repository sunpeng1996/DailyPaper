---
title: Representational Atoms in Neural Networks
title_zh: 神经网络中的表征原子
authors:
- Chenhui Hu
- Pengfei Cao
- Kang Liu
- Jun Zhao
affiliations:
- 中国科学院自动化研究所复杂系统认知与决策智能重点实验室
- 中国科学院大学人工智能学院
arxiv_id: '2611.14168'
url: https://arxiv.org/abs/2611.14168
pdf_url: https://arxiv.org/pdf/2611.14168
published: '2026-11-10'
collected: '2026-11-12'
category: Other
direction: 神经网络可解释 · 基础表征单元识别
tags:
- Model Interpretability
- Sparse Autoencoder
- Representation Learning
- FRU
- TSAE
one_liner: 定义基础表征单元FRU及两大评估准则，提出基于TSAE的高可靠FRU识别框架
practical_value: '- 可复用TSAE（阈值激活稀疏自编码器）结构拆解推荐/大语言模型的隐层表征，挖掘可解释的语义单元，替代传统黑盒embedding分析方法

  - 高稳定FRU的筛选逻辑可迁移到电商推荐的用户/物品语义特征提纯流程，过滤噪声特征，提升召回排序的泛化性与可解释性

  - FRU跨层语义组合方法可用于优化RAG检索系统的多粒度语义召回架构，提升query与候选内容的语义匹配精准度'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
神经网络内部表征的组织机制不透明，缺乏可严格定义的基础表征单元，无法对齐人类概念结构，制约模型可解释性优化、故障排查等下游应用。
### 方法关键点
1. 正式定义基础表征单元（FRU，即表征原子），明确保真度（表征还原能力）、稳定性（输入扰动下的一致性）两大核心评估准则；
2. 理论证明阈值激活稀疏自编码器（TSAE）在合适参数配置下，可识别高保真、高稳定的FRU；
3. 设计大规模对照实验验证理论结论，系统性分析FRU的语义特性与层级组合规律。
### 关键结果
实验验证TSAE识别FRU的效果显著优于基线方法，高稳定性FRU的单语义性大幅提升，跨层组合可复现与人类概念结构对齐的语义组织，构建了FRU定义、评估、识别的统一框架。
