---
title: 'TRWH: A Text-Driven Random Walk Heterogeneous GNN for Semantic-Aware Sparse
  Recommendation'
title_zh: TRWH：文本驱动随机游走异质GNN的语义感知稀疏推荐方法
authors:
- He Ma
- Chen Liu
affiliations:
- The University of Sydney
- Nankai University
arxiv_id: '2607.25471'
url: https://arxiv.org/abs/2607.25471
pdf_url: https://arxiv.org/pdf/2607.25471
published: '2026-07-28'
collected: '2026-07-29'
category: RecSys
direction: 稀疏推荐 · LLM与异质GNN融合
tags:
- Heterogeneous GNN
- Random Walk
- Sparse Recommendation
- LLM Embedding
- Semantic Awareness
one_liner: 融合LLM语义特征与异质GNN结构，优化稀疏推荐，验证随机游走对不同嵌入的差异化影响
practical_value: '- 结构增广适配策略：业务中如果用LLM生成的高语义精度用户/物品嵌入，不要盲目加随机游走类的图增广操作，避免语义被邻域噪声稀释；如果用Word2Vec等浅语义嵌入，新增1-hop随机游走生成的二阶用户/物品关联边，可显著提升稀疏场景下的推荐效果

  - 异质图边类型可复用：电商推荐的异质图可新增多类业务边，除常规购买/评分/评论边外，可加同店铺物品关联边、基于交互的二阶用户相似边，充分挖掘稀疏场景下的关联信号

  - LLM profile生成方案可落地：生成用户/物品语义profile时，给LLM添加明确的推理步骤要求，输入结构化的用户交互历史/评论、物品属性/用户评价，再用instruction-tuned文本嵌入模型转向量，可有效降低幻觉，提升语义特征的准确性

  - 目标导向选型：如果业务核心是降低极端预测误差（如避免给用户推完全不感兴趣的商品）优先选LLM语义嵌入方案；如果核心是降低整体平均误差，优先选浅嵌入加随机游走增广的方案，匹配业务目标做选型'
score: 9
source: arxiv-cs.MM
depth: full_pdf
---

### 动机
传统GNN推荐依赖交互结构缺语义信号，LLM推荐有语义但缺协同结构信息，稀疏场景下两者融合存在语义易稀释、结构增广效率低的痛点，现有方案无法兼顾两种模态的优势。
### 方法关键点
- 嵌入层双路径设计：分别采用Word2Vec（基于物品标题、用户评论训练）和LLM（Llama-3.2-3B-Instruct，结构化prompt引导生成带推理的用户/物品profile，经instructor-xl转嵌入）生成节点初始特征
- 多关系异质GNN：整合9类边（评分、评论、购买、同店物品关联、1-hop随机游走生成的二阶用户-用户/物品-物品边等），采用简化消息传播机制，去掉非线性变换提升训练效率
- 可控随机游走增广：仅在用户-物品交互边上做1-hop游走生成二阶关联边，避免多跳游走带来的噪声扩散和语义漂移
### 关键结果
在Amazon 2023极稀疏的Fashion（2M用户、825K物品，户均交互1.23次）、Beauty（631K用户、112K物品，户均交互1.11次）数据集上，对比MF、P5、ChatGPT few-shot等10+SOTA基线，Fashion数据集RMSE最高降80.0%、MAE最高降52.6%，Beauty数据集RMSE提升25.7%、MAE提升10.8%。
### 核心洞察
随机游走结构增广的效果完全依赖初始嵌入的语义精度：对Word2Vec类浅嵌入提效显著，对LLM生成的高精细语义嵌入反而会稀释特征精度，导致效果下降。
