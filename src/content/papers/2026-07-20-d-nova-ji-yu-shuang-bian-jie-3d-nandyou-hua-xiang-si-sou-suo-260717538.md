---
title: 'D-NOVA: In-Storage Retrieval Accelerator via Dual-Bound 3D NAND-Optimized
  Similarity Search with Vector Adaptation'
title_zh: D-NOVA：基于双边界3D NAND优化相似搜索的存内检索加速器
authors:
- Chang Eun Song
- Sumukh Pinge
- Tianqi Zhang
- Sung Eun Kim
- Tajana S. Rosing
- Mingu Kang
affiliations:
- University of California, San Diego
arxiv_id: '2607.17538'
url: https://arxiv.org/abs/2607.17538
pdf_url: https://arxiv.org/pdf/2607.17538
published: '2026-07-20'
collected: '2026-07-21'
category: RAG
direction: RAG检索 · 3D NAND存内计算加速
tags:
- RAG
- In-Storage Computing
- Vector Search
- ANN
- Hardware Acceleration
- 3D NAND
one_liner: 软硬协同设计3D NAND存内RAG检索加速器，较SOTA存内方案吞吐量高12.13倍、能效高1.26倍
practical_value: '- 可借鉴IVF分阶段精度-吞吐量调优思路：粗筛阶段放宽量化精度/并行度提升吞吐，中心匹配、精排阶段保精度，可直接落地到现有FAISS等向量检索引擎的参数调优，适配电商亿级商品向量库的检索场景。

  - 低比特向量检索的query侧轻量适配方案：当低比特量化、硬件加速的度量空间和通用embedding的cosine/L2空间不匹配时，仅需在query侧增加一个0.4M参数级的小适配器，用检索难负例做InfoNCE微调，无需修改存量库向量即可将召回损失控制在2%以内，适合大规模向量库的低成本优化。

  - 向量库存储布局优化：将语义相近的聚类向量存储在相邻存储块，可降低40%的查询IO开销，可复用在云原生向量数据库的冷热数据分层、SSD存储布局设计中，降低大规模电商/推荐RAG系统的检索成本。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
RAG的稠密向量检索占端到端延迟70%以上，现有近存加速器依然需要将大量向量数据搬出NAND阵列做计算，70%的检索时间消耗在阵列外的处理器计算和数据传输上，数据移动仍是核心瓶颈，无法完全突破带宽限制。

### 方法关键点
- 软硬协同设计D-NOVA架构，将IVF三级检索（中心搜索、粗筛Top-K2、精排Top-K1）全部下沉到3D NAND阵列内执行，仅SSD控制器完成轻量排序操作，消除中间数据移动。
- 提出双边界紧相似感知（DTS）度量，将向量检索转换成NAND字线电压驱动的阈值搜索，纯数字操作无需模拟电流累加，避免NAND多轮读开销。
- 设计轻量对比适配器，离线用DTS挖掘的难负例做InfoNCE训练，将通用embedding映射到DTS友好的度量空间，仅在query侧推理，不修改库内向量，几乎无运行时开销。
- 分阶段调整并行度m：精度敏感的中心搜索和精排阶段用小m保精度，粗筛阶段用大m提吞吐量，搭配局部感知的向量存储映射降低IO开销。

### 关键结果
在NQ、HotpotQA等6个RAG检索数据集上测试，对比CPU基线，吞吐量最高提升41.7×、能效提升71×；对比SOTA存内RAG加速器REIS，吞吐量高12.13×、能效高1.26×，召回仅比全精度FP32 IVF低1.43%~1.76%。

### 核心洞察
向量检索的性能瓶颈本质是数据移动而非计算，把检索逻辑尽可能下沉到存储介质内部，配合上层算法和模型适配，可以在不损失太多精度的前提下获得数量级的能效和吞吐量提升。
