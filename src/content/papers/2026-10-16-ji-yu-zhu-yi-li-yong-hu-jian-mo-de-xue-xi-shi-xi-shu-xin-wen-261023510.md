---
title: 'LSNR: Learned Sparse News Recommendations with Attentive User Modeling'
title_zh: 基于注意力用户建模的学习式稀疏新闻推荐方法LSNR
authors:
- David Vos
- Andrew Yates
- Maarten de Rijke
affiliations:
- University of Amsterdam
- Johns Hopkins University
arxiv_id: '2610.23510'
url: https://arxiv.org/abs/2610.23510
pdf_url: https://arxiv.org/pdf/2610.23510
published: '2026-10-16'
collected: '2026-10-19'
category: RecSys
direction: 稀疏推荐 · 用户兴趣建模
tags:
- News Recommendation
- Learned Sparse Retrieval
- User Modeling
- Attention Mechanism
- SPLADE
one_liner: 提出单文独立编码+注意力聚合的稀疏新闻推荐模型，解决历史拼接的两大瓶颈
practical_value: '- 长文本内容（商品详情、攻略、长文案）推荐场景，可复用「单内容独立编码+注意力聚合」架构，避免用户历史拼接导致的上下文窗口溢出和兴趣坍缩问题

  - 冷启动/短历史用户推荐场景，可尝试学习式稀疏表示方案，相比密集表示在数据不足时更稳定，文中短历史场景下NDCG@10比SOTA密集推荐高2.5%~2.7%

  - 需降低推荐系统索引存储成本时，可参考双路径稀疏编码设计，索引大小比未压缩密集基线小一个数量级，效果损失可控

  - 用户兴趣聚合模块优先选用无位置编码的注意力机制，新闻/内容场景下时序位置信号反而会损害效果，无参数池化效果远低于学习式注意力'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有学习式稀疏推荐方法（如STAR）直接拼接用户交互历史为单文本，在长文本内容推荐场景存在两大瓶颈：一是拼接会抹平用户多元兴趣，无法区分不同历史内容的权重；二是长文本拼接极易超出LLM上下文窗口，强制截断会严重损失效果。同时新闻/内容场景冷启动、短历史用户占比高，密集推荐模型在这类场景下易出现语义漂移，鲁棒性不足。

### 方法关键点
- 新闻编码器：基于SPLADE同时输出单篇内容的稀疏词汇表示（用于检索打分）和辅助密集表示（用于用户侧聚合），候选内容的稀疏表示可预计算后离线存储
- 用户编码器：双路径聚合架构：① 词汇路径：用注意力对历史内容的稀疏表示加权求和，保留单篇内容的直接词汇信号；② 语义路径：将注意力加权后的密集用户表示投影为稀疏向量，实现用户级语义扩展；最终用户稀疏向量为两路输出之和
- 训练推理：用用户与候选稀疏向量的内积打分，可基于倒排索引高效检索，训练时用LFLOPS正则约束表示稀疏度，平衡效果和存储效率

### 关键实验结果
在MIND、EBNeRD两个公开新闻推荐数据集验证：
1. 比稀疏基线STAR的NDCG@10提升11%，短历史（仅1条交互）场景下仍领先3.6%~7%
2. 全历史场景下和SOTA密集推荐模型效果相当，短历史场景下NDCG@10比密集基线高2.5%~2.7%
3. 索引大小比未压缩密集基线小一个数量级，用户编码速度比STAR快7倍

### 核心结论
学习式稀疏推荐的核心瓶颈不是上下文窗口限制，而是历史交互的聚合方式，独立编码+注意力加权的双路径架构能同时兼顾效果、存储效率和冷启动鲁棒性
