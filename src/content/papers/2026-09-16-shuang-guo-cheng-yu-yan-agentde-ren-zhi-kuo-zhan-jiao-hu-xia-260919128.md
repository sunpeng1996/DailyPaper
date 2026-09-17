---
title: 'Cognitive Extensions for Dual-Process Language Agents: Memory and Self-Reflection
  in Interactive Environments'
title_zh: 双过程语言Agent的认知扩展：交互环境下的记忆与自反思模块
authors:
- João Meneses dos Santos
- Arlindo L. Oliveira
affiliations:
- Instituto Superior Técnico, Universidade de Lisboa
- INESC-ID, Lisboa, Portugal
arxiv_id: '2609.19128'
url: https://arxiv.org/abs/2609.19128
pdf_url: https://arxiv.org/pdf/2609.19128
published: '2026-09-16'
collected: '2026-09-17'
category: Agent
direction: Agent 双过程架构认知扩展
tags:
- Dual-Process Agent
- Episodic Memory
- Self-Reflection
- Interactive Agent
- SwiftSage
one_liner: 为双过程语言Agent添加显著性门控记忆与边界化自反思模块，提升长交互任务表现
practical_value: '- 做电商导购Agent、搜索query纠错类交互Agent时，可优先上线前置Gate-1校验逻辑，在动作触达用户前过滤无效查询、违规回复、重复动作，无需改动大模型即可快速拿到效果收益

  - 记忆模块无需全量存储历史交互数据，仅留存转化成功、动作报错、接近达成目标等高显著性事件的半结构化记录，仅在动作失败、需要规划等特定触发点召回，大幅降低内存和prompt开销

  - 自反思、纠错类模块必须设置调用预算与冷却机制，单轮会话的大模型纠错调用次数不可过多，过度调用会打断正常交互流程、拉高推理成本，反而导致效果下降

  - 双过程Agent迭代优先级先稳执行链路再补记忆增强，执行层错误过滤带来的收益远高于单独加记忆模块，符合业务从0到1的迭代节奏'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
双过程语言Agent（如SwiftSage）在长周期交互任务中存在两个核心瓶颈：一是无持久化episodic memory，无法复用历史成功/失败经验；二是动作执行前缺少校验，易输出无效动作、陷入停滞循环，仅靠增大prompt无法解决生成结果与环境交互的边界错误。

### 方法关键点
- **Adaptive Memory Module（AMM）**：仅在发生得分变化、动作无效、成功/接近成功等显著性事件时存储半结构化短episodic记录，仅在快速动作通路（Swift）失败、慢通路（Sage）规划时触发检索，向prompt注入不超过3-5条记忆片段，记忆优先级低于当前环境状态。
- **Self-Reflection Module（SRM）**：动作触达环境前增加Gate-1校验，过滤/轻量修复无效动作；步后检测是否出现重复无效动作等停滞状态，仅在停滞时调用Critic生成最多5步修正动作，单轮任务Critic调用上限为3次，修正动作同样进入FIFO缓冲过Gate-1校验。

### 关键实验
在ScienceWorld交互基准上对比基线SwiftSage、基线+AMM、基线+SRM、全系统4种配置：全系统最终得分64.62（相对基线提升25.1%）、成功率43.17%、成功步数19.33步（相对基线降低21%）；单独加SRM得分64.33，贡献97%以上的全系统增益，单独加AMM仅提升4.1%。

### 核心结论
交互Agent优化的第一优先级是稳定执行链路，执行控制带来的收益远高于单独的记忆增强，记忆模块只有在执行链路稳定后才能发挥最大价值。
