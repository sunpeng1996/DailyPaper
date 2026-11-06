---
title: User Embeddings are Superpositions of Interpretable Behavioral Modes
title_zh: 用户嵌入可分解为可解释行为模式的稀疏叠加
authors:
- Jonathan Kozaczuk
- Zheng Dong
- Noyan Evirgen
- Keivan Majidi
- Eddie K. H. Ng
- Chris Porter
- Qi Zhao
- Jia Geng
- Changmao Li
- Brandon R. Feng
affiliations:
- Amazon
arxiv_id: '2611.08487'
url: https://arxiv.org/abs/2611.08487
pdf_url: https://arxiv.org/pdf/2611.08487
published: '2026-11-05'
collected: '2026-11-06'
category: RecSys
direction: 推荐系统 · 用户嵌入可解释性
tags:
- User Embedding
- Sparse Autoencoder
- Interpretability
- Audience Retrieval
- Recommendation System
one_liner: 用稀疏自编码器后 hoc 分解预训练用户嵌入，提取可解释行为模式，支持零样本自然语言受众检索
practical_value: '- 可直接复用后 hoc SAE分解方案，无需修改现有用户嵌入生产链路，低成本实现用户分群、推荐结果可解释性升级，对现有业务侵入性极低

  - 4倍输入维度的过完备SAE+L1稀疏约束的配置可直接复用，在合成/真实电商、内容场景下均能稳定恢复可解释行为模式，效果优于K-Means、ICA等传统方法

  - 可复用「SAE提取模式+LLM自动标注模式语义+自然语言匹配召回受众」的链路，替代传统lookalike需要种子用户的痛点，零样本实现自定义人群圈选'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有推荐/个性化系统核心依赖的用户嵌入是稠密黑盒，无法直接解释推荐理由、审计嵌入包含的用户敏感信息，也无法支持自然语言查询自定义用户群；传统用户分群方法要么需要修改上游嵌入模型训练链路，要么依赖原始交互数据做LLM逐用户标注，成本极高无法在已有生产嵌入体系下落地。

### 方法关键点
- 基于超叠加假设，提出用户嵌入是可解释行为模式的稀疏线性叠加，仅需预训练用户嵌入即可通过过完备稀疏自编码器（SAE）无监督恢复行为模式
- 采用4倍输入维度的过完备ReLU SAE，用L1正则约束隐层稀疏性，解码器列向量对应行为模式的嵌入方向，隐层激活值对应用户在该模式的权重
- 对SAE提取的模式，输入对应高激活用户的交互历史给LLM自动生成自然语言标签，无需人工标注即可实现自然语言查询用户群，整个流程无侵入现有嵌入系统

### 关键实验结果
- 合成数据集上，SAE恢复已知行为模式的准确率比PCA/ICA/K-Means等传统方法高15%-40%，在Transformer编码的用户嵌入上仍能恢复73/75个已知模式
- 电商公开数据集上，零样本自然语言受众检索Lift达1.93×，比FastICA高3.7%，比文本嵌入基线高38.8%；生活事件检索Lift达5.30×，比K-Means高23.5%
- MovieLens数据集上，SAE提取的行为模式冗余度比K-Means低2.2倍，受众覆盖率高16-17个百分点

### 核心结论
用户嵌入的可解释性不需要重建上游训练流程，后 hoc 过完备稀疏分解即可低成本解锁可解释、可查询的用户表示能力。
