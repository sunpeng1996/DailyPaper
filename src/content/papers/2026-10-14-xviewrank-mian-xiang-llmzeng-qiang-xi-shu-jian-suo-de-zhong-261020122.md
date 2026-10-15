---
title: 'XViewRank: Overlap-Conditioned Score Fusion for LLM-Augmented Sparse Retrieval'
title_zh: XViewRank：面向LLM增强稀疏检索的重叠条件分数融合方法
authors:
- Xinxuan Lv
- Minghan Li
- Guodong Zhou
affiliations:
- Soochow University
arxiv_id: '2610.20122'
url: https://arxiv.org/abs/2610.20122
pdf_url: https://arxiv.org/pdf/2610.20122
published: '2026-10-14'
collected: '2026-10-15'
category: RecSys
direction: 稀疏检索 · 多视图分数融合优化
tags:
- Sparse Retrieval
- Query Expansion
- Rank Fusion
- LLM4Rec
- BM25
one_liner: 以查询视图结果重叠为上下文，自适应融合多视图BM25结果，性能超固定融合策略
practical_value: '- 电商搜索场景可直接复用多query视图生成逻辑：原query+LLM生成的假设答案视图+抽象step-back视图，覆盖不同匹配维度，无需修改倒排索引，落地成本低

  - 融合阶段可借鉴重叠条件的轻量融合设计：无需复杂语义重排，仅用各视图归一化BM25分数+视图结果集Jaccard重叠特征，用极小MLP做融合， latency增加可忽略，性能优于RRF/CombSUM等固定融合策略

  - 可做场景化降本适配：针对低视图重叠的query（短query、歧义query）触发融合逻辑，高重叠query用固定融合策略，平衡收益与成本

  - 跨垂类迁移成本低：仅需源域少量标注数据训练融合MLP，小数据集可零-shot迁移，适合电商多行业垂类搜索快速适配'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
LLM生成多查询视图可有效解决稀疏检索的词表不匹配问题，但现有多视图融合方法存在明显缺陷：固定权重融合（RRF、CombSUM）无法适配不同query的视图互补/冗余差异，语义重排类方法会大幅增加latency，难以在检索侧实现轻量自适应融合。

### 方法关键点
- 多视图生成：每个原始query对应三个检索视图：原query、LLM生成的假设视图（模拟答案段落匹配具体词汇）、step-back抽象视图（提炼上层概念匹配更广范围内容）
- 特征构造：每个候选对应6维特征：3个视图的归一化BM25分数 + 3组视图两两top-500结果的Jaccard重叠度（query级全局特征，同query所有候选共享）
- 融合模型：采用2层极小MLP（128→64隐藏层）做非线性融合，利用重叠度作为上下文动态调整不同视图分数的权重，无需对query和文档做联合语义编码
- 训练策略：采用query平衡的加权二分类交叉熵，缓解稀疏检索正负样本不均衡问题，正样本权重根据其在三个视图中的最高排名动态调整

### 关键结果
在MS MARCO passage数据集上测试，TREC DL 2019上比匹配输入的RRF基线提升nDCG@10 +0.0207、MAP +0.0212（p<0.05）；TREC DL 2020上提升nDCG@10 +0.0098、MAP +0.0081；在低视图重叠的query子集上，nDCG@10相对RRF提升达+0.0422，MAP提升+0.0338；零-shot迁移到FiQA、NFCorpus数据集也超过所有固定融合基线。

**最值得记住的结论**：多视图LLM查询扩展的收益不仅来自生成高质量视图，更来自对不同视图检索证据的保留和自适应条件融合。
