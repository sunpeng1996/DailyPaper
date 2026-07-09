---
title: 'Agon: Competitive Cross-Model RL with Implicit Rival Grading of Reasoning'
title_zh: Agon：基于隐性对手推理评分的跨模型竞争强化学习
authors:
- Vladislav Beliaev
affiliations:
- Independent Researcher
- thinkdense.ai
arxiv_id: '2607.07690'
url: https://arxiv.org/abs/2607.07690
pdf_url: https://arxiv.org/pdf/2607.07690
published: '2026-07-08'
collected: '2026-07-09'
category: Training
direction: LLM推理优化 · 竞争强化学习
tags:
- RL
- GRPO
- LoRA
- Reasoning
- LLM Training
- Multi-Agent
one_liner: 用双LoRA跨模型竞争RL实现隐性推理评分，无需过程标签大幅提升LLM推理能力
practical_value: '- 推荐/Agent场景的RL优化可复用双LoRA竞争范式，无需额外标注过程标签，仅用可验证的业务目标（点击、转化等）作为奖励即可提升策略质量，内存开销仅增2%，落地成本极低

  - 推理类Agent（电商客服话术生成、选品决策Agent等）可复用draft-challenge两阶段级联架构，先出草稿再校验优化，在翻倍推理预算的前提下大幅提升输出准确率，还可缩短输出长度降低延迟

  - GRPO训练的长度膨胀问题可借鉴转换奖励+可选长度tiebreak机制，在不损失准确率的前提下压缩输出token数，适合低延迟要求的场景如搜索query改写、实时推荐文案生成'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前基于结果的RL（如GRPO）仅评判最终答案，在难任务上会诱导模型生成长推理链凑正确率，出现严重的长度膨胀、推理密度低问题；而推理过程标注成本极高，过程奖励模型又存在不稳定、难验证的缺陷，无法从根本上解决问题。

### 方法关键点
- 双策略竞争架构：两个差异化策略轮流担任drafter和challenger，drafter生成解决方案，challenger阅读drafter的推理摘要（隐藏最终答案）后独立作答，相互作为对方的隐性评审
- 高效实现：共享基座大模型，仅新增两个差异化LoRA适配器，内存开销仅增加~2%，通过不同初始化和独立更新流保证策略的行为差异
- 无标注奖励设计：仅用可验证的最终正确性作为基础奖励，新增转换bonus：challenger在drafter答错的场景下答对可获得额外奖励，无需任何过程标签
- 推理级联：训练和推理架构一致，直接采用draft→challenge两阶段级联输出结果

### 关键结果
在DeepMath-hard数据集上测试Qwen3-0.6B：Agon的pass@1达61%，是vanilla GRPO（30%）的2倍，比未训练MoA（34%）高27pp，同时最终推理链长度从GRPO的8.1k压缩到3.5k；在CodeContests代码任务上pass@1从24%提升到34%；效果可跨模型家族迁移（Qwen3.5、Gemma4均生效），小模型增益更显著，0.6B规模Agon效果超过7倍大的4B模型vanilla GRPO的表现。

最值得记住的一句话：两个差异化弱策略通过竞争互训获得的能力增益，远高于单一强策略和无训练的多模型聚合，是低资源提升模型能力的高性价比路径。
