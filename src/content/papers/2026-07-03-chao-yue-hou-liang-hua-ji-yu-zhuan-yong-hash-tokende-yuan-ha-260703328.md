---
title: 'Beyond Post-Quantization: Native Hash Learning with a Dedicated HASH Token'
title_zh: 超越后量化：基于专用HASH Token的原生哈希学习
authors:
- Xinze Liu
- Ding Wang
- Hengjie Zhu
- Dayan Wu
arxiv_id: '2607.03328'
url: https://arxiv.org/abs/2607.03328
pdf_url: https://arxiv.org/pdf/2607.03328
published: '2026-07-03'
collected: '2026-07-07'
category: Other
direction: 原生哈希学习 · 视觉Transformer优化
tags:
- Deep Hashing
- Vision Transformer
- Image Retrieval
- Token Learning
- Quantization
one_liner: 提出内置专用HASH Token的HashViT架构，解决后量化范式特征编码不一致问题，实现SOTA级图像检索性能
practical_value: '- 电商多模态检索场景可复用专用HASH Token设计，将哈希编码融入Transformer主干训练，替代后量化流程降低特征-编码偏差，提升召回精度

  - 可借鉴HASH Token的双结构设计（Hash Register+Semantic Workspace），兼顾离散编码检索效率和连续语义表征的准确性，适配大规模向量检索降本需求

  - 轻量Hash Refinement Adapter的逐层优化思路可复用在LoRA等轻量化微调场景，用极小参数开销实现特定目标（如哈希、语义对齐）的表征优化'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有深度哈希方法普遍采用后量化范式，先学习连续视觉特征再通过末端投影生成二值编码，导致连续表征空间与离散汉明空间存在特征-编码偏差，制约检索精度。
### 方法关键点
1. 提出HashViT架构，在Transformer内部新增专用HASH Token作为哈希导向的持久检索状态，将哈希编码从末端操作改为主干内的Token演化过程；
2. 将HASH Token拆分为直接生成二值编码的Hash Register和保留连续语义的Semantic Workspace，搭配轻量Hash Refinement Adapter实现跨层的哈希状态迭代优化；
3. 采用可学习语义中心监督、类Token相似性蒸馏、量化正则化的统一优化目标。
### 关键结果
在3个通用基准数据集上取得SOTA或极具竞争力的检索性能，同时保留紧凑汉明编码的低存储、高检索效率优势。
