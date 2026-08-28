---
title: 'RedEvoAgent: Automatic Red-Teaming Agent with Experience-Driven Skill Evolution'
title_zh: RedEvoAgent：具备经验驱动技能演化能力的自动化红队智能体
authors:
- Junjie Zhang
- Hui Liu
- Kecheng Chen
- Xianbo Mo
- Changsheng Chen
- Haoliang Li
affiliations:
- City University of Hong Kong
- Shenzhen MSU-BIT University
arxiv_id: '2608.27439'
url: https://arxiv.org/abs/2608.27439
pdf_url: https://arxiv.org/pdf/2608.27439
published: '2026-08-27'
collected: '2026-08-28'
category: Agent
direction: Agent安全评估 · 经验驱动技能演化
tags:
- Agent
- Red Teaming
- Skill Evolution
- Jailbreak
- LLM Security
one_liner: 通过经验蒸馏可读攻击技能+验证棘轮机制，提升LLM Agent红队攻击效果与可迁移性
practical_value: '- 业务Agent安全测试场景可复用该框架，替代全轨迹检索做自动化越狱风险探测，既降低上下文开销，又提升攻击覆盖率，提前发现风险漏洞

  - 推荐/广告系统的多策略工具调度场景（如多召回源/排序策略调度），可借鉴Deciding-Tool Attribution方法，归因最终效果对应的关键工具，解决工具共现导致的贡献误判问题，优化调度策略

  - Agent自我迭代场景可复用验证棘轮机制，仅保留在独立验证集上效果严格提升的策略更新，降低迭代噪音、避免过拟合

  - 演化得到的结构化可读技能具备跨模型跨场景迁移性，可沉淀不同业务场景的可解释技能库，降低新场景Agent冷启动成本'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前LLM Agent已广泛落地到产品级执行环境，越狱攻击会触发有害工具调用、修改系统持久化状态，风险远高于单纯的不安全文本生成。现有自动红队方案要么依赖固定攻击策略泛化性差，要么基于全轨迹检索，存在检索偏差、工具贡献归因不清、上下文开销大、可解释性弱的缺陷，亟需更高效、可解释的自动化红队方案。

### 方法关键点
- 架构上将7种互补越狱工具集成到统一工具箱，将跨案例攻击轨迹蒸馏为简洁可读的Markdown格式攻击技能文档，作为Agent调度工具的核心指导，大幅降低推理时上下文开销
- 构建Tool-Effectiveness Profile，在训练集上单独评估每个工具的攻击效果，输出工具优先级基线，避免先验工具选择偏差
- 设计Deciding-Tool Attribution机制，将成功轨迹中直接导致攻击生效的工具标记为决定工具，解决轨迹中工具共现导致的贡献误判问题
- 引入验证棘轮机制，候选技能更新只有在独立验证集上效果严格优于当前版本才会被保留，否则丢弃并记录失败迭代方向，避免无效更新和过拟合

### 关键结果
在ASB、AgentHarm两个安全基准上测试，覆盖3款主流目标模型、2种产品级执行环境，对比固定攻击工具、RedCodeAgent、MAJIC等基线：
1. 所有场景下均匹配或超过最优单工具效果，ASB数据集最高ASR达100%，AgentHarm数据集最高HarmScore达74.4%
2. 单案例平均工具调用次数降低30%以上，攻击效率显著提升
3. 演化得到的攻击技能可跨攻击模型、跨执行环境零样本迁移，相比无技能基线带来5%~10%的效果提升

**最值得记住的一句话**：多工具调度型Agent的经验迭代，将轨迹蒸馏为结构化可读技能+验证棘轮的模式，效果显著优于全轨迹检索或固定策略，同时兼具可解释性和可迁移性。
