---
title: 'ReSID: Rethinking Long-Tail Retrieval in Generative Recommendation through
  Item Reachability'
title_zh: ReSID：基于物品可达性的生成式推荐长尾召回优化方法
authors:
- Muyu Zou
- Shunye Tang
- Yi Xu
- Haibo Xing
- Yandong Wang
- Lingyu Mu
- Jinxin Hu
affiliations:
- Alibaba International Digital Commerce Group
- Nankai University
arxiv_id: '2611.16404'
url: https://arxiv.org/abs/2611.16404
pdf_url: https://arxiv.org/pdf/2611.16404
published: '2026-11-12'
collected: '2026-11-13'
category: GenRec
direction: 生成式推荐 · 长尾召回优化
tags:
- Generative Recommendation
- Semantic ID
- Long-tail Retrieval
- Beam Search
- Partial Matching
one_liner: 从Semantic ID构造、解码、匹配全链路优化生成式推荐长尾召回，已落地阿里生产
practical_value: '- 优先选择并行Semantic ID而非序列SID：相同码长下并行SID可避免头部商品的前缀垄断累积，长尾召回提升可达17%，不损失整体推荐效果

  - 可复用的解码优化trick：在生成式推荐beam search阶段加入流行度校准+用户语义对齐，窄波束下即可保留更多高相关性长尾候选，无需扩大波束提升算力成本

  - 匹配阶段可放松为局部SID匹配：并行SID下容忍≤3个位置错配可将长尾召回提升4倍以上，超过一半的长尾命中来自局部匹配而非完全匹配

  - 工业落地参考：该框架在阿里电商广告场景实测可提升广告收入1.3%、CTR1.1%、GMV0.8%、长尾曝光占比4.0%，可直接基于开源代码适配业务'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
生成式推荐（GR）通过Semantic ID（SID）将召回转为序列生成任务，但受交互分布偏斜、线上服务算力约束影响，长尾物品召回效果差。现有方案仅优化训练阶段SID表示，忽略解码剪枝、匹配规则对长尾可达性的影响：头部商品容易垄断beam前缀导致长尾候选提前被剪枝，完全匹配规则进一步丢弃大量带有效局部信号的生成结果。

## 方法关键点
- 长并行SID构造：将物品向量拆分为多个独立子空间分别量化，无跨位置残差链，避免序列SID的头部偏置逐层累积
- 可达性感知引导波束搜索：解码时对logit做流行度校准（减去训练频率先验的缩放对数），加入用户语义对齐得分（前缀下所有物品与用户向量的相似度均值），共同引导剪枝保留高相关性长尾前缀
- 局部SID匹配：匹配阶段容忍最多r个位置错配，按错配数量、波束得分排序召回候选，充分利用生成序列的局部有效信号

## 关键结果
在Amazon Industrial、Office公开数据集和阿里电商内部数据集上对比RQ-VAE、TIGER、OneRec、Ghost等基线，离线长尾Recall@200平均提升41.2%，长尾部有效覆盖率提升17.6%；线上A/B测试实现广告收入+1.3%、CTR+1.1%、GMV+0.8%、长尾曝光占比+4.0%，同时波束宽度仅为基线的1/3~1/10，latency降低2~8倍，吞吐量提升3.7~16.7倍。

## 核心洞察
生成式推荐的长尾优化不能仅局限于训练阶段的表示学习，需要从SID构造、解码、匹配全链路协同优化，才能在不提升算力成本的前提下兼顾效果和效率。
