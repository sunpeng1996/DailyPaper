---
title: 'Lost in Recovery: Demystifying Recovery Behavior of Computer-Use Agents via
  Goal-Oriented Action Replay'
title_zh: 基于目标导向动作重放的计算机操作Agent恢复行为揭秘
authors:
- Byeonghun Bang
- Sangwoo Park
- Jinheon Baek
- Kangsan Kim
- Youngwan Lee
- Sung Ju Hwang
affiliations:
- KAIST
- ETRI
- DeepAuto.ai
arxiv_id: '2610.27954'
url: https://arxiv.org/abs/2610.27954
pdf_url: https://arxiv.org/pdf/2610.27954
published: '2026-10-19'
collected: '2026-11-03'
category: Agent
direction: 计算机操作Agent · 故障恢复能力评估
tags:
- Computer-Use Agent
- Failure Recovery
- Agent Evaluation
- Action Replay
- POMDP
one_liner: 提出RETRACE评估框架，系统量化计算机操作Agent的自主模型级恢复能力
practical_value: '- 长链路业务Agent（如电商运营自动化、智能导购Agent）的故障恢复模块优先选用通用大模型而非仅做过单向任务post-train的专用模型，后者的内置恢复能力会被大幅削弱，显式恢复指令下提升幅度仅0.4%左右。

  - 错误恢复评估可借鉴Transition-Consistent Recovery逻辑：除校验界面相似度外，额外验证恢复后执行相同后续动作是否得到一致结果，避免因隐藏状态变更导致的恢复成功误判，比纯LLM评估器的人评匹配度高28%。

  - 长任务Agent的重试策略优先采用「回到错误前一步重试」而非完全重启任务，相同重试预算下Success@1比完全重启高22%，重试效率大幅提升。

  - 无需额外训练，仅给Agent增加明确的恢复目标指令即可平均提升17.86%的恢复成功率，通用大模型最高可提升48.1%，是低成本提升Agent鲁棒性的有效手段。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前计算机操作Agent在长周期任务中错误会累积传播，现有恢复方案存在明显局限性：环境重置在生产专有场景不可行，全轨迹动作重放成本随链路长度指数上升，API回退仅支持web场景，Agent自主的模型级恢复能力从未被系统研究，其潜在价值和当前Agent的恢复水平均不明确。

### 方法关键点
- 提出RETRACE可扩展评估框架，定义**Transition-Consistent Recovery**作为恢复成功标准：恢复后的状态与目标状态执行相同下游动作必须得到完全一致的结果，同时叠加界面观察匹配校验，覆盖无视觉变化的隐藏状态变更场景。
- 评估流程分三步：先收集多次重放均成功的同策略轨迹，构造转移一致性数据集；再对轨迹注入受控扰动生成错误状态；最后通过目标导向动作重放，验证从错误状态恢复后能否复现原任务成功结果。
- 对比两类恢复策略：隐式恢复（直接复用前向决策策略，无额外恢复指令）、显式恢复（给Agent明确的恢复目标与对应上下文）。

### 关键实验
在OSWorld、WindowsAgentArena两个通用桌面Agent基准上测试5款主流Agent：① 理想恢复场景下，回到错误前1步的策略Success@1比完全重启任务高22%；② 现有Agent隐式恢复成功率普遍低于5%，加显式恢复指令后平均提升17.86%，通用大模型最高可提升48.1%；③ 准确的显式恢复能提升端到端任务成功率最高4.88%，但恢复准确率不足的专用模型会出现性能下降。

### 核心结论
当前计算机操作Agent的恢复能力是潜在存在的，只是未被常规前向任务执行流程激发，准确的模型级恢复是提升长链路Agent可靠性的核心杠杆。
