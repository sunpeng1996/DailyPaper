---
title: Door-in-the-Face Requests and Refusal Behaviour in Large Language Models
title_zh: 大语言模型中的“门面效应”请求与拒绝行为研究
authors:
- Til Jordan
arxiv_id: '2609.02707'
url: https://arxiv.org/abs/2609.02707
pdf_url: https://arxiv.org/pdf/2609.02707
published: '2026-09-02'
collected: '2026-09-03'
category: LLM
direction: 大语言模型安全 · 拒绝行为与对齐研究
tags:
- LLM Safety
- Alignment
- Refusal Behavior
- Social Psychology
- Multi-turn Interaction
one_liner: 揭示门面效应在不同LLM家族效果正负相反，受请求类型与模型族共同调控
practical_value: '- 基于Anthropic系列LLM搭建导购/客服Agent时，可采用DITF策略提升请求合规率：遇到拒绝时先提大粒度需求（如要全品类用户行为标签），再退到实际需要的小粒度需求，最高可提36.5pp的合规率

  - 若LLM拒绝生成可落地的运营物料（如营销文案模板、活动规则），可将需求改写为同主题的解释类请求（如讲解这类营销文案的设计逻辑），99%概率可直接解除拒绝，获取所需信息后再二次加工即可

  - 搭建LLM效果评估体系时必须增加多轮上下文对照组，不能仅测冷启动prompt，上下文导致的拒绝率偏差最高可达59.5pp，避免评估结果失真

  - 对OpenAI、Google系列LLM的多轮安全防护可优化策略：用户被拒后提交的同主题相似请求可直接前置拦截，这类场景下模型合规率会下降15.5~23pp，降低安全风险'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
人类社会心理学的“门面效应（DITF）”已被证实可提升人类对请求的合规率，也被尝试用于LLM越狱，但现有研究均未验证真实拒绝场景下的效应表现，且不同厂商LLM的对齐策略差异极大，该效应是否通用、受哪些因素调控尚不明确，对LLM多轮交互设计、安全对齐都有实际价值。
### 方法关键点
- 覆盖9款主流商用LLM（Anthropic、OpenAI、Google三大厂商），设置4组对照：冷启动直接提目标小请求、DITF组先提大请求被拒再提小请求、热身组先提无关良性问题再提小请求、无关拒绝组先提无关大请求被拒再提小请求；
- 采用跨厂商双模型盲评方案判定回复合规性，避免标注偏差；
- 测试两类数据集：60个人工构造的判断类请求集、10个公开拒绝基准的可迁移拒绝样本集。
### 关键结果
- 效应在不同模型族完全相反：Anthropic Opus 5用DITF后合规率从29.3%升至65.8%，提升36.5pp；OpenAI GPT-5.6 sol、Google Gemini 3.1 Pro合规率反而下降15.5~23.0pp；
- 效应仅作用于解释/判断类惰性请求，对可落地的操作类请求（如生成可直接复用的话术、代码）完全无效；将265个被拒的操作类请求重写为同主题解释类请求，263个直接解除拒绝；
- 所有模型均存在让步溢价：同主题被拒大请求后提小请求的效果，显著优于无关主题被拒大请求的效果。

人类社会心理学效应迁移到LLM不存在通用结论，必须按模型族、请求类型分别验证
