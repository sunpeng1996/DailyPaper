---
title: 'Cliff: Learning Process Rewards from the First Mistake'
title_zh: Cliff：从推理首次错误中学习过程奖励的RL训练方法
authors:
- Peixuan Han
- Runhui Wang
- Ketan Ramaneti
- Jie Hao
- Gerald Friedland
- Chris Kong
affiliations:
- Amazon Web Services
- University of Illinois Urbana-Champaign
arxiv_id: '2609.02817'
url: https://arxiv.org/abs/2609.02817
pdf_url: https://arxiv.org/pdf/2609.02817
published: '2026-09-01'
collected: '2026-09-03'
category: Training
direction: LLM RL训练 · 过程奖励优化
tags:
- RLVR
- GRPO
- Process Reward
- Reward Shaping
- LLM Post-Training
one_liner: 基于GRPO的奖励塑造策略，定位推理首错分配细粒度优势，较GRPO提7%、较OPD提15%
practical_value: '- 做垂域Agent/LLM4Rec的RL微调时，可直接复用Cliff的奖励分配逻辑，无需额外训练PRM，仅定位任务反馈的首个错误点分配正负优势，大幅降低对齐成本

  - 业务场景有可量化验证指标（如推荐转化、搜索准确率）时，可搭配自动verifier+中等能力垂域模型作为老师执行Cliff训练，无需依赖SOTA大模型即可获得稳定收益

  - 训练超参数λ直接设0，同时增加超长输出全序列判负规则，可彻底避免模型为刷奖励生成无意义长文本的长度hack问题

  - 无ground truth可验证的场景下，使用能力足够的内部垂域SOTA模型作为老师，Cliff性能几乎无损失，适配无标注业务场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有基于可验证奖励的强化学习（RLVR）仅给全推理轨迹分配粗粒度结果奖励，credit分配效率极低；过程奖励模型（PRM）需额外训练，易出现reward hacking，On-Policy Distillation（OPD）要求师生推理模式、分词器一致，适用场景受限，亟需通用的细粒度过程奖励方案。
### 方法关键点
- 基于GRPO扩展，引入老师模型定位学生推理轨迹的首个错误（Pitfall Step），将轨迹拆分为正确前缀、错误后缀两段，无需逐步评估
- 优势分配规则：全对轨迹所有token分配统一正优势；错误轨迹前缀给低优势、后缀给负优势，λ控制前缀奖励强度，新增偏移项b实现组内优势零均值校准
- 容错机制：老师先自行解题，仅当老师输出被自动verifier验证正确时执行Cliff逻辑，否则退化为原生GRPO，避免错误引导
- 稳定性设计：λ设为0避免长度hack，超过最大长度的输出直接全序列判负，进一步降低奖励作弊风险
### 关键结果
在数学推理、编码两大领域共12个场景测试，对比GRPO、OPD、知识蒸馏等基线，平均性能较OPD高15%，较原生GRPO高7%；即使是能力中等的开源老师模型也能获得稳定收益；无ground truth过滤时，强SOTA老师性能几乎无损失，弱老师仅掉2%左右，仍优于原生GRPO。
### 核心结论
过程监督不需要精准评估每一步推理，只要找到首次出错的位置，就能获得足够高效的细粒度训练信号。
