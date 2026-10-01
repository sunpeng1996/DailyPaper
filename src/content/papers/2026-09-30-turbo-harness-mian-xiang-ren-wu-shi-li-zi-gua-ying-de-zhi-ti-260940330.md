---
title: 'Turbo Harness: Instance-Adaptive Harness Optimization'
title_zh: Turbo Harness：面向任务实例自适应的智能体Harness优化框架
authors:
- Tunyu Zhang
- Hao Wang
- Kai Xu
- Dimitris N. Metaxas
affiliations:
- Rutgers University
- Red Hat AI Innovation
- MIT-IBM Watson AI Lab
arxiv_id: '2609.40330'
url: https://arxiv.org/abs/2609.40330
pdf_url: https://arxiv.org/pdf/2609.40330
published: '2026-09-30'
collected: '2026-10-01'
category: Agent
direction: 智能体Harness优化 · 实例自适应
tags:
- Agent
- Harness Optimization
- Instance Adaptive
- Reinforcement Learning
- Playbook
one_liner: 复用全局Harness优化历史训练轻量化编辑器，为每个任务实例生成专属Harness补丁提效降本
practical_value: '- 可复用业务中现有prompt/策略迭代的历史成功/失败轨迹、候选方案，蒸馏为结构化Playbook，无需从零构建实例自适应策略库，大幅节省优化成本

  - 采用小模型做补丁式修改而非全量生成策略的设计，推理 overhead 极低，还能减少上层大模型的执行步骤，适合电商客服Agent、搜索Query自适应改写等在线低延迟场景

  - 用RL微调小模型匹配实例特征与Playbook策略的范式，可迁移到个性化推荐的prompt自适应、不同用户群/商品类别的召回/排序策略适配场景，比直接调用大模型做决策成本低80%以上'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有Harness优化仅产出全局统一的执行框架，平均表现最优但无法适配每个任务实例的差异化需求；同时优化过程中产生的大量候选策略、执行轨迹、成败反馈等中间产物被直接丢弃，造成经验资产浪费，无法进一步挖掘优化收益。

### 方法关键点
- 复用全局Harness优化阶段的搜索归档数据，蒸馏为结构化Playbook，记录不同场景下生效/失效的Harness编辑策略、适用条件、效果反馈
- 训练轻量化Harness Editor（实验采用Qwen3.5-9B），基于GRPO做RL微调，输入任务实例、全局最优Harness、Playbook，输出适配当前实例的Harness补丁
- 推理阶段仅调用1次Editor生成补丁，补丁应用失败则自动fallback到全局Harness，额外开销可忽略

### 关键实验
覆盖交互Agent、软件工程、长周期终端任务3大类共7个基准，对比Meta-Harness、ReAct、Harness-R1等主流基线：
- 4个通用Agent基准上平均表现比全局最优的Meta-Harness高5.9个百分点
- SWE-smith-MR编码任务搭配Gemini 3.7 Flash时，通过率从70.7%提升至88.0%，执行步骤从23.1降至8.7，推理成本降低6.7倍
- 长周期Terminal-Bench 2.1任务上通过率达55.5%，比最优人工设计Harness高3.2个百分点，同时单任务成本降低11.5%

### 核心结论
Harness优化的中间产物不是废弃副产品，而是可复用的经验资产，实例级自适应适配能在全局优化基础上进一步释放性能、降低推理成本
