---
title: Stochastic Linear Bandits with Partially Observed Actions
title_zh: 面向部分观测动作场景的随机线性老虎机算法研究
authors:
- Gautam Dasarathy
- Vineet Gattani
- Lalit Jain
affiliations:
- Arizona State University
- GE Vernova
- Google
arxiv_id: '2607.08971'
url: https://arxiv.org/abs/2607.08971
pdf_url: https://arxiv.org/pdf/2607.08971
published: '2026-07-09'
collected: '2026-07-13'
category: RecSys
direction: 线性老虎机 · 部分观测低秩结构优化
tags:
- Linear Bandit
- Partial Observation
- Low Rank
- Online Learning
- Regret Bound
one_liner: 提出TOFU-POV算法，借助低秩结构突破部分观测线性老虎机的次线性regret理论瓶颈
practical_value: '- 电商推荐/广告在线冷启动场景中，若商品/用户特征因隐私合规、存储限制存在部分缺失，可复用「低秩子空间估计+epoch冻结表征+特征补全」框架，替代现有零填充特征的老虎机策略，降低探索regret

  - 工程实现可直接复用逆概率加权修正协方差估计方法，对缺失特征的协方差矩阵做无偏估计，无需额外标注数据，适配线上流式特征更新场景

  - 无法预先获知特征隐空间维度时，可采用秩自适应变种RA-TOFU-POV，通过特征值阈值自动选择隐空间维度，无需人工调参，适配不同品类的商品特征分布'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
随机线性老虎机（SLB）是推荐、广告在线探索的核心框架，但实际场景中受隐私、存储、计算约束，动作（商品/广告）的特征向量往往只能观测到随机子集，无额外结构时次线性regret理论上不可实现；而真实场景中动作特征普遍存在低秩结构，可借此突破观测限制。

### 方法关键点
- TOFU-POV为epoch式算法：先通过burn-in阶段积累数据，用逆概率加权修正的协方差估计器从掩码动作中估计低秩隐子空间，每个epoch冻结子空间表征，对当前动作做补全后在低维空间运行OFUL。
- 理论证明regret仅和隐子空间维度m相关，而非原始特征维度d，随T呈√T增长，同时量化了缺失率p、决策集大小K、子空间条件数κ对regret的影响。
- 提供秩自适应变种，无需预先知道隐空间维度m，通过特征值阈值自动选择维度，regret缩放和已知m的版本一致。

### 关键结果数字
合成数据（d=30，m=3，K=8，T=400）和MNIST真实特征实验中，对比零填充OFUL、零填充PSLB等基线，当缺失率p=0.2时，TOFU-POV的最终累计regret比基线低60%以上，缺失越严重收益越大。

### 核心结论
动作特征存在低秩结构时，仅观测部分特征也可通过子空间估计+补全实现次线性regret，无需获取完整特征。
