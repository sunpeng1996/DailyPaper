---
title: 'Love for Believable AI: Artificial Partiality and Relationship Persistence
  as an Engineerable Stance'
title_zh: 可信对话AI的人工偏好与关系持久性可工程化实现框架
authors:
- Sebastian Cochinescu
affiliations:
- University of Bucharest
arxiv_id: '2610.09895'
url: https://arxiv.org/abs/2610.09895
pdf_url: https://arxiv.org/pdf/2610.09895
published: '2026-10-07'
collected: '2026-10-08'
category: Agent
direction: 对话Agent · 关系偏好建模
tags:
- Conversational Agent
- Personalization
- Human-AI Interaction
- Relationship Modeling
- AI Ethics
one_liner: 提出可工程化的对话Agent人工偏好框架，拆分为资源分配与用户状态建模两层
practical_value: '- 搭建陪伴型Agent、电商智能客服时，可复用分层资源分配逻辑：设置所有用户通用的基础服务保底（如固定检索slot、响应长度下限），再按用户关系深度加权分配剩余稀缺资源（主动触达次数、额外检索上下文、更长响应长度），既不降低新用户体验，又能提升长期用户的粘性

  - 用户关系状态建模的规则可直接复用：trust值可按交互长度、专属提及事件加权单调更新，历史记忆检索采用salience×recency×relevance的加权规则，适配业务场景时仅需调整权重参数即可

  - 个性化效果评估可借鉴四通道divergence指标：对比老用户/新用户/错配用户的主动触达率、专属引用使用率、响应深度、偏好对齐度四个维度，量化个性化的真实有效性，同时可通过质量等价校验控制个性化对通用服务能力的损耗

  - 落地相关Agent产品时需配套硬约束：设置新用户服务质量保底阈值、偏好分配总预算封顶、禁止将付费金额/留存目标作为偏好分配的直接输入，规避用户情感依赖、过度信任等伦理风险'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
默认无状态的LLM对话Agent对所有用户采用统一服务策略，虽公平可解释，但无法让用户感知到交互关系的特殊性，极大限制了陪伴类、长期服务类Agent的体验上限；现有记忆增强、个性化方案仅调整输出内容匹配用户偏好，不涉及稀缺交互资源的优先级分配，无法实现真正的关系型偏好表达。
### 方法关键点
- 人工偏好拆解为两层：caring为保底服务之上的稀缺资源（主动触达slot、检索上下文、响应深度）零和分配，按用户关系状态（trust值、交互深度）加权；particularity为每个用户独立维护的关系状态，包含交互历史、偏好EWMA、共享引用库、trust标量、交互深度5个字段，trust按交互长度、共享提及事件单调更新
- 设计四通道divergence指标量化偏好程度：计算相同探针下，已知用户与陌生用户在主动触达率、共享引用使用率、响应深度、偏好对齐度4个维度的归一化差异
- 配套7条可落地伦理约束，包含新用户服务保底、偏好预算封顶、机制披露、依赖信号触发去强化、禁止将情感依恋变现等
### 关键结果
以Qwen2.5-0.5B-Instruct-4bit为基座，对比空状态、错配用户状态、仅分配、仅状态建模、通用个性化、原生基座6个baseline，修订后的R1版本在校准探针集上服务质量与原生基座差异<0.03，满足等价要求；最终divergence达0.23~0.30，用户状态估计准确率比空状态高0.375，仅完整机制可通过所有协议校验。
### 最值得记住的话
无法表现出偏好的系统，永远无法让用户在交互关系中感知到自身的重要性。
