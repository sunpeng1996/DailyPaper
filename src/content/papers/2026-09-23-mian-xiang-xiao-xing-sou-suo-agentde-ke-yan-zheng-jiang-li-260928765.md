---
title: Reinforcement Learning with Verifiable Rewards for Small Search Agents
title_zh: 面向小型搜索Agent的可验证奖励强化学习方法
authors:
- Gaurisankar Jayadas
- Aske Plaat
- Álvaro Serra-Gómez
- Sandheep P
affiliations:
- Leiden University
arxiv_id: '2609.28765'
url: https://arxiv.org/abs/2609.28765
pdf_url: https://arxiv.org/pdf/2609.28765
published: '2026-09-23'
collected: '2026-09-27'
category: Agent
direction: 小型Agent · 可验证奖励强化学习
tags:
- RLVR
- GRPO
- Small Language Model
- Reward Shaping
- Tool Use
- RAG
one_liner: 无需蒸馏用GRPO训练0.8B小搜索Agent，效果超基线3.8倍，验证稀疏精确匹配奖励表现最差
practical_value: '- 训练轻量化搜索/导购Agent时，放弃大模型常用的稀疏Exact Match奖励，改用token-F1类稠密奖励，可在无大模型蒸馏的前提下，用1B以下小模型实现3倍以上的效果提升，大幅降低训练和部署成本

  - 复用GRPO+检索工具的无蒸馏训练框架，仅需4卡消费级GPU即可完成小搜索Agent的训练，适配电商高并发的商品检索、售后问答等场景的轻量化Agent需求

  - 奖励设计中可添加格式合法性基础分，能降低无效无答案的rollout占比，减少线上推理时的token消耗和超时率，提升服务稳定性'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
RLVR（可验证奖励强化学习）在大模型多步推理、搜索工具调用任务上效果显著，但1B以下小模型此前仅能通过大模型蒸馏实现同类能力，无蒸馏训练方案缺失；小模型推理成本仅为大模型的1/10甚至更低，适配高并发、端侧部署需求，探索小模型搜索Agent的无蒸馏训练方案、适配小模型的奖励设计具备极高落地价值。
### 方法关键点
- 基座选用Qwen3.5-0.8B，采用无价值网络的GRPO优化器，训练显存开销比PPO降低近50%
- 控制变量对比三类奖励：稀疏0/1精确匹配（EM-only）、稠密token-F1（F1-only）、带格式合法性floor的F1+fmt
- 仅用MuSiQue多跳QA数据集训练，配套Wikipedia检索工具，检索返回内容掩码不参与损失计算，全程无蒸馏步骤
### 关键结果
在7个跨分布QA基准上测试，未训练基线平均EM为0.092，最优F1-only奖励模型平均EM达0.352，实现3.8倍提升；匹配训练步长下EM-only奖励在所有种子上表现最差，比F1类奖励平均低3.6pct，种子间波动最大；F1+fmt奖励种子稳定性最高，性能波动仅0.013。
### 核心结论
小模型RLVR不能直接照搬大模型的训练配方，需要针对性设计奖励信号，稠密的偏序奖励比稀疏的二值奖励更适配小模型的GRPO训练。
