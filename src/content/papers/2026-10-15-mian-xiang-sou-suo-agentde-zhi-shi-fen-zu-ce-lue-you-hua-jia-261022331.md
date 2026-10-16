---
title: 'KnowGPO: Knowledge-Grouped Policy Optimization for Search Agents'
title_zh: 面向搜索Agent的知识分组策略优化框架KnowGPO
authors:
- Siqi Chen
- Zhengxi Lu
- Yuchen Yan
- Xingyu Wu
- Qipeng Chen
- Xin Zhang
- Aiting Liu
- Chao Deng
- Jie Liu
- Jin Ma
affiliations:
- Zhejiang University
- Tencent
arxiv_id: '2610.22331'
url: https://arxiv.org/abs/2610.22331
pdf_url: https://arxiv.org/pdf/2610.22331
published: '2026-10-15'
collected: '2026-10-16'
category: Agent
direction: 搜索Agent · RL信用分配优化
tags:
- Search Agent
- Policy Optimization
- Credit Assignment
- Reinforcement Learning
- Long-Horizon Reasoning
one_liner: 提出知识分组策略优化框架，解决深度搜索Agent长时序信用分配问题，8B模型比肩32B开源系统
practical_value: '- 电商搜索导购Agent的RL训练可复用知识状态分组思路，将用户多轮搜索路径拆解为商品属性、活动规则、售后政策等可验证的原子知识条件，替代表面行为匹配，解决长路径搜索的信用分配问题，提升query改写、商品推荐决策的有效性

  - 可直接复用「增量知识增益」作为过程奖励的设计，无需训练额外奖励模型，仅基于已验证的知识获取量计算步级奖励，训练额外开销不足0.1%，适合业务场景快速迭代落地

  - 两阶段知识条件构建Pipeline可迁移至多跳商品查询、复杂售前咨询等知识密集型场景，先拆解推理骨架再做实体对齐，大幅降低知识标注的人力成本'
score: 9
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有深度搜索Agent的RL训练存在严重的信用分配短板：GRPO仅依赖终局奖励无法区分中间决策的价值；GiGPO依赖表面状态匹配，在异构搜索场景下状态重合度极低难以生效；IGPO基于模型内部置信度的奖励易受长噪声上下文干扰，导致长时序搜索决策优化效率低、效果差。
### 方法关键点
- 两阶段构建查询专属原子知识条件集：先仅基于查询拆解推理骨架生成带占位符的知识条件，再结合标准答案、成功参考轨迹对占位符做实体对齐，保证条件的原子性、完备性、实体一致性。
- 用知识状态表征轨迹进度：每步用外部LLM验证器检测当前观测新满足的知识条件，单调累加得到累积知识状态，消除表面观测差异的干扰。
- 混合优势计算：同知识状态的轨迹步做组内对比，以增量知识增益作为步级奖励，与终局优势按ω=0.3混合，用于PPO clipped目标优化，无需额外训练价值网络或奖励模型。
### 关键结果
在Xbench、BrowseComp-ZH、GAIA三个深度搜索基准上测试，对比GRPO、GiGPO、IGPO等同初始化基线，KnowGPO平均领先3.8~4.2个百分点；基于Qwen3-8B训练的模型性能超过多数32B开源搜索Agent，训练额外开销仅比GRPO增加0.08%。
### 核心结论
长时序知识密集型Agent的信用分配，锚定可验证的外部知识进度，远优于锚定表面状态或模型内部置信度
