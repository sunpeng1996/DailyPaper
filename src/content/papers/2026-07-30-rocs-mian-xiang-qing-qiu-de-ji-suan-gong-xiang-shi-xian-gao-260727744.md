---
title: 'ROCS: Request-Oriented Compute Sharing for Efficient Large-Scale Recommendation'
title_zh: ROCS：面向请求的计算共享实现高效大规模推荐系统
authors:
- Yuxin Chen
- Liang Luo
- Buyun Zhang
- Jian Jiao
- Boda Li
- Haoyu Wang
- Tongyi Tang
- Ao Cai
- Zijian Shen
- Zhengkai Zhang
affiliations:
- Meta AI
arxiv_id: '2607.27744'
url: https://arxiv.org/abs/2607.27744
pdf_url: https://arxiv.org/pdf/2607.27744
published: '2026-07-30'
collected: '2026-07-31'
category: RecSys
direction: 推荐系统效率优化 · 推理计算复用
tags:
- Recommendation Inference
- Compute Sharing
- GPU Optimization
- Model System Co-design
- CTR Prediction
- Ranking
one_liner: 通过模型-系统协同设计复用请求侧计算，大幅提升推荐推理效率且不损失精度
practical_value: '- 架构改造可复用GLM的算子级依赖约束，将用户/上下文等请求侧特征与候选侧特征解耦，请求侧计算仅执行1次即可跨所有候选复用，尤其适合候选量大的召回、粗排场景

  - 长序列建模可参考DCA设计，用户行为序列编码仅在请求侧执行1次，K/V全局复用，候选侧仅生成Query做跨注意力，既保留层式序列交互效果又大幅降低计算量

  - 工程实现可复用IKBO思路，GPU内核内通过索引映射关联候选与对应请求，无需显式广播请求侧张量，大幅节省HBM带宽，提升大候选Batch下的QPS

  - 资源分配可参考RRR策略，将计算节省的成本优先投入请求侧模型扩容，请求侧计算分摊到多候选，扩容性价比远高于候选侧，可实现不增成本还提效果'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
大规模推荐模型依赖特征交互、长序列模块提升效果，但推理时单个请求需打分几十到上万个候选，传统架构过早融合请求与候选特征，导致请求侧计算每个候选都要重跑，算力浪费严重；两塔架构虽能复用但牺牲中间交互效果，蒸馏、模型合并等方案又存在精度损失、特征新鲜度不足等问题。

### 方法关键点
- **Generalized Layer Masking (GLM)**：算子级定义依赖契约，仅允许信息从请求侧流向候选侧，确保请求侧输出与候选完全无关，支持MLP、FM、Norm等所有主流推荐算子
- **Deep Cross Attention (DCA)**：长序列编码仅在请求侧执行一次，K/V缓存全局复用，候选侧仅生成Query做跨注意力，保留层式序列交互效果的同时避免重复计算
- **Request-Oriented Resource Reallocation (RRR)**：将节省的计算资源优先投入请求侧模型扩容，请求侧成本分摊到多候选，扩容性价比远高于候选侧
- **In-Kernel Broadcast Optimization (IKBO)**：GPU内核内通过索引映射关联候选与请求，无需显式广播请求侧张量，大幅降低内存带宽消耗

### 关键结果
公开数据集覆盖KuaiRand、KuaiVideo、KKBox，适配DCNv2、FinalMLP、Wukong等骨干，单请求100候选场景下FLOPs最高下降90.6%；Meta生产环境中，召回模型QPS提升3倍无精度损失，短视频排序模型相对LogLoss下降0.5%同时QPS提升50%，广告排序模型QPS提升62%不掉点；线上全量部署后，最高实现0.2%业务指标提升+29%算力成本下降。

### 核心结论
推荐推理的请求级冗余是模型-系统协同设计的核心机会，而非仅实现层面的可优化细节。
