---
title: 'Item Representations Matter: Bridging Hard Semantic IDs and Soft Prototype
  Mixtures for Generative Retrieval'
title_zh: 生成式检索优化：桥接硬语义ID与软原型混合的物品表示
authors:
- Vicente Balmaseda
- Dongqi Fu
- Jiarui Feng
- Ren chen
- Hanqing Zeng
- Tianxin Wei
- Yinglong Xia
- Tianbao Yang
- Hong Li
affiliations:
- Meta
- Texas A&M University
arxiv_id: '2611.05799'
url: https://arxiv.org/abs/2611.05799
pdf_url: https://arxiv.org/pdf/2611.05799
published: '2026-11-04'
collected: '2026-11-05'
category: GenRec
direction: 生成式推荐 · 物品表示优化
tags:
- Generative Retrieval
- Semantic ID
- Item Representation
- Flow Matching
- Recommendation
one_liner: 提出CAP-Mix软原型混合物品表示，同时提升生成式推荐的精度与推理效率
practical_value: '- 物品表示优化：可直接替换现有生成式推荐的平层item lookup表，用「软原型混合+item独有向量」结构，既保留跨item参数共享提升泛化性，又避免硬SID的量化损失，长尾/冷启动item收益显著

  - 工程落地友好：推理阶段预计算所有item的混合embedding，无额外查询开销，吞吐量比离散SID类生成式推荐模型高1.4~161倍，可直接适配现有大规模推荐召回链路

  - 预训练资产复用：支持无缝接入已有离线SID作为软分配先验、或商品图文预训练embedding初始化item独有向量，不需要重构现有预训练流程，迁移成本极低'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前生成式检索技术分为两条路线：离散路线用Semantic ID（SID）实现跨物品参数共享，提升泛化性，但硬量化会丢失原始内容嵌入信息、容易出现ID碰撞；连续路线避免了量化损失，但物品嵌入采用独立平层表，无跨物品参数共享，长尾物品泛化性差，亟需同时兼顾二者优势的物品表示方案。

### 方法关键点
- 核心表示设计：每个物品的最终嵌入由两部分加权相加：共享原型的软混合结果（实现跨物品参数共享）、物品独立训练的独有向量（保留个性化信息，避免量化损失），所有参数端到端联合训练，推理阶段保留软权重不做离散化
- 兼容多类预训练资产：支持三种训练模式：从零开始仅用交互数据训练、接入离线预训练SID作为软分配先验、用物品内容预训练嵌入初始化独有向量，可灵活适配不同业务的资产储备情况
- 训练优化：新增代码匹配损失和原型利用率正则，避免训练过程中参数共享通道失效，保证原型的有效利用

### 关键实验
在Amazon Beauty/Industrial/Office、Steam、MovieLens-1M、Yelp共6个公开数据集上测试，对比FlowRec、TIGER、MaskGR等SOTA生成式推荐基线，平均HR@5相对提升6.9%，NDCG@5相对提升13.6%；推理吞吐量是离散SID类基线的1.4~161倍；仅用离线SID输入时，比同tokenizer构建的硬SID表HR@5高4.45%~14.9%。

### 核心结论
生成式推荐的物品表示无需在「离散共享」和「连续独立」间做取舍，软原型混合结构可同时获得二者的性能和效率收益
