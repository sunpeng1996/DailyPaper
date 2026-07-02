---
title: 'RACORN-1: Adaptive Recall-Preserving Speedup for Low-Selectivity Filtered
  Vector Search'
title_zh: RACORN-1：低选择性过滤向量搜索的保召回自适应加速方案
authors:
- Yoonseok Kim
- Gyusik Choe
affiliations:
- Naver Corporation
arxiv_id: '2607.00768'
url: https://arxiv.org/abs/2607.00768
pdf_url: https://arxiv.org/pdf/2607.00768
published: '2026-07-01'
collected: '2026-07-02'
category: RAG
direction: RAG 低选择性过滤向量检索优化
tags:
- Filtered Vector Search
- HNSW
- ANN Search
- Low Selectivity
- RAG
- Vector Database
one_liner: 基于ACORN-1解决低选择性过滤向量搜索的召回坍塌，实现9-75倍加速无额外构建开销
practical_value: '- 电商/推荐的带属性过滤向量召回场景可直接复用ASF机制，无需修改现有HNSW索引，即可解决低过滤占比下的召回坍塌，同时提升检索
  latency 9~26倍

  - RAG系统的带元数据过滤检索环节可部署RACORN-1+，结合AEF自适应切换线性扫描，在<0.1%极低选择性场景下保证召回1.0的同时实现20~75倍加速

  - 检索路径多样性优化可复用步长采样替换前缀截断，几乎无额外成本即可提升0.02~0.04召回，对跨模态余弦相似度检索增益更明显

  - 可参考bridge_ratio调优策略：无相关性场景调高BR提升召回，负相关场景调低BR至0.25~0.5，损失<0.02召回即可降低一半延迟'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
过滤向量搜索（FVS）是RAG、电商推荐向量召回的核心组件，主流ACORN-1算法在过滤选择性<5%时召回下降，<1%时彻底坍塌，无法满足业务低选择性过滤需求；而HNSW原生过滤延迟随选择性降低线性飙升，无法适配高吞吐生产环境。
### 方法关键点
- 自适应搜索回退（ASF）：两跳内满足过滤条件的候选不足时，将过滤失败节点作为临时桥接点加入搜索队列（不进入最终结果），重连断裂遍历路径，自动在ACORN-1和HNSW行为间插值
- 步长采样：对桥接点和两跳候选做间隔均匀采样，保证候选空间多样性，避免局部路径偏置
- RACORN-1+新增自适应精确回退（AEF）：运行时过滤通过率低于阈值时自动切换到预过滤线性扫描，保证极低选择性下召回1.0
### 关键结果
在SIFT1M、GIST1M、Text2Image1M/40M四个数据集上对比HNSW、ACORN-1：1%~0.3%选择性区间RACORN-1比HNSW快9~26倍，将ACORN-1的召回从0.45~0.72（1%）、0.03~0.10（0.3%）提升到0.70~0.96、0.77~0.98；<0.1%选择性下RACORN-1+实现20~75倍加速、召回1.0；负相关对抗场景下RACORN-1保持召回0.80~0.98，比HNSW快5~9倍。
### 核心结论
过滤向量搜索中过滤失败的节点不是冗余开销，而是可复用的路径连接资源，仅修改搜索逻辑不改动索引即可实现大幅低选择性性能提升
