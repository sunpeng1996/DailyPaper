---
title: 'Beyond the Timeline: Augmenting Long-Video Memory with Grounded Entity Biographies'
title_zh: 跳出时间线：基于落地实体传记的长视频记忆增强方法
authors:
- Hui Ren
- Lei Fan
- Henry Pao
- Han Guo
- Zeeshan Zia
- Ying Chen
- Alexander Schwing
- Gang Hua
affiliations:
- University of Illinois Urbana-Champaign
- Amazon.com, Inc.
arxiv_id: '2609.38155'
url: https://arxiv.org/abs/2609.38155
pdf_url: https://arxiv.org/pdf/2609.38155
published: '2026-09-28'
collected: '2026-09-30'
category: Agent
direction: 多模态Agent · 长视频实体记忆优化
tags:
- Long Video Understanding
- Entity Memory
- Multimodal Agent
- Video QA
- Grounded Representation
one_liner: 提出GEB长视频记忆框架，关联跨片段同实体观测构建传记，优化长视频问答性能
practical_value: '- 电商商品匹配/用户行为建模场景可借鉴GEB的实体关联逻辑：放弃纯文本标签匹配，引入视觉特征+同框互斥校验，解决同标题不同款、同款多别名的匹配错误，提升商品关联推荐准确率

  - 多轮问答/客服Agent的RAG系统可复用其关联检索机制：命中某条实体记录后，自动召回该实体的全量历史交互上下文，而非仅返回命中片段，大幅提升多跳推理类query的证据覆盖率，减少用户补充信息次数

  - 实体记忆构建可采用保守匹配策略：通过双相似度阈值+冲突观测否决机制，比单一阈值匹配的错误关联率更低，适合对错误容忍度低的业务场景如广告人群标签归因、售后事件溯源'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长视频跨天级问答需要关联同一实体在不同时间的事件，现有基于时序描述、文本实体的记忆方案存在身份歧义问题：不同实体可能共享相同文本描述，同一实体在不同场景下的描述也可能存在差异，仅检索相关事件无法确定其归属的实体身份，导致多跳推理类问题准确率低。
### 方法关键点
- 提出Grounded Entity Biographies（GEB）记忆框架，将同一物理实体跨片段的视觉落地观测按时间排序组成可检索的实体传记，每个观测保留对应上下文和原始视觉证据
- 记忆构建阶段：用开放词表检测器+单clip追踪生成实体观测，基于视觉+上下文特征做跨clip实体关联，采用双相似度阈值（最低一致性阈值θ_cons、最高匹配阈值θ_match）+同框IoU互斥校验的保守匹配策略，避免错误关联
- 检索阶段：采用Personalized PageRank做关联传播，命中某条观测后自动召回同实体的所有历史观测及对应上下文，返回的传记片段同时标注未检索到的观测时间点，引导Agent进一步搜索
### 关键结果
在4个长视频基准上测试，对比SOTA记忆框架MAGIC-Video（控制控制器、答案模型、检索限制完全一致）：
- EgoLifeQA（周级第一视角视频）准确率72.0%，领先4.4个百分点，证据命中率从37.6%提升至58.9%
- Ego-R1-Bench准确率领先6.6个百分点，MM-Lifelong周级开放问答准确率36.83%，领先第二名5.41个百分点
- MultiHop-EgoQA多跳问答完整证据覆盖率比MAGIC-Video提升47%，答案评分从2.58提升至3.11

**最值得记住的结论**：记忆不仅要记录发生了什么事件，更要关联每个事件涉及的持久化物理实体，实体传记是跨事件推理的核心桥梁。
