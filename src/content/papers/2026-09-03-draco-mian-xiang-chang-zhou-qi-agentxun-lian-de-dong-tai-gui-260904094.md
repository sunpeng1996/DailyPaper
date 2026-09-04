---
title: 'DRACO: Fine-Grained Credit Assignment with Dynamic Rubrics for Long-Horizon
  Agent Training'
title_zh: DRACO：面向长周期Agent训练的动态规则细粒度信用分配
authors:
- Shubham Gandhi
- Saurabh Goyal
- Kiran Kate
- Yara Rizk
affiliations:
- Carnegie Mellon University
- IBM Research
arxiv_id: '2609.04094'
url: https://arxiv.org/abs/2609.04094
pdf_url: https://arxiv.org/pdf/2609.04094
published: '2026-09-03'
collected: '2026-09-04'
category: Agent
direction: 长周期Agent训练·信用分配
tags:
- Agent
- GRPO
- Credit Assignment
- Long-horizon
- Rubric
- RL
one_liner: 无ground truth验证器的长序列Agent训练框架，动态评分加闭式信用分配提效
practical_value: '- 电商客服、多轮导购类工具Agent无明确ground truth校验场景，可复用动态rubric生成逻辑：先基于每轮轨迹生成个性化评估标准再打分训练，效果优于固定规则评估

  - GRPO训练时可直接复用闭式信用分配逻辑，无需额外训练归因模块，仅基于评分关联的步骤重分配单步优势，就能大幅提升长序列任务的执行一致性，适合多轮推荐、履约Agent的RL训练

  - 可复用自评分降本方案：用训练中的策略模型自身作为评分器，搭配3次投票一致性校验，能将大模型评分成本降低5倍以上，效果接近外挂前沿大模型评分的水平，适合业务大规模落地

  - 长序列业务任务优化时，可重点对齐passk（连续k次成功）指标而非仅看pass@k，能有效降低重复调用的bad case率，与DRACO的训练优化目标天然匹配'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有长horizon Agent训练依赖可程序化的ground truth验证器，但电商客服、开放域导购、多轮推荐等真实业务场景大多没有这样的校验器，仅能基于过程标准提供奖励；同时轨迹级的单一奖励信号无法区分长序列中每一步的实际贡献，信用分配错配会直接导致训练效率低、效果不稳定、重复调用bad case多。

### 方法关键点
- 动态生成单轮轨迹专属rubric评分规则：先从任务指令生成基础评估标准，再结合每轮采样的多条轨迹补充分子目标与典型错误点，合并去重后仅保留组内至少1条轨迹未通过的标准，避免奖励过早饱和
- 闭式步级信用分配：将GRPO的轨迹级优势值，按评分器输出的每个评估标准关联的执行步骤，重新分配到对应步骤，总优势量、符号与原GRPO完全一致，长步骤的优势会被均分避免冗余，无关联的步骤继承组内平均质量分
- 无额外训练开销，整个分配过程为闭式计算，无需额外训练归因模块或奖励模型

### 关键实验
在AppWorld工具Agent基准上，DRACO较基础模型Task Goal Completion（TGC）提升15.9个点，较基于ground truth稀疏奖励训练的GRPO高5.3个点；零样本迁移到τ-bench银行业务场景，较基础模型成功率高4.6个点；采用策略模型自评分+3次投票校验的版本，评分成本降低5.1倍，效果仍超过基于ground truth训练的基线。

> 最值得记住的一句话：长horizon Agent无验证器训练的核心是先让评估标准精细到可对应具体执行步骤，再匹配信用分配逻辑，二者结合才能同时提升效果与训练效率
