---
title: Matched-Context Group Policy Optimization for LLM Agent Training
title_zh: 面向LLM Agent训练的上下文匹配分组策略优化算法MCGPO
authors:
- Chenxu Zhang
- Yaorui Shi
- Wenlong Zhang
- Jianchao Tan
- Zihan Wang
- Yiming Cheng
affiliations:
- Imperial College London
- University of Science and Technology of China
- Meituan
- Tsinghua University
arxiv_id: '2610.13755'
url: https://arxiv.org/abs/2610.13755
pdf_url: https://arxiv.org/pdf/2610.13755
published: '2026-10-09'
collected: '2026-10-12'
category: Agent
direction: 长 horizon LLM Agent 训练策略优化
tags:
- LLM Agent
- Policy Optimization
- Reinforcement Learning
- Credit Assignment
- Long Horizon
one_liner: 通过状态+任务进度匹配构造加权动作偏好，无额外critic提升长 horizon Agent训练效果
practical_value: '- 训练电商导购、商品搜索类Agent时，可直接复用「状态摘要+任务进度里程碑」的匹配规则构造动作对比偏好，无需额外标注即可提升长序列下单、多步搜索任务的训练效率

  - 可直接套用固定折叠划分思路，将同批次生成的rollout拆分为候选集和证据集，既避免偏好标注的数据泄露，又最大化已有交互数据的复用率，降低训练数据成本

  - 对于已落地GraphGPO等分组RL训练流程的业务，可直接叠加MCGPO的加权 pairwise 辅助损失，无需重构原有训练pipeline即可获得稳定的成功率提升'
score: 9
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
长 horizon LLM Agent训练的核心痛点是稀疏终端奖励下的中间步骤信用分配，现有分组策略优化方法仅靠重复状态匹配动作对比，忽略了任务前置进度差异，导致动作价值评估偏差，且对比组容易出现单动作样本不足的问题，无法生成可信的偏好监督信号。

### 方法关键点
- 匹配阶段：构造「状态摘要+观测到的评分进度+规则标注的可达成任务边界」的三元对比上下文，按精确→粗粒度的顺序匹配，仅保留两个动作都有足够样本的对比组
- 标注阶段：将同批次rollout固定划分为2个折叠，用相反折叠的终端结果标注偏好方向，结合结果差异幅度、样本支撑数、匹配粒度生成证据权重
- 训练阶段：在原有GraphGPO任务损失基础上，叠加加权 pairwise 辅助损失，完全复用已有rollout数据，不需要额外critic或交互

### 关键实验
在ALFWorld、WebShop两个基准，搭配Qwen2.5 1.5B/7B、Qwen3 4B/8B共6种设置测试，对比基线为GraphGPO：ALFWorld（基线成功率>92%）提升0.47~1.46个百分点，WebShop搭配Qwen3 4B/8B分别提升3.96、5.16个百分点；消融实验验证联合状态+进度匹配、交叉折叠证据、证据加权三个设计均带来正向收益。

### 核心结论
仅通过合理复用已有rollout数据构造上下文匹配的偏好信号，无需新增交互或引入critic，即可稳定提升长序列Agent训练效果。
