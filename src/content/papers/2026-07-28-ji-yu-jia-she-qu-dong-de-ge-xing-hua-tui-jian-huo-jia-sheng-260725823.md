---
title: Hypothesis-Driven Shelf Generation for Personalised Recommendation
title_zh: 基于假设驱动的个性化推荐货架生成系统
authors:
- Aleksandr V. Petrov
- Tarun Chillara
- Matthew D. Moellman
- Lucas de Haas
- Yabai Song
- Alina Susoykina
- Melissa Crawford
- Gabriel Negash
- Erik Franco
- Tasnim Rahman
affiliations:
- Spotify
arxiv_id: '2607.25823'
url: https://arxiv.org/abs/2607.25823
pdf_url: https://arxiv.org/pdf/2607.25823
published: '2026-07-28'
collected: '2026-07-29'
category: GenRec
direction: 生成式推荐 · 货架个性化生成
tags:
- GenRec
- Generative Retrieval
- Semantic ID
- LLM-as-a-Judge
- Shelf Recommendation
one_liner: 提出四阶段假设驱动货架生成架构，替代人工固定模板，在Spotify生产环境验证有效
practical_value: '- 架构拆分可复用：将个性化概念生成和物料履约拆为两个独立阶段，前者负责用户意图挖掘，后者负责召回匹配，降低模块耦合度，可直接迁移到电商主题会场、专属专区生成等场景

  - 生成式检索落地技巧：履约阶段用扩展了Semantic ID词表的小LLM做约束解码，效果优于BM25、稠密检索基线，还能避免全库扫描，适合大物料库的条件召回场景

  - 低风险落地方案：所有LLM推理全链路离线执行，生成的货架作为候选输入现有排序链路，完全不增加线上服务延迟，大幅降低生成式推荐落地的性能风险

  - 生成式推荐评估方法：针对开放式生成的推荐集合，采用分阶段LLM评审（用户到假设、假设到货架）代替传统点指标，可有效定位链路问题，适配生成式推荐的离线迭代'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有生产推荐系统的主题化货架（如首页推荐行）普遍采用人工设计的固定模板+专属召回逻辑，仅能覆盖通用用户意图，无法满足用户长尾个性化口味，维护不同品类、场景、用户分层的模板成本极高，难以规模化扩展。

### 方法关键点
- 四阶段解耦架构：1）假设生成：蒸馏后的小LLM基于用户行为、市场等特征生成结构化货架假设，包含自然语言意图描述、内容类型、熟悉度约束、草稿标题等字段；2）目录履约：基于扩展了Semantic ID词表的小LLM做约束生成式检索，解码时用trie树保证返回的都是合法物料实体；3）货架对齐：LLM筛选最优k个物料，重写标题和副标题，保证内容与标题语义承诺一致；4）所有生成逻辑离线执行，最终货架作为候选输入现有首页排序链路，无线上推理延迟。
- 分阶段LLM-as-a-Judge评估：设计两个评审模块，User-to-Hypothesis评审假设与用户的匹配度，Hypothesis-to-Shelf评审召回物料与假设的匹配度，均采用0-2分粗粒度量表保证评分稳定性。

### 关键实验结果
- 假设生成阶段：蒸馏小LLM与大模型的评审得分几乎一致（78.3% vs 78.2%），无明显质量损失；
- 履约阶段：生成式检索整体得分0.71，比最优基线BM25高26.8%，在所有评审维度均领先；
- 对齐阶段：对齐后整体评审得分从0.71提升到1.27，涨幅78%，标题承诺匹配度涨幅99%；
- 线上随机曝光实验：专辑类货架30秒流率比现有生产基线高36%，在10个候选货架中排名第一。

### 核心结论
生成式推荐落地无需完全推翻现有架构，通过引入中间语义假设做链路拆分、全链路离线预计算的范式，可在不增加线上延迟的前提下大幅扩展推荐供给的个性化覆盖边界。
