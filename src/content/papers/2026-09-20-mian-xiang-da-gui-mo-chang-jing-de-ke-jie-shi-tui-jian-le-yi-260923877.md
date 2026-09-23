---
title: 'Explainable Recommendations at Scale: LLM Rationales for YouTube Music Artist
  Discovery'
title_zh: 面向大规模场景的可解释推荐：YouTube音乐艺人发现的LLM解释方案
authors:
- Xiao Liu
- Yanwei Song
- Srivaths Ranganathan
- Yuan Chen
- Zheyun Feng
- Parker Steenburgh
- Jochen Klingenhoefer
- Nathan Lasche
- Gergo Varady
- Tim Steele
affiliations:
- Google LLC
arxiv_id: '2609.23877'
url: https://arxiv.org/abs/2609.23877
pdf_url: https://arxiv.org/pdf/2609.23877
published: '2026-09-20'
collected: '2026-09-23'
category: GenRec
direction: 生成式推荐 · 可解释性规模化落地
tags:
- LLM4Rec
- Explainable_Recommendation
- Decoupled_Architecture
- LLM_as_a_Judge
- Knowledge_Graph
- Music_Recommendation
one_liner: 提出离线预生成LLM推荐解释的解耦架构，落地YouTube音乐大幅提升发现页用户参与度
practical_value: '- 架构可直接复用：将LLM重计算任务（如推荐解释生成、长尾候选挖掘、广告文案生成）转移到异步离线层执行，在线层仅做缓存检索和结果挂载，完全规避实时LLM推理的延迟和成本问题，适配电商推荐、搜索、广告等对延迟要求严苛的场景

  - 质量管控流程可迁移：采用「LLM生成→LLM-as-Judge多维度评分→反馈迭代prompt→KG实体对齐校验」的全链路管控方案，无需大量人工标注即可大幅降低LLM幻觉率，可直接用于电商商品推荐解释、内容推荐理由生成等场景

  - 收益归因方法可复用：做LLM相关功能A/B实验时，通过holdback测试单独屏蔽单个功能（如仅屏蔽解释、仅屏蔽新候选），即可精准量化不同模块的业务贡献，避免多功能耦合无法归因'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
音乐流媒体平台长期面临「消费熟悉内容」和「探索新内容」的权衡，用户对陌生艺人的信任门槛极高，传统启发式解释模板（如“XX艺人粉丝推荐”）生硬、覆盖范围窄，无法有效降低探索阻力；LLM生成个性化自然语言解释的能力极强，但直接在线部署推理成本过高、延迟无法满足生产级<1s的要求，难以适配亿级用户规模。
### 方法关键点
- 解耦双阶段架构：离线层仅对活跃用户异步触发LLM推理，基于全量听歌历史生成包含陌生艺人候选和个性化解释的发现档案，避免无效算力浪费；在线层仅做缓存检索与解释挂载，完全规避实时LLM推理开销
- 全链路质量管控：离线用LLM-as-Judge分两步打分（先校验口味聚类内聚性，再校验候选与聚类的匹配度），低于3分的结果触发反馈迭代prompt，无需微调仅靠prompt tuning就将推荐通过率从64.8%提升到74.4%；后处理阶段通过KG实体对齐过滤幻觉艺人，再用全量用户历史过滤已消费内容保证新颖性
- 成本优化：利用闲时抢占式TPU资源运行离线推理，配置动态刷新周期平衡内容新鲜度和算力成本
### 关键实验
在YouTube音乐每日发现栏开展两周大流量A/B测试，对照组为传统启发式解释的生产基线，实验组注入LLM生成的候选与解释：核心指标上，发现栏整体用户参与度提升22.43%，发现类留存指标提升8.07%，在线服务延迟仅增加0.3%，完全满足生产要求；holdback测试验证LLM解释本身是参与度提升的核心贡献项。
### 核心结论
自然语言解释是降低用户对陌生推荐信任门槛的核心抓手，LLM能力落地生产的核心不是强推实时推理，而是通过架构设计适配业务的延迟、成本约束。
