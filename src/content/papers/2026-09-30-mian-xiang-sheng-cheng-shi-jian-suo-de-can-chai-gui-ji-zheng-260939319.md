---
title: Residual Trajectory Distillation for Generative Retrieval
title_zh: 面向生成式检索的残差轨迹蒸馏框架ResTD
authors:
- Weihao Shen
- Wei Chen
- Fuwei Zhang
- Guojun Liu
- Qingsong Hua
- Wei Lin
- Fuzhen Zhuang
affiliations:
- Beihang University
- Meituan
arxiv_id: '2609.39319'
url: https://arxiv.org/abs/2609.39319
pdf_url: https://arxiv.org/pdf/2609.39319
published: '2026-09-30'
collected: '2026-10-01'
category: GenRec
direction: 生成式检索 · Semantic ID 蒸馏优化
tags:
- Generative Retrieval
- Semantic ID
- Residual Quantization
- Knowledge Distillation
- E-commerce Search
one_liner: 蒸馏残差量化轨迹信息增强生成式检索训练，无需改动已有索引与推理流程
practical_value: '- 针对已上线的RQ-based Semantic ID生成式检索/推荐系统，可直接叠加ResTD训练策略，无需改动线上索引和推理逻辑，零额外推理成本即可获得性能提升

  - 做软监督蒸馏时可复用碰撞感知教师构造方法，既保留残差偏好信息，又避免与已部署的SID地址冲突，完美适配工业界已上线的静态索引场景

  - 多视野蒸馏的设计可迁移到其他自回归生成任务，用未来层的分布信号监督早期解码状态，缓解自回归生成的前缀错误累积问题

  - 针对小语种、长尾query等低召回率的电商搜索场景，ResTD的增益更显著，可优先试点落地'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前基于残差量化（RQ）构造Semantic ID的生成式检索方案，仅将最终SID的硬编码作为训练监督，丢弃了量化过程中产生的残差轨迹信息：相同硬编码可能对应完全不同的码本偏好，残差轨迹还隐含后续量化层的决策信息，导致索引阶段的大量有效信息未被检索训练利用，限制了生成式检索的性能上限。
### 方法关键点
- 将冻结的RQ索引器作为过程教师，把残差诱导的码本偏好分布蒸馏到SID解码状态，全程不改动原有检索索引与自回归推理逻辑
- 设计多视野蒸馏机制：用后续量化层的残差码本偏好监督早期解码状态，让解码器在生成前缀时即可编码后续SID后缀的相关信息
- 碰撞感知教师构造：针对SID碰撞修正场景，最小程度调整残差分布保证存储的SID为最高概率，同时完整保留备选码的相对偏好关系
- 训练阶段仅增加轻量辅助蒸馏损失，推理阶段完全移除新增模块，无任何额外推理开销
### 关键实验结果
在多语言电商检索基准ESCI的英文/西班牙文/日文三个数据集上，对比稀疏、稠密、生成式检索SOTA基线：
- 相比最强基线CaLIR，英文数据集R@10提升13.0%、N@10提升16.8%，西班牙文R@10提升12.2%、N@10提升14.4%，日文R@10提升19.0%、N@10提升20.5%
- 扩展到生成式推荐任务，在Beauty/Instruments/Yelp数据集上R@10最高提升14.3%，N@10最高提升15.2%
### 核心 takeaway
生成式检索/推荐的训练不仅可以用最终SID的硬标签做监督，索引构造过程中被丢弃的中间信息是零成本的优质监督信号，无需改动线上部署就能拿到明确性能增益。
