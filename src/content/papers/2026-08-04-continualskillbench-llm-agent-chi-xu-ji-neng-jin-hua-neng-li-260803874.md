---
title: 'ContinualSkillBench: Can LLM Agents Truly Evolve Their Capabilities?'
title_zh: ContinualSkillBench：LLM Agent 持续技能进化能力评测基准
authors:
- Tianyi Guan
- Yiding Wang
- Haotong Yang
- Siyuan Cao
- Shirui Liu
- Yi Hu
- Jiaqi Li
- Muhan Zhang
affiliations:
- Institute for Artificial Intelligence, Peking University
- Beijing Institute for General Artificial Intelligence
arxiv_id: '2608.03874'
url: https://arxiv.org/abs/2608.03874
pdf_url: https://arxiv.org/pdf/2608.03874
published: '2026-08-04'
collected: '2026-08-05'
category: Agent
direction: Agent 持续技能学习能力评测
tags:
- LLM Agent
- Continual Learning
- Skill Evolution
- Benchmark
- In-Context Learning
one_liner: 推出覆盖5个领域的有序连续任务评测基准，量化LLM Agent持续技能进化的真实收益与机制
practical_value: '- 电商/运营类Agent迭代可参考结论：纯In-Context Learning平均收益与显式技能维护相当，仅在需要精确输出、固定复用流程的场景（如合规文案生成、订单金额计算）才需要额外做显式技能库，大幅降低开发成本

  - 业务Agent的技能库管理可落地优化：定期清理低复用率的碎片化技能，合并语义相似技能，避免弱模型生成的大量细碎技能抬高检索成本、降低技能利用率

  - 垂直领域Agent评测可复用任务构造逻辑：按技能依赖关系、难度递进构造有序连续任务流，相比孤立任务测试更贴近真实业务连续交互场景，评测结果更具参考性'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前LLM Agent普遍依赖外部技能库提升复杂任务解决能力，但现有评测均基于孤立任务、固定技能库，无法衡量Agent在连续业务交互中自主演化技能、跨任务迁移能力的真实水平，也不清楚技能迭代对任务效果的实际贡献机制。
### 方法关键点
- 覆盖金融、法律、医疗、数学、办公5个垂直领域，每个领域构造100个按难度递进、存在跨任务技能复用依赖的有序子任务，69.5%的任务可复用历史核心技能
- 对比三类执行模式：独立执行（每轮清空记忆/技能库，基线）、纯ICL（保留上下文但不可修改技能库）、顺序执行（可动态维护更新技能库）
- 适配不同任务类型，采用Exact Match/F1/数值匹配/规则评审/程序执行多维度指标评估
### 关键结果
- 顺序执行相比独立执行在14/15的模型-领域组合上提升归一化奖励，平均相对增益达16.9%
- 纯ICL与显式技能维护的平均归一化奖励几乎持平（0.605 vs 0.602），显式技能仅在需要精确输出、固定复用流程的任务上有明显优势
- 能力较弱的模型（如GPT-4o）生成的技能库规模比GPT-5.3-Codex大87%，但技能调用频率低40%，碎片化严重导致复用效率极低
### 核心结论
当前Agent的持续学习收益大多来自上下文记忆而非可迁移的抽象技能，要实现稳定的技能演化还需解决技能合并、高复用技能提炼的核心问题
