---
title: 'Teaching LLMs to Self-Evolve: Cultivating Core Meta-Skills with Reinforcement
  Learning'
title_zh: 基于强化学习的大语言模型自我进化核心元技能培养框架
authors:
- Shujin Wu
- Cheng Qian
- Xiusi Chen
- Heng Ji
affiliations:
- University of Illinois Urbana-Champaign
arxiv_id: '2607.21971'
url: https://arxiv.org/abs/2607.21971
pdf_url: https://arxiv.org/pdf/2607.21971
published: '2026-07-24'
collected: '2026-07-27'
category: Training
direction: LLM自进化 · 元技能强化学习训练
tags:
- Reinforcement Learning
- Meta-Skill
- Self-Evolution
- GRPO
- Code Generation
one_liner: 通过代码域强化学习训练大模型自进化元技能 实现跨任务跨域性能大幅提升
practical_value: '- 自优化Agent训练可复用轨迹合成思路：无需昂贵在线多轮rollout，从静态业务数据（如历史推荐策略迭代轨迹、广告文案优化记录）合成进化历史样本，大幅降低训练成本

  - 跨业务元能力训练可参考其奖励设计：针对业务目标构造可量化细粒度奖励（如推荐CTR+转化率、广告ROI+曝光效率组合），优先训练正向迭代轨迹（80%正确起始点+20%错误样本）效果优于均衡样本

  - 生成式推荐/文案优化的迭代推理可直接复用其超参配置：10轮迭代、每轮采样20个候选、保留Top5优质解的进化策略，在效率和效果平衡上表现最优

  - 系统自我纠错能力优化可复用多样性过滤方法，构造差异足够大的候选池，避免模型陷入局部最优的微小修改'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有测试时自进化框架（如AlphaEvolve）性能提升显著，但依赖推理时启发式策略，底层支撑的自我反思、反馈迭代、历史经验复用等元技能未被作为训练目标；传统后训练仅优化单轮任务完成率，无法支撑多轮自进化需求，元技能的跨域泛化价值也未被充分挖掘。

### 方法关键点
- 数据合成：基于大规模代码数据集，对每个问题采样10个候选解，经两阶段多样性过滤（问题层面筛选解多样性足够的样本，响应层面平衡质量和多样性）生成6k+高价值样本；每个样本构造包含问题、当前解、适配分（正确率+运行效率组合得分）、1-3轮合成进化历史的上下文prompt
- RL训练：采用GRPO算法，奖励为新生成解与当前解的适配分差值，未提升则给-1分惩罚，直接激励模型产出更优解
- 推理：复用AlphaEvolve的进化搜索框架，仅替换骨干模型为训练后模型

### 关键结果
在7个代码基准（4个训练域内、3个域外）和跨域算法优化基准AlgoTune上对比Best-of-N、Self-Refine、AlphaEvolve等基线：域内任务平均较最强基线高10.01%绝对提升，域外任务平均高24.12%绝对提升，跨域算法优化任务相对提升46.9%，生成的解结构新颖度也显著更高。

最值得记住的一句话：自我进化元技能可通过单域强化学习训练获得且能跨域迁移，比单纯堆推理计算量的提升效率高一个数量级。
