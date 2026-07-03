---
title: 'Bi-NAS: Towards Effective and Personalized Explanation for Recommender Systems
  via Bi-Level Neural Architecture Search'
title_zh: Bi-NAS：基于双层神经架构搜索的推荐系统个性化解释框架
authors:
- Longfeng Wu
- Yao Zhou
- Tong Zeng
- Zhimin Peng
- Bhanu Pratap Singh Rawat
- Lecheng Zheng
- Giovanni Seni
- Dawei Zhou
affiliations:
- Virginia Tech
- Google
- Amazon
arxiv_id: '2607.01387'
url: https://arxiv.org/abs/2607.01387
pdf_url: https://arxiv.org/pdf/2607.01387
published: '2026-07-01'
collected: '2026-07-03'
category: RecSys
direction: 可解释推荐 · 神经架构搜索
tags:
- Explainable Recommendation
- Neural Architecture Search
- Cross Attention
- Feature Interaction
- LLM
one_liner: 通过双层NAS自动优化跨注意力与特征交互，结合LLM生成低幻觉高准确率的推荐解释
practical_value: '- 可复用用户/物品细粒度特征计算方法：基于评论的(Aspect, Opinion, Sentiment)三元组生成用户偏好向量、物品质量向量，比纯行为特征解释性更强，可直接接入现有推荐解释模块

  - 轻量NAS落地方案：仅将跨注意力结构、特征交互算子作为搜索空间（共72种候选），用可微松弛将离散搜索转为连续梯度优化，计算成本远低于传统NAS，适合中小业务快速适配不同品类数据集

  - 解决LLM推荐解释幻觉的trick：不直接让LLM生成解释，先输出用户-物品对齐的核心特征再喂入LLM做零样本生成，既保证解释事实准确，又兼顾自然语言流畅度

  - 不同品类架构选型参考：小数据集选3输入（用户特征+物品特征+物品ID）、用Plus算子；大数据集选Concat/Multiply算子，可直接复用该结论优化现有可解释推荐架构'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有可解释推荐依赖专家手工设计注意力、交互结构，跨品类泛化性差、适配成本高；直接用LLM生成解释易出现幻觉、事实不准、个性化不足，既降低用户信任，也影响转化效率。
### 方法关键点
- 从用户评论抽取(Aspect, Opinion, Sentiment)三元组，计算用户偏好向量（基于特征提及频次）、物品质量向量（基于特征提及频次+平均情感），映射到[0,T]区间
- 双层NAS搜索空间：内层搜索4种跨注意力结构（用户/物品独立建模、用户特征全局影响、物品特征全局影响、交叉影响），外层搜索3种特征交互算子（Plus/Multiply/Concat），总候选仅72种；采用可微松弛将离散搜索转为连续梯度优化，大幅降低计算成本
- LLM解释生成：基于NAS输出的用户-物品对齐核心特征，用零样本prompt调用Llama-3.1-8B生成自然语言解释，从根源避免事实幻觉
### 关键实验
在Amazon 4个公开数据集（Instrument/Video/Beauty/Clothing）上对比NCF、VBPR、CER、NAR、MANAS等基线：推荐效果上，Hit@10最高提升15.1%（Instrument数据集，0.342 vs 基线最高0.284），NDCG@10最高提升25.8%；解释效果上，F1最高提升15.5%，Precision最高提升19.3%，全面优于基线。
### 核心结论
不存在适配所有场景的最优可解释推荐架构，针对不同品类数据集自动搜索跨注意力与交互结构，比人工设计的固定架构效果更优
