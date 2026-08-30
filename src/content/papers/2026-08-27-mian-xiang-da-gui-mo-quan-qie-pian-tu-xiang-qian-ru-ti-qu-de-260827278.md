---
title: Decoupled I/O-Dominant Pipelines for Large-Scale Whole-Slide Image Embedding
  Extraction
title_zh: 面向大规模全切片图像嵌入提取的解耦I/O主导流水线
authors:
- Mayanka Chandrashekar
- Xi Zhang
- Ethan Seefried
- Tirthankar Ghosal
- John Gounley
- Heidi Hanson
affiliations:
- Oak Ridge National Laboratory
arxiv_id: '2608.27278'
url: https://arxiv.org/abs/2608.27278
pdf_url: https://arxiv.org/pdf/2608.27278
published: '2026-08-27'
collected: '2026-08-30'
category: Other
direction: 大规模嵌入提取 · 流水线I/O优化
tags:
- Embedding Extraction
- Pipeline Optimization
- I-O Optimization
- Vector Database
- High Throughput
one_liner: 三阶段解耦I/O感知流水线，显著提升大规模WSI嵌入提取吞吐量与可扩展性
practical_value: '- 大规模多模态物料（如商品图、短视频片段）预计算嵌入时，可复用三阶段解耦架构，分离I/O、计算、向量库写入环节，降低跨环节调度开销

  - 高并发嵌入生成场景下，可将物料预切片、预缓存与推理任务并行执行，规避存储I/O成为性能瓶颈，大幅提升整体吞吐量

  - 向量入库时绑定对应物料元数据（如商品ID、类目、属性标签），支持下游召回、RAG等任务的多维度过滤检索，提升向量库复用率'
score: 4
source: arxiv-cs.CV
depth: abstract
---

### 动机
全切片图像（WSI）单张可达数十GB，传统patch式嵌入提取流程I/O与编排开销占比极高，端到端性能受限于I/O而非算力，大规模落地成本高昂。
### 方法关键点
采用解耦I/O感知流水线架构，拆分工作流为三个独立阶段：1）patch生成与缓存预热；2）无通信开销的多节点并行推理；3）分片向量数据库批量写入。实现数据移动与计算完全隔离，生成的embedding自动绑定对应元数据直接入库。
### 关键结果
相同硬件下吞吐量较耦合架构提升数倍，验证中等并发以上场景存储I/O是核心瓶颈，重新定义大规模嵌入提取为数据中心型系统问题而非计算绑定问题，生成的向量库可直接复用至检索、分类、少样本学习任务，低资源场景增益显著。
