---
title: When Does Action Credit Need Updating?
title_zh: 工具使用Agent策略更新后动作信用的刷新时机判定方法
authors:
- Hongye Yang
- Boxiao Huang
affiliations:
- Georgia Institute of Technology
arxiv_id: '2609.29007'
url: https://arxiv.org/abs/2609.29007
pdf_url: https://arxiv.org/pdf/2609.29007
published: '2026-09-24'
collected: '2026-09-25'
category: Agent
direction: 工具Agent · 历史信用自适应更新
tags:
- ToolAgent
- CreditAssignment
- PolicyUpdate
- OffPolicyEvaluation
- AdaptiveGate
one_liner: 提出DSC-Gate自适应复用修正历史动作信用，减近40%工具调用几乎不抬升regret
practical_value: '- 电商客服/运营工具Agent迭代时可复用该机制，仅对策略更新影响大的动作分支重新采样，可降低30%+的工具调用成本，几乎不影响效果

  - 推荐系统策略迭代后，可借鉴pairwise branch sensitivity判断召回/排序分支的性能漂移是否影响最终排序结果，避免全量回扫评估，大幅降低迭代成本

  - 可复用一阶锚定信用传输方法，用历史交互轨迹低成本修正策略更新后的动作价值估计，不用全量重跑离线评估流程'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
工具使用Agent持续迭代时，每次策略更新后全量重算动作信用会产生大量额外工具调用与环境交互成本，现有全局策略距离等指标无法精准判断历史信用是否失效；实际上数值层面的信用漂移不一定会改变最终决策，仅当漂移足够大到推翻原有动作排序时才需要刷新信用，因此需要更轻量化的判定机制降低迭代成本。

### 方法关键点
- 提出pairwise branch sensitivity，度量策略更新对候选动作下游差异访问区域的影响程度，相比全局策略KL更精准刻画相对信用漂移
- 推导一阶锚定信用传输估计器，基于历史干预轨迹修正旧信用，无需重新采样即可得到更新后的动作相对价值
- 设计DSC-Gate三级决策机制：若旧动作间隙大于漂移上限则直接复用历史信用，否则尝试传输修正，结果置信度足够则采纳，剩余场景才触发重新采样

### 关键实验
覆盖4层受控实验+真实零售场景工具Agent验证，对比Gap-Gate、WIS-Gate等基线；独立测试集上DSC-Gate相对Gap-Gate仅提升regret 0.00004，同时将平均新工具步骤从472降至286，减少39.4%；在经LoRA更新的Qwen3-4B真实工具Agent上，同样保持regret几乎不变，减少30.9%的新工具调用。

### 核心结论
Agent策略更新后无需全量重算所有动作信用，仅当漂移可能改变动作排序时才需要刷新，可大幅降低迭代交互成本。
