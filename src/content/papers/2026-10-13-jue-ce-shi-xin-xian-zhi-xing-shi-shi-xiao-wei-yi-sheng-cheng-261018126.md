---
title: 'Fresh at Decision, Stale at Action: Routing New Information to LLM Decisions
  Already Made'
title_zh: 《决策时新鲜、执行时失效：为已生成的LLM决策路由新信息》
authors:
- Ayoub Merimi
- Souhail Bakkali
- Abdeljalil Sakat
arxiv_id: '2610.18126'
url: https://arxiv.org/abs/2610.18126
pdf_url: https://arxiv.org/pdf/2610.18126
published: '2026-10-13'
collected: '2026-10-14'
category: Agent
direction: LLM Agent 决策时效性优化
tags:
- LLM Agent
- Decision Routing
- Temporal Validity
- Freshness
- Memory System
one_liner: 提出决策时间戳理论与决策账本架构，解决LLM决策生成后执行前的信息更新有效性问题
practical_value: '- 做预约类电商Agent（订座、行程规划、预下单等）时，可引入决策账本机制：记录决策的依赖实体、修订截止时间、执行时间，替代仅存会话历史的简单方案，降低执行时信息失效的客诉。

  - 决策路由层优先采用watch conditions方案：决策生成时让LLM输出3-8条触发重决策的条件，对比全量背景知识索引，误召回率降低77%（20 vs
  89个陷阱召回），小模型场景下收益更显著。

  - 对依赖时间判断的决策，可前置规则级时间过滤：直接过滤掉生效时间晚于决策执行结束时间的消息，Qwen3-235B这类中大型模型准确率可提升6.7%，无额外推理成本。

  - 决策执行间隔超过1小时的场景，不要仅依赖决策时的RAG新鲜度：实验表明决策时再新鲜的信息，准确率上限由执行间隔时长和依赖实体变化率决定，必须加后决策路由环节。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有LLM时间相关研究仅关注决策生成时的信息新鲜度，适配问答类即时输出场景，但LLM Agent生成的预约、行程、预下单类决策往往间隔数小时到数天才能执行，决策时正确的结论会因执行窗口期内的新信息失效，该痛点尚未被系统性解决。

### 方法关键点
- 提出6个时间戳定义的决策有效性理论，推导新鲜度上限：决策执行时的准确率上限由决策生成到执行的时间间隔、依赖实体的变化率共同决定，仅提升决策时的信息新鲜度无法突破该上限。
- 设计决策账本架构：每条决策存储执行时间、修订截止时间、依赖实体背景知识、watch conditions（决策时生成的触发重决策的条件），新增路由层将新产生的事件匹配到关联的未执行决策，仅收到匹配事件的决策才触发重推理。
- 路由层提供三种索引方案：仅索引决策文本、索引决策+全量依赖背景、索引决策+watch conditions，适配不同推理能力的基座模型。

### 关键结果
在3套合成决策流（DIRECT/STRESS/INDIRECT）上测试5款LLM（从8B到GPT-6.1）：1. 无后决策路由时准确率恰好等于新鲜度上限（36%-50%）；2. 路由召回率达92%时，决策准确率最高提升61.4%；3. watch conditions方案对比全量背景索引，在保持92.2%召回率的同时，误召回的无关消息从89条降到20条；4. 小模型在路由召回足够时，90.6%的情况下能正确切换失效决策，剩余误差主要来自时间判断。

最值得记住的一句话：信息新鲜度只保证决策生成时正确，路由与时间判断才能保证决策执行时正确。
