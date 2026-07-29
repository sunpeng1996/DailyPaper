---
title: 'MARS: Multi-Agent Re-ranking for Repeat-Order Food Delivery Recommendation'
title_zh: MARS：面向外卖复购推荐的多智能体重排序框架
authors:
- Jiahao Tian
- Zhenkai Wang
affiliations:
- Georgia Institute of Technology
- The University of Texas at Austin
arxiv_id: '2607.25420'
url: https://arxiv.org/abs/2607.25420
pdf_url: https://arxiv.org/pdf/2607.25420
published: '2026-07-28'
collected: '2026-07-29'
category: RecSys
direction: 多Agent重排序 · 外卖复购推荐
tags:
- Multi-Agent
- Re-ranking
- LLM4Rec
- LightGCN
- Swing Similarity
- Food Delivery Recommendation
one_liner: 融合轻量协同信号与LLM推理的多Agent外卖复购重排序框架，性能优于传统专用推荐模型
practical_value: '- 可复用粗到细的两阶段重排序架构：先做类目（如餐饮菜系、电商商品类目）粗筛，再做细粒度商品/商家排序，大幅降低LLM推理候选空间，提升落地可行性

  - 轻量协同信号+LLM的混合范式可直接迁移：用LightGCN做全局偏好召回、Swing相似性做局部用户行为挖掘，无需对LLM全量微调，仅通过prompt即可超过传统专用推荐模型效果

  - 落地可参考容错与去偏设计：候选集输入LLM前随机打乱消除顺序偏差，配置规则化兜底策略避免LLM输出格式错误，保障线上稳定性

  - 算力允许的场景下可开启LLM推理思考模式，可稳定提升排序效果，无需额外训练成本'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有LLM4Rec的性能增益来源不清晰，难以区分是预训练底座本身还是周边管道的贡献；同时外卖复购推荐需要同时融合长期偏好、实时时空上下文、协同信号，传统端到端训练的推荐模型可解释性差、异构信号融合灵活度低，亟需透明可控的混合框架。

### 方法关键点
- 采用4模块多Agent hub-and-spoke架构：Manager负责流程编排与兜底、Profiler检索用户历史、时空候选、协同信号三类证据、Analyzer基于上下文与LightGCN全局偏好输出Top-K菜系粗筛结果、Critic结合Swing局部相似用户证据对时空可行的候选商家排序
- 无LLM微调依赖：仅用3层LightGCN训练用户-菜系二部图获取全局偏好，用Swing相似性挖掘局部同好用户行为证据，LLM全程零样本推理，仅通过结构化prompt输入所有特征
- 流程优化降低推理偏差：候选商家输入prompt前随机打乱消除顺序偏见，要求LLM输出结构化JSON降低解析成本，配置规则兜底保证鲁棒性

### 关键结果
在Delivery Hero的两个真实外卖数据集DHRD-SE（斯德哥尔摩，复购率56.5%）、DHRD-SG（新加坡，复购率42.3%）上对比传统启发式、序列推荐、图推荐、专用外卖推荐基线，MARS搭配Gemini-2.5-Pro在DHRD-SE上HR@3达0.756，较最优非LLM基线SNPR提升4.4%；在DHRD-SG上NDCG@3达0.601，较最优非LLM基线DPVP提升7.3%；开启LLM推理思考模式可进一步稳定提升各项指标。

最值得记住的结论：轻量协同检索 + 结构化上下文喂给强预训练LLM的混合范式，可在复购类推荐场景下直接媲美甚至超过专用端到端优化的推荐系统，兼具高性能与可解释性优势。
