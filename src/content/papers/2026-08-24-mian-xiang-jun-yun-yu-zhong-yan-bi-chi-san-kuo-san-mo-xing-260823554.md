---
title: Provably adaptive sampling with uniform and remasking discrete diffusion models
title_zh: 面向均匀与重掩蔽离散扩散模型的可证明自适应采样方法
authors:
- Daniil Dmitriev
- Zhihan Huang
- Yuting Wei
arxiv_id: '2608.23554'
url: https://arxiv.org/abs/2608.23554
pdf_url: https://arxiv.org/pdf/2608.23554
published: '2026-08-24'
collected: '2026-08-25'
category: Other
direction: 离散扩散模型 · 高效采样理论优化
tags:
- Discrete Diffusion
- Adaptive Sampling
- Sampling Complexity
- Dual Total Correlation
- Remasking
one_liner: 提出基于留一去噪器的一阶采样器，证明其采样复杂度由目标分布DTC而非环境维度决定
practical_value: '- 若业务中采用离散扩散实现生成式推荐/文案生成，可参考采样复杂度与目标分布DTC挂钩的结论，调整采样步数平衡质量与延迟

  - 留一去噪器的并行坐标更新设计可复用至多token并行生成场景，降低大维度离散生成任务的采样耗时'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
离散扩散模型支持并行生成，相比自回归方案更具效率优势，但现有均匀前向过程的标准τ-leaping采样器复杂度下界随环境维度d线性增长，需确认该维度依赖是否为前向过程的固有属性。
### 方法关键点
1. 提出基于留一去噪器的一阶采样器，支持均匀、重掩蔽过程的坐标并行更新，可在采样过程中修正去噪错误
2. 设计贝叶斯最优辅助采样器分离离散化误差与分数估计误差，基于互信息给出通用前向过程离散化误差的信息论表示
### 关键结果
忽略对数因子时，仅需$O(\mathrm{DTC}(X_0)/\varepsilon)$步离散化即可达到$O(\varepsilon_{\mathrm{score}}+\varepsilon)$的采样误差，复杂度由目标分布的对偶总相关DTC而非环境维度d决定，合成数据实验验证了其维度自适应特性。
