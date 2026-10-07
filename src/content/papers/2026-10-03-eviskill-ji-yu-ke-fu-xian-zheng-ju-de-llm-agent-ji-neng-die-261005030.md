---
title: 'EVISKILL: Grounding Skill Evolution in Replayable Evidence'
title_zh: EVISKILL：基于可复现证据的 LLM Agent 技能迭代框架
authors:
- Yan Zhou
- Yili Wang
- Yiwei Dai
- Qinggang Zhang
- Xin Wang
affiliations:
- School of Artificial Intelligence, Jilin University
arxiv_id: '2610.05030'
url: https://arxiv.org/abs/2610.05030
pdf_url: https://arxiv.org/pdf/2610.05030
published: '2026-10-03'
collected: '2026-10-07'
category: Agent
direction: Agent 技能自迭代优化
tags:
- LLM Agent
- Skill Evolution
- Replayable Evidence
- Continual Learning
- Procedural Knowledge
one_liner: 提出证据驱动的 Agent 技能迭代框架，通过可复现证据卡、定向重放验证和跨轮次传播提升技能有效性
practical_value: '- 搭建Agent技能迭代链路时，可将每个技能修正与对应的轨迹证据、触发区间绑定，仅重放关联片段验证效果，过滤无效修正，降低全量更新的试错成本

  - 整轮技能更新未通过全局验证时无需全量丢弃，通过单条修正的局部重放验证保留有效调整，放入临时账本跨轮次迭代，避免有效经验浪费

  - 可复用Replayable Evidence Card的设计，给推荐策略更新、用户行为分析结论等增加可追溯的证据标签，方便后续排查效果波动的根因'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有经验驱动的LLM Agent技能迭代方法存在两个核心痛点：一是技能修正与对应的行为证据、任务上下文脱离，容易生成看似符合轨迹逻辑但实际执行无效的更新，甚至导致技能退化；二是全局验证不通过就丢弃整批修正，会浪费其中局部有效的调整，技能进化效率极低。

### 方法关键点
- 设计Replayable Evidence Card结构，记录每个技能修正建议对应的轨迹触发区间、任务上下文，保留修正的溯源依据
- 分三阶段实现证据驱动的迭代：1）证据对齐的修正合成：从当前轨迹、跨轮次轨迹对比中抽取证据卡，生成绑定证据的候选修正；2）重放引导的修正验证：仅重放修正关联的轨迹片段，验证实际行为效果，对可修复的修正迭代优化后再审；3）跨轮次证据传播：整批更新被全局拒绝时，单条重放保留局部有效修正放入临时账本跨轮次迭代，未解决的证据卡可用于后续轮次的修正合成

### 关键实验
在ALFWorld、AppWorld、ScienceWorld三个交互基准，覆盖6个LLM骨干测试：1）18个模型-数据集组合中14个取得SOTA，相对无技能基线平均提升17.93pp；2）ScienceWorld任务上，Qwen3.5-9B下比最强基线高15.64pp，GPT-5.4下比最强基线高10.43pp；3）消融实验显示，移除重放验证平均掉点2.49~4.56pp，移除跨轮次传播平均掉点1.64~4.16pp。

**最值得记住的一句话**：技能进化不是经验修正的简单累加，而是要在每一次更新前验证实际行为效果、保留有效经验跨轮次迭代，才能避免技能退化、持续提升泛化性
