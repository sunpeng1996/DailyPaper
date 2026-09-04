---
title: 'Comparing Retrieval Methods for Academic Advisor Discovery: A Six-Method Study
  of 768 CS Faculty Profiles Across 9 US Universities'
title_zh: 学术导师发现场景检索方法对比：针对768份CS教职画像的6种方案测评
authors:
- Biraj Subedi
affiliations:
- Independent Researcher
arxiv_id: '2609.03901'
url: https://arxiv.org/abs/2609.03901
pdf_url: https://arxiv.org/pdf/2609.03901
published: '2026-09-03'
collected: '2026-09-04'
category: RAG
direction: RAG检索模块选型 · 多方案效果对比
tags:
- Retrieval
- BM25
- Semantic Retrieval
- Hybrid Retrieval
- Learning to Rank
one_liner: 对比6类检索方法在学术导师匹配场景的表现，给出选型依据与字段优化结论
practical_value: '- 检索模块选型可参考结论：语义检索>混合检索>BM25>TF-IDF，不确定query域时优先选稳定性最高的BM25

  - 字段优化可复用 ablation 结论：优先保留核心高信息量字段，非核心标签/冗余文本拼接会引入噪声降低检索精度，避免无差别拼接多源文本

  - 多源异质文本的检索融合优先选择 late-fusion 架构，避免直接拼接文本导致的核心信息稀释问题'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有垂直领域检索匹配方案缺乏系统性测评，不同检索方法的效果差异、字段影响无明确可落地的选型依据。

### 方法关键点
针对CS学术导师匹配任务，对比6类检索方法：稀疏 lexical 匹配（Jaccard、TF-IDF、BM25）、密集语义检索（all-MiniLM-L6-v2 句嵌入）、混合分数融合、Learning-to-Rank；构建含768份美国高校CS教职画像的数据集，标注5类学生研究兴趣query对应的162份0/1/2级相关性标签，开展多组ablation实验。

### 关键结果
重排方案NDCG@10最高（0.477），其次是语义检索（0.450）、混合检索（0.421）、BM25（0.406）、Jaccard（0.303）、TF-IDF（0.246）；BM25跨query稳定性最高（std=0.090）；仅用个人简介字段的NDCG（0.634）优于拼接研究领域标签的结果（0.593）；直接拼接arXiv摘要会使NDCG@10下降0.176，验证late-fusion架构必要性。
