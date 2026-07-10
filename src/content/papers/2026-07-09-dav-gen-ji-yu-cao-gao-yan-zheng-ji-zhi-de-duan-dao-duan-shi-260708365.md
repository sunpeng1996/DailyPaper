---
title: 'DaV-Gen: End-to-End Generative Retrieval via Draft-and-Verify'
title_zh: DaV-Gen：基于草稿-验证机制的端到端生成式检索框架
authors:
- Meng Zhao
- Chunmei Liu
- Qinyong Wang
affiliations:
- Alibaba HUJING Digital Media & Entertainment Group
arxiv_id: '2607.08365'
url: https://arxiv.org/abs/2607.08365
pdf_url: https://arxiv.org/pdf/2607.08365
published: '2026-07-09'
collected: '2026-07-10'
category: GenRec
direction: 生成式推荐 · 召回排序端到端统一
tags:
- Generative Retrieval
- Semantic ID
- Hybrid Embedding
- End-to-End RecSys
- Draft-and-Verify
one_liner: 提出草稿-验证架构的端到端生成式检索框架，解决级联目标不一致与生成模型延迟过高问题
practical_value: '- 可复用混合稀疏稠密表征设计，融合RQ-VAE稠密向量与Semantic ID上下文表征，提升ANN搜索召回效果，优于单独使用稀疏ID或稠密向量

  - 训练可借鉴渐进式知识注入策略：先冻结PLM主干仅对齐Semantic ID嵌入与PLM语义空间，再全参数微调，避免灾难性遗忘，解决PLM与领域ID的语义gap

  - 推理阶段的KV cache广播机制可直接落地：用户上下文KV仅计算1次，批量计算所有候选生成分数，大幅降低生成式推荐推理延迟，满足线上SLA要求

  - 复合损失设计可迁移：将对比召回损失、生成式语义损失、pairwise排序损失加权联合训练，统一召回与排序目标，解决传统级联系统误差传播问题'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统级联检索推荐系统存在多阶段目标不一致、误差传播问题，而新兴的端到端生成式检索依赖自回归解码，推理延迟过高，无法满足工业级实时服务要求，同时难以精准控制推荐列表长度，亟需兼顾效果和效率的统一架构。
### 方法关键点
- 混合稀疏稠密表征：融合RQ-VAE输出的稠密内容向量与Semantic ID序列编码得到的稀疏结构向量，生成的固定长度混合嵌入同时支持高效ANN搜索和精准语义校验
- 渐进式知识注入训练：先冻结PLM主干仅对齐Semantic ID嵌入与PLM语义空间，再全参数微调，避免灾难性遗忘，实现领域商品知识与PLM通用知识的融合
- 三模块联合损失：对比召回损失优化混合嵌入的语义聚类效果，生成式损失学习商品细粒度语义与用户偏好的匹配度，pairwise融合损失直接对齐最终排序目标，三者加权联合训练统一召回排序目标
- 并行推理pipeline：先通过ANN快速召回候选集（Draft阶段），再复用用户上下文KV cache批量并行计算所有候选的融合得分完成排序（Verify阶段），规避自回归解码的延迟问题
### 关键结果
在3个公开推荐数据集上，对比SOTA生成式推荐模型OneRec，Recall@10和NDCG@10平均提升~2.8%；在亿级商品规模的工业视频搜索数据集上，Recall@50比稠密检索基线高32.7个百分点，NDCG@10比工业MoE排序基线高3.5%；线上A/B测试用户时长提升2.09%，转化率提升0.47%，推理latency仅70ms，比传统级联架构快46%。

生成式检索无需完全依赖自回归解码，通过将任务拆分为向量召回+并行校验的两阶段统一架构，可同时实现比级联系统更好的效果和更低的推理延迟。
