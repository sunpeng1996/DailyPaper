---
title: Leveraging Binary Hashing for Scalable Index Assignment in Semantic Communications
title_zh: 基于二进制哈希的语义通信可扩展索引分配方法研究
authors:
- Leonardo Roque
- Kuangyun Zhu
- Louis-Adrien Dufrène
- Quentin Lampin
- Grégoire Lefebvre
- Mohamad Assaad
affiliations:
- Orange Research, France
- Laboratoire des Signaux et Systèmes, CentraleSupélec, France
- INSA Lyon, France
arxiv_id: '2611.21260'
url: https://arxiv.org/abs/2611.21260
pdf_url: https://arxiv.org/pdf/2611.21260
published: '2026-11-16'
collected: '2026-11-17'
category: Other
direction: 语义通信 · 嵌入压缩与索引优化
tags:
- Binary Hashing
- Semantic Compression
- LSH
- ITQ
- Embedding Compression
- Index Assignment
one_liner: 将信息检索领域二进制哈希用于语义通信语义索引，验证CCA-ITQ方案性能最优
practical_value: '- 大规模推荐召回系统可复用CCA-ITQ哈希方法，将高维embedding压缩为二进制码，降低存储成本与向量相似度计算耗时

  - 跨端/跨服务embedding传输场景（如端侧特征上传、多节点召回集群通信）可采用该方案压缩传输带宽

  - 语义ID生成场景可借鉴数据依赖型哈希思路，相比随机LSH提升语义相近向量的编码重合度，优化召回准确率

  - 对传输噪声敏感的分布式推荐系统可增加ITQ校准步骤，提升压缩编码抗干扰性，降低下游任务精度损失'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
语义通信场景下高维embedding传输码率开销极高，传统向量量化方案存在可扩展性差、编码复杂度高、索引分配效果不佳等缺陷。

### 方法关键点
引入信息检索领域二进制哈希技术作为通用语义索引方案，对比测试随机LSH、PCA-LSH、CCA-LSH及结合ITQ迭代量化的四类变体；流程为将embedding压缩为二进制码，接收端通过共享码表的汉明检索重建向量，在二进制对称信道下验证性能。

### 关键结果
在MTEB、Banking77数据集上，数据依赖型哈希性能优于随机LSH，ITQ校准可提升编码抗信道噪声能力；CCA-ITQ在所有测试信道条件下分类精度最优，可作为传统量化方案的高效可扩展替代方案。
