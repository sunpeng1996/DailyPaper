---
title: 'Capability-Gated Planning: Cost-to-Goal Discovery and the Limits of Myopic
  Experiment Selection'
title_zh: 能力门控规划：目标成本发现与短视实验选择的局限性
authors:
- Ahmed Hassoon
- Mark Dredze
affiliations:
- Johns Hopkins University
arxiv_id: '2608.05085'
url: https://arxiv.org/abs/2608.05085
pdf_url: https://arxiv.org/pdf/2608.05085
published: '2026-08-05'
collected: '2026-08-06'
category: Agent
direction: Agent 序列决策规划优化
tags:
- Planning
- Myopic Policy
- Sequential Decision Making
- Capability-Aware Planning
- Stochastic Shortest Path
one_liner: 证明固定前瞻短视信息最大化规划器有结构性缺陷，提出能力感知的CG-Plan解决长链能力获取问题
practical_value: '- 电商/推荐系统冷启动、新场景落地时，可借鉴CG-Plan的启发式拆分逻辑，把新特征管线、新召回通路这类建设性动作的成本和后续长期收益分开评估，避免短视的ROI排序直接砍掉高价值长期建设项

  - 业务Agent做复杂长周期任务（如大促全链路优化、用户生命周期价值运营）时，不要仅用固定步长前瞻收益做动作排序，可叠加能力依赖图的最短路径计算，平衡短期即时收益和长期能力建设价值

  - AB实验优先级评估可复用能力门控框架，区分即时收益类实验和基础设施类实验，避免资源全部倾斜到马上能拿到小收益的实验，忽略能解锁后续大量高价值实验的建设性实验'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前自动化序列决策系统大多采用短视评分（如单位成本EIG）选择动作，无法评估建设性动作的价值——这类动作本身不产生即时信息，但能解锁后续高价值操作。当目标达成需要长链建设性动作时，短视规划器会完全忽略前置能力建设，陷入低效率的局部操作，甚至永远无法达成目标。

### 方法关键点
- 将目标导向的决策过程建模为信念空间的SSP问题，建设性动作会改变下游可行动作图的拓扑结构
- 证明对任意固定前瞻深度d，都存在场景让短视信息最大化规划器的近似比无界，极端情况下永远无法达成目标
- 提出CG-Plan增量重规划器，设计能力感知的目标成本启发式 `h = h_cap + h_exp`：`h_cap`计算解锁目标所需全部能力的最小建设成本，`h_exp`估算能力完备后达成置信度目标所需的实验成本；加入路径感知逻辑对比建设路线和直接测量路线的成本，避免不必要的建设

### 关键结果
在布尔电路受控测试床中：
1. γ=0.02的门控场景下，CG-Plan在100个测试用例中100%达成目标，平均成本9.2，所有短视方法（贪心EIG、有限前瞻EIG等）成功率为0
2. 有限前瞻规划器只有当能力链长短于前瞻深度时才能成功，CG-Plan对任意链长都能100%成功
3. 增加无关干扰建设项时，CG-Plan成本保持稳定，短视方法+ε探索的成本是CG-Plan的11~19倍，干扰项较多时完全失败

**最值得记住：任何仅基于固定窗口内即时收益的决策规则，都会在需要长链前置能力建设的场景下失效，动作价值必须覆盖其对下游可行动作空间的扩展价值**
