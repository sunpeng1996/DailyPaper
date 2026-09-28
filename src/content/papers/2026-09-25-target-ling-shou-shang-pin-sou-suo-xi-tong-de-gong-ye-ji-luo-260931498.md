---
title: 'Retail Product Search: A Practical Approach at Target'
title_zh: Target 零售商品搜索系统的工业级落地实践
authors:
- Darshan Sonagara
- Qujiaheng Zhang
- Ankit Singh
- Alex Li
affiliations:
- Target Corporation
arxiv_id: '2609.31498'
url: https://arxiv.org/abs/2609.31498
pdf_url: https://arxiv.org/pdf/2609.31498
published: '2026-09-25'
collected: '2026-09-28'
category: RecSys
direction: 电商商品搜索 · 混合检索架构优化
tags:
- Hybrid Search
- Dense Retrieval
- Rank Fusion
- E-commerce Search
- Contrastive Learning
one_liner: 公开Target词法+向量混合商品搜索落地方案，线上较纯词法搜索CTR提0.97%、转化提0.98%
practical_value: '- 混合检索结果融合阶段，若词法、向量两路召回结果重叠度低，优先选择weighted interleaving而非RRF，实测该策略在Target线上A/B测试中全指标优于RRF

  - 向量检索阶段强制加精度控制模块，用NER提取query显式属性（品牌、尺寸、性别）+ 分类器预测隐式品类意图做双层过滤，可将向量召回P@1从0.89提升至0.929

  - 电商域预训练embedding选型无需盲目追大，e5-small-v2相比e5-large-v2仅损失0.0068离线NDCG，但CPU推理p99 latency可控制在50ms以内，大幅降低部署成本

  - 双编码器对比学习训练时，加入曝光无交互硬负样本、语义相似硬负样本，可将NDCG@1提升0.0154，效果远高于单纯扩大训练数据量的边际收益'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
传统词法商品搜索无法处理同义词、拼写错误、自然语言query等词汇不匹配场景，纯向量检索易返回低精度结果、漏精确匹配项，且电商搜索需同时平衡相关性、营收、延迟等多目标，亟需兼顾二者优势的可落地工业级方案。
### 方法关键点
1. 并行双路召回架构：词法检索基于Solr倒排索引，向量检索采用fine-tune的e5-small-v2双编码器，ANN索引基于AlloyDB的ScaNN实现，两路结果合并后进入排序层
2. 训练数据构造：分层采样覆盖全品类、头/中/尾全量query区间；正样本采用多周聚合的转化>加购>点击加权得分；负样本结合in-batch负、曝光无交互硬负、语义相似硬负三类
3. 向量精度控制：NER提取query显式属性（品牌、尺寸、性别）+ query分类器预测隐式品类意图，双层过滤向量召回结果，降低误召回
4. 结果融合：对比RRF后选用weighted interleaving策略，通道权重通过多轮A/B测试迭代调优
### 关键结果
在线4周A/B测试对比纯词法搜索基线，最优版本CTR提升0.97%，订单转化率提升0.98%，访客需求（GMV）提升1.10%，零结果搜索率下降约50%；离线ablation显示加硬负样本后NDCG@1提升0.0154，加精度控制后向量召回P@1从0.89提升至0.929。
### 核心结论
电商域向量检索的效果增益核心来自domain fine-tune而非模型规模，小模型+业务数据适配的路线投入产出比远高于盲目上大模型。
