---
title: Unpaired Modality-Agnostic Generative Recommendation
title_zh: 面向非配对多模态数据的模态无关生成式推荐
authors:
- Weihao Shen
- Wei Chen
- Fuwei Zhang
- Meng Yuan
- Yuqin Lan
- Guojun Liu
- Qingsong Hua
- Wei Lin
- Fuzhen Zhuang
affiliations:
- Beihang University
- Meituan
arxiv_id: '2608.02477'
url: https://arxiv.org/abs/2608.02477
pdf_url: https://arxiv.org/pdf/2608.02477
published: '2026-08-03'
collected: '2026-08-04'
category: GenRec
direction: 生成式推荐 · 多模态语义ID学习
tags:
- Generative Recommendation
- Semantic ID
- Multimodal Learning
- Unpaired Data
- Residual Quantization
one_liner: 基于非配对多模态数据学习统一语义ID空间，提升生成式推荐全场景性能
practical_value: '- 多模态Semantic ID构建可复用「轻量模态专属投影+共享Transformer+共享残差码本」架构，解决电商商品图文非配对、模态缺失痛点，无需维护多套tokenizer

  - 可直接复用模态可靠性加权融合策略：基于码本分配熵计算模态置信度，避免低质量模态（如商家乱填的商品标题、模糊主图）污染Semantic ID

  - 电商冷启动商品可直接用单模态数据生成兼容的Semantic ID，无需额外特征补全或fallback模型，大幅降低冷启动链路复杂度

  - 训练时采用配对/单模态数据平衡采样+码本使用均匀正则策略，可有效避免码本塌陷，提升Semantic ID的覆盖率和区分度'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有多模态生成式推荐依赖商品级图文配对数据构建Semantic ID，但电商/内容平台的图文数据往往来自不同运营链路，大量商品仅有单模态数据（缺图或缺文），直接使用非配对数据会因量化边界偏移生成不兼容的语义ID，严重影响推荐效果。

### 方法关键点
- 架构设计：仅保留轻量模态专属输入投影层，共享后续Transformer trunk和残差码本，所有配对/单模态数据优化同一套参数，保证语义空间统一
- 跨模态共识机制：基于码本分配的熵计算图文模态的置信度，加权融合得到配对数据的统一表征，避免低质量模态干扰
- 训练目标：混合配对/单模态数据的重建损失+跨模态表征对齐+量化分配一致性正则+码本使用均匀正则，平衡各模态数据贡献，避免码本塌陷
- 推理链路：冻结tokenizer后，单模态/配对数据生成的Semantic ID在同一空间，仅需一套自回归推荐模型即可处理所有模态场景，无需特征补全

### 关键结果
在Arts、Games、Instruments三个公开数据集上对比SynGR等SOTA多模态生成式推荐模型：完全观测场景下HR@1最高提升22.86%，NDCG@5最高提升16.17%；模态缺失场景下HR@10最高较基线提升31.48%；训练时间较SynGR最高降低42%，推理延迟最高降低21%。

> 最值得记住的结论：多模态生成式推荐的核心瓶颈不是多模态数据不足，而是现有方法要求模态必须严格配对才能用于语义ID学习
