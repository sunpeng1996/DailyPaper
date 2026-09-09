---
title: Exploring Bottom-Up Clustering for Creating Semantic IDs
title_zh: 基于自底向上聚类的Semantic ID构造方法研究
authors:
- Leah Woldemariam
- Sudhanshu Garg
- Taha Belkhouja
- Charles Kim-Yip
- Ali Sahami
affiliations:
- Cornell University
- PayPal
arxiv_id: '2609.08310'
url: https://arxiv.org/abs/2609.08310
pdf_url: https://arxiv.org/pdf/2609.08310
published: '2026-09-08'
collected: '2026-09-09'
category: GenRec
direction: 生成式推荐 · Semantic ID构造
tags:
- Semantic ID
- Generative Retrieval
- Clustering
- Recommendation System
- Cold Start
one_liner: 提出自底向上聚类的Semantic ID生成方案，解决ID碰撞与局部语义丢失问题
practical_value: '- 可直接复用自底向上聚类的Semantic ID生成流程，替代现有RQ-VAE/R-KMeans方案，天然解决ID碰撞问题，无需额外补加去重后缀

  - 冷启动新品ID赋值可复用「取最近邻前L-1位码+簇内唯一索引」的方案，无需重建全量ID体系，大幅降低工程成本

  - 评估Semantic ID质量时可同时参考簇轮廓系数、同簇余弦相似度、下游召回/NDCG三类指标，平衡语义性与业务效果'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有Semantic ID多采用RQ-VAE、残差K-Means等顶向下量化方案，存在两大核心痛点：一是ID碰撞，单个ID映射多个物品，需额外加去重后缀；二是码本坍塌，大量物品集中在少数码位，局部嵌入语义丢失，最终导致生成式检索冷启动、泛化效果不佳，亟需同时保证ID唯一性、保留嵌入局部结构的构造方案。

### 方法关键点
- 先做最细粒度聚类：对物品嵌入做小批量KMeans聚类，每个细簇内给物品分配唯一的最后一级ID，天然保证全量ID无碰撞
- 逐层向上合并：每级对上一级簇质心做带样本权重的聚类，合并后的簇标签反向同步给所有物品，形成多级ID结构，天然保留嵌入局部相似性
- 冷启动适配：新品直接取最近邻物品的前L-1级ID，分配新的末级ID即可，簇超容时动态拆分，无需重建全量ID体系

### 关键实验
对比基线为工业界主流RQ-VAE方案，数据集覆盖自定义5.8M物品集、Amazon Beauty、Sports&Outdoors三类电商数据集。核心结果：①ID碰撞率降为0，平均每个ID对应物品数为1（RQ-VAE为1.35~1.63）；②细簇轮廓系数提升2~29倍，最高达0.29；③下游next-item预测Recall@10最高提升80%（自定义数据集从0.02升至0.036），NDCG@10最高提升100%。

### 核心结论
Semantic ID构造时优先保留嵌入局部结构，比优先拟合全局层次更能提升下游生成式检索的实际效果。
