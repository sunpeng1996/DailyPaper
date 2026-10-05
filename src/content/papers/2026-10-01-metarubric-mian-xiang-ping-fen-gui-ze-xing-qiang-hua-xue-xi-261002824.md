---
title: 'MetaRubric: Learning to Reward for Rubric-Based Reinforcement Learning'
title_zh: MetaRubric：面向评分规则型强化学习的奖励优化框架
authors:
- Yuxuan Fan
- Jaehong Yoon
affiliations:
- Nanyang Technological University (NTU), Singapore
arxiv_id: '2610.02824'
url: https://arxiv.org/abs/2610.02824
pdf_url: https://arxiv.org/pdf/2610.02824
published: '2026-10-01'
collected: '2026-10-05'
category: Training
direction: RL训练 · 评分规则动态优化
tags:
- Reinforcement_Learning
- GRPO
- Reward_Modeling
- Rubric
- Alignment
one_liner: 解决评分规则型RL空信用问题，提出证据感知策略与动态评分规则交替优化框架，医疗任务性能大幅超越基线
practical_value: '- 做LLM-based Agent/生成式推荐的RLHF/RRHF时，可复用证据感知奖励校验逻辑：每个评分维度必须同时满足满意度、内容覆盖、证据支撑三个条件才给分，避免奖励作弊

  - 电商大模型文案生成/导购Agent的评分规则可以动态迭代：根据当前模型的错误分布调整不同评分维度的权重，同时修正规则描述歧义，不用一开始就追求完美规则

  - 可复用反事实prompt pair构造方法：通过修改一个关键事实构造对照样本，强化模型输出对任务关键信息的感知，避免生成泛泛而谈的无效内容

  - 训练过程中加入辅助QA奖励验证输出有效性：用小模型从生成的回答中抽取关键信息答题，确保模型输出确实包含用户需要的核心信息，避免空泛回复拿高分'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
基于评分规则（Rubric）的强化学习在开放任务中存在「空信用（Vacuous Credit）」问题：即使响应完全没有包含规则要求的信息/动作，打分器仍会给高分，导致奖励信号失真，GRPO优化的优势符号可能被反转，最终模型偏好生成泛泛而谈的无效回复而非满足真实需求的内容，该问题在对输出准确性要求高的场景影响尤为严重。

### 方法关键点
- 双循环交替优化架构：内循环做证据感知的GRPO策略优化，外循环基于当前模型的输出动态调整评分规则
- 证据感知奖励计算：每个评分维度的得分取满意度、内容覆盖、证据支撑三个得分的最小值，整体奖励额外加全局证据上限、质量因子，再结合辅助QA奖励（小模型从生成内容中抽取关键信息答题的准确率）
- 动态评分规则优化：每轮训练后，基于模型错误分布调整不同严重度规则的权重（保证优先级顺序不变），再基于输出修正规则描述，仅保留能提升和专家打分一致性、且不改变规则原始语义的修订
- 反事实样本增强：每个原始prompt配对一个修改单个关键事实的反事实prompt，强化模型对关键信息的感知

### 关键实验
在PubMedQA、HealthBench-Hard两个文本医疗数据集，MMOral-X、MMOral-OPG两个多模态医疗数据集上测试，对比静态judge GRPO、DAPO、Dr.GRPO等基线，PubMedQA准确率提升6.00–20.40个百分点，HealthBench-Hard提升2.46–3.19个百分点，多模态任务提升1.29–3.82个百分点。

### 最值得记住的一句话
静态评分规则必然存在的歧义会导致奖励作弊，将奖励和输出的实际证据绑定、同时让评分规则适配模型当前的错误分布，能大幅提升RL的训练效果。
