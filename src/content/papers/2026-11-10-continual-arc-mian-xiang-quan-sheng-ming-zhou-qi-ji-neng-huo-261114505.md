---
title: 'Continual-ARC: Measuring Skill Acquisition over a Working Lifetime'
title_zh: Continual-ARC：面向全生命周期技能获取的持续学习评测基准
authors:
- Daniel Lenton
affiliations:
- Unify
arxiv_id: '2611.14505'
url: https://arxiv.org/abs/2611.14505
pdf_url: https://arxiv.org/pdf/2611.14505
published: '2026-11-10'
collected: '2026-11-11'
category: Agent
direction: Agent 持续学习能力评测基准
tags:
- Continual Learning
- Agent Evaluation
- ARC Benchmark
- LoRA
- Memory vs Weights
one_liner: 提出统一评测记忆/权重类学习方法的持续学习基准，验证权重微调泛化性显著优于Agent外置记忆
practical_value: '- 落地企业级Agent时优先用LoRA微调沉淀通用技能，外置记忆仅用来固化明确可验证的规则类任务，二者搭配投入产出比更高

  - 开源Agent默认记忆模块效果远低于朴素的任务演示缓存，需补充显式引导prompt，要求模型提取并存储验证后的可复用规则

  - 多用户共享的Agent系统可通过2个及以上用户的行为数据联合微调提升泛化能力，2用户即可达到泛化收益峰值，无需过度扩容训练数据源

  - 评估Agent长期学习能力时需拆分记忆（见过的任务复用）和泛化（新任务能力提升）两类指标，避免高估纯记忆带来的短期收益'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有持续学习基准存在三大缺陷：仅聚焦单一领域，模型预训练知识会干扰效果评估；单任务实例仅出现一次，无法区分模型记忆的是固定答案还是抽象规则；仅支持单类学习方法（要么梯度更新要么prompt/外置记忆），无法公平对比不同方案的优劣，亟需无领域偏置、跨方案统一的评测基准。
### 方法关键点
- 基于ARC-AGI三个版本构建终身任务流，任务无需领域知识，仅依赖计数、物体识别等核心先验，相同任务休眠间隔后以全新实例返回，避免缓存答案作弊
- 设计反馈计费机制：错误提交、申请演示各扣1点预算，单实例预算上限16点，按预算消耗占比打分，统一适配外置记忆、prompt、权重更新三类方案
- 任务流结束后设置两类测试：见过的任务新实例测记忆能力，未见过的新任务测泛化能力，同时支持单用户、多用户（2/4个并发用户，全局知识共享）两种评测场景
### 关键结果数字
在ARC-AGI-1数据集上测试，对比演示缓存、程序归纳库两类baseline，3款开源Agent，以及LoRA微调（DAgger算法用GLM-5.3 Flash输出训练Qwen3.5-9B）：
- 无显式引导的Agent记忆方案记忆能力比朴素演示缓存低30%以上，泛化收益为0
- 加专家引导（明确要求存储验证后的Python规则）的Agent记忆能力S_seen达0.74，追平程序归纳库，但泛化收益仍不显著
- LoRA微调方案记忆收益S_seen=0.57，泛化收益S_held=0.29，2用户联合训练时泛化收益提升至0.40，之后无明显增益
### 核心结论
仅靠Agent外置记忆无法实现跨任务泛化，权重微调才是沉淀通用技能的核心路径
