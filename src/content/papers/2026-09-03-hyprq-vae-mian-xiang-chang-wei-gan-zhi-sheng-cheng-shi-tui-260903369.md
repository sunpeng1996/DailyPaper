---
title: 'HypRQ-VAE: Hyperbolic Item Indexing for Long-Tail-Aware Generative Recommender
  Systems'
title_zh: HypRQ-VAE：面向长尾感知生成式推荐的双曲空间物品索引方法
authors:
- Longfeng Wu
- Tong Zeng
- Giovanni Seni
- Zhimin Peng
- Bhanu Pratap Singh Rawat
- Si Zhang
- Yao Zhou
- Lecheng Zheng
- Bo Ji
- Yujun Yan
affiliations:
- Virginia Tech
- Amazon
- Meta AI
- Google
- Dartmouth College
arxiv_id: '2609.03369'
url: https://arxiv.org/abs/2609.03369
pdf_url: https://arxiv.org/pdf/2609.03369
published: '2026-09-03'
collected: '2026-09-04'
category: GenRec
direction: 生成式推荐 · 双曲空间Semantic ID
tags:
- Generative Recommendation
- Hyperbolic Representation
- Semantic ID
- RQ-VAE
- Long-tail Recommendation
one_liner: 首个将双曲几何融入残差量化VAE生成物品Semantic ID的框架，大幅提升长尾推荐效果
practical_value: '- 针对长尾商品占比高的电商/内容推荐场景，可直接将现有生成式推荐的Euclidean空间RQ-VAE语义ID生成模块迁移到双曲空间，无需额外正则就能获得更均衡的头/尾物品表示，长尾推荐效果最高可提升50%+

  - 双曲空间的指数容量特性天然适配推荐数据的幂律分布，做Semantic ID时可优先选用Poincaré球模型，搭配Möbius加减/指数对数映射实现空间转换，已有成熟算子可直接工程复用

  - 解决Semantic ID碰撞问题时，可复用纸中的级联token重分配策略：从最后一层codebook开始按最近距离分配，冲突时优先分配给距离更近的物品，再向上层回溯，无需增加额外辅助ID即可降低碰撞率

  - 超参选择上，Semantic ID长度选4-6、单层codebook大小选256即可平衡表示精度和自回归生成的误差积累问题，无需盲目堆参数'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有生成式推荐基于Euclidean空间的RQ-VAE生成Semantic ID，无法适配推荐数据天然的长尾幂律分布，头物品占用过多表示容量，尾物品表示精度差，导致推荐效果尤其是长尾推荐表现不佳，还容易出现ID碰撞、生成幻觉问题。

### 方法关键点
- 提出HypRQ-VAE框架，首次将双曲几何引入残差量化VAE流程，用Poincaré球模型适配物品的层级结构和长尾分布特性
- 编码时将物品文本嵌入经指数映射投影到双曲空间，在双曲空间完成多层残差量化，用Möbius加减操作计算残差和聚合码本向量，再经对数映射回欧氏空间做重建
- 设计级联token重分配策略解决Semantic ID碰撞问题，从最下层codebook开始按距离分配冲突token，向上回溯直到所有物品获得唯一ID
- 生成式推荐阶段把用户历史交互的物品Semantic ID序列拼入prompt，用LoRA微调LLaMA2-7B做自回归预测下一个物品的ID

### 关键实验
在MovieLens、亚马逊Instruments、Arts三个公开数据集上对比SASRec、TIGER、LC-Rec、LETTER等SOTA基线，整体指标平均提升3%-14%；其中长尾物品Hit@10最大提升52.71%，NDCG@10最大提升43.43%，同时推荐列表中长尾物品占比平均提升约10个百分点。

### 核心结论
双曲空间的指数体积膨胀特性天然适配推荐数据的幂律分布，不需要额外正则就能实现头/尾物品的均衡表示，是提升生成式推荐长尾效果的低成本路径。
