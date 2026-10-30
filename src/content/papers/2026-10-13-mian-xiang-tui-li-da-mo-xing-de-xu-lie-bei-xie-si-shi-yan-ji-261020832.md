---
title: Amortizing Sequential Experimental Design in Reasoning LLMs
title_zh: 面向推理大模型的序列贝叶斯实验设计分摊方法
authors:
- Anita Kriz
- Antonin Berthon
- Nicolás Astorga
- Mihaela van der Schaar
affiliations:
- University of Cambridge
arxiv_id: '2610.20832'
url: https://arxiv.org/abs/2610.20832
pdf_url: https://arxiv.org/pdf/2610.20832
published: '2026-10-13'
collected: '2026-10-30'
category: Reasoning
direction: LLM主动信息采集 · 推理优化
tags:
- Bayesian Experimental Design
- Information Gathering
- LLM Reasoning
- Reinforcement Learning
- Transfer Learning
one_liner: 通过RL训练LLM推理过程实现序列BED分摊，提升信息采集能力且支持跨任务迁移
practical_value: '- 电商/客服Agent的主动澄清问题训练可复用该框架：用外部独立先验假设集+语义oracle计算EIG奖励，不依赖LLM自身置信度，训练出的提问策略泛化性更强、推理延迟更低

  - 生成式推荐冷启动用户偏好采集可借鉴该设计：用K步滚动非myopic EIG奖励训练，平衡短期信息收益和长期采集效率，避免冗余提问降低用户体验

  - 多轮交互场景（搜索query消歧义、导购对话）的奖励设计可参考：用期望信息增益（EIG）替代单步实际信息增益，减少奖励方差、提升训练稳定性，扩大训练假设集覆盖度可有效提升跨域迁移效果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM在多轮交互的主动信息采集任务中表现不佳：推理时实时计算贝叶斯实验设计（BED）的期望信息增益（EIG）延迟极高，无法适配实时交互场景；训练时若依赖LLM自身置信度生成奖励信号，易受幻觉影响，学到的策略泛化性差、跨任务迁移能力弱。
### 方法关键点
- 提出AR-BED框架，将序列BED的计算完全分摊到训练阶段，推理时无需额外EIG计算即可直接输出最优行动；
- 训练时将实验生成模型与策略LLM完全解耦：用固定的外部先验假设集计算EIG，用更大的外部LLM作为语义oracle评估问题似然，奖励信号不受策略LLM认知偏差影响；
- 支持K步滚动的非近视奖励优化，可选择单步EIG或多步累积EIG作为训练奖励，适配不同长度的交互场景。
### 关键结果
- 在Twenty Questions任务上，AR-BED跨域（动物→植物/名人/国家）平均solve rate比基线高12%以上，推理速度是推理时BED方案BED-LLM的61倍，训练速度是现有训练时摊销方案ASIG的2.9倍；
- 跨任务迁移到临床问诊数据集Medi-Q，OOD科室诊断准确率从84.8%提升至90.2%，Brier分数降低30.8%。
### 核心结论
主动信息采集能力可以作为通用推理技能植入LLM，无需推理时做复杂贝叶斯计算，且能跨域跨任务迁移。
