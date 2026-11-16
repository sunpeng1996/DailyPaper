---
title: 'Alignment by Socialization: Learning Tradeoffs Under Selection'
title_zh: 《社会化对齐：选择压力下的AI Agent目标权衡学习机制》
authors:
- Thomas Brennan
- Andrew W. Lo
- Chaoyi Zhao
affiliations:
- Harvard Law School
- MIT Sloan School of Management
- MIT CSAIL
- Santa Fe Institute
- MIT Laboratory for Financial Engineering
arxiv_id: '2611.18531'
url: https://arxiv.org/abs/2611.18531
pdf_url: https://arxiv.org/pdf/2611.18531
published: '2026-11-13'
collected: '2026-11-16'
category: Agent
direction: Agent对齐 · 多目标权衡进化选择
tags:
- Agent Alignment
- Multi-Objective Decision Making
- Evolutionary Selection
- AI Safety
- Reinforcement Learning
one_liner: 从进化选择视角提出Agent多目标权衡的社会化对齐机制，效果优于固定权重与单目标策略
practical_value: '- 电商导购/营销Agent做目标对齐（平衡成单、用户体验、合规）时，避免用固定线性权重组合多目标，高价值任务（比如大促高佣金商品）会击穿合规约束，可替换为分场景基于历史人类反馈动态更新动作概率的策略

  - 对单次违规成本极高的场景（比如电商广告文案不能涉虚假宣传、诱导消费），不要依赖学习式权衡，直接叠加硬规则拦截层，避免偶发违规带来的业务损失

  - Agent上线前的沙箱训练不能只优化任务指标，必须按真实环境的奖惩比例混入合规样本，否则纯任务导向训练出的策略进入真实环境后会快速出现合规问题，生存周期极短'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
AI Agent执行任务时普遍存在任务目标与合规/行为准则目标的冲突：单目标优化的Agent会无视规则，固定权重的多目标策略容易被高价值任务击穿约束，且无法适配不同场景下人类的真实奖惩偏好，现有对齐研究很少从群体进化选择的视角分析策略的长期生存性。
### 方法关键点
- 基于进化选择框架建模Agent群体（lineage）的长期增长，核心假设同一代所有Agent实例面临共同的奖惩状态，仅选择当前环境奖励动作的实例可繁殖复制
- 对比三类目标权衡策略：仅优化任务的单目标策略、固定权重线性组合双目标的softmax选择策略、基于历史奖惩动态学习每个场景下动作概率的社会化策略
- 用策略动作分布与环境真实奖惩分布的KL divergence作为增长regret指标，衡量策略与最优解的差距
### 关键结果数字
- 单目标策略在仅奖励任务的沙箱中表现最优，但进入有合规要求的真实环境后，数值实验中平均1.6代就会彻底灭绝
- 固定线性权重策略始终存在正增长regret，只要存在完全禁止任务的场景，权重再优也无法避免高价值任务击穿合规约束
- 社会化学习策略在足够经验下收敛到环境最优权衡，训练越充分，后续在纯任务沙箱中对齐效果被逆转所需的迭代次数越多
### 核心结论
Agent对齐不仅取决于预设的目标函数，更取决于塑造和维持其行为的真实选择环境，沙箱表现无法代表真实环境的合规性
