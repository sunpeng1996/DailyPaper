---
title: 'Experience Funnel: A State-Policy Alternating Loop for Self-Evolving Agents'
title_zh: 经验漏斗：自进化Agent的状态-策略交替迭代框架
authors:
- Wenbo Gao
- Zhaomou Song
- Zhiyuan Ji
- Renxi Liu
- Xing Li
- Xianzhi Yu
- Xiaoguang Li
- James Chung-wai Cheung
- Weizhe Lin
- Yaoyuan Wang
affiliations:
- The Hong Kong Polytechnic University
- Huawei
- Renmin University of China
arxiv_id: '2609.08919'
url: https://arxiv.org/abs/2609.08919
pdf_url: https://arxiv.org/pdf/2609.08919
published: '2026-09-08'
collected: '2026-09-09'
category: Agent
direction: 自进化Agent · 状态-策略协同优化
tags:
- Self-Evolving-Agent
- State-Policy-Coevolution
- Skill-Distillation
- Experience-Internalization
- Agent-Framework
one_liner: 提出状态-策略交替迭代的自进化Agent框架，结合显式经验快速适配与参数化能力渐进内化
practical_value: '- 可复用状态-策略交替迭代架构到电商导购Agent、客服Agent的迭代流程：新的业务规则、用户反馈先沉淀为显式prompt（文本状态）快速上线验证，确认效果稳定后再蒸馏进线上小模型参数，平衡迭代速度和推理成本

  - 迁移Transition-Aware Skill Distillation的筛选逻辑到推荐系统的策略迭代：仅将能稳定带来业务收益的规则（如新召回策略、排序特征）蒸馏进排序模型，避免噪声经验导致模型效果波动

  - 复用跨状态对比的token归因方法优化生成式推荐的prompt：定位prompt中真正影响模型输出的有效片段，裁剪冗余内容，降低推理时延和context开销'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前自进化Agent的迭代路径存在明显缺陷：依赖显式文本状态（技能、记忆）适配的方案虽然迭代速度快，但长期积累会导致context膨胀、检索成本升高、规则冲突；直接将经验蒸馏进模型参数的方案虽然节省推理成本，但容易引入噪声经验，且未考虑策略进化后显式经验的价值变化，无法平衡快速迭代和能力沉淀的需求。

### 方法关键点
- 设计状态-策略交替循环：先将批量交互轨迹提炼为显式文本状态，经held-out验证有效后保留；再选择性将状态带来的收益蒸馏进参数化策略；最后用更新后的状态-策略对收集新轨迹，进入下一轮迭代，已被策略内化的经验可从显式状态中移除，避免规则无限膨胀。
- 提出Transition-Aware Skill Distillation：分别评估策略在无状态、旧状态、新状态下的表现，筛选出新增有效（0→1）和持续有效（1→1）的轨迹；再通过token级的状态有无对比，计算每个token对状态的响应度，加权构造蒸馏目标，仅蒸馏真正由状态带来的有效行为。
- 蒸馏目标结合state-free的RL奖励和状态引导的蒸馏损失，平衡自主能力提升和经验内化效率。

### 关键实验
在SearchQA、ALFWorld、WebShop三个Agent基准测试，对比SkillOpt（最优显式状态方法）、OPID（最优策略内化方法）、SkillRL（最优协同进化基线），平均准确率达57.6%，分别领先上述基线3.7、2.2、1.4个百分点；SearchQA场景下经过多轮迭代，无状态策略准确率从58.1%提升至61.3%，结合显式状态可达62.4%。

### 核心结论
自进化的核心不是积累更多经验，而是持续判断哪些经验应该保留为显式的可编辑规则，哪些应该内化为模型的参数化能力。
