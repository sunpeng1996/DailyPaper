---
title: 'DIRECTOR: Dynamic Index-based Recommendation with Transport-Optimized Retrieval'
title_zh: DIRECTOR：基于动态索引与最优传输优化的并行重排框架
authors:
- Yuanhao Pu
- Chenghao Zhang
- Chao Feng
- Xiang Li
- Defu Lian
affiliations:
- University of Science & Technology of China
- Kuaishou Technology
arxiv_id: '2607.26418'
url: https://arxiv.org/abs/2607.26418
pdf_url: https://arxiv.org/pdf/2607.26418
published: '2026-07-29'
collected: '2026-07-30'
category: RecSys
direction: 推荐系统重排 · 非自回归生成
tags:
- Reranking
- Optimal Transport
- Non-autoregressive Generation
- Generative Recommendation
- Industrial Deployment
one_liner: 提出最优传输引导的并行重排框架，解决自回归重排效率低、非自回归协同性差的问题
practical_value: '- 重排模块迭代可直接复用「最优传输软约束训练+全局硬匹配解码」范式，既解决非自回归生成的item重复问题，又比自回归束搜索降低50%+推理延迟，适配低
  latency 业务场景

  - 当下游只有全局列表级Reward（如多目标业务分、黑盒评估器）时，可复用前缀锚定信用分配方案，将全局Reward拆解为位置级监督信号，大幅降低生成式重排的强化学习优化难度

  - latency 敏感的工业场景优先选用CVAE作为动态索引生成器，仅需一次前向传播即可生成候选序列，效果与扩散版接近但推理速度提升3倍以上

  - 部署时可复用其工程优化技巧：单个请求内候选embedding仅计算一次，多候选slate的匹配逻辑全并行，可在效果不降的前提下降低60%+CPU消耗'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前生成式重排存在两类核心痛点：自回归（AR）方案依赖顺序解码，推理 latency 高且束搜索易提前剪枝全局最优排列；非自回归（NAR）方案虽并行效率高，但位置独立预测易产出重复item、跨位置协同性差。同时Generator-Evaluator范式下下游Evaluator通常仅返回全局标量奖励，无法给生成器提供细粒度监督，进一步限制了工业落地。

### 方法关键点
- 动态索引生成：不直接预测每个位置的离散item，而是并行生成所有位置的连续隐式检索向量（融合用户上下文、候选集特征、位置embedding），支持CVAE/扩散两种生成器，采样多组索引即可快速得到多份候选slate
- 最优传输（OT）引导的训练与解码：训练阶段引入带熵正则的容量约束OT损失，耦合位置级偏好避免冲突；推理阶段直接对位置-候选相似度矩阵做全局硬匹配，无需迭代OT计算，一步产出无重复的合法slate
- 前缀锚定信用分配：构造从基线slate到生成slate的有效性保持路径，将全局奖励拆分为每个位置的贡献差值，解决黑盒Evaluator下的细粒度监督问题

### 关键结果
离线在ML-1M、Amazon-Books、工业RecFlow数据集上，相比最优基线NDCG@6分别提升3.69%、2.80%、3.61%；快手线上A/B测试VV提升0.519%、评论提升0.695%，相同QPS、P99 latency和服务可用性约束下，CPU消耗降低66.7%。

### 核心结论
非自回归生成式重排只要解决好跨位置协同的问题，就能同时拿到比自回归方案更好的效果和数倍的推理效率收益。
