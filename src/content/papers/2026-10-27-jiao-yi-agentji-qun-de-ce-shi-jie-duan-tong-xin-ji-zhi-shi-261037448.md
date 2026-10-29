---
title: Test-Time Communication in Trading Agent Swarms
title_zh: 交易Agent集群的测试阶段通信机制实证研究
authors:
- Avid Fayaz
- Harry Zhang
- Håvard Alstadheim
- Erik Nordlöf
- Vilhelm Karlin
- André Silva
affiliations:
- Infinite Ascent, Stockholm, Sweden
arxiv_id: '2610.37448'
url: https://arxiv.org/abs/2610.37448
pdf_url: https://arxiv.org/pdf/2610.37448
published: '2026-10-27'
collected: '2026-10-29'
category: Agent
direction: 交易Agent集群 · 测试时通信机制
tags:
- TradingAgent
- MultiAgentCommunication
- TestTimeExecution
- HerdingBehavior
- AgentSwarm
one_liner: 基于200个交易Agent的7天实盘实验，量化不同通信规则对集群决策与行为的影响
practical_value: '- 做多Agent协作系统时，可直接复用本文的5种通信粒度设计做AB测试，匹配业务目标（如电商定价Agent需规避趋同踩踏、内容生成Agent需兼顾多样性与一致性）

  - 评估多Agent羊群效应时必须设置无通信基线组，排除公共输入导致的自然趋同干扰，避免对通信机制的效果误判

  - 电商/广告场景下的多Agent竞价集群，可参考通信机制的灰度设计，在提升决策效率的同时控制集体趋同风险'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有多Agent通信研究多针对共享目标、反馈及时明确的任务，交易场景下Agent独立决策、市场反馈延迟且有噪声，集群趋同是风险而非目标，缺乏针对性实证结论。
### 方法关键点
将200个分属4个模型家族的交易Agent按10人分组，在5种通信机制（完全隔离/竞争消息板/协作消息板/带提醒消息板/peer共享笔记）下开展7个美股交易日实测，全链路记录Agent决策前所有输入。
### 关键结果
2个模型家族的通信组持仓重合度远高于隔离组，组收益基本由成员共同持仓的收益决定；看到同伴帖子的Agent复用8字短语的概率提升7pct，无通信基线组的短语自然重合率为14%；通信组同步卖出频率显著高于隔离组，羊群效应评估需基于无peer基线的超额趋同度。
