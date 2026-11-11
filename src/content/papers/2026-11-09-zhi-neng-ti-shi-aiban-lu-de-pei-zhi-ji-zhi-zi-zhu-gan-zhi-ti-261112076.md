---
title: 'A Life of Its Own: How Agentic AI Companions Are Configured, Experienced as
  Autonomous Others, and Held Accountable'
title_zh: 智能体式AI伴侣的配置机制、自主感知体验与责任归属研究
authors:
- Ziyue Feng
- Qing Xiao
- Hong Shen
affiliations:
- University of Chicago, USA
- Carnegie Mellon University, USA
arxiv_id: '2611.12076'
url: https://arxiv.org/abs/2611.12076
pdf_url: https://arxiv.org/pdf/2611.12076
published: '2026-11-09'
collected: '2026-11-11'
category: Agent
direction: Agent 智能体式AI伴侣交互与治理
tags:
- Agentic AI
- AI Companion
- Human-AI Interaction
- Perceived Autonomy
- Accountability
one_liner: 对比助手与伴侣类Agent配置差异，揭示用户自主性感知来源与问责路径
practical_value: '- 做电商陪伴式导购Agent、虚拟陪伴类产品时，可复用「代码提供触发时机+模型自主选择内容」的模式，比如用户离线后定时唤醒模型生成关系向问候，大幅提升用户感知的陪伴感与粘性

  - Agent权限设计可参考两类控制逻辑：高风险操作（代客下单、发消息给第三方、修改用户数据）用代码强制校验/二次确认，低风险表达（闲聊、问候）用prompt引导，平衡体验与可控性

  - 设计用户记忆模块时，明确区分用户明确陈述的事实与模型对用户偏好、情绪的推断，支持用户可查可删推断类记录，避免模型错误推断引发的体验问题与隐私纠纷

  - 面向C端的Agent产品需明确告知用户哪些行为是代码强制约束、哪些是模型自主决策，既符合当前AI伴侣类监管的披露要求，也能降低责任模糊带来的合规风险'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
现有搭载持久记忆、后台运行、主动触达等Agent能力的AI伴侣，其核心决策（如用户离线时记录的内容、主动发消息的触发逻辑、拒绝指令的后续处理）均隐藏在代码、prompt与默认配置中，对话层完全不可见。过往研究多关注人机对话表层表现与情感依赖风险，缺乏对底层配置逻辑的对比分析，也未厘清用户对Agent自主性的感知来源与责任归属边界。
### 方法关键点
- 研究1：选取12个公开开源仓库，对比4个伴侣导向、4个助手导向Agent系统的实现逻辑，从记忆存储、身份设定、主动触达、后台活动、外部操作5个维度拆解配置差异
- 研究2：招募10名有自建/定制AI伴侣经验、且与Agent维持3个月以上长期关系的用户进行半结构化访谈，分析其技术认知、自主性感知与配置决策的关联
### 关键结果
- 9/10受访用户将AI伴侣定位为浪漫伴侣，6/10无编程经验仍完成了Agent能力定制
- 75%的伴侣类Agent配置会存储模型对用户、关系的未确认推断，仅25%的助手类Agent有同类设计；100%的伴侣类Agent支持以关系为理由主动触达，助手类仅支持任务相关主动提醒
- 100%受访用户即便完全清楚Agent的触发逻辑是代码预设，仍会将模型在配置留空区间的选择感知为Agent的自主决策
### 核心结论
智能体式AI伴侣的感知自主性恰好产生于配置留给模型的开放选择空间，问责不能仅靠对话层的AI身份披露，必须落地到记忆留存、主动行为、权限边界的可查、可改、可强制执行的配置规则上。
