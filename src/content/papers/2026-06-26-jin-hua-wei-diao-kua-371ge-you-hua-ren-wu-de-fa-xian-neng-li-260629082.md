---
title: 'Evolution Fine-Tuning: Learning to Discover Across 371 Optimization Tasks'
title_zh: 进化微调：跨371个优化任务的发现能力学习
authors:
- Young-Jun Lee
- Seungone Kim
- Minki Kang
- Alistair Cheong Liang Chuen
- Zerui Chen
- Seungho Han
- Taehee Jung
- Dongyeop Kang
affiliations:
- University of Minnesota
- Carnegie Mellon University
- KAIST
- University of Cambridge
- Amazon
arxiv_id: '2606.29082'
url: https://arxiv.org/abs/2606.29082
pdf_url: https://arxiv.org/pdf/2606.29082
published: '2026-06-26'
collected: '2026-07-01'
category: Training
direction: 大模型训练 · 进化微调范式
tags:
- Evolutionary Fine-Tuning
- Cross-Task Generalization
- Optimization Agent
- Supervised Fine-Tuning
- Preference Learning
one_liner: 提出进化微调EFT范式，基于156K跨域优化轨迹训练LLM，实现跨任务发现能力迁移
practical_value: '- 做业务优化类Agent（如广告出价策略、推荐召回规则迭代）时，可收集历史优化轨迹做EFT SFT，把优化经验内化到小模型，降低对大模型的依赖，提升跨任务优化效率

  - 轨迹过滤优先保留性能提升的正样本训练，再搭配KTO偏好学习区分优化方案好坏，该微调trick可直接复用到业务模型迭代流程

  - 小模型经过EFT预训练后再做test-time RL，效果优于直接用base模型做在线微调，可应用于推荐排序策略在线迭代、营销活动规则实时优化等场景

  - 跨多领域轨迹训练可带来迁移增益，构建业务优化数据集时可覆盖尽可能多的场景（如促销规则、选品策略、流量分配），提升模型通用优化能力'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM结合进化搜索的优化方案，要么依赖闭源大模型、优化能力完全依赖外部搜索框架，要么test-time微调仅适配单任务，优化经验无法跨任务复用，小开源模型在进化搜索中表现极差，缺乏让模型内化跨任务进化优化能力的通用训练范式。

### 方法关键点
- 提出Evolution Fine-Tuning（EFT）中间训练范式，将进化搜索的父代-子代改进轨迹转化为监督信号，让LLM学习可迁移的变异优化策略
- 构建Finch Collection数据集：覆盖10个领域371个优化任务，共156K条有效进化轨迹，过滤错误、无改进的负向轨迹后，仅用性能提升的正样本做SFT，还可搭配KTO偏好学习区分优化方案好坏，进一步提升能力
- 训练2B~9B参数的Finch系列模型，可同时适配test-time搜索（权重冻结）、test-time RL（在线微调）两类进化搜索框架

### 关键结果
- 22个未见测试任务上，Finch模型平均比同参数base模型高10.22%，9B版本提升达10.24%，4B Finch效果超过8B base模型
- 搭配test-time RL后，Finch在两个圆形填充任务上达到SOTA，在Erdős最小重叠问题上超过base模型3.2%，部分指标接近人类最优水平
- 训练任务数从15提升到355时，模型跨任务性能平均提升14.1%，呈现明确的scaling效应

### 核心结论
进化微调是将外部搜索框架的优化能力内化到模型参数的高效路径，小开源模型经过跨任务进化轨迹训练即可达到接近大模型的优化效果。
