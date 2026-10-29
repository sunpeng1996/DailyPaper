---
title: 'AdaPRA: Process Reward Agents with Adaptive Rubrics for Data Science'
title_zh: AdaPRA：面向数据科学任务的带自适应评分标准的过程奖励Agent
authors:
- Atharva Naik
- Vivek Chari
- Pol Llado
- Daniel Fried
- Carolyn Rosé
- Benjamin Van Durme
- Sam Thomson
- Justin Svegliato
affiliations:
- Carnegie Mellon University
- Microsoft
arxiv_id: '2610.33245'
url: https://arxiv.org/abs/2610.33245
pdf_url: https://arxiv.org/pdf/2610.33245
published: '2026-10-22'
collected: '2026-10-29'
category: Agent
direction: Agent过程监督·自适应评分标准
tags:
- Process Reward Agent
- Adaptive Rubrics
- Data Science Agent
- Persistent Workspace
- Process Supervision
one_liner: 提出带持久工作空间、自适应评分标准的过程奖励Agent，显著提升数据科学任务表现
practical_value: '- 针对迭代式Agent任务（如广告策略优化、推荐特征工程自动化），可复用持久工作空间设计，跨尝试保留历史EDA、特征、模型结果，避免重复劳动，提升迭代效率

  - 过程监督无需仅依赖轨迹判断，可引入代码执行级校验，针对推荐链路的silent error（如特征泄露、线下线上不一致）设计可落地的rubric校验规则，自动识别隐性错误

  - 可先从简单任务离线挖掘通用rubric，再在复杂任务上自适应补充场景化规则，比如先在通用电商推荐数据集挖掘特征工程、模型验证的通用校验规则，再适配垂直品类场景，降低规则定制成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有数据科学Agent存在大量过程错误（如过早收敛到简单模型、验证集泄露、重复无效实验），且工作空间每次尝试重置、历史经验无法复用，导致排行榜表现远低于人类；传统过程奖励依赖静态规则，无法覆盖不同任务的专属坑点，也无法识别仅从轨迹看不到的隐性错误。

### 方法关键点
- 持久工作空间架构：跨尝试保留历史EDA笔记、特征、训练好的模型、验证结果，仅重置模型上下文，让后续尝试避免重复劳动，聚焦新方向
- 过程奖励Agent（PRA）：固定间隔校验Agent轨迹与工作空间，通过代码执行实现规则落地，仅返回重要的失败规则反馈，避免占用上下文，可在任务执行中实时纠正错误
- 自适应评分标准（rubric）：先从简单任务的Agent历史运行数据离线挖掘通用rubric，再针对每个任务动态增改rubric，补充场景专属校验规则，通用规则可跨任务迁移

### 关键实验
在DSGym的DSPredict-Easy（38个简单Kaggle任务）和DSPredict-Hard（54个跨模态复杂任务）上测试，基于80B Qwen3-Coder-Next作为基础Agent：
- 对比DSGym基线，AdaPRA将Easy任务平均排行榜百分位提升24.5个点，Hard任务提升14.8个点，表现匹配甚至超过GPT-5.1（high）单轮结果
- 消融实验显示：持久工作空间贡献Easy任务16.3个点增益，自适应rubric带来Hard任务4.3个点额外增益，代码执行校验带来Easy任务6个点增益
- 从Easy任务挖掘的通用rubric迁移到Hard任务仍能带来6.3个点的增益，且rubric可跨基础模型迁移，在DeepSeek-V3.2上也能显著提升表现

### 核心结论
Agent过程监督的效果提升来自「经验可复用的持久化架构+可落地校验的规则+通用+场景化结合的自适应规则体系」三者的协同，而非单一模块的优化
