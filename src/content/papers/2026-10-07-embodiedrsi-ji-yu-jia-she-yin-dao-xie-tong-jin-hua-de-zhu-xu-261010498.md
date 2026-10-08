---
title: 'EmbodiedRSI: Active Continual Robot Learning Through Hypothesis-Guided Co-Evolution'
title_zh: EmbodiedRSI：基于假设引导协同进化的主动持续机器人学习
authors:
- Python Song
- Zhixuan Liang
- Kelsey Fu
- Mengdi Wang
- Junfeng Yang
- Shilong Liu
affiliations:
- Columbia University
- Princeton University
arxiv_id: '2610.10498'
url: https://arxiv.org/abs/2610.10498
pdf_url: https://arxiv.org/pdf/2610.10498
published: '2026-10-07'
collected: '2026-10-08'
category: Agent
direction: 具身Agent 自进化架构优化
tags:
- Embodied Agent
- Continual Learning
- Dual System Architecture
- Co-Evolution
- Sim2Real Transfer
one_liner: 提出快慢双系统自进化具身Agent框架，冻结基座模型前提下大幅提升机器人任务泛化与迁移能力
practical_value: '- 信息价值优先的试验选择逻辑可复用在推荐系统冷启动探索：用VOI/成本排序待验证的召回/排序策略，减少无效流量测试，降低A/B测试成本

  - 快慢双系统架构可迁移到Agent化推荐系统：快系统做实时策略迭代响应即时需求，慢系统做长期经验沉淀与记忆优化，平衡迭代效率和长期收益

  - 多模块协同增益评估方法可复用：验证策略+特征组合效果时，固定初始条件分别测试单独与组合表现，精准定位贡献来源，避免A/B测试的混淆变量

  - 奖励驱动的记忆学习方法可用于RAG系统迭代：基于下游任务收益自动决定记忆的留存、合并、遗忘，替代人工设定的固定阈值规则'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
机器人基座模型在部署环境偏离预训练分布（如物体位置、任务指令变化）时性能骤降，微调需大量高成本人工遥操作数据；现有自进化具身harness对物理试验资源利用率极低，代码与技能单独进化、记忆按固定规则留存，无法支撑持续高效自适应。
### 方法关键点
- 快慢双系统架构：快系统基于Hypothesis Graph维护代码/技能候选及置信度，以信息价值/成本指标选择物理试验，快速迭代策略；慢系统构建三级分层记忆（M1原始交互数据、M2假设图、M3抽象认知）沉淀长期经验
- 代码-技能协同进化：固定初始状态分别测试代码、技能单独及组合效果，量化协同增益，将正向关系存入假设图
- 奖励锚定记忆学习：用PPO训练记忆操作策略，基于后续任务收益、不确定性降低、试验成本的综合奖励，自动决定记忆的留存/合并/遗忘
### 关键结果
- RoboCasa365基准整体成功率77.0%，分布外Composite-Unseen任务成功率71.3%，较最优基线Harness VLA提升77.8%；LIBERO-Pro基准整体成功率86.8%，较最优基线提升14.7pct
- 零样本Sim2Real迁移到真实机械臂任务，整体成功率从46.0%提升至71.3%，推理类任务提升8倍
- 相比随机探索，50次试验后成功率高45.8pct，学习AUC提升105.5%
### 核心结论
冻结基座模型前提下，通过高资源利用效率的自进化harness迭代，即可实现跨分布泛化与零样本跨模态迁移，无需大量标注数据重训基座
