---
title: 'Accelerating A/B-Tests with Counterfactual Estimation: Reducing Variance through
  Policy Overlap'
title_zh: 利用反事实估计与策略重叠降低方差 加速A/B测试
authors:
- Olivier Jeunen
affiliations:
- Independent Researcher, Belgium
- aampe
arxiv_id: '2607.14604'
url: https://arxiv.org/abs/2607.14604
pdf_url: https://arxiv.org/pdf/2607.14604
published: '2026-07-16'
collected: '2026-07-17'
category: Eval
direction: A/B测试 · 反事实估计 方差优化
tags:
- A-B Testing
- Off-Policy Evaluation
- Variance Reduction
- Counterfactual Inference
- Recommender System
one_liner: 通过利用策略重叠的Δ-OPE框架，无偏降低A/B测试方差，大幅缩短实验所需流量与周期
practical_value: "- 现有A/B测试流程可直接复用该方法：针对推荐/搜索策略增量更新场景（策略重叠度高），将原DiM估计器替换为Δ-IPS/Δ-DR估计器，无需调整流量分配即可降低方差、缩短实验周期\n\
  - 实验流量分配无需强制50/50：可基于新旧策略重叠度预计算最优分配比\textit{p}^★，例如给高探索性新策略多分流量，实测比均分降低18%方差\n-\
  \ 优化CUPED/CUPAC类控制变量模型：将MSE损失替换为Δ-MRDR加权损失，让模型聚焦新旧策略决策不一致的样本，比普通DR进一步降低8%左右方差\n\
  - 推荐/搜索排序场景可直接复用Δβ★-DCG估计器：结合位置偏置建模，全策略重叠区间都比普通DCG差值法方差更低，尤其适合小流量、小效应的实验场景"
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
线上A/B测试是电商/推荐/搜索策略迭代的黄金标准，但用户行为指标（CTR、GMV等）噪声大、方差高，小幅度的增量策略迭代往往需要极长实验周期或大流量占比，机会成本极高。现有方差降低方法（如CUPED）未利用新旧策略的结构重叠信息，大量两边决策一致的样本仅贡献噪声不提供ATE估计信号，严重浪费统计效力。

### 方法关键点
- 将A/B测试的流量分配机制重构为元策略，直接复用Δ-OPE（成对策略离策略评估）框架，得到无偏ATE估计器，方差由策略间divergence而非原始指标方差决定
- 理论证明只要新旧策略存在重叠，该估计器严格优于传统DiM估计器，同时给出方差最小的最优流量分配比	extit{p}^★的计算方法，无需强制50/50流量分配
- 提出Δ-MRDR损失，训练回归控制变量时给策略决策差异大的样本更高权重，聚焦对ATE估计最重要的区域，进一步降低方差
- 扩展到排序场景，提出	extit{Δβ}^★-DCG估计器，结合位置偏置建模与位置级最优基线，适配推荐/搜索的Top-K排序实验

### 关键结果
基于可控模拟环境（可获取真实ATE）验证，对比基线为传统DiM、普通DR估计器：高策略重叠场景下Δ-IPS方差趋近于0，远优于DiM，且在5000维大动作空间下稳定；新旧策略不对称场景下，最优分配比	extit{p}^★≈0.81，比50/50分配降低18%方差；Δ-MRDR比普通Δ-DR再降8%方差，比原始Δ-IPS降75%方差；排序场景下	extit{Δβ}^★-DCG在全策略重叠区间均优于传统DiM。

### 核心结论
A/B测试中，新旧策略决策一致的样本几乎不提供ATE估计的有效信号，利用这一点降方差的边际成本极低、收益极高
