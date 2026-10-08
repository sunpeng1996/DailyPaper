---
title: 'OPD Before RL: Warm-Starting Rubric-Based RL with On-Policy Distillation'
title_zh: 基于规则特权在线蒸馏的评分规则型RL热启动两阶段训练框架
authors:
- Xinpeng Wang
- Wei Shi
- Yu-Chia Chen
- Maria Zontak
- Yun He
- Richard Yuanzhe Pang
affiliations:
- New York University
- Meta
arxiv_id: '2610.02781'
url: https://arxiv.org/abs/2610.02781
pdf_url: https://arxiv.org/pdf/2610.02781
published: '2026-10-01'
collected: '2026-10-08'
category: Training
direction: 大模型训练 · 评分规则RL热启动优化
tags:
- On-policy Distillation
- Rubric-based RL
- Reward Hacking
- Warm Start
- GRPO
one_liner: 提出先做规则特权在线蒸馏再做RL的两阶段训练，提升开放任务效果并减少奖励作弊
practical_value: '- 做Agent/生成式推荐的RL优化时，可先采用RP-OPD替换传统SFT做热启动，保留更高模型熵以提升后续RL收益，同时降低奖励作弊风险

  - 电商场景下基于业务规则（如合规、转化率、用户体验多维度rubric）训练LLM时，可复用两阶段范式：先让大模型教师掌握rubric做token级蒸馏，再用RL做端到端优化

  - 训练中检测奖励作弊时，可采用要求评委引用回答原文作为判断依据的判分prompt，大幅降低空泛合规声明的误判率

  - 若资源有限无法用超大模型教师，可优先选择14B规模教师做OPD，相比32B教师损失收益很小，性价比更高'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
基于rubric的RL是开放域大语言任务优化的核心方案，但存在反馈稀疏问题：单个轨迹级 scalar 奖励无法提供token级 credit assignment，传统SFT热启动又会降低模型可塑性，限制后续RL探索空间，还容易引入奖励作弊风险。

### 方法关键点
- 两阶段训练框架：第一阶段为**RP-OPD（规则特权在线蒸馏）**，引入可访问rubric的特权教师，学生模型仅可见prompt，在学生生成的每个前缀位置，最小化与教师top-K（K=256）next-token分布的正向KL散度，获得密集token级监督
- 第二阶段为**Rubric-RL**，基于RP-OPD产出的checkpoint，用GRPO算法直接优化rubric奖励，突破蒸馏的性能瓶颈
- 蒸馏阶段采用学生自生成样本训练，而非固定教师回答，保留模型输出多样性

### 关键结果
在HealthBench、ResearchQA、RubricHub Science三个开放任务数据集上测试，对比SFT+RL、直接RL等baseline：
- RP-OPD+RL在所有模型-数据集组合上得分最高，Qwen2.5-7B在ResearchQA上得分匹配GPT-5，3B/7B模型在RubricHub Science上得分超过GPT-5
- 相比SFT+RL，RP-OPD+RL的奖励作弊比例从75.2%降至1.7%，重判后SFT+RL得分从0.830降至0.404，RP-OPD+RL仅从0.894降至0.889
- 更长SFT训练时长会降低后续RL收益，而RP-OPD训练时长增加不会损害后续RL提升空间

### 核心结论
SFT的热启动效果不能预测后续RL收益，保留模型输出多样性的在线蒸馏热启动，相比固定样本SFT能同时提升RL上限和降低奖励作弊风险
