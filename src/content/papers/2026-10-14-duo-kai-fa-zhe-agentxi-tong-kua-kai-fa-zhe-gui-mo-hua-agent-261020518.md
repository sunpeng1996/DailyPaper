---
title: 'The Wealth of Agents: Scaling Agentic AI Across Developers'
title_zh: 多开发者Agent系统：跨开发者规模化Agent AI的新范式
authors:
- Austin W. Hanjie
- Carlos E. Jimenez
- Zirui Wang
- Karthik Narasimhan
affiliations:
- Princeton University
- UC Berkeley
arxiv_id: '2610.20518'
url: https://arxiv.org/abs/2610.20518
pdf_url: https://arxiv.org/pdf/2610.20518
published: '2026-10-14'
collected: '2026-10-15'
category: Agent
direction: Agent 跨开发者协作规模化优化
tags:
- Multi-Developer Agent
- Agent Orchestration
- Specialized Agent
- Agent Scaling
- Incentive Mechanism
one_liner: 提出多开发者Agent系统（MDA）架构，验证跨开发者组合专精Agent可获得优于单开发者系统的性能与成本效率
practical_value: '- 搭建电商/广告Agent生态时可参考MDA架构，接入商家/垂类服务商的专精Agent（如商品规格查询、售后政策解答Agent），无需全链路自研，降低开发成本的同时提升场景覆盖能力

  - Agent价值评估不能仅看孤立准确率，需评估其在组合系统中的互补价值，例如单独表现差的垂类客服Agent接入全局系统后可能大幅提升特定场景准确率

  - 路由层效果直接决定MDA整体性能，需基于实际交互数据动态调整路由策略，不可仅依赖Agent开发者的自描述，避免能力夸大的误导

  - 窄域任务（如纯搜索类Query回答）不适合MDA架构，额外的分解/编排开销反而会拉低性能、提升成本，优先采用rSDA即可'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前主流Agent系统均为单开发者构建（SDA），需重复开发全栈基础能力，资源浪费严重；中小开发者缺乏资源打造通用Agent，其专精能力无法贡献到全局系统；现有多Agent研究未考虑多开发者的异质性与激励问题，难以突破单开发者的资源天花板。

### 方法关键点
- 定义三类系统架构：单开发者Agent系统（SDA）、路由式SDA（rSDA，全任务选择最优单SDA）、多开发者Agent系统（MDA，任务拆分为子任务后路由到对应专精Agent，再组合结果）
- 用meta-agent模拟不同资源等级的开发者，在全局总预算一致的前提下生成三类Agent池：通用Agent池AG、专精Agent池AS、单开发者多Agent池AMAS
- 设计自学习σ路由Agent，基于实际交互效果而非Agent开发者自描述做路由决策，降低能力夸大的干扰

### 关键结果
- 在多能力要求的GAIA基准上，AS池中单Agent最高准确率仅35%，组合为MDA后准确率达70%，较耗费数倍预算的中位数通用SDA高12pp，较最优SDA高3pp，成本仅为最优SDA的1/2
- 单独准确率仅19%的垂类专精Agent接入MDA后，可将原有MDA准确率从40%提升至53%
- 在纯搜索类窄域基准SealQA上，MDA的编排开销抵消组合收益，性能低于rSDA

### 核心结论
Agent的价值不能仅用孤立场景的准确率衡量，跨开发者组合互补的专精能力，是比单开发者堆资源做通用Agent更高效的规模化路径。
