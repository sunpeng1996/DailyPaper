---
title: 'Sparse Dictionary Learning for Measure-Valued Data via Linearized Optimal
  Transport: Efficient Algorithms and Sample Complexity'
title_zh: 基于线性化最优传输的测度值数据稀疏字典学习：高效算法与样本复杂度
authors:
- Brendan Mallery
- Shuchin Aeron
- James Murphy
affiliations:
- Independent Researcher
- Department of Electrical and Computer Engineering, Tufts University
- The NSF AI Institute for Artificial Intelligence and Fundamental Interactions (IAIFI)
- Department of Mathematics, Tufts University
arxiv_id: '2610.12924'
url: https://arxiv.org/abs/2610.12924
pdf_url: https://arxiv.org/pdf/2610.12924
published: '2026-10-09'
collected: '2026-10-13'
category: Other
direction: 最优传输 · 稀疏表征学习
tags:
- Optimal Transport
- Sparse Dictionary Learning
- Representation Learning
- Generalization Bound
- Autoencoder
one_liner: 结合线性化最优传输与稀疏自编码器，提出测度值数据可扩展字典学习框架并证明泛化边界
practical_value: '- 针对用户行为分布、商品语义分布这类测度型数据，可复用该框架做稀疏压缩表征，降低召回、排序链路的特征存储与计算开销

  - LLM embedding的分布表征可通过该方法做稀疏编码，优化RAG检索召回的向量匹配效率，减少语义检索的算力消耗

  - 可借鉴线性化最优传输的嵌入思路，优化多模态商品表征的对齐效果，提升跨模态搜索的精度'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有Wasserstein字典学习（WDL）存在计算复杂度高、规模化落地困难的痛点，且缺乏可证明的泛化性能保障，难以适配测度值类分布数据的高效表征需求。
### 方法关键点
1. 利用最优传输几何衍生特征将概率测度嵌入希尔伯特空间，结合稀疏自编码器参数化学习数据自适应字典，输出低维稀疏有限维编码；
2. 推导$L^2$值测度嵌入下稀疏字典学习目标的泛化边界，针对最优传输、熵传输映射字典给出覆盖数边界与显式收敛速率。
### 关键结果
在高光谱图像、几何点云、LLM隐空间文档embedding三类模态数据上验证了框架有效性，可实现测度值数据的快速、可扩展表征
