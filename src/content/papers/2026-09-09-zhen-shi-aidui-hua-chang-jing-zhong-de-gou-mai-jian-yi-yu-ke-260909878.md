---
title: Purchase Advice and Observable Buyer Responses in Real AI Conversations
title_zh: 真实AI对话场景中的购买建议与可观测买家反馈
authors:
- Benjamin Tannenbaum
affiliations:
- Aiso Boost Ltd., Tel Aviv, Israel
arxiv_id: '2609.09878'
url: https://arxiv.org/abs/2609.09878
pdf_url: https://arxiv.org/pdf/2609.09878
published: '2026-09-09'
collected: '2026-09-10'
category: Eval
direction: AI导购Agent 效果评估
tags:
- Conversational Agent
- Purchase Recommendation
- User Behavior
- Conversation Audit
- Measurement Limitation
one_liner: 审计317条真实AI导购对话，发现仅靠对话日志无法观测用户后续购买决策，不能推导转化或说服效果
practical_value: '- 对话式导购Agent效果评估不能仅用对话深度、用户回复率作为转化替代指标，该类指标对有效后续反馈的高估率达27.8%，必须打通对话日志与交易数据链路才能准确归因

  - 当前商用AI导购几乎不会主动建议用户放弃购买某品类，可探索增加高性价比负向建议（如劝退低匹配度商品）作为差异化体验点

  - 无交易数据打通的前提下，仅靠对话日志完全无法量化AI导购的实际转化/说服效果，避免投入资源做仅基于对话的无效效果归因'
score: 6
source: arxiv-cs.IR
depth: abstract
---

### 动机
当前对话式AI导购的效果评估常直接基于对话日志推导用户决策与转化效果，缺乏对该方法合理性的验证，无法明确对话内容与用户实际购买行为的关联度。
### 方法
审计Aiso数据库中317条经用户授权的去标识化商用AI助手导购历史对话，经单Agent筛选、去重后得到67条2023年4月-2025年7月的有效购买相关会话，做结构化标注统计。
### 关键结果
77.6%的会话中AI提供了商品选项、购买渠道或偏好建议，仅1例出现引导用户避开特定住宿产品的内容，无任何会话中AI建议用户放弃对应购买品类；仅26.9%的会话存在用户同购买任务的后续回复，用总对话深度作为有效后续反馈指标的高估率达27.8%；所有47条用户后续回复中未观测到明确的购买承诺、完成购买或放弃购买的声明，仅靠对话日志完全无法推导实际转化或说服效果。
