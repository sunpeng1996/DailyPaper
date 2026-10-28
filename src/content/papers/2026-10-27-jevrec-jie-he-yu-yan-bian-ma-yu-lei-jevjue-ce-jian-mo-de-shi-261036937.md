---
title: 'JevRec: Linguistic Encoding with Jev-like Decision Modeling for LLM-based
  Generative Recommendation'
title_zh: JevRec：结合语言编码与类Jev决策建模的LLM生成式推荐框架
authors:
- Qiyong Zhong
- Jiajie Su
- Ming Yang
- Li Zhang
affiliations:
- Zhejiang University
arxiv_id: '2610.36937'
url: https://arxiv.org/abs/2610.36937
pdf_url: https://arxiv.org/pdf/2610.36937
published: '2026-10-27'
collected: '2026-10-28'
category: GenRec
direction: 生成式推荐 · 可变长度Semantic ID
tags:
- Generative Recommendation
- Semantic ID
- LLM4Rec
- Variable Length Tokenization
- Sequential Recommendation
one_liner: 为商品分配频率感知可变长度Semantic ID，用双输出头消解梯度冲突提升生成式推荐性能与效率
practical_value: '- 可直接复用频率感知可变长SID设计：按商品交互频率分3-5档，热门品用短SID降低推理延迟，长尾品用长SID保留语义，适配电商千万级SKU场景的性能效率平衡需求

  - 双输出头架构可迁移：将序列生成的长度预测与内容预测解耦，共享上游编码、独立下游头的设计，可直接用于缓解生成式推荐、多任务生成场景的梯度冲突问题

  - 推理侧优化无需改模型：长度概率配额分配+跨分支联合得分排序的策略，可直接叠加到现有生成式推荐推理流程，零训练成本提升TopK推荐准确率'
score: 10
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有生成式推荐普遍采用固定长度Semantic ID（SID），热门商品频繁生成长ID重复消耗算力，若统一缩短SID长度又会损失长尾商品的语义表征能力；同时长度预测与内容生成共享同一个输出头，存在持续梯度冲突，同时制约效果与效率。
### 方法关键点
- 语言编码：按商品训练集交互频率分档，热门商品分配更短SID、长尾商品保留更长语义编码，所有商品共享残差量化码本，末尾追加冲突消解token保证SID全局唯一
- 类Jev决策建模：共享用户交互历史编码，用独立MLP头预测SID长度分布，内容生成头基于给定长度条件生成对应SID，消解两个任务的梯度冲突
- 长度感知推理：按长度概率分配各分支的候选配额，各分支独立生成候选后按「长度概率+内容生成概率」的联合得分跨分支排序，输出最终推荐列表
### 关键结果
在3个Amazon公开数据集（乐器、工业科学、游戏）上对比13个基线（含TIGER、ActionPiece等SOTA生成式推荐模型），所有12组指标均排名第一，相对SOTA平均提升6.52%，Recall@5最高提升9.86%；相比TIGER训练时间平均降低15.75%，推理速度最高提升16%，收敛速度快20个epoch。
### 核心结论
借鉴自然语言高频词更短的规律设计频率感知可变长度Semantic ID，是同时提升生成式推荐效果与效率的低门槛优化路径
