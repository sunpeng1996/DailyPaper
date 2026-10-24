---
title: 'Beyond Best-of-$k$: Prior-Consistent DAPS for Ambiguous Nonlinear Inverse
  Problems'
title_zh: 超越k选最优：面向歧义非线性逆问题的先验一致DAPS方法
authors:
- Merve Kocabas
- Benjamin A. Burns
- Andreas Geiger
- Kent Gauen
- Sara Fridovich-Keil
affiliations:
- University of Tübingen
- Max Planck Institute for Intelligent Systems
- Georgia Institute of Technology
- Tübingen AI Center
- ELLIS Institute
arxiv_id: '2610.31592'
url: https://arxiv.org/abs/2610.31592
pdf_url: https://arxiv.org/pdf/2610.31592
published: '2026-10-22'
collected: '2026-10-24'
category: Other
direction: 扩散模型逆问题求解 · 采样优化
tags:
- Diffusion Model
- Inverse Problem
- Posterior Sampling
- Prior Consistency
- Sampling Optimization
one_liner: 提出无需真值的先验一致PC-DAPS采样方法，单轮维护多候选解决非线性逆问题采样偏差
practical_value: '- 生成式推荐/商品文案/AIGC图采样可借鉴单轮多候选剪枝思路，替代多次采样选最优的方案，降低推理算力成本

  - 模糊Query理解/多模态歧义生成场景，可复用无需真值的先验一致性评估逻辑，筛选符合用户分布的输出结果

  - 扩散模型采样优化可参考退火过程动态剪枝弱候选的trick，在保留输出多样性的前提下提升结果符合度'
score: 5
source: arxiv-cs.LG
depth: abstract
---

### 动机
扩散模型是逆问题求解的强先验，但歧义非线性逆问题场景下，现有采样器的局部近似易生成符合测量规则但不符合真实先验分布的结果，现有评估依赖k次采样选最优（需真值）的逻辑掩盖了该缺陷。
### 方法关键点
提出先验一致DAPS（PC-DAPS），单轮采样过程中维护多个候选解，在退火噪声下降阶段无需访问真值，仅依据候选与预学习先验的一致性对弱候选进行剪枝、替换。
### 关键结果
非线性逆问题场景下先验不一致样本的出现概率显著降低，样本质量明显提升；同时线性逆问题场景下可保持原有采样的样本质量与多样性，无性能损失。
