---
title: 'Not All Branches Are Equal: Adaptive Semantic ID Construction for Generative
  Recommendation'
title_zh: 面向生成式推荐的自适应分支语义ID构建方法
authors:
- Guy Hadad
- Haggai Roitman
- Bracha Shapira
affiliations:
- Ben-Gurion University of the Negev
arxiv_id: '2611.11549'
url: https://arxiv.org/abs/2611.11549
pdf_url: https://arxiv.org/pdf/2611.11549
published: '2026-11-08'
collected: '2026-11-10'
category: GenRec
direction: 生成式推荐 · Semantic ID 构造
tags:
- Generative Recommendation
- Semantic ID
- Hierarchical Clustering
- Tokenization
- Adaptive Branching
one_liner: 提出自适应轮廓树AST构造层次化语义ID，较现有基线平均提升13%以上
practical_value: '- 语义ID构造可直接复用AST思路，替换现有固定分支残差量化方案，按局部轮廓系数动态调整分支数的层次聚类，保证相似商品共享更长前缀，提升生成式推荐解码准确率

  - 电商长尾场景可启用AST-V2约束变体，给每个分支设置最小交互占比阈值，用MILP求解分配，避免低支持度前缀带来的训练不充分问题，平衡头尾部推荐效果

  - 新商品冷启可复用AST的贪心树遍历分配逻辑，仅需比较每层聚类中心即可生成有效语义ID，无需重新训练全量tokenizer，适配电商商品快速上新需求

  - AST对嵌入backbone依赖更低，业务落地时可搭配现有轻量文本嵌入模型使用，无需额外优化嵌入侧即可拿到ID构造的性能收益'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有生成式推荐的语义ID普遍基于残差量化实现，默认各层token语义独立；但实证发现语义ID是前缀依赖的层次化路径，固定分支的量化逻辑与该隐含结构不匹配，存在代码本利用率低、无效解码路径多、长尾商品学习不充分等问题。
### 方法关键点
- 提出**Adaptive Silhouette Tree (AST)**：采用自顶向下的分裂式层次聚类构造语义ID，每个节点根据局部数据的轮廓系数最优值动态选择分支数，密集语义区域细分、同质区域粗分，保证相似商品共享更长前缀
- 推出两类约束变体：AST-V1基于KMeans中心用MILP修正分配，满足最小交互质量阈值；AST-V2全程融入商品交互权重，用加权轮廓系数打分+迭代优化，避免低支持度前缀导致的训练不充分
- 最终token按桶内商品排序分配保证全局唯一，冷启新商品可通过贪心遍历树的最近聚类中心快速生成语义ID，无需全量重训
### 关键实验结果
在5个Amazon Review电商数据集上对比11种主流语义ID构造基线（RQ-VAE、SEATER、RRS等），AST-V2较最优非AST基线平均提升13.08%，头尾部性能均位于帕累托前沿，对不同嵌入backbone的鲁棒性显著优于基线。
### 核心结论
生成式推荐的语义ID本质是层次化树路径而非独立token集合，前缀依赖的自适应构造是性能提升的核心来源
