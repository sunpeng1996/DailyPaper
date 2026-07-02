---
title: 'Behavior-Adaptive Conversational Agents: Toward a Fluid Personality Framework'
title_zh: 行为自适应对话Agent：动态人格适配框架
authors:
- Hasibur Rahman
- Smit Desai
affiliations:
- Northeastern University
arxiv_id: '2607.01034'
url: https://arxiv.org/abs/2607.01034
pdf_url: https://arxiv.org/pdf/2607.01034
published: '2026-07-01'
collected: '2026-07-02'
category: Agent
direction: 对话Agent · 动态人格自适应设计
tags:
- Conversational Agent
- LLM Persona
- Personality Adaptation
- Dynamic Persona
- Behavior Change
one_liner: 提出联合适配隐喻人设与人格表达强度的动态框架，优化对话Agent场景适配能力
practical_value: '- 电商智能客服/导购Agent可复用双维度适配逻辑：根据咨询场景（售前咨询/售后纠纷/促销触达）动态切换人设（顾问/好友/工具）、调整表达强度，提升用户信任和转化率

  - 行为改变类场景（例如会员复购引导、健康消费提醒）可直接借鉴「人格表达强度倒U型」结论，优先采用中等强度的人格表达，避免过于生硬或过度热情的反效果

  - 工程上可低成本落地：无需模型微调，仅通过prompt工程实现人设切换和表达强度调制，每轮对话前根据上下文/用户标签动态更新system prompt即可'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM-based Conversational Agent (CA)普遍采用固定的「友好助手」人设与表达风格，跨场景适配性差：严肃场景下过于随意会丧失可信度，共情场景下过于生硬会拉远用户距离。过往研究分别验证了动态人设切换、人格强度适配的价值，但二者独立优化，单独调整单一维度仍会出现匹配偏差，例如合适的教练人设却因过度热情造成用户压力。
### 方法关键点
- 构建双维度正交适配的Fluid Personality Framework，每轮对话前基于任务场景、用户特征、交互历史动态调整两个模块参数
- 隐喻人设模块：维护可切换的人设库（如规划师、啦啦队、导师、知识库工具等），切换时采用自然语言过渡保证交互连贯性，落地可通过prompt工程实现无需额外训练
- 人格表达强度模块：基于大五人格维度动态调整外向度、亲和度、尽责度等特质的表达强度，如紧急场景减少冗余闲聊、内向用户降低表达外向度
### 关键结果
框架的有效性基于两项已验证的实证结论：1. 人格表达强度与用户评价呈倒U型关系，中等强度相比低/高强度，信任、感知智能、愉悦度指标分别高18%、21%、24%；2. 动态切换隐喻人设相比固定单一助手人设，用户喜爱度、采纳意愿分别高12%、17%，同时信任度与感知智能水平无显著下降
### 核心结论
对话Agent没有最优的固定人格解，适配场景的角色+适度的表达强度的组合效果远优于统一的「友好助手」人设。
