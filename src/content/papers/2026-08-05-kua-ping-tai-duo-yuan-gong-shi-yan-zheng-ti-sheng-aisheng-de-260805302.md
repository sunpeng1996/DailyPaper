---
title: Cross-platform epistemic verification for improving factual reliability in
  AI-generated news summarization
title_zh: 跨平台多源共识验证提升AI生成新闻摘要的事实可靠性
authors:
- Zhuo Xie
- Haoze Ni
affiliations:
- Bank of Changsha Co., Ltd., China
- College of Communication, Boston University, US
arxiv_id: '2608.05302'
url: https://arxiv.org/abs/2608.05302
pdf_url: https://arxiv.org/pdf/2608.05302
published: '2026-08-05'
collected: '2026-08-07'
category: LLM
direction: 大模型幻觉校正 · 多源共识验证
tags:
- Hallucination Correction
- Fact Verification
- Multi-source Retrieval
- LLM-as-Judge
- Post-hoc Correction
one_liner: 提出多源证据共识验证框架MECV，在不改模型前提下降低AI生成新闻摘要幻觉且避免过度改写
practical_value: '- 多源证据+异构LLM陪审团的校验框架可直接复用到电商生成式内容（商品文案、AI导购回答、金融资讯摘要）的幻觉校正，无需修改基座模型，接入成本低

  - 最小化编辑的迭代修正策略可迁移到内容生成后处理链路，在保证事实正确性的同时避免破坏原有语义、语气和营销框架，减少过度改写

  - 检索结果缓存的工程实现（按检索通道+query+topK做key）可大幅降低多轮迭代的检索开销，适合高吞吐的线上内容生成场景

  - 跨源一致性信号可作为内容可信度打分特征，补充到推荐系统的内容质量排序规则里，过滤低事实性的生成式内容'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前LLM广泛应用于新闻摘要、自动化内容生产场景，但生成内容常存在事实错误、幻觉信息，现有后校正方法依赖单一检索源，易受检索偏差、证据不全、平台信息不一致影响，且多存在过度改写问题，在金融、新闻等高信息敏感场景会带来极高决策风险。

### 方法关键点
- 核心框架MECV为后处理校正流程，分为三个阶段：原子事实抽取、多源证据下的异构LLM陪审团矛盾打分、最小化编辑迭代修正
- 证据池整合三类异构数据源：原文文档（高精度）、维基百科（通用背景知识）、公开网页检索（时效性信息），覆盖不同类型事实的校验需求
- 陪审团采用不同厂商训练的异构LLM独立给出矛盾得分，取平均值判断事实可靠性，避免单一模型的推理偏差
- 修正阶段仅修改矛盾得分超过阈值的事实点，采用RARR风格的最小化编辑策略，尽可能保留原摘要的语义、结构和语气

### 关键实验
在SummEdits-news 100样本基准上测试，对比RARR+Bing、RARR+黄金原文等基线：Fact得分82，比非oracle基线高22分，比黄金原文oracle高15分；平均NED<0.01，比RARR+Bing的0.14低一个数量级，改写幅度极小；人类评估显示事实可靠性从3.72提升到4.08，可信度从3.69提升到4.05，可读性基本无下降。

### 核心结论
跨异构信息源的一致性可作为事实不确定性的强信号，保守的最小化编辑校正策略在高事实要求场景下的综合收益远高于激进改写。
