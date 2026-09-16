---
title: 'When AI Becomes Hard to Understand: Cognitive Demands in Real-World Human-AI
  Conversations'
title_zh: 当AI难以理解：真实场景人机对话中的认知需求研究
authors:
- Yingcan Carol Wang
- Iman Munire Bilal
- Qamar Zaman
affiliations:
- Stripe Partners, United Kingdom
arxiv_id: '2609.17301'
url: https://arxiv.org/abs/2609.17301
pdf_url: https://arxiv.org/pdf/2609.17301
published: '2026-09-15'
collected: '2026-09-16'
category: Eval
direction: LLM 人机对话认知负荷研究
tags:
- Human-AI Interaction
- Cognitive Load
- Conversational AI
- LLM Evaluation
- User Experience
one_liner: 分析8.4万条ChatGPT、Gemini真实对话，提出对话复杂度预算，揭示响应特征组合对认知难度的影响
practical_value: '- 开发电商导购Agent、智能客服时可参考复杂度预算机制：短回复适当提升用词丰富度，长回复严格控制词汇多样性，降低用户认知负荷减少追问

  - 生成商品详情、活动规则等AI运营文案时，可通过长度+词汇多样性的组合特征预判用户理解难度，提前优化表达降低信息差

  - 可复用该研究的行为指标（重复提问、澄清请求）作为对话类Agent交互体验的离线/在线评估维度，替代主观调研降本提效'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 动机
生成式AI已广泛支撑金融、健康等高风险场景的用户决策，但真实对话场景中AI响应用户认知难度的影响规律尚不明确，用户理解障碍不仅会提升交互摩擦，还会直接降低决策质量。

### 方法关键点
分析超8.4万条ChatGPT、Gemini的真实用户公开对话，以用户误解后的重复提问、澄清请求作为认知难度的客观行为指标，探究响应长度、可读性、词汇多样性等特征与认知难度的关联，提出「对话复杂度预算」框架解释特征间的依赖关系。

### 关键结果
响应长度、可读性、词汇多样性等单一特征与认知难度无固定关联，影响由特征组合决定：短回复中更高的词汇多样性对应更少的重复提问，该关联随回复长度上升逐步减弱，该规律在金融、健康两类高 stakes 场景对话中均稳定复现。
