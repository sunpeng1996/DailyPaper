---
title: 'FlyHash for LLM Agent Memory: An Empirical Validation and a New Application'
title_zh: FlyHash在LLM Agent记忆检索中的实证验证与落地边界分析
authors:
- Mohan Bheemadolu
- Chrisogonas O. Odhiambo
affiliations:
- Independent Researcher
arxiv_id: '2611.05791'
url: https://arxiv.org/abs/2611.05791
pdf_url: https://arxiv.org/pdf/2611.05791
published: '2026-11-04'
collected: '2026-11-05'
category: Agent
direction: Agent 记忆检索 · 哈希算法优化
tags:
- FlyHash
- LLM Agent
- Memory Retrieval
- SimHash
- HNSW
- LSH
one_liner: 首次将FlyHash应用于LLM Agent记忆检索，明确其性能优势与落地适用场景
practical_value: '- 资源极端受限的端侧Agent（如电商导购端侧）若必须用哈希压缩记忆，可替换SimHash用FlyHash，低比特预算下mAP最高提升4.2倍，尤其适合用户偏好记忆检索场景

  - 万级及以下规模的Agent记忆系统优先采用HNSW索引，其mAP可达0.98+、查询延迟<0.1ms，哈希方案仅适合单记录存储预算<32字节的极端场景

  - 做哈希方案对比时必须统一活跃比特数（而非总编码长度），避免文献中常见的参数混淆导致的结果偏差'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
LLM Agent依赖外部记忆实现长上下文交互，现有主流稠密向量+HNSW检索方案内存和算力开销高，传统SimHash压缩方案检索精度不足；受果蝇嗅觉电路启发的FlyHash此前被证明比特级检索精度优于SimHash，但从未落地到Agent记忆场景，也缺乏面向生产的资源开销验证。

### 方法关键点
- 设计匹配活跃比特数的公平对比协议，避免将FlyHash总编码长度m与有效活跃比特数k混淆的常见实验陷阱
- 从检索精度、内存占用、查询延迟三个维度全面对比FlyHash、SimHash、HNSW三类方案的优劣势
- 构造含6000条 persona 记忆、150条带真实 relevance 标签的Agent记忆benchmark，避免仅用嵌入近邻作为伪标签的循环验证问题

### 关键结果
跨4个多模态数据集、10种子重复实验，FlyHash在所有比特预算下mAP均显著优于SimHash，低比特（k=16）场景下相对优势最高达4.2倍；默认实现下FlyHash查询延迟是SimHash的10~70倍，改用稀疏集比对后仍高2~5倍；万级规模下HNSW的mAP可达0.98+、查询延迟<0.1ms，综合表现全面优于两类哈希方案；在带真实标签的Agent记忆benchmark上，FlyHash的精度优势依然稳定。

最值得记住的结论：哈希算法的比特级精度优势不等于实际部署的资源优势，FlyHash仅适合存储约束极端严格的Agent记忆场景，普通规模场景优先用HNSW。
