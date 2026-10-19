---
title: 'GLOBE: Evolving Structured Agentic Memory for E-commerce Product Optimization
  in Generative Search'
title_zh: GLOBE：面向生成式搜索电商商品优化的结构化智能体记忆进化框架
authors:
- Hyunseo Kim
- Suil Choe
- Sukkyoung So
- Daeyeon Yi
affiliations:
- LG Electronics AI Lab, South Korea
arxiv_id: '2610.23709'
url: https://arxiv.org/abs/2610.23709
pdf_url: https://arxiv.org/pdf/2610.23709
published: '2026-10-16'
collected: '2026-10-19'
category: Agent
direction: 电商生成式搜索 · 智能体记忆进化
tags:
- Agentic Memory
- Generative Search
- E-commerce Optimization
- LLM4Rec
- Structured Memory
one_liner: 提出带字段约束的结构化行为手册智能体记忆，通过反馈迭代进化优化生成式搜索下的商品排名
practical_value: '- 做商品文案优化类Agent时，避免使用整体prompt改写，将优化策略拆解为绑定目标字段（标题/卖点/详情）的独立行为规则，既能减少结构性错误，也方便人工审核与迭代

  - Agent长期记忆复用可采用「行为手册+反馈迭代」模式：每次迭代后通过embedding语义+功能双重去重过滤冗余规则，得分负向且过了probation期的规则直接下线，可同时提升效果、降低坏案例风险

  - 规则效果归因可采用简单批量分配逻辑：单次改写用到的所有规则共享本次排名增益反馈，配上前N次试用保护期，无需复杂信用分配机制即可拿到不错的迭代效果

  - 需要跨品类迁移的优化规则无需做品类专属微调，基于通用规则迭代的结构化手册跨品类迁移MRG损失仅0.07，远优于整体prompt优化的负迁移表现'
score: 10
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
生成式搜索普及后，电商商品列表优化需要适配大模型的排序逻辑，现有整体prompt改写方法既容易出现结构性错误（如将卖点内容错误写入标题），也无法将成功优化策略沉淀为可复用知识，换品类需重新试错，效果不稳定且易出现排名下降的坏案例。

### 方法关键点
- 结构化行为手册设计：每条优化行为绑定允许修改的商品字段（标题/卖点/详情）、互斥规则、历史效果统计数据，编辑器仅能在允许字段内应用对应规则，避免结构性错误
- 迭代进化流程：每批次运行后，Reflector基于排名反馈生成新增/修改规则的提议；Moderator先做语义（cosine similarity>0.9去重）+功能双重去重；Curator更新手册，规则累计得分（有效次数-有害次数）为负且过了5次试用保护期则下线
- 轻量信用分配：单次改写用到的所有规则共享本次排名增益反馈，无需逐规则做复杂归因，大幅降低实现成本

### 关键结果
基于E-GEO电商生成式搜索基准实验：
1. 全量GLOBE的Mean Rank Gain（MRG）达1.611，较整体prompt优化的0.351提升359%，优化成功率61.6%，Downside Risk（DSR）下降45%
2. 跨品类迁移时，仅用5个品类训练的手册在unseen品类上仍保留93%的MRG增益，无去重变种则出现明显效果波动
3. 跨排序模型迁移时，GLOBE在Qwen3.5、Gemini-3.5-flash排序模型上仍保持MRG>1的增益，prompt优化的增益则转为负值

**最值得记住的一句话**：将智能体的优化知识拆解为带领域约束的结构化行为，再通过反馈迭代和冗余过滤，比整体prompt优化在效果、稳定性、可迁移性上都有数量级提升
