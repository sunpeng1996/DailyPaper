---
title: Diffusion Language Model for Recommendation
title_zh: 面向推荐系统的离散扩散语言模型框架DLMRec
authors:
- Chengyi Liu
- Yongqi Zhou
- Junwei Pan
- Zhixiang Feng
- Chengguo Yin
- Haijie Gu
- Jie Jiang
- Yinghao Liu
- Yujuan Ding
- Qing Li
affiliations:
- The Hong Kong Polytechnic University
- Tencent Inc.
arxiv_id: '2607.21519'
url: https://arxiv.org/abs/2607.21519
pdf_url: https://arxiv.org/pdf/2607.21519
published: '2026-07-23'
collected: '2026-07-24'
category: GenRec
direction: 生成式推荐 · 扩散语言模型
tags:
- Diffusion Model
- Generative Recommendation
- LLM4Rec
- Tokenization
- Collaborative Filtering
one_liner: 提出适配推荐场景的离散扩散语言模型，替代自回归范式提升生成式推荐效果与稳定性
practical_value: '- 可复用collaborative-aware stochastic tokenizer设计：将多跳协同信号按传播深度分层编码为无序列依赖的离散token，适配扩散/双向建模的生成式推荐场景，规避RQ式序列化token引入的不必要顺序依赖，也可直接用于现有Semantic
  ID生成流程优化

  - 两阶段curriculum训练策略可直接迁移：第一阶段用item级渐进掩码完成协同token与物品文本语义的对齐，第二阶段引入hard negative对比损失做token级偏好建模，能显著提升LLM适配推荐任务的收敛速度和效果，微调可结合LoRA降低算力成本

  - 推理侧稳定性感知投票机制适配电商场景：聚合多步迭代预测结果，高置信度token提前固定，低置信度位置通过多步投票选优，能有效降低生成波动，提升推荐结果的一致性，可直接集成到现有生成式推荐解码链路

  - 若当前自回归生成式推荐遇到错误累积、顺序依赖过强的痛点，可尝试替换为离散扩散语言模型作为生成骨干，相同参数量下有望获得7%~10%的Recall/NDCG提升，同时训练稳定性更优'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有LLM驱动的生成式推荐大多采用自回归范式，存在三点核心缺陷：一是next-token优化目标侧重序列顺序，和推荐依赖物品间结构关联、交互顺序噪声大的特性不匹配；二是前缀约束限制双向上下文建模，无法捕捉全局偏好结构；三是左到右解码会导致早期错误累积，难以修正。离散扩散语言模型的双向建模、迭代精炼特性天然适配推荐场景，但直接落地存在token化不兼容、训练目标不匹配、解码不稳定的问题。

### 方法关键点
- 提出collaborative-aware stochastic tokenizer（CAST）：基于LightGCN提取多跳协同信号，按跳数分层做随机量化编码，生成无序列依赖的离散token，适配扩散模型的双向去噪特性
- 设计curriculum-driven训练策略：分两阶段微调，第一阶段用item级渐进掩码完成协同token和物品文本语义的对齐；第二阶段用token级掩码结合偏好对比损失，让扩散去噪过程和用户偏好恢复目标对齐
- 提出stability-aware投票解码机制：迭代精炼过程中固定高置信度的稳定token，对不稳定token聚合多步预测结果投票选优，提升生成一致性

### 关键结果
在MovieLens-1M、LastFM、Amazon-Beauty三个公开数据集上，对比LightGCN、BERT4Rec、TokenRec等12个SOTA基线，Recall@10平均提升7.6%，NDCG@10平均提升8.2%；在稀疏度最高的Amazon-Beauty数据集上Recall@20较自回归基线TokenRec提升9.7%，训练过程的Recall波动比自回归模型低40%以上。

### 核心洞察
离散扩散语言模型是比自回归范式更适配推荐场景的生成式推荐骨干，能在相同参数量下实现效果和稳定性的双重提升。
