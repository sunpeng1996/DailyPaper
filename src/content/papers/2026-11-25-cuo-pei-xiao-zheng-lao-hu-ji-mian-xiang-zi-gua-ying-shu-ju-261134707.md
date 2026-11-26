---
title: 'When the Proxy Is Wrong: Mismatch-Corrected Bandits for Adaptive Data Sampling'
title_zh: 错配校正老虎机：面向自适应数据采样的代理模型偏差修正方法
authors:
- Amine Saadi
- Elissa Mhanna
- Raphaël Féraud
- Gwénolé Lecorvé
affiliations:
- Orange Research, France
- École Polytechnique, Institut Polytechnique de Paris, France
arxiv_id: '2611.34707'
url: https://arxiv.org/abs/2611.34707
pdf_url: https://arxiv.org/pdf/2611.34707
published: '2026-11-25'
collected: '2026-11-26'
category: Training
direction: 大模型训练优化 · 自适应数据采样
tags:
- Bandit Algorithm
- Adaptive Data Sampling
- Proxy Model
- Multi-fidelity Learning
- Training Optimization
one_liner: 用多保真度老虎机建模代理-目标模型偏差，低审计成本提升大模型训练数据分配效果
practical_value: '- 训练大尺寸推荐/广告排序/领域LLM时，可先用小代理模型预选高价值训练数据，叠加少量审计步骤校正偏差，在不损失效果的前提下大幅降低训练成本

  - 冷启动数据采样场景可复用错配校正老虎机框架，无需假设代理与目标模型排序一致性，适配异构数据源的价值评估需求

  - 动态分布偏移场景（如电商大促、社会热点事件期）采用滑动窗口均匀分配审计预算，避免前期耗尽预算导致的线性后悔，提升模型在分布变化下的鲁棒性'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
大模型训练通常依赖小代理模型筛选训练数据，两者对数据价值的排序偏差会导致训练效果次优，全量用目标模型评估数据的成本过高不可行。
### 方法关键点
1. 将数据分配问题建模为多保真度老虎机任务，每轮可观测低成本的代理奖励，仅对不确定性高的决策做少量审计获取目标奖励，通过配对残差校正代理偏差，无需假设代理与目标排序一致或偏移量固定。
2. 静态场景下证明仅用代理的策略会产生线性后悔，明确最低配对审计量要求；动态分布偏移场景下提出滑动窗口均匀分配审计预算策略，后悔上界为$\sqrt{Γ_T T\log T}​$。
### 关键结果
CivilComments-WILDS数据集上用BERT-Small引导BERT-Large训练，相同审计预算下均匀分配审计策略将最差组准确率提升6.3~10.5pp；相同目标模型预算下错配校正策略优于仅用目标模型的基线。
