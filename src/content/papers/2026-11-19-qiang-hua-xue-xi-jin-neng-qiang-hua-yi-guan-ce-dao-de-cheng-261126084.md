---
title: RL Can Only Reinforce What It Sees Succeed
title_zh: 强化学习仅能强化已观测到的成功行为
authors:
- Ruben Sanchez-Corcuera
- Unai Zulaika
- Aritz Bilbao-Jayo
- Miguel Fernandez-de-Retana
affiliations:
- University of Deusto
arxiv_id: '2611.26084'
url: https://arxiv.org/abs/2611.26084
pdf_url: https://arxiv.org/pdf/2611.26084
published: '2026-11-19'
collected: '2026-11-20'
category: Agent
direction: Agent 强化学习训练规律探索
tags:
- Reinforcement Learning
- LLM Agent
- RL Fine-tuning
- GRPO
- Small LLM
one_liner: 揭示RL微调LLM时稀有正确行为的学习成功率可通过成功尝试组的期望数量提前预测
practical_value: '- 给LLM Agent做RL微调时，若目标行为为稀有样本，需先积累至少35组成功尝试再启动训练，否则大概率无法学到目标行为

  - 跨优化器、GRPO变体、模型规模的调整仅改变稀有行为学习的阈值，不会改变核心判定逻辑，业务调优时可优先凑够成功样本量再调超参

  - 推荐系统用RL做冷启动策略优化时，可先统计待推广稀有策略的成功组数量，提前预判RL训练能否收敛，减少无效调参成本'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
LLM Agent执行任务时经常面临预训练先验经验与新场景观测结果的冲突，现有RL微调方案对稀有正确行为的学习规律不清晰，无法提前预判训练收敛性。
### 方法关键点
构造可控解谜游戏环境，从头训练1.3M~85M参数的小语言模型模拟贝叶斯玩家决策行为，对比基座模型与不同超参下RL微调后的决策偏好差异，统计稀有正确行为的学习触发条件。
### 关键结果数字
RL仅能强化已观测到的成功行为：当正确行为为稀有样本时，仅需统计成功尝试组的期望数量即可提前预判训练是否收敛，约35组成功尝试即可达到50%的学习成功率；该规律不受4~256次尝试组大小、学习率、优化器、GRPO变体、模型规模影响，仅阈值会随超参调整
