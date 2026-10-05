---
title: 'SOLO: Certified-Recall Metric Similarity Search with Scan-Only Sampled Inverted
  Lists'
title_zh: SOLO：基于仅扫描采样倒排表的带召回保证的度量相似性搜索
authors:
- Édgar Chávez
affiliations:
- CICESE
arxiv_id: '2610.02387'
url: https://arxiv.org/abs/2610.02387
pdf_url: https://arxiv.org/pdf/2610.02387
published: '2026-10-01'
collected: '2026-10-05'
category: RecSys
direction: 向量召回 · ANN索引性能优化
tags:
- ANN
- Similarity Search
- Inverted Index
- Vector Retrieval
- HNSW
one_liner: 提出无排序启发式的仅扫描ANN索引，召回可预认证，低内存下性能优于HNSW
practical_value: '- 向量召回层可复用SOLO的召回预认证机制，提前在业务query分布上计算所有配置的召回率，无需后验实测HNSW等图索引的效果，规避线上召回波动风险

  - 高维向量量化优化可采用「量化仅做初筛、全精度重排」的设计，8bit/4bit量化下无精度损失，吞吐量最高可提升2.8倍，适合电商大规模商品向量检索场景

  - 低内存部署场景可参考递归分裂倒排表的架构，Deep-100M规模向量库仅需256MB内存即可达到0.9964的recall@10，适合成本敏感或端侧部署的业务'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
主流图ANN索引（如HNSW）存在四大痛点：召回上限饱和无法调优，Deep-100M下HNSW最高recall@10仅0.9989；召回不可预测，只能后验实测无法提前认证；内存占用极高，DiskANN部署Deep-100M需至少12GB内存；动态增删改实现复杂，需修复图结构。
### 方法关键点
- 基于数据库均匀随机采样点构建倒排表，每个向量存入其最近b个采样点的倒排表，查询时路由到最近ks个采样点，全量扫描对应倒排表后用真实距离排序，无任何剪枝/投票启发式逻辑，召回等于采样覆盖概率可提前计算
- 超过长度阈值的倒排表递归应用相同规则分裂，无需聚类或图索引，构建完全并行无迭代，成本比带图索引的混合方案低25倍
- 采用8bit/4bit全局/按维度量化做初筛，保留Top-R候选后全精度重排，无精度损失；倒排表按列表顺序存储实现流式扫描，SIMD友好，吞吐量更高
### 关键结果
- Deep-100M数据集：1GB内存下recall@10达0.9977（仅10.7字节/对象），256MB内存下达0.9964；Deep-1B数据集512MB内存下recall@10达0.9925
- 高召回区间（>0.997）吞吐量比调优后的HNSW高1.1~1.8倍，SIFT-1M数据集0.9992召回下吞吐量达8836qps，是HNSW的2.1倍
- 增删改仅需操作对应倒排表，无需复杂图修复逻辑
> 最值得记住：量化仅用于初筛不能做最终打分，仅扫描结构的ANN索引可实现召回可预认证，低内存高召回场景下性能优于主流图索引
