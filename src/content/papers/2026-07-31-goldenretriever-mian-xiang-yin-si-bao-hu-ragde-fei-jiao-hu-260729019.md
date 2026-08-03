---
title: 'GoldenRetriever: Non-Interactive Homomorphic Encrypted Retrieval for Privacy-Preserving
  RAG'
title_zh: GoldenRetriever：面向隐私保护RAG的非交互式同态加密检索框架
authors:
- Yang Gao
- Gang Quan
- Scott Piersall
- Qian Lou
- Dongdong Wang
- Liqiang Wang
affiliations:
- University of Central Florida
- Florida International University
- University of Florida
arxiv_id: '2607.29019'
url: https://arxiv.org/abs/2607.29019
pdf_url: https://arxiv.org/pdf/2607.29019
published: '2026-07-31'
collected: '2026-08-03'
category: RAG
direction: 隐私保护RAG · 同态加密检索
tags:
- RAG
- Homomorphic Encryption
- Privacy Preservation
- CKKS
- Dense Retrieval
one_liner: 以阈值选择替代同态top-k排序，实现低延迟非交互式隐私保护RAG加密检索
practical_value: '- 强隐私要求的RAG场景（如电商用户敏感查询、企业内部知识库、金融咨询Agent）可优先用阈值选择替代同态top-k排序，复杂度从O(B²)降至O(B)，大幅降低加密检索延迟

  - 同态近似计算后需离散结果恢复的场景，可复用论文提出的7阶掩码极化多项式，将误差从O(ε)收缩到O(ε⁴)，保证token等离散值的正确还原

  - 部署隐私RAG时可通过调节阈值τ平衡召回率和返回文档量，电商场景可结合业务召回要求预调阈值，兼顾隐私保护和检索效果

  - 当前同态加密检索延迟仍远高于明文，仅适合对隐私要求极高、延迟容忍度高的B端场景，C端高并发场景暂不具备落地条件'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
RAG通过引入外部知识提升LLM效果，但现有明文RAG在处理用户敏感查询、企业机密知识库时存在严重隐私泄露风险。此前基于同态加密的隐私检索方案依赖交互式协议或top-k排序，同态下top-k排序复杂度极高，单查询延迟超10⁴秒完全无法落地，且交互过程易泄露查询、相似度得分、访问模式等敏感信息，亟需非交互式低延迟的加密检索方案。

### 方法关键点
- 用阈值选择替代top-k排序：仅保留相似度高于预设阈值τ的文档，无需排序，将加密检索复杂度从O(B²)降到O(B)，B为文档量
- 基于CKKS同态加密实现全流程加密：查询、相似度计算、文档选择全在密态下完成，检索侧无法获取任何明文信息
- 精度稳定的掩码极化：设计7阶多项式将同态计算得到的近似0/1掩码的误差收缩到O(ε⁴)，满足6万词表下token离散值还原的精度要求
- 全结构返回防访问泄露：返回全部文档的掩码结果，仅选中文档token保留原值，未选中为0，不暴露选中文档索引，避免访问模式泄露

### 关键实验结果
在MS MARCO、Natural Questions、HotpotQA、FiQA 4个标准检索基准下，和明文基线、同态top-k排序基线对比：
- 检索效果和两者完全持平：Recall达1.0，Token准确率100%，文档准确率100%
- 延迟相比同态top-k排序从16579.9s降到1051.8s，降低93.7%；延迟随文档量线性增长，1000文档时延迟4361.2s，效果保持不变
- 阈值τ可灵活调整：中低阈值保持100%召回，高阈值召回降到0.5，返回文档数减半

### 核心结论
同态加密下的RAG检索无需盲目对齐明文的top-k范式，阈值选择是兼顾隐私、效果、效率的实用落地方向
