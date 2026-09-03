---
title: 'SafeEvolve: Harness-Policy Co-Evolution from Agent Experience for Safety Alignment'
title_zh: SafeEvolve：基于Agent交互经验的Harness与策略协同安全对齐框架
authors:
- Qinghua Mao
- Wanying Qu
- Dadi Guo
- Leitao Yuan
- Qingyu Liu
- Yu Li
- Guanxu Chen
- Yanwei Fu
- Xi Lin
- Xia Hu
affiliations:
- 上海人工智能实验室
- 上海交通大学
- 复旦大学
- 香港科技大学
- 浙江大学
arxiv_id: '2609.02786'
url: https://arxiv.org/abs/2609.02786
pdf_url: https://arxiv.org/pdf/2609.02786
published: '2026-09-02'
collected: '2026-09-03'
category: Agent
direction: Agent安全对齐 · 策略与Harness协同进化
tags:
- Agent Safety
- Safety Alignment
- Co-evolution
- Harness
- SFT
- RL
one_liner: 通过Harness与策略的协同进化循环实现Agent安全对齐，降风险同时保留甚至提升任务效用
practical_value: '- 电商导购/客服Agent可直接复用该框架：先从历史交互轨迹提取安全风险（如引导私下交易、隐私泄露）迭代Harness的安全prompt/技能库，再通过两阶段SFT+RL让模型内化规则，避免纯规则Harness不被弱策略执行的问题

  - 可复用分场景奖励设计：正常任务奖励效用、恶意请求奖励安全得分、注入攻击场景同时加权效用和安全，适配推荐/广告Agent的差异化风险场景（如恶意引流、恶意query的差异化处理）

  - Harness的版本化、可审计更新机制可直接落地业务，每次安全规则更新都绑定风险案例、支持回滚，适配电商/广告的高合规要求，避免安全调整导致正常业务效果暴跌'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有Agent安全对齐方案要么仅迭代外部Harness（容易超出弱策略执行能力，多步交互中规则易失效），要么仅优化模型策略（固定Harness无法应对新兴风险，安全能力跨模型迁移差），两类方案都无法兼顾runtime安全控制与模型内在安全能力，多步工具调用场景下的prompt注入、恶意指令执行风险无法有效解决。

### 方法关键点
- 搭建Harness-策略协同进化闭环：用Agent与环境交互的on-policy轨迹作为共同输入，同时迭代外部Harness和内部模型策略
- Harness进化模块：将轨迹级安全证据转化为安全prompt、分层安全技能库的bounded版本化更新，所有更新可审计、可回滚
- 策略优化采用两阶段SFT-RL范式：第一阶段Harness-use SFT让模型先学会正确使用迭代后的Harness artifacts；第二阶段Harness-augmented RL用验证器分解的分场景奖励，让模型内化多步交互中的安全决策能力

### 关键实验
在AgentDojo（环境注入风险）、AgentDyn（动态注入风险）、AgentHarm（恶意query风险）三个基准上对比SFT、DPO、GRPO、MetaSecAlign、AgentAlign等基线；对Qwen3.5-4B，AgentDojo上ASR降低3倍（从2.37%到0.79%），同时良性效用从59.79%提升到61.86%；AgentHarm上有害得分从56.45降到12.27，拒绝率从28.98%提升到83.83%；对Qwen3-4B，AgentDojo效用从44.33%提升到60.82%，ASR从13.38%降到2.42%。

**最值得记住的结论**：Agent安全对齐不能孤立优化Harness或策略，协同进化既能获得可审计的外部安全控制能力，又能让模型内化安全决策，实现最优的安全-效用权衡。
