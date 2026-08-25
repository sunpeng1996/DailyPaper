---
title: 'Rethinking Item Tokenization in Generative Recommenders: From Fixed Atoms
  to Semantic Subwords'
title_zh: 生成式推荐物品Tokenization优化：从固定原子到语义子词
authors:
- Xinrui Miao
- Mingjia Yin
- Jiaqing Zhang
- Wei Guo
- Yong Liu
- Yuyang Ye
- Hao Wang
- Enhong Chen
affiliations:
- University of Science and Technology of China
- Huawei Technologies
arxiv_id: '2608.22734'
url: https://arxiv.org/abs/2608.22734
pdf_url: https://arxiv.org/pdf/2608.22734
published: '2026-08-24'
collected: '2026-08-25'
category: GenRec
direction: 生成式推荐 · Semantic ID Tokenization
tags:
- Generative Recommendation
- Semantic ID
- Tokenization
- Attention Optimization
- Sequential Recommendation
one_liner: 提出不对称语义子词Tokenization方案SST，缓解生成式推荐历史侧组内注意力过载，保留目标解码稳定性
practical_value: '- 架构选择：采用不对称Tokenization设计，历史侧做语义压缩优化，目标侧保留固定长度SID，既降低编码器负担又保证解码稳定性，无需修改原有解码链路

  - 方法Trick：可直接复用IST组件，基于现有固定长度SID，用BPE/WordPiece/CondEntropy规则合并高频共现的相邻原子Token为语义子词，缩短历史序列长度降低注意力开销

  - 数据增强：复用BCA组件，挖掘用户序列中高频语义前缀跳转对做样本增强，可引导模型关注跨物品行为规律，同时缓解长尾曝光不足问题

  - 工程落地：SST与现有主流生成式推荐Backbone完全兼容，无系统性耗时增加，可作为增量优化模块直接嵌入现有GenRec链路'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前基于Semantic ID的生成式推荐普遍采用固定长度原子Token序列表示物品，历史侧将用户交互序列展开后，编码器需要消耗大量注意力在同物品的原子Token重组任务上，即组内注意力过载，挤占了跨物品行为规律建模的容量。现有变长SID优化方案仅关注物品标识的区分度，未解决该注意力浪费问题，限制了推荐效果的进一步提升。
### 方法关键点
- 不对称Tokenization设计：仅优化历史侧的Token表示，目标侧始终保留固定长度SID，不破坏原有解码逻辑的稳定性
- Item-level Subword Tokenization（IST）：借鉴NLP子词Tokenization思路，基于SID语料统计，按照BPE/WordPiece/CondEntropy规则合并高频、高语义耦合的相邻原子Token为语义子词，缩短历史序列长度，将低阶原子共现规则直接编码到Token结构中，降低编码器重组负担
- Behavior-induced Co-occurrence Augmentation（BCA）：挖掘用户行为序列中的高频语义前缀跳转对，生成对应增强样本注入训练，引导IST释放的注意力容量聚焦于跨物品的高阶行为规律建模
### 关键结果
在Amazon Beauty、Instruments、Yelp三个公开数据集上，面向TIGER-KM、TIGER-VAE、LETTER三个主流生成式推荐Backbone测试，SST相对最优基线的HR@10提升1.3%-6.7%，NDCG@10提升3%-10.1%；组内注意力开销平均降低15%以上，训练推理整体耗时无显著增加，同时可提升长尾物品的推荐效果。
### 核心结论
生成式推荐中SID的历史侧编码功能与目标侧解码功能不需要对齐，分别优化才能兼顾建模效率和生成稳定性
