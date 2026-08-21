---
title: End-to-end Early Classification of Time Series in Non-Stationary Environments
title_zh: 非平稳环境下的时间序列端到端早分类方法研究
authors:
- Aurélien Renault
- Alexis Bondu
- Antoine Cornuéjols
- Vincent Lemaire
affiliations:
- Orange Research
- AgroParisTech
- AgroParisTech UMR MIA-Paris
arxiv_id: '2608.20044'
url: https://arxiv.org/abs/2608.20044
pdf_url: https://arxiv.org/pdf/2608.20044
published: '2026-08-20'
collected: '2026-08-21'
category: Other
direction: 时序早分类 · 非平稳环境自适应
tags:
- Time Series
- Reinforcement Learning
- Online Learning
- Early Classification
- Drift Adaptation
one_liner: 提出基于强化学习的统一架构DQeND，联合优化三类任务，显著提升非平稳时序早分类的漂移鲁棒性
practical_value: '- 电商用户行为时序、广告转化时序的早预测场景（如用户流失预判、点击转化预判）可借鉴端到端联合优化思路，替代分类+触发分离的传统架构，提升漂移场景下的鲁棒性

  - 针对业务数据分布漂移的时序任务，可引入RL框架联合更新表示模块与决策模块，避免分离优化导致的适配性下降

  - 做时序在线学习任务时，可参考论文的漂移场景对比实验设计，验证不同方案的鲁棒性边界'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有时间序列早分类(ECTS)方法普遍假设数据平稳，采用分类、触发决策分离优化的设计，在数据分布漂移的非平稳场景下适配性极差，无法满足线上动态环境的早决策需求。
### 方法关键点
1. 首次系统对比了可控漂移场景下分离式与端到端两类ECTS方案的效果差异；
2. 基于强化学习提出统一架构DQeND，联合学习时序表示、分类决策、触发时机三个模块，可直接与SOTA分离式基线对齐对比。
### 关键结果
在各类分布漂移场景下，DQeND鲁棒性显著优于所有分离式基线；消融实验证明表示与决策模块的联合更新是效果提升的核心原因，端到端方案在动态环境适配性上较分离式有明确优势。
