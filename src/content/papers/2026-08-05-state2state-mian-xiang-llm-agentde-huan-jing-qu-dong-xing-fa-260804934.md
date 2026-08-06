---
title: 'State2State: Environment-Derived Mid-Training for LLM Agents'
title_zh: STATE2STATE：面向LLM Agent的环境驱动型中间训练方法
authors:
- Xuanyu Lei
- Yiqi Zhu
- Chenliang Li
- Kaiming Liu
- Peng Li
- Ming Yan
- Jieping Ye
- Ya-Qin Zhang
- Yang Liu
affiliations:
- 清华大学人工智能产业研究院(AIR)
- 清华大学计算机科学与技术系
- 阿里巴巴集团智能计算研究院
arxiv_id: '2608.04934'
url: https://arxiv.org/abs/2608.04934
pdf_url: https://arxiv.org/pdf/2608.04934
published: '2026-08-05'
collected: '2026-08-06'
category: Agent
direction: LLM Agent 环境驱动中间训练优化
tags:
- LLM-Agent
- Mid-Training
- Reinforcement-Learning
- Environment-Exploration
- GRPO
one_liner: 无需人工标注任务与专家轨迹，将探索到的环境状态转化为训练目标，提升LLM Agent的交互与泛化能力
practical_value: '- 电商导购/客服Agent训练可复用零标注环境预训练思路：先让Agent在模拟交互环境中随机探索，将访问到的状态配对为「初始状态→目标状态」训练任务，无需人工标注即可先习得通用环境交互能力

  - 训练顺序可直接复用：SFT→环境驱动中间训练→下游任务RL，比直接做下游RL或把环境训练放在SFT前的效果更优

  - 稀疏奖励场景可适配动态采样GRPO：过滤全成功/全失败的无梯度样本组，大幅提升电商Agent等奖励稀疏场景的训练效率

  - 跨场景Agent迁移优先用环境驱动预训练：相比源域人工标注任务预训练，环境状态级预训练的跨域泛化效果更强，可用于跨品类导购、多平台客服等迁移场景'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM Agent训练范式分为两类：依赖专家轨迹的SFT，成本高且受限于轨迹覆盖范围；依赖人工设计任务与奖励的RL，瓶颈在任务与验证规则的人工构造。两类范式均被人工定义的任务分布束缚，无法覆盖环境中更多未被标注的状态，导致Agent泛化能力不足、训练成本高。

### 方法关键点
- 环境探索阶段：优先采用低成本的随机探索策略（而非带任务先验的LLM探索策略）遍历环境，最大化覆盖未被人工任务覆盖的可达状态，构建目标状态池
- 任务构建阶段：过滤无效状态后做多样性采样，重放3次验证状态可达性，将初始状态与目标状态配对为「状态迁移」训练任务，无需人工编写指令
- 训练阶段：基于归一化的状态精确匹配给出规则化奖励，用带动态采样的GRPO训练，过滤全成功/全失败的无梯度样本组，提升稀疏奖励下的训练稳定性
- 训练范式：作为中间训练阶段放在SFT之后、下游任务RL之前，先习得环境通用交互能力，再对齐人类任务目标

### 关键实验
在ALFWorld（家居交互）、ScienceWorld（科学实验）、MobileWorld（移动GUI交互）三类场景测试，对比基线包括仅RL、专家SFT、Agent Early Experience等：
- 全流程STATE2STATE+RL在ALFWorld上Qwen3-8B模型成功率达97.45%，比直接RL高5.09个百分点；在ScienceWorld上平均成功率达56%，比直接RL高3.87个百分点
- 下游RL训练效率提升2倍，50步即可达到直接RL 150步的效果
- 跨环境迁移时，ScienceWorld上做STATE2STATE预训练比用ScienceWorld人工任务预训练，在ALFWorld上成功率高2.57个百分点

### 最值得记住的一句话
Agent训练无需被人工定义的任务框住，从环境本身挖掘的无标注训练信号，既能降低标注成本，还能提升Agent的通用交互能力与跨场景泛化能力。
