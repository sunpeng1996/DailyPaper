---
title: 'DSCH-Loss: A Dynamic Semantic Channel Objective for Deep Semantic Hashing'
title_zh: DSCH-Loss：面向深度语义哈希的动态语义通道损失函数
authors:
- Tobias J. Bauer
- Christian Riess
- Daniel Loebenberger
- Christian Bergler
affiliations:
- Fraunhofer AISEC
- Friedrich-Alexander-Universität Erlangen-Nürnberg
- Ostbayerische Technische Hochschule Amberg-Weiden
arxiv_id: '2607.24567'
url: https://arxiv.org/abs/2607.24567
pdf_url: https://arxiv.org/pdf/2607.24567
published: '2026-07-27'
collected: '2026-07-28'
category: RecSys
direction: 跨模态检索 · 深度语义哈希
tags:
- Deep Semantic Hashing
- Cross-modal Retrieval
- Loss Function
- Hamming Space
- Retrieval Metric
one_liner: 提出无断点动态语义通道哈希损失，提升跨模态/单模态检索的哈希编码质量
practical_value: '- 召回层哈希编码训练可直接替换原有SCH/pairwise损失为DSCH-Loss，解决损失断点导致的优化不稳定问题，跨模态检索场景tie-aware
  mAP可提升最多1.75pp

  - 哈希检索的效果评估统一改用tie-aware mAP，避免同汉明距离下样本排序随机性带来的指标虚高/波动，对齐业务真实召回效果

  - 多模态商品/内容检索场景可复用CLIP+共享哈希MLP的混合流架构，相比双流架构跨模态检索mAP可提升3pp以上

  - 超参数调优时，DSCH-Loss的通道宽度曲线系数γw默认取8即可，无需大量调参即可获得接近最优的检索效果'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
原有固定宽度语义通道哈希（SCH）损失在样本相似度为0处存在断点，导致损失面不连续、优化易震荡；同时常用的mAP指标未考虑汉明距离离散性带来的同距离样本排序歧义，评估结果波动大、不可靠，现有哈希方案在跨模态/单模态检索场景下的语义一致性仍有较大提升空间。
### 方法关键点
- 设计动态语义通道：通道宽度随样本标签余弦相似度动态插值，相似度越高通道越窄，完全消除损失面断点，优化过程更平滑
- 补充跨模态量化损失：对齐不同模态的哈希编码分布，避免模态偏移，强化共享汉明空间的语义一致性
- 采用tie-aware mAP作为核心评估指标：消除相同汉明距离下样本随机排序带来的指标偏差，评估结果更贴合真实业务表现
- 提供高效向量化损失实现，支持常规批训练，无需特殊训练流程
### 关键实验结果
在NUS-WIDE、MIR Flickr 25k两个通用跨模态数据集上，对比SCH、TDSRDH两种SOTA损失，覆盖16/32/64/128bit四种哈希长度，40个跨模态/单模态检索任务中35个任务取得最优tie-aware mAP，相比次优方案最高提升1.75个百分点；搭配CLIP混合流架构时，跨模态检索mAP相对传统双流架构提升3pp以上。
### 核心结论
哈希损失的连续性对编码质量的影响远大于固定的硬约束，动态适配语义相似度的损失设计能显著降低优化难度、提升检索效果
