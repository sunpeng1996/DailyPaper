---
title: 'Beyond the Final Embedding: Retrieving Memories from Token-Level Evidence'
title_zh: 超越最终嵌入：基于Token级证据的记忆检索方法
authors:
- Han Luo
- Zhan Zhuang
- Xu He
- Jujia Zhao
- Yu Li
- Suqin Yuan
- Dong Li
- Lei Feng
affiliations:
- Southeast University
- MemoraX AI
- Leiden University
- University of Sydney
arxiv_id: '2610.13277'
url: https://arxiv.org/abs/2610.13277
pdf_url: https://arxiv.org/pdf/2610.13277
published: '2026-10-09'
collected: '2026-10-12'
category: RAG
direction: RAG记忆检索 · Token级稀疏匹配
tags:
- Retrieval
- Token-level Matching
- RAG
- Memory Retrieval
- LoRA
- Embedding
one_liner: 复用冻结嵌入模型的上下文token表征做稀疏匹配，无需重训即可大幅提升检索效果
practical_value: '- 现有向量检索系统可直接复用冻结嵌入模型的token表征，无需重新训练或重建向量索引，仅通过稀疏token匹配+全局相似度融合即可快速提升商品/用户评论/历史咨询的检索效果，改造成本极低

  - 可选的LoRA式查询适配器仅调整查询侧token表征，完全不改动已存储的商品/记忆索引，适合多租户电商推荐、Agent长期记忆更新等不能重构索引的业务场景

  - 4bit标量量化可将token索引存储降低80%以上，仅损失不到1%的检索精度，仅增加5ms左右查询延迟，适配大规模商品库/用户行为库的检索性能要求

  - 调参成本极低：融合权重α设为0.5、token检索预算k设为32-64即可取得最优效果，可快速上线验证'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有单向量嵌入检索仅依赖最终全局池化表征，无法精准匹配查询所需的局部细粒度信息，而嵌入模型前向计算过程中生成的上下文token表征被完全浪费；多向量检索方案通常需要重新训练模型、全量重构索引，落地成本极高，亟需一种无需额外训练、不改动现有索引的检索优化方案。
### 方法关键点
- 离线阶段对所有记忆做一次冻结嵌入编码，同时存储全局池化嵌入和所有内容token的上下文表征，每个token绑定所属记忆ID
- 在线阶段对每个查询token做全局稀疏匹配，取top-k匹配记忆token的相似度，聚合得到每个记忆的局部匹配得分
- 对局部得分和全局嵌入得分做查询维度标准化后加权融合，得到最终排序，全程无需修改编码器和已存储的记忆索引
- 可选LoRA式低秩查询适配器，仅调整查询侧token表征，用MaxSim作为可微替代损失训练，进一步提升匹配精度
### 关键实验
覆盖8个检索基准（含对话记忆、金融报告、科学文献等）、8个不同架构/大小的嵌入骨干，无训练版平均提升Recall@10/NDCG@10达11.3/11.9个百分点；加查询适配器后，在Qwen3-Embedding-4B上平均提升13.3/14.3个百分点，下游问答精度最高提升16.95个百分点；4bit标量量化可将token索引存储降低85%，仅增加约5ms查询延迟。
### 核心结论
现有冻结嵌入模型的细粒度token表征远未被充分利用，无需重新训练就能挖掘出远超单向量检索的性能潜力。
