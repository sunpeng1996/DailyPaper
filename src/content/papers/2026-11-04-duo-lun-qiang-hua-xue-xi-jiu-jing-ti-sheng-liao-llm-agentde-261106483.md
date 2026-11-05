---
title: What Does Multi-Turn Reinforcement Learning Really Improve in LLM Agents?
title_zh: 多轮强化学习究竟提升了LLM Agent的哪些能力
authors:
- Kejian Zhu
- Zhuoran Jin
- Shangqing Tu
- Tianyi Men
- Yupu Hao
- Jiachun Li
- Kang Liu
- Jun Zhao
affiliations:
- 中国科学院自动化研究所
- 中国科学院大学人工智能学院
- 清华大学
arxiv_id: '2611.06483'
url: https://arxiv.org/abs/2611.06483
pdf_url: https://arxiv.org/pdf/2611.06483
published: '2026-11-04'
collected: '2026-11-05'
category: Agent
direction: LLM Agent 多轮RL能力分析与优化
tags:
- LLM Agent
- Multi-Turn RL
- Budget Robustness
- Pass@(K,T)
- GRPO
one_liner: 揭示多轮Agent RL收益依赖交互预算，提出BudgetMix实现跨预算鲁棒性能
practical_value: '- 业务部署多轮Agent（如导购Agent、客服Agent、Query纠错Agent）时，不能仅验证满交互预算下的效果，必须补充严预算（如交互轮数限制）下的测试，避免上线后资源受限场景效果暴跌

  - 若业务有严格交互轮数限制，无需额外采集高成本过程监督信号，直接使用BudgetMix训练策略，训练时随机采样不同交互预算，几乎不增加成本即可提升低预算下性能且不损失满预算效果

  - 多轮RL的核心优势是错误恢复，优先用于允许有限次重试的场景（如推荐结果不满意后的重推、Query改写重试）；单次决策要求高的场景（如高风险广告投放、不可逆操作）不要盲目上RL，避免单步决策质量下降'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
多轮Agent RL是当前提升LLM Agent长程任务性能的主流范式，但现有评估仅关注满交互预算下的轨迹成功率，忽略实际部署中普遍存在的交互轮数限制场景，RL的能力增益来源、部署风险均不明确，亟需系统性分析指导落地。

### 方法关键点
1. 提出双维度评估指标Pass@(K, T)，同时覆盖采样广度K（独立采样轨迹数）和交互深度T（单条轨迹最大交互轮数），量化不同约束下的Agent性能
2. 从轨迹层、步骤层双维度拆解RL能力：对比RL前后的单步决策质量、错误状态恢复能力、不同轨迹阶段的决策表现差异
3. 提出BudgetMix RL训练策略：训练时按10%间隔随机采样任务的最大交互预算，将预算信息加入prompt，超过预算未完成的轨迹 reward 置0，无需额外过程监督信号

### 关键结果数字
在DeepCoder-MT、BFCL、InterCode-SQL、FrozenLake四个跨域任务上，基于Qwen3-4B/8B底座，对比GRPO、GiGPO、PPO三种RL算法：
- BudgetMix在25%、50%、75%交互预算下，相对传统全预算RL平均提升4.2~4.8个百分点，满预算下性能无损失
- 传统全预算RL训练过程中单步决策质量平均下降0.005~0.018，BudgetMix可缓解该问题，单步质量稳定甚至略有提升
- 错误状态下RL的决策准确率比base模型高20%以上，是RL增益的核心来源

### 最值得记住的一句话
多轮Agent RL的收益核心来自错误恢复和长程执行韧性，而非单步决策质量的提升，其优势仅在充足交互预算下显现。
