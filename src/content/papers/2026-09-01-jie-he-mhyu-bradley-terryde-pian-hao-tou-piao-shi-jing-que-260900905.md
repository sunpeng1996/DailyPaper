---
title: 'When Metropolis and Hastings Meet Bradley and Terry: Exact MCMC From Preference
  Voting'
title_zh: 结合MH与Bradley-Terry的偏好投票式精确MCMC采样方法
authors:
- Ariel Smogorghevski
- Nir Rosenfeld
- Yaniv Romano
affiliations:
- Technion – Israel Institute of Technology
arxiv_id: '2609.00905'
url: https://arxiv.org/abs/2609.00905
pdf_url: https://arxiv.org/pdf/2609.00905
published: '2026-09-01'
collected: '2026-09-04'
category: Other
direction: 条件生成 · 偏好驱动采样
tags:
- MCMC
- Metropolis-Hastings
- Bradley-Terry
- Preference Sampling
- Conditional Generation
- LLM Judge
one_liner: 提出仅依赖二元成对偏好反馈的Pref-MH采样器，无需精确密度评估即可实现条件分布采样
practical_value: '- 推荐冷启动/小样本场景可复用Pref-MH的成对偏好采样逻辑，无需精确计算用户偏好密度，仅通过LLM Judge/少量用户pairwise反馈即可生成符合需求的推荐候选集

  - 生成式推荐候选优化环节可将Pref-MH作为轻量采样模块替代传统重排序，在控制预算前提下实现Peskun-Tierney最优的候选多样性和相关性平衡

  - Agent生成内容/服务适配场景可基于该方法仅用二元偏好反馈调整生成分布，无需额外标注训练数据，降低业务落地标注成本'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
Metropolis-Hastings（MH）是经典条件采样框架，但依赖逐点目标密度的精确评估，生成式场景下该密度通常无法获取；而人类/模型Judge的二元成对偏好反馈获取成本低，缺乏适配的精确采样方案。

### 方法关键点
1. 提出Pref-MH通用精确采样器，核心发现MH未归一化密度比与Bradley-Terry（BT）选择模型的偏好几率完全匹配，可直接用成对偏好反馈替代密度计算
2. 设计适配二元采样反馈的接受/拒绝规则，可证明马尔可夫链收敛到目标分布
3. 固定proposal核与采样预算时，Pref-MH是同类精确可逆接受规则中Peskun-Tierney最优的

### 关键结果
在LLM Judge支撑的文本生成、分子设计，VLM Judge支撑的图像生成任务上均验证有效，在成对反馈易获取的场景下兼具实用性与灵活性
