---
title: Monosemanticity in Recommender Systems
title_zh: 推荐系统中的单语义性研究
authors:
- Yagel Alfasi
- Eden Rzezak
- Eadan Schechter
affiliations:
- School of Industrial & Intelligent Systems Engineering, Tel Aviv University
arxiv_id: '2606.29341'
url: https://arxiv.org/abs/2606.29341
pdf_url: https://arxiv.org/pdf/2606.29341
published: '2026-06-28'
collected: '2026-06-30'
category: RecSys
direction: 推荐系统可解释性 · 隐特征解析
tags:
- Monosemanticity
- Sparse Autoencoder
- Collaborative Filtering
- Interpretability
- Matrix Factorization
one_liner: 用Matryoshka稀疏自编码器从协同过滤嵌入提取可解释单语义隐特征
practical_value: '- 电商推荐可借鉴该方法从预训练协同过滤嵌入中提取可解释语义特征，支撑合规审计、用户偏见排查和定向干预

  - 针对标准SAE缩放时的特征退化问题，可复用MSAE的分层训练架构规避缺陷

  - 可结合LLM对提取出的隐特征自动打标签，降低人工解释特征的成本'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：传统隐因子模型（如矩阵分解）是推荐系统的常用方法，但学到的稠密嵌入维度缺乏明确语义解释，不透明性限制了推荐的透明度、可解释性和可控干预。近年稀疏自编码器（SAEs）被用于从稠密神经表示提取单语义特征，但标准SAEs随字典规模增大，会出现特征分裂、特征吸收、特征组合等缩放退化问题，损害可解释性。

**方法关键点**：针对协同过滤嵌入，探究分层稀疏表示能否暴露可解释结构；先在Amazon Fashion数据集训练大规模矩阵分解推荐模型，再将Matryoshka Sparse Autoencoder (MSAE)应用于学到的嵌入；通过元数据对齐、LLM生成标签评估隐特征的语义一致性与解耦性，还对分析得到的性别相关隐神经元完成定向干预。

**关键结果**：证实协同过滤嵌入中存在可恢复的分层结构，Matryoshka训练是暴露交互驱动推荐模型中可解释隐因子的有效机制，可支持对推荐行为的可控干预。
