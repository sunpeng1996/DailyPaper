---
title: 'The Autonomous Agency Scale: A Behavioral Framework for Measuring Self-Directed
  Behavior in AI Systems'
title_zh: 自主能动性量表(AAS)：AI系统自导向行为的量化评估框架
authors:
- Samuel Presgraves
affiliations:
- Independent Researcher
arxiv_id: '2607.17947'
url: https://arxiv.org/abs/2607.17947
pdf_url: https://arxiv.org/pdf/2607.17947
published: '2026-07-20'
collected: '2026-07-21'
category: Agent
direction: Agent 自主行为量化评估
tags:
- AI Agent
- Autonomy Evaluation
- Behavioral Framework
- Self-Directed Behavior
- Idle-Gap Test
one_liner: 提出分活跃/空闲双时段、7维度0-5级的AI自主行为量化框架，测评6款主流Agent系统
practical_value: '- 开发电商智能导购/会员陪伴Agent时，可复用AAS双时段（活跃会话/空闲静默）+7维度的评估逻辑，将主动推送潜在兴趣优惠、自主跟进未完成咨询等行为纳入量化指标，避免仅评估会话内响应效果。

  - Idle-Gap Test可直接用于Agent主动能力校验：移除所有定时触发、用户配置规则、环境事件后仍输出合理自导向行为的才是真主动智能，可过滤伪主动的规则型方案，减少业务上线后“伪智能”投诉。

  - 做Agent选型时可复用AAS分级rubric做量化评分：任务型Agent（如工单处理、客服Agent）侧重Active band评分，陪伴型Agent侧重Ambient
  band评分，替代主观选型判断。'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
现有AI评估框架仅聚焦认知能力、任务自动化效率、灾害风险三类维度，无法量化系统的自主能动性——即自导向行为的程度，很多能力顶尖的系统依然是完全被动的，仅在收到prompt时响应、任务结束即停止活动，缺乏对AI从被动工具向主动Agent演进过程的量化标尺。

### 方法关键点
- 定义0-5级自主能动性分级词典，从无响应的Dormant到完全自主设定目标的Sovereign共6级，所有分级均对应可观测行为阈值，无需访问系统内部架构即可评测。
- 拆分两个独立评估时段：Active band（用户发起的活跃任务/会话期）、Ambient band（无用户交互、无任务的空闲期），两个时段评分独立计算、不合并为单一分数。
- 覆盖7个评估维度：认知自主性、时间持久性、环境能动性、社交能动性、创意能动性、自我意识、目标形成，每个维度下设3个子维度和可证伪阈值测试；Ambient band 4级及以上评分需通过Idle-Gap Test：移除所有触发条件后仍有源自内部状态的活动，区分真正的自导向行为和预设定时/规则行为。

### 关键实验
测评6款主流系统，包括任务Agent（Claude Code、Manus、Hermes）、消费级助手（ChatGPT、Siri）、持久陪伴架构Airi：任务Agent的Active复合分达2.29~2.43，但Ambient复合分仅0.57~1.86，所有空闲期行为均来自用户配置的定时规则，无一通过Idle-Gap Test；消费级助手Active复合分1.57~1.71，Ambient复合分仅0.29~0.86，基本为完全被动架构；仅陪伴架构Airi通过Idle-Gap Test，Active复合分3.71、Ambient复合分3.86，是唯一空闲期评分高于活跃期的系统。

### 核心结论
当前主流任务Agent仅在任务内具备较高自主性，任务间隙几乎完全休眠，真正能在无任何外部触发下产生自导向行为的系统仍极为罕见。
