---
title: Training AI Scientists to Replicate Research
title_zh: 训练可复现科研工作的AI科学家智能体
authors:
- Damon Falck
- Samer Sabri
- Anja Surina
- Thom Foster
- Anya Sims
- Sam Devlin
- Dylan Rogers
- Tantum Collins
- Kaloyan Aleksiev
- Louis Kirsch
affiliations:
- Inherent
arxiv_id: '2608.13331'
url: https://arxiv.org/abs/2608.13331
pdf_url: https://arxiv.org/pdf/2608.13331
published: '2026-08-13'
collected: '2026-08-14'
category: Agent
direction: AI科研Agent 论文复现能力训练
tags:
- AI Scientist
- GRPO
- LLM Agent
- Rubric Evaluation
- LoRA
one_liner: 提出Replica复现任务空间与rubric评分框架，训练27B参数Faraday超过Claude Opus 4.8与GPT-5.5
practical_value: '- 非可验证长周期任务奖励设计：可借鉴「自动生成任务专属rubric+多轮judge结果聚合」的方案，替代硬编码规则，解决电商营销方案生成、用户调研类Agent的奖励信号噪声大的问题

  - 小模型调度大模型的CAT架构可复用：用小尺寸LoRA微调的调度模型调用大模型完成推荐物料生成、A/B测试执行等子任务，比直接调用大模型成本低、可控性高

  - 长Horizon RL稳定性优化：可采用turn-level credit assignment的GRPO变种，解决推荐/广告多轮引导用户转化类Agent的训练不稳定、credit分配不准的问题'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前科研领域存在严重的复现危机，现有LLM Agent多针对明确闭合任务优化，难以处理论文复现这类天然信息缺失、需要开放探索的长周期任务，且缺乏低噪声、符合人类科研判断的奖励信号支撑RL训练。

### 方法关键点
- 构建Replica任务空间：从1990-2026年的100篇ML/AI for Science论文中自动生成310个图表复现任务，隐去原图表，要求Agent在1小时单GPU预算下复现，支持实验合理缩比
- 低噪声奖励机制：先由Claude Opus 4.7基于元prompt生成任务专属评分rubric（覆盖视觉匹配、科学claim支撑、实验合理性、资源利用、科研诚信5个维度），再用Codex GPT-5.5作为judge，取3次评估的均值作为奖励，同时输出turn-level credit分配权重降低RL训练方差
- 模型训练：基于Qwen3.6-27B用LoRA微调，采用改进的GRPO算法训练Faraday，支持调用Codex作为编码工具，调度大模型完成代码编写、实验执行等子任务

### 关键结果
在域内ML任务上，Faraday在73%的任务上超过Claude Opus 4.8和GPT-5.5，平均得分0.856，比Claude高6%，比Codex高8%；在域外侧重于AI for Science的测试任务上，60%的任务性能超过两个基线，平均得分0.791；自动prompt优化的Codex无法抹平性能差距，人类专家在Faraday占优的rollout中70.7%的情况更偏好Faraday的结果。

最值得记住的结论：用小参数模型训练判断能力、调度大参数模型完成执行任务的CAT架构，既能获得超过前沿大模型的综合性能，又具备可解释、成本低的优势。
