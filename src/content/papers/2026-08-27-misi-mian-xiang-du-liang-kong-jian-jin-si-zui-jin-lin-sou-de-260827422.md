---
title: 'misi: a Metric Inverted Sample Index'
title_zh: MISI：面向度量空间近似最近邻搜索的倒排样本索引
authors:
- Edgar Chavez
affiliations:
- CICESE
arxiv_id: '2608.27422'
url: https://arxiv.org/abs/2608.27422
pdf_url: https://arxiv.org/pdf/2608.27422
published: '2026-08-27'
collected: '2026-08-28'
category: RecSys
direction: ANN索引 · 低资源检索优化
tags:
- ANN
- Metric Search
- Inverted Index
- Low Memory Serving
- Vector Retrieval
one_liner: 提出基于线性规模采样词汇的倒排度量索引，适配低内存、频繁重建的ANN搜索场景
practical_value: '- 电商频繁更新的商品召回索引场景，可复用其完全并行、确定性的构建逻辑，10亿级向量构建速度比同召回图索引快3.7倍，大幅降低索引更新的TCO

  - 端侧/边缘设备个性化推荐场景，可复用其低内存设计，8GB内存即可支持亿级向量检索，填补SSD-Graph类索引无法运行的低资源窗口

  - 离线批量相似任务（如商品去重、用户分群、相似物料召回）优先保证吞吐而非单查询延迟，可直接适配该索引降低离线计算成本

  - 自定义相似度的多模态检索场景，其黑盒度量适配特性可直接接入融合相似度，无需修改索引核心逻辑'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统ANN索引（如HNSW、DiskANN）存在构建成本高、结果非确定、内存占用大等问题，无法适配电商频繁更新的商品池、低内存端侧部署、批量相似计算等非峰值吞吐优先场景；此前的邻域近似索引NAPP受固定 pivot 规模限制，posting list长度随数据量线性增长，扩展性差。
### 方法关键点
- 采样规模为αn的数据库子集作为词汇表，替换NAPP的固定 pivot，每个对象存储其k_b个最近采样点作为签名，posting list平均长度固定为ρ=k_b/α，不随数据量增长
- 查询时先检索采样点的k_s个最近邻，合并对应posting list，用idf加权共享邻居投票排序，取top-C候选做精确距离校验返回结果
- 构建过程为n次独立的采样点检索，完全无锁并行、结果跨线程确定性，支持流式构建，内存占用可控制在3GiB以内
### 关键实验
在SIFT1M、GloVe-200、Deep1B亿级前缀向量数据集上对比NAPP、hnswlib、GRAFT、DiskANN：10亿级向量构建速度比同召回的图索引快3.7倍，仅需8GB内存即可从NVMe服务亿级向量，单查询QPS 8~30；内存充足时同召回下图索引QPS是其6~16倍，0.99召回的验证预算随数据量增长呈n^0.30的亚线性规律。
### 核心结论
没有通吃的ANN索引，在低内存、频繁重建、批量计算等非峰值吞吐优先场景，放弃部分查询性能换取构建、部署成本的优化是更划算的选择
