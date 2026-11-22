---
title: Differentially Private Score Estimation with Applications to Score-Based Generative
  Models
title_zh: 差分隐私得分估计及其在基于得分的生成模型中的应用
authors:
- Mengxiao Gao
- Elly K. H. Hung
- Yuchen Wu
- Yi Yu
arxiv_id: '2611.25536'
url: https://arxiv.org/abs/2611.25536
pdf_url: https://arxiv.org/pdf/2611.25536
published: '2026-11-19'
collected: '2026-11-22'
category: Training
direction: 差分隐私 · 生成模型训练优化
tags:
- Differential Privacy
- Score-based Generative Model
- Diffusion Model
- Langevin Monte Carlo
- Minimax Bound
one_liner: 提出满足(α,β)-差分隐私的得分估计器，构建隐私与去噪步数无关的差分隐私扩散模型
practical_value: '- 做用户敏感行为数据驱动的生成式推荐、个性化文案生成时，可复用该差分隐私得分估计框架规避数据泄露风险

  - 落地隐私合规的扩散模型生成业务（如虚拟商品、个性化素材生成）时，可采用隐私保证与去噪步数无关的设计，无需为多步去噪额外叠加隐私预算

  - 隐私计算场景下的用户分布建模任务，可参考B样条+指数机制的估计器实现，平衡隐私约束与模型精度'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
基于得分的生成模型（如扩散模型）训练时易记忆训练样本，存在成员推理、数据提取等隐私泄露风险，现有隐私得分估计的统计边界尚不清晰。
### 方法关键点
针对带局部γ-Hölder连续得分的d维次高斯分布，基于二次B样条+指数机制构建采样型隐私得分估计器，通过投影Langevin Monte Carlo实现，运行时为样本量n的多项式级。
### 关键结果数字
1. 估计器满足(α,β)-差分隐私，期望密度加权平方误差为`polylog(n) max(n^{-2γ/(d+2γ+2)}, (nα)^{-2γ/(d+γ+1)})`，与推导的极小极大下界几乎匹配，明确了隐私-精度权衡关系；
2. 基于该估计器构建的差分隐私扩散模型，隐私保证与去噪步数无关，在所有隐私分布估计器中达到近似极小极大最优的期望总变差误差，实验验证了理论结论。
