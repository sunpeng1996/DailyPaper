---
title: 'SCOPE-RL: Optimizing Reasoning Paths Before and After Success'
title_zh: SCOPE-RL：面向成功前后阶段的推理路径优化框架
authors:
- Xiaojian Liu
- Han Xu
- Jianqiang Xia
- Zhixuan Li
- Ke Xu
- Yiwei Dai
- Xinran Chen
- Changwo Wu
- Yuchen Li
affiliations:
- Baidu Inc.
- Shandong University
arxiv_id: '2607.11506'
url: https://arxiv.org/abs/2607.11506
pdf_url: https://arxiv.org/pdf/2607.11506
published: '2026-07-13'
collected: '2026-07-14'
category: Training
direction: LLM训练 · RL推理优化
tags:
- RLVR
- GRPO
- Reward Shaping
- Sparse Reward
- Reasoning Optimization
one_liner: 基于成功前后分阶段稠密化奖励信号的RLVR框架，兼顾推理精度与效率
practical_value: '- 做Agent推理优化可复用两阶段训练思路：先通过子目标奖励解决难任务探索不足问题，正确率达标后加过程奖励剪枝冗余推理，降低token消耗且不损失效果

  - 自适应路由策略可直接落地：仅对当前模型解决率低于阈值的难query触发子问题拆解、RAG等辅助增强，易case走原流程，平衡效果与算力成本

  - 正确性门控的过程奖励设计可复用：先通过规则验证最终结果正确，再为推理过程打分优化，避免为了简洁性牺牲正确性，适配营销文案生成、售后应答等电商场景'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
基于稀疏最终答案正确性奖励的RLVR框架存在两大痛点：成功前难任务的中间推理进度无有效奖励信号，训练易陷入停滞；成功后无法区分高价值正确路径与冗余/局部缺陷的正确路径，导致推理token浪费、效率低下。
### 方法关键点
- 两阶段设计全程保留GRPO更新逻辑，仅通过奖励稠密化优化效果，无需修改策略更新模块
- 第一阶段Adaptive Scaffolded RL：离线生成答案隐藏的子问题链，在线按当前模型任务解决率自动路由，难任务走脚手架路径，给连续正确的子前缀发部分奖励，补全成功前的奖励信号
- 第二阶段Quality-Aware Process RL：仅对最终答案正确的轨迹触发过程奖励，用固定LLM裁判将步骤分为5类，组合有用步占比、低价值步惩罚、对数长度惩罚生成奖励，优化成功后路径的质量与效率
### 关键结果
在Qwen3-8B-Instruct上训练，对比仅用最终奖励的GRPO基线：DAPO-Math数据集平均准确率提升10.55pp，推理token减少16.2%；Big-Math数据集平均准确率提升11.21pp，推理token减少27.1%；收益在GSPO优化器、Qwen3-0.6B小模型上均成立。

**最值得记住的一句话**：对带稀疏可验证奖励的RL任务，针对成功前后两个阶段分别做奖励稠密化，是比优化策略更新逻辑更通用的效果与效率提升路径。
