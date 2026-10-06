---
title: 'SPRIG: Semantic-ID-enhanced Paths for Knowledge Graph-based Generative Recommendation'
title_zh: SPRIG：融合语义ID的知识图谱路径生成式推荐框架
authors:
- Justin Hangoebl
- Marta Moscati
- Alessandro B. Melchiorre
- Shah Nawaz
- Markus Schedl
affiliations:
- Johannes Kepler University Linz
- Albatross AI
- Criteo AI Lab
- Linz Institute of Technology
arxiv_id: '2610.06590'
url: https://arxiv.org/abs/2610.06590
pdf_url: https://arxiv.org/pdf/2610.06590
published: '2026-10-05'
collected: '2026-10-06'
category: GenRec
direction: 生成式推荐 · Semantic ID+KG路径推理
tags:
- Generative Recommendation
- Semantic ID
- Knowledge Graph
- Path Reasoning
- Transformer Decoder
one_liner: 将Semantic ID与知识图谱路径推理融合，打造参数更高效的生成式推荐框架
practical_value: '- 可直接复用分层Semantic ID替换传统原子item ID的思路，将商品/内容特征量化为固定长度的离散码，大SKU池下词表压缩率可达20倍以上，彻底解决生成式推荐词表随SKU线性膨胀的问题

  - 两阶段训练范式可直接迁移：先用全量KG随机路径做无监督预训练吸收结构化知识，再用用户交互路径微调适配推荐任务，实测相比纯微调方案提升冷启动场景下的泛化能力

  - 工程落地优先选用残差K-means做SID量化，效果略优于RVQ/RQ-VAE（误差约1%），且SID效果与底层商品/内容特征质量强相关，优先选用高区分度的预训练嵌入生成SID

  - 可解释生成式推荐场景可基于该框架迭代，后续对齐SID分层码与商品属性标签，即可生成带属性维度的推荐理由路径，兼顾推荐效果与可解释性'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前生成式推荐存在两条并行技术路线：一是用Semantic ID替换原子item ID，解决传统ID不透明、词表随SKU线性膨胀的问题；二是基于知识图谱路径推理做生成式推荐，注入结构化关系、提升可解释性。两者存在互补缺陷：SID类模型缺结构化关系grounding，泛化性不足；KG类生成式推荐仍采用原子item ID，无法实现跨相似item的参数共享，大SKU池下效率极低。

### 方法关键点
- 离线量化：采用残差K-means将item的内容预训练嵌入量化为3层、每层256个码的分层Semantic ID，相似item共享前缀，天然支持跨item参数共享
- 路径改写：将KG路径中的所有item实体替换为对应的SID序列，构建统一词表，item相关词表固定为768，完全与SKU规模解耦
- 两阶段训练：第一阶段用不含用户交互的通用KG路径预训练因果Transformer解码器，学习全局结构化关系；第二阶段用用户到item的交互路径微调，适配推荐任务
- 推理逻辑：给定用户前缀自回归生成SID序列，逆映射回对应item，按路径对数似然排序得到推荐结果

### 关键实验
在MovieLens-1M（电影）、Onion（音乐）两个数据集上验证，对比SASRec、OpenP5、TIGER、KGGLM等基线：相比直接基线KGGLM，ML-1M上nDCG@10提升44%，Onion上提升58%，所有指标提升均统计显著；参数规模比KGGLM小19%，单步FLOP降低近50%；Onion数据集上SID词表相比原子ID压缩24倍，无精度损失。

### 核心结论
Semantic ID与知识图谱路径推理高度互补，两者结合可同时实现生成式推荐的效果提升、参数效率提升、词表规模与SKU规模完全解耦。
