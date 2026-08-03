---
title: 'TransX: Scaling Transformer-based Recommendation via Behavioral and Serving
  Stream Crossings'
title_zh: TransX：通过行为与服务流交叉实现可扩展Transformer推荐
authors:
- Da Xu
- Liyan Fang
- Divya Venugopalan
- Sunny Hsu
- Xukai Wang
- Rishav Roy Chowdhury
- Cindy Liang
- Nishant Satya Lakshmikanth
affiliations:
- LinkedIn
arxiv_id: '2607.28940'
url: https://arxiv.org/abs/2607.28940
pdf_url: https://arxiv.org/pdf/2607.28940
published: '2026-07-31'
collected: '2026-08-03'
category: RecSys
direction: 工业级Transformer推荐 · 模型基建协同设计
tags:
- Transformer
- Sequential Recommendation
- Cross-Attention
- KV Caching
- CTR Prediction
one_liner: 工业级编解码推荐架构，协同优化模型与基建，实现CTR大幅提升与服务成本下降
practical_value: '- 架构设计可复用双流分离思路：拆分用户历史行为流与实时服务流，行为编码移至近线异步计算，在线仅做轻量跨注意力与解码，大幅降低在线延迟

  - 工程优化可直接落地：近线行为编码缓存+请求级KV缓存+局部-全局稀疏跨注意力的组合方案，实测降低80%在线计算，成本持平传统DLRM

  - 训练范式可迁移：用单遍seq2seq训练替代传统DLRM的逐事件重复编码，训练时长减少50%，适配长序列用户行为建模

  - 业务落地可参考精度-效率trade-off：用10条最近行为+全局池化的稀疏注意力设计，仅损失极少量精度换数倍效率提升，满足工业SLA'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前工业界Transformer类推荐多将异构用户行为、系统服务事件合并为单一token流，既混淆了两类数据的因果语义差异，又需逐请求重复编码全量历史，导致建模效率低、训练与服务成本高，长序列建模难以落地。

### 方法关键点
- 架构采用不对称编解码结构：编码器异步处理用户全量历史行为流，输出上下文表征；解码器通过分组多查询稀疏跨注意力（仅关注最近N条行为+全局池化表征），实现行为流与实时服务候选流的交叉建模
- 训练采用单遍seq2seq范式：全量行为序列仅编码一次，所有服务事件的损失在单轮前向反向传播中聚合，避免逐事件重复编码历史
- 服务端基建协同优化：行为编码近线计算后缓存，请求级复用KV缓存，在线仅执行轻量跨注意力与并行非自回归动作解码，延迟与全量行为序列长度无关

### 关键结果
在LinkedIn最大社交推荐场景180天行为数据集上，对比LiDLRM、SASRec、TransAct、GRM等同算力基线，离线AUC达0.862，优于所有基线；线上A/B测试相对DLRM基线获CTR+6.0%、转化率+4.4%，在线计算减少80%，服务成本与传统DLRM持平。

### 核心结论
工业推荐系统的核心是建模性能与服务成本的权衡，模型-基建协同设计可以同时推进帕累托前沿的两端，模型扩容不必然带来在线硬件成本的线性增长。
