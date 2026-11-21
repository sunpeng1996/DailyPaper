---
title: 'Flow Matching from Non-Gaussian Sources: A Theory of Efficient Sampling'
title_zh: 非高斯源的流匹配：高效采样理论
authors:
- Yuchen Zhou
- Lili Zheng
- Yuxin Chen
- Gen Li
arxiv_id: '2611.26407'
url: https://arxiv.org/abs/2611.26407
pdf_url: https://arxiv.org/pdf/2611.26407
published: '2026-11-19'
collected: '2026-11-21'
category: Other
direction: 生成模型 · 流匹配高效采样理论
tags:
- Flow Matching
- Non-Gaussian Distribution
- Euler Discretization
- Nonasymptotic Convergence
- Sampling Efficiency
one_liner: 建立非高斯源线性插值流匹配欧拉离散的非渐近收敛理论，给出有限步采样复杂度上界
practical_value: '- 生成式推荐场景用流匹配做item/用户表征生成时，可尝试非高斯源（如混合高斯、t分布）替代高斯源，降低采样步数

  - 工程侧可参考给出的复杂度上界公式，根据允许的生成误差ε估算最小采样步数，优化流匹配推理延迟

  - 若生成目标分布无光滑密度/无界支持，优先选择满足论文假设的非高斯源训练流匹配，保障生成稳定性'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有流匹配生成框架支持灵活选择重尾、多模态等非高斯源分布，但缺乏非高斯源下有限步采样的收敛性理论保障，限制了非高斯源的落地应用。
### 方法关键点
针对线性插值流匹配的欧拉离散化过程，提出非渐近收敛分析框架，仅要求源分布满足处处正的连续可微密度、有限总方差$	extsf{TotVar}_	extsf{base}$、L-Lipschitz得分，目标分布满足温和二阶矩条件。
### 关键结果
满足假设条件下，采样总变差误差不超过ε所需的迭代次数仅为$	ilde{O}(Ld	extsf{TotVar}_	extsf{base}/	extsf{ε})$；覆盖的源分布包括自由度>2的多元t分布、共享协方差的有限高斯混合，同时支持无光滑密度、无界支持的目标分布。
