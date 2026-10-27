---
title: 'PinGER: Token-Efficient Generative Retrieval with Semantic IDs'
title_zh: 《PinGER：基于语义ID的Token高效生成式检索系统》
authors:
- Xinyi Li
- Sujan Reddy Ale
- Yi-Ping Hsu
- Zelun Wang
- Yilin Chen
- Hanyu Li
- Hanlin Lu
- Arkin Dharawat
- Lulu Yao
- Yaxin Li
affiliations:
- Pinterest
arxiv_id: '2610.33435'
url: https://arxiv.org/abs/2610.33435
pdf_url: https://arxiv.org/pdf/2610.33435
published: '2026-10-24'
collected: '2026-10-27'
category: GenRec
direction: 生成式推荐 · Semantic ID 效率与多样性优化
tags:
- Generative Retrieval
- Semantic ID
- Sequential Recommendation
- Beam Search
- Serving Optimization
one_liner: 通过非对称注意力掩码兼顾SID监督与推理效率的生成式检索，已落地Pinterest推荐
practical_value: '- 可复用训练推理不对称设计：训练阶段每个item交错SID token与dense token，通过非对称注意力掩码让推理阶段仅保留dense
  token，无需损失SID监督信号即可将相同上下文窗口的历史长度提升6倍，适配长序列推荐需求

  - 分层前缀多样性惩罚可直接替换温度采样：在生成式检索的beam搜索阶段引入该惩罚，相同召回率下beam的一级前缀多样性提升7.9倍，有效率比温度采样高4.7倍，适配电商推荐的多样性需求

  - 级联解码架构可直接用于生成式检索serving优化：共享历史KV缓存，单请求仅读一次历史即可服务所有beam，W=400时推理速度比paged attention快32倍，KV内存降低48.7倍，大幅降低宽beam的线上成本

  - 复用下游排序器日志做DPO对齐：无需单独训练奖励模型，直接用排序器的线上打分构造偏好对做DPO后训练，可提升召回候选在排序阶段的通过率10%，低成本实现召回排序的目标对齐'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有基于Semantic ID的生成式检索每历史item占L个token，相同上下文窗口能容纳的历史长度仅为单token embedding检索的1/L，历史长度不足会导致召回率下降10%；同时宽beam解码成本高、beam前缀坍缩多样性差，难以落地工业级推荐场景。
### 方法关键点
- 非对称注意力掩码：训练时每个item交错L个SID token+1个dense token，掩码限制仅当前item的SID可读取自身前缀与历史dense token，后续位置不读取历史SID，推理时直接丢弃历史SID，实现单token per item，计算逻辑与训练完全一致
- 分层前缀多样性惩罚：beam选择时按已有beam的公共前缀深度加罚，避免前缀坍缩，有效率远高于温度采样
- 级联解码serving架构：共享历史KV缓存，单请求仅读一次历史即可服务所有beam；搭配GPU端约束解码+主机本地索引，消除ANN检索的网络开销
- DPO后训练对齐：直接复用下游排序器的线上打分构造偏好对，无需单独训练奖励模型，提升召回候选的排序通过率
### 关键结果
离线对比TIGER（现有SID生成式检索）、PinRec（Pinterest生产embedding检索）：相同serving token下Recall@100比TIGER高9.5%，是PinRec的3.9倍；上线Related Pins场景后，整体收藏提升0.62%，发布28天内的新Pin收藏提升3.6%，端到端latency降低0.7%，完全替代原有ANN检索集群。
> 最值得记住：生成式检索的训练和推理可通过不对称设计解耦，兼顾全监督训练效率、长历史推理成本，同时消除ANN检索的线上开销
