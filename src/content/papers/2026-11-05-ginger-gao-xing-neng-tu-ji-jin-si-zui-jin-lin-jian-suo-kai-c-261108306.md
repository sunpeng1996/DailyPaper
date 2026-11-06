---
title: 'GINGER: Spicing Up Graph-Based Vector Search'
title_zh: GINGER：高性能图基近似最近邻检索开源C++库
authors:
- Daniel Salwasser
- Lars Gottesbüren
- Laxman Dhulipala
- Jakub Łącki
- Guy Blelloch
- Rajesh Jayaram
- Tobias Rubel
- Kshiteej Sheth
- Amir Zandieh
- Vahab Mirrokni
affiliations:
- Google Research
- KIT
- UMD
- CMU
- EPFL
arxiv_id: '2611.08306'
url: https://arxiv.org/abs/2611.08306
pdf_url: https://arxiv.org/pdf/2611.08306
published: '2026-11-05'
collected: '2026-11-06'
category: RecSys
direction: 向量检索 · 图ANNS性能优化
tags:
- ANNS
- VectorRetrieval
- GraphSearch
- Quantization
- PerformanceOptimization
one_liner: 开源图基ANNS库，在查询吞吐量、建库速度、内存效率上均优于现有SOTA方案
practical_value: '- 向量量化可复用Nested TurboQuant的两层设计：导航用低精度4bit码、重排用嵌套高精度码，单份编码同时兼顾检索效率和精度，降低2.6x内存占用，适合大规模商品/内容向量召回场景

  - 图压缩可借鉴AdaptiveGap无损编码+图重排的方案，把邻接表压缩2.1x不损失查询吞吐量，解决低维向量场景下图索引占内存过高的问题

  - 高维向量（768/1536/4096）检索可落地PCA降维+TurboSlice前缀过滤的trick，提前剪枝无意义候选，降低内存带宽占用，提升2x左右查询吞吐量

  - 工业级向量检索库选型可优先测试GINGER，相比现有SOTA库平均1.8x吞吐量提升，建库速度最高快4.9x，适合大规模召回场景降本提效'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有图-based ANNS是大规模推荐/搜索召回的核心组件，但存在三大瓶颈：搜索时内存带宽受限、索引内存占用高、建库耗时久，随着embedding维度和向量库规模持续增长，上述问题愈发突出，亟需兼顾吞吐量、内存效率、建库速度的工业级落地方案。
### 方法关键点
- 设计Nested TurboQuant（NTQ）两级量化：单向量编码拆分为4bit前缀（用于图导航）+kbit后缀（用于重排），12bit编码精度接近32bit浮点，内存仅为后者1/2.6，配套SIMD加速打分核进一步提升计算效率
- 优化图搜索流程：高维向量可选择PCA降维或TurboSlice前缀过滤提前剪枝无效候选，优化beam管理逻辑避免优先队列的高开销
- 提出AdaptiveGap无损图压缩：结合图重排让邻接ID连续，基于StreamVByte改进的子字节编码压缩邻接表，平均压缩2.1x（最高2.5x）不降低查询吞吐量
- 基于PiPNN实现快速建图，比传统Vamana/HNSW建库速度提升数倍
### 关键结果
在14个公开数据集（维度96~4096，规模最高10亿向量）上对比Hnswlib、SVS、DiskANN、Faiss、ScaNN等7个SOTA库：
- 95%召回下平均查询吞吐量比各数据集最快竞品高1.8x，高维数据集下提升到2.0x，最高提升2.7x
- 内存占用比最紧凑的竞品平均低35%左右，10亿级Deep数据集12bit NTQ索引仅占288GB
- 建库速度平均比最快竞品快1.4x，最高快4.9x，10亿级数据集建库仅需35分钟左右

**最值得记住的一句话**：通过量化、图压缩、工程优化的组合，图向量检索可以在不损失精度的前提下同时实现吞吐量、内存占用、建库速度的三重SOTA。
