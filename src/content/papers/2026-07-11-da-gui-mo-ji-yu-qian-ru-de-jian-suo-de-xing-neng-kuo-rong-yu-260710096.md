---
title: Scaling and Stabilizing Large-Scale Embedding-Based Retrieval
title_zh: 大规模基于嵌入的检索的性能扩容与迭代稳定性优化
authors:
- Zhen Yang
- Juexin Lin
- Hongwei Shang
- Kaihao Li
- Feng Liu
- Satya Chembolu
- Xunfan Cai
- Xinyi Liu
- Cun Mu
- Tony Lee
affiliations:
- Walmart Global Tech
arxiv_id: '2607.10096'
url: https://arxiv.org/abs/2607.10096
pdf_url: https://arxiv.org/pdf/2607.10096
published: '2026-07-11'
collected: '2026-07-14'
category: RecSys
direction: 电商检索 · EBR召回优化
tags:
- Embedding-based Retrieval
- Hard Negative Mining
- Knowledge Distillation
- E-commerce Search
- Dual Encoder
one_liner: 沃尔玛生产级EBR优化框架，结合混合难负采样与旧模型感知蒸馏提升检索质量与迭代稳定性
practical_value: '- 难负采样可直接复用「在线跨batch all-gather+离线交叉编码器+元数据规则」的组合，零额外前向开销扩大负例池，同时过滤假负、挖掘细粒度难负样本，提升EBR模型判别力

  - 模型架构升级时新增逆蒸馏预热阶段：用已迭代多年的成熟生产模型作为教师，蒸馏得到新大模型的初始化权重，避免直接冷启动丢失历史领域知识、导致业务指标波动

  - EBR训练可采用用户engagement+语义相关性的联合损失，平衡行为信号的业务导向性和语义匹配的相关性，缓解纯行为信号的bias问题

  - 评估阶段分两步：离线用小索引测召回、大索引测精度，线上先做人工相关性评估再开AB测业务指标，最大化降低上线风险'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
电商场景下基于嵌入的检索（EBR）存在两大工业界痛点：一是训练推理gap，训练阶段依赖单batch负例，判别力不足，推理阶段需在亿级商品库做匹配，效果落差大；二是模型升级风险，直接替换更高容量的编码器会丢失旧模型多年迭代积累的领域知识，导致检索行为不稳定、业务指标回落。
### 方法关键点
- 混合难负采样：在线侧通过跨GPU的all-gather通信共享batch embedding，零额外前向开销将负例池扩大一个数量级；离线侧在传统品类匹配规则基础上，引入交叉编码器筛选品类匹配但关键属性（品牌、规格等）不符的细粒度难负，降低假负噪声。
- 旧模型感知热启动蒸馏：升级到GTE-base编码器前，先以生产级成熟DistilBERT模型为教师，用KL散度拟合新旧模型的query-item相似度分布，迁移历史领域知识后再做正式微调。
- 训练采用engagement+relevance联合损失，权重各占0.5，平衡用户行为信号与语义相关性。
### 关键实验
基于沃尔玛1年的400万带转化匿名查询、9亿训练对训练，基线为线上在用的DistilBERT EBR模型；离线EM Recall@20最高提升4%，EM Precision@20提升2.01%；线上人工评估NDCG@5提升7.34%，NDCG@10提升6.89%，线上AB测总营收提升0.5%，已全量上线生产。
### 核心结论
工业界EBR优化不仅要做性能扩容，更要优先保障模型迭代的稳定性，避免技术升级带来的业务收益损耗。
