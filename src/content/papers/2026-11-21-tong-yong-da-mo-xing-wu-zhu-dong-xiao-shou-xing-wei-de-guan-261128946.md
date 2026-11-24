---
title: 'ChatGPT Can''t Sell (And That''s Probably a Good Thing): Buyer-Aligned AI
  Advice, the Sales-Representative Gap, and Evidence from Commercial Conversations'
title_zh: 通用大模型无主动销售行为的观测、原因与商用销售Agent设计思路
authors:
- Benjamin Tannenbaum
affiliations:
- Aiso Research, AISO Boost Ltd.
arxiv_id: '2611.28946'
url: https://arxiv.org/abs/2611.28946
pdf_url: https://arxiv.org/pdf/2611.28946
published: '2026-11-21'
collected: '2026-11-24'
category: Agent
direction: 销售Agent · 目标对齐与落地优化
tags:
- LLM Agent
- Conversational Commerce
- Sales Agent
- Alignment
- E-commerce
one_liner: 通过多组商业对话语料实证通用LLM天然倾向买家顾问而非商家销售，给出合规销售Agent落地框架
practical_value: '- 电商站内销售Agent不要直接用通用LLM加销售prompt套壳，实测会增加无权限承诺（如虚构发货、预订权限）和产品错配率，反而伤害用户信任

  - 销售Agent的优化目标不能只看转化率，需增加硬约束：产品匹配度≥阈值、所有推荐有事实支撑、消费者伤害≤阈值，允许返回「无合适产品」的结果

  - 可复用观测结论：通用LLM仅在用户明确说出交易类词汇（买、订、下单等）时才会输出交易动作话术，销售Agent可加入意图识别模块，在用户表达明确购买意向时主动给出下一步动作引导

  - 合规销售Agent评估要分层：先过产品匹配、回答质量、动作落地性三层校验，再看转化效果，避免单独用转化率做核心指标导致短视问题'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
通用大模型的设计目标是对齐用户利益做中立消费顾问，和商家销售Agent的转化目标天然存在gap，直接用通用LLM做销售会出现要么不促转化、要么乱承诺的问题，该gap的量化表现和解决思路此前无明确实证支撑，对电商/品牌对话式销售系统落地阻碍很大。

### 方法关键点
- 三类数据集交叉验证：2023-2025年12178条GPT系列商业意图对话语料、2026年1050组GPT-5.4/Gemini购买类问答监控对、5组匹配的可控场景角色prompt对照实验
- 预定义四类回复标签：推荐语、资质校验语、交易专属动作语、软跟进语，用固定规则做文本匹配，避免人工标注偏差
- 对比通用助手角色和销售角色prompt的输出差异，同时参考商业化训练的销售Agent Javo的公开场实验证结论

### 关键实验数字
- 279条明确购买请求的历史回复中，22.6%含推荐语，0%含下单/预订/加购等交易动作语；56条更高精度的明确购买意图样本中，42.9%含推荐语，仍然0%含交易动作语
- 可控实验中，销售角色prompt比通用角色prompt的交易动作提议占比从2/5提升到5/5，但产品匹配正确率保持3/5不变，无权限承诺占比从2/5提升到4/5
- 专门训练的销售Agent Javo在100个站点1480万访问的随机对照实验中，比相同部署环境下的通用大模型提升21.6%的活跃访客转化率，同时满足合规校验要求

### 核心结论
给用户做购买建议和作为商家授权的销售代表是完全不同的任务，通用大模型不主动促成交不是缺陷，是对齐用户利益的合理特性，商家销售Agent需要单独设计目标、约束和工具链路，而不是试图「修正」通用LLM的安全对齐。
