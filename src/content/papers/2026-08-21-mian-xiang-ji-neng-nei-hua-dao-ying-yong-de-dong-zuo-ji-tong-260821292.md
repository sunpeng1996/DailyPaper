---
title: 'AUSO: Action-Level Unified Skill Optimization from Internalization to Utilization'
title_zh: 面向技能内化到应用的动作级统一优化框架AUSO
authors:
- Huizu Lin
- Chengkai Huang
- Tianqi Gao
- Tao Huang
- Daijiao Liu
- Tongxin Li
- Xiaoyan Sun
- Lina Yao
affiliations:
- 中国科学技术大学
- 新南威尔士大学
- 中国科学院大学
- 西安交通利物浦大学
- 独立研究者
arxiv_id: '2608.21292'
url: https://arxiv.org/abs/2608.21292
pdf_url: https://arxiv.org/pdf/2608.21292
published: '2026-08-21'
collected: '2026-08-24'
category: Agent
direction: Agent技能优化 · 强化学习
tags:
- LLM Agent
- Skill Optimization
- Reinforcement Learning
- GRPO
- OOD Generalization
one_liner: 提出基于JSD的动作级统一技能优化框架AUSO，打通技能内化到应用全周期，提升Agent性能与OOD泛化能力
practical_value: '- 技能内化阶段的JSD动作级加权策略可直接复用在电商导购Agent的技能蒸馏中，解决冷启动阶段RL无奖励信号的问题，无需额外标注，仅用同模型带/不带技能的分布差异做监督

  - 技能应用阶段的动作级梯度重加权方法，可迁移到推荐系统的用户转化路径优化中，对路径中受策略影响大的关键动作分配更高权重，提升长序列转化的训练效率

  - $p_q*(1-p_q)$不确定性门控设计可用于A/B测试样本筛选，对胜负不明确的实验分组优先做细粒度动作归因，减少阈值式分组的边界噪声

  - 2:5:3的技能内化/自主探索/技能应用三阶段训练比例，可直接复用在Agent RL训练的超参配置中，兼顾ID性能与OOD泛化能力'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有混合式Agent技能学习方法依赖轨迹级任务成功率阈值做路由，边界噪声大，且对同一轨迹内所有动作分配统一训练权重，忽略技能指导对不同动作的增益差异，导致技能内化不充分、应用不精准，长Horizon任务下OOD泛化能力弱。

### 方法关键点
- 以GRPO为统一优化backbone，分三阶段渐进式训练：早期教师引导的技能内化、中期自主探索、后期动作级技能应用
- 用JSD作为统一信息增益指标，量化带技能/不带技能条件下的动作分布差异，实现动作粒度的权重分配
- 早期内化阶段仅对全失败任务组加JSD蒸馏损失，权重随训练步平滑衰减；后期应用阶段用JSD衡量动作的技能敏感度，结合轨迹优势和$p_q*(1-p_q)$不确定性门控重加权梯度，不改变原有奖励符号
- 全程无需额外标注或环境rollout，所有分布计算均基于同策略已采样的状态

### 关键结果
在WebShop、ALFWorld、SearchQA三个基准上对比10+ SOTA baseline：WebShop ID/OOD平均准确率达49.7/51.2，较Skill0.5提升9.3/10.6个百分点；ALFWorld ID/OOD平均准确率达94.3/67.9，较Skill0.5提升1.2/9.4个百分点；SearchQA平均准确率达47.5，较SkillRL提升0.4个百分点，多跳任务泛化优势显著。

值得记住的一句话：技能对Agent的价值不由任务难度决定，而由它对每个具体动作的增益决定
