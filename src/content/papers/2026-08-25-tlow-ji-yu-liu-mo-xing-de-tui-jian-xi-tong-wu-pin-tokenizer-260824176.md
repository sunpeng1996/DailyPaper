---
title: 'Tlow: Flow-based Item Tokenizer for Recommendation'
title_zh: Tlow：基于流模型的推荐系统物品Tokenizer
authors:
- Nian Li
- Chonggang Song
- Jingtao Ding
- Lingling Yi
- Yong Li
- Qingmin Liao
affiliations:
- Tsinghua University
- Tencent Inc.
- Shenzhen International Graduate School, Tsinghua University
arxiv_id: '2608.24176'
url: https://arxiv.org/abs/2608.24176
pdf_url: https://arxiv.org/pdf/2608.24176
published: '2026-08-25'
collected: '2026-08-26'
category: GenRec
direction: 生成式推荐 · Semantic ID生成
tags:
- Semantic ID
- Item Tokenizer
- Flow-based Model
- Generative Recommendation
- Cold Start
one_liner: 基于流模型将语义embedding映射为标准正态分布，生成高语义质量的独立物品Semantic ID
practical_value: '- 可直接复用Tlow的流变换架构优化现有Semantic ID生成流程，替换OPQ/RQ-VAE，既能保留并行解码效率，还能提升ID语义区分度，适配跨域、多模态、冷启动场景

  - 代码本引导损失可直接接入现有生成式推荐训练流程，通过对齐token嵌入空间和代码本空间的相似性分布，无额外推理成本提升推荐效果

  - 工业部署可参考其参数配置：C=16、S=256时token嵌入参数量仅4096，远低于千万级item ID参数量，Tlow仅需百万级item embedding即可收敛，单GPU可完成每日千万级新item的tokenization

  - 冷启动场景优先尝试：新品无需交互数据即可生成Semantic ID，微信线上实验新品UCTR提升11.64%，尤其适合电商新品推荐、内容平台新内容分发场景'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统推荐依赖随机分配的物品ID，存在参数量随物品数线性膨胀、冷启动无法解决的核心问题。现有Semantic ID生成方案中，RQ-VAE类序列化tokenizer解码效率低，OPQ/PQ类并行tokenizer受语义embedding维度强相关、分布各向异性影响，量化误差大、ID语义区分度差，在跨域、多模态等复杂场景表现受限。
### 方法关键点
- 基于流模型构建多尺度Tlow架构，每个流单元包含ActNorm、可逆线性、仿射耦合三层，可将任意语义embedding映射为服从标准正态分布、维度完全独立的隐层embedding
- 对隐层embedding做乘积量化（PQ）生成独立Semantic ID，支持全并行解码，推理效率与PQ类方法持平，远高于RQ-VAE
- 新增代码本引导损失，通过对齐token嵌入空间与量化代码本空间的余弦相似性分布，强化token语义区分度，无额外推理开销
### 关键实验结果
离线在4个Amazon公开数据集上，对比13种ID类、tokenizer类基线，Recall@10相对最优基线提升3.89%~11.45%，跨域、冷启场景增益更显著。微信线上多模态图文检索场景，单域下整体UCTR提升10.32%，新物品UCTR提升11.64%；跨域场景下整体UCTR提升7.20%，新物品UCTR提升9.45%，同时token嵌入参数量仅4096，存储成本较千万级ID嵌入降低99%以上。
### 核心结论
将语义embedding先映射到维度独立、分布规整的标准正态空间再做量化，是同时兼顾Semantic ID生成效率和语义质量的高性价比工业落地路径
