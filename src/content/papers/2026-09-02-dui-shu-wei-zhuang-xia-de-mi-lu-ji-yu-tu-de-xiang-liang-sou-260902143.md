---
title: 'A Power Law in Logarithm''s Clothing: On the Scalability of Graph-Based Vector
  Search'
title_zh: 对数伪装下的幂律：基于图的向量搜索可扩展性研究
authors:
- Sajad Faghfoor Maghrebi
- Navid Eslami
- Niv Dayan
affiliations:
- University of Toronto
arxiv_id: '2609.02143'
url: https://arxiv.org/abs/2609.02143
pdf_url: https://arxiv.org/pdf/2609.02143
published: '2026-09-02'
collected: '2026-09-03'
category: RecSys
direction: 向量检索 · 图索引可扩展性
tags:
- ANN
- HNSW
- Vamana
- Vector Search
- Scalability
- Power Law
one_liner: 推翻图向量索引对数扩展的传统认知，证明固定召回下先呈亚线性幂律增长，数据量足够大后转为次多项式
practical_value: '- 做RAG/向量召回的容量规划时，摒弃传统对数增长的算力预估逻辑，按亚线性幂律（0<c<1，c随召回目标、数据固有维度升高而增大）估算，避免上线后算力不足

  - 优化HNSW/Vamana配置时，可通过提升ef_construction和M参数降低幂律指数c，平衡建库成本、查询成本和召回率的长期tradeoff，数据量越大优化收益越明显

  - 电商向量召回数据集几乎都处于亚线性幂律区间（达到拐点需数据量指数级于固有维度，业务场景几乎不可能触及），可直接基于论文给出的成本模型拟合业务专属c值做成本预判

  - 难查询（高LID区域）同样遵循幂律增长规律，无需单独做特殊扩展逻辑，只需统一按目标召回率调整ef_search即可'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有向量数据库普遍采用HNSW、Vamana等图索引做近似最近邻（ANN）搜索，行业长期默认固定召回下搜索成本随数据量呈多对数增长，但该结论仅在特殊假设下成立，无实用索引的实证支撑，且主流基准测试仅在单一数据量下测召回-成本tradeoff，无法指导大规模数据下的容量规划与成本优化。

### 方法关键点
- 拆解图索引查询成本：80%以上成本集中在查询邻域探索阶段，全局导航阶段占比极低，成本核心由查询邻域内的向量数量决定
- 提出双区间增长理论：稀疏区间（数据量N远小于指数级的固有维度阈值），局部固有维度（LID）随logN线性增长，查询成本服从N^c亚线性幂律；稠密区间（N足够大），LID趋于稳定，成本增长转为次多项式，符合传统认知
- 给出可落地的成本预测模型，可根据召回目标、索引参数（M、ef_construction）拟合幂律指数c，指导参数调优

### 关键实验
在8个公开数据集（含SIFT、OpenAI ada-002 embedding数据集，维度128~1536，固有维度19.2~46.5）上测试HNSW、Vamana两种主流索引：
- 所有数据集在常用规模下均符合亚线性幂律，指数c在0.08~0.64之间，随召回目标、固有维度升高而上升，随M、ef_construction升高而下降
- 仅SpaceV、OpenAI两个数据集在超大规模下出现向次多项式增长的拐点，SIFT/DEEP在10亿级规模下仍服从幂律

> 最值得记住的结论：绝大多数业务场景下的图向量索引查询成本随数据量呈亚线性幂律增长，而非行业普遍认知的对数增长
