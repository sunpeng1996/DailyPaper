---
title: Tracing Query Expansion Effects through Sparse Autoencoder Features
title_zh: 基于稀疏自编码器特征的查询扩展效果追踪研究
authors:
- Fangan Dong
- Weiran Shi
- Zhiwei Xu
- Xuri Ge
- Ben He
- Xin Xin
- Zhumin Chen
- Ying Zhou
affiliations:
- Shandong University
- University of Chinese Academy of Sciences
- Institute of Software, Chinese Academy of Sciences
arxiv_id: '2609.06968'
url: https://arxiv.org/abs/2609.06968
pdf_url: https://arxiv.org/pdf/2609.06968
published: '2026-09-07'
collected: '2026-09-09'
category: QueryRec
direction: 查询扩展 · 稀疏自编码器可解释性
tags:
- QueryExpansion
- SparseAutoencoder
- DenseRetrieval
- ActivationSteering
- Interpretability
one_liner: 利用SAE追踪密集检索器中QE的内部特征变化，通过激活steering无需微调提升检索效果
practical_value: '- 电商搜索Query扩展场景可复用SAE分析框架，识别有效QE对应的特征维度，避免传统文本扩展易出现的语义漂移问题，无需改写Query即可提效

  - 可复用激活steering工程方案，针对离线挖掘的有效特征维度，推理时直接叠加定向偏移向量，无需重训召回/检索模型，上线成本极低

  - 搜索拼写纠错、Query扰动降噪场景可复用该方法，提取有害扰动对应的latent特征，推理时反向叠加向量抵消噪声影响，提升鲁棒性

  - 密集召回模型可解释性分析可复用层维度SAE拆解方法，识别中深层与检索意图/实体属性强相关的特征维度，指导后续模型优化'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统Query Expansion（QE）在稀疏检索中效果明确，但在现有密集检索系统中效果不稳定，甚至常出现负向收益；现有研究大多仅关注最终检索指标或embedding全局偏移，无法解释QE在检索模型内部的特征变化机制，难以为QE优化提供落地指导。

### 方法关键点
- 为密集检索器的每一层独立训练BatchTopK SAE，将层输出的稠密表示拆分为可解释的稀疏激活特征，SAE重构后的embedding几乎不损失原有检索效果
- 收集2000组QE后检索效果正向的Query对，对比原始Query和扩展Query的层稀疏激活差异，用Cohen's d筛选与QE强相关的latent特征
- 推理时无需改写Query，仅在对应层输出叠加由QE相关latent的decoder权重加权得到的steering向量，即可定向优化Query表示

### 关键实验结果
在MS MARCO、Natural Questions、TREC DL 19/20四个基准上测试，对比Q2D、Q2E、Q2C三类主流QE方法：传统QE方法普遍不稳定，多数场景低于基线，最多在MS MARCO上降3.5个MRR@10；SAE steering实现全场景稳定正向收益，在SimLM检索器上TREC DL 19、20的NDCG@10分别提升1.503、1.404个点，所有指标均超过基线和三类QE方法。

最值得记住的结论：QE的效果不只取决于扩展文本的表面语义，更取决于检索模型内部对扩展内容的编码特征，通过SAE定向调整内部特征比直接改写Query更稳定可控
