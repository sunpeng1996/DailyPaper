---
title: 'FAIRGate: Agentic Runtime Policy Selection and Verified Repair for Fairer
  Recommendation Delivery'
title_zh: FAIRGate：面向公平推荐分发的智能体运行时策略选择与校验修复
authors:
- Navkar Jain
- Enock Ayiku
- Kenneth Fletcher
affiliations:
- University of Massachusetts Boston
arxiv_id: '2610.30359'
url: https://arxiv.org/abs/2610.30359
pdf_url: https://arxiv.org/pdf/2610.30359
published: '2026-10-21'
collected: '2026-10-23'
category: RecSys
direction: 公平推荐 · 智能体运行时策略选择
tags:
- Fairness
- Recommender System
- Agentic AI
- Runtime Policy
- Post-Ranking
- Auditability
one_liner: 在基础排序器与最终推荐列表间增加有界智能体策略选择层，兼顾推荐公平性与效用
practical_value: '- 可复用「预定义策略库+智能体动态选择+确定性校验」三层架构，避免LLM直接参与排序决策的不可控问题，适配电商/内容推荐等强合规场景

  - 策略库可内置业务常用干预规则（长尾商品曝光、商家流量均衡、同质化内容压制、用户兴趣校准等），智能体仅做选择不生成规则，大幅降低幻觉风险

  - 推荐解释可复用审计链路绑定模式，LLM仅基于结构化审计trace生成话术，杜绝无依据公平性声明，满足监管/商家/用户的可解释要求

  - 可直接套用请求维度的动态策略适配逻辑，替代固定重排规则，解决不同用户/候选池场景下固定公平性干预效用损失过高的问题'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有公平推荐方法要么训练时编码固定公平目标，要么推理时采用固定重排规则，无法适配不同请求的动态上下文（候选池分布、用户历史偏好、曝光债务、效用预算的差异）；直接用LLM做公平性决策又存在不可控、不可复现、易出幻觉的问题，缺乏可审计的落地路径。

### 方法关键点
- 架构上在基础排序器与最终top-K列表间插入FAIRGate控制器，采用「智能体决策层+确定性执行校验层」解耦设计，智能体仅负责从预定义策略库选策略，不发明公平规则
- 预定义策略库覆盖5类常见公平目标：长尾曝光兜底、组曝光均衡、集中度控制、校准保护、无可行方案时弃权
- 智能体拆分为3个职责明确的模块：上下文Agent输出结构化风险画像，策略选择Agent基于度量触发选择策略子集，修复规划Agent输出有界调整方案；执行层先做约束修复，通过相关性、校准度、元数据覆盖率等确定性校验后才允许下发
- 解释生成仅基于校验后的结构化审计trace，禁止LLM访问原始排序数据，杜绝无依据声明

### 关键实验
在MovieLens 1M数据集测试，对比base BPR-MF、静态长尾重排、固定顺序策略门等baseline，相同效用预算下：LT-Cov@10相对提升21.52%，策略匹配通过率从0.091提升至0.607，NDCG@10仅下降0.0003几乎无损；基于审计trace的解释无依据声明率从100%降至9.59%。

### 核心结论
自适应做策略选择、确定性做规则执行、可审计做解释输出，是将Agent落地到推荐公平性等强约束业务场景的可行路径。
