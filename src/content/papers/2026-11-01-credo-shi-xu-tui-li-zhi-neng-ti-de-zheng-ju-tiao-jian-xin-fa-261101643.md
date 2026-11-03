---
title: 'CREDO: Evidence-Conditioned Credit Assignment for Temporal Reasoning Agents'
title_zh: CREDO：时序推理智能体的证据条件信用分配方法
authors:
- Yue Leng
- Shengtao Wen
- Xiang Chen
- Xinyi Zeng
- Yu Tian
- Sheng-Jun Huang
affiliations:
- Nanjing University of Aeronautics and Astronautics
- Tsinghua University
- 360 Security Capability Center, Qihoo 360
arxiv_id: '2611.01643'
url: https://arxiv.org/abs/2611.01643
pdf_url: https://arxiv.org/pdf/2611.01643
published: '2026-11-01'
collected: '2026-11-03'
category: Agent
direction: Agent 时序推理训练优化
tags:
- Agent
- Credit Assignment
- GRPO
- Temporal Reasoning
- Reinforcement Learning
one_liner: 提出证据驱动的GRPO信用分配机制，从失败轨迹提取有效步骤信号，提升时序推理Agent性能
practical_value: '- 训练多步决策Agent（如电商导购Agent、多轮搜索推理Agent）时，可复用CREDO思路：不对全轨迹梯度按中间步骤证据质量重新分配权重，避免有用的检索/过滤步骤被最终错误结果连带惩罚

  - 同问题所有rollout全失败无有效GRPO信号时，可通过不同rollout的中间指标（如检索结果与目标答案token overlap、召回item相关性）做局部排名奖励，充分挖掘失败样本价值

  - 电商多步导购/搜索多轮推荐Agent训练可直接复用三阶段掩码设计，用检索结果与目标的重叠度作为机会代理信号，默认超参ρ=0.04、λ_local=0.03效果稳定，调参成本低'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
基于GRPO的多步决策Agent训练仅用终端奖励给全轨迹所有token分配相同权重，存在两个核心缺陷：1）最终答案错误时，有用的中间检索、证据过滤步骤会被连带惩罚；2）同问题所有rollout都失败时，GRPO奖励全部为0，中间步骤的质量差异无法被利用，浪费大量失败样本的训练价值，在需要多步时序推理的任务（如时序KGQA、多轮导购问答）场景下问题尤为突出。

### 方法关键点
- 拆分Agent推理流程为检索(Q)、证据选择(E)、推理回答(R)三个阶段，为每个阶段定义独立token掩码，明确梯度分配粒度
- 用中间证据与参考答案的token overlap作为质量代理指标，对同问题的不同rollout做阶段内排名，给排名更高的阶段分配正向局部奖励，即使全失败组也能生成有效学习信号
- 对保留了答案相关证据的轨迹，将默认0.04比例的GRPO梯度权重从检索、选择阶段转移到推理回答阶段，总权重保持不变，不改变原GRPO的终端奖励和轨迹级优势计算
- 无需额外训练评判模型，推理阶段无额外开销，仅在训练阶段生效

### 关键结果
在MultiTQ时序KGQA数据集上，相比最强基线Temp-R1，Overall准确率从78.0%提升到82.4%，多步推理问题准确率从55.0%提升到65.6%；跨KG迁移任务TimelineKGQA ICEWS Actor数据集上，准确率从30.9%提升到36.4%。

最值得记住的一句话：多步Agent训练中失败轨迹的价值远未被充分挖掘，仅通过同问题样本的中间证据相对比较，无需额外标注成本就能大幅提升训练效率。
