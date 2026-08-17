---
title: 'Dion3: Full-Stack Orthogonal Updates'
title_zh: Dion3：面向Muon优化器的全栈正交更新加速方案
authors:
- Noah Amsel
- Jack Zhang
- Kwangjun Ahn
- Ali Naeimi
- Austin Feng
- Berlin Chen
- Tri Dao
- John Langford
affiliations:
- New York University
- Princeton University
- NVIDIA
- Yale University
- Microsoft Research
arxiv_id: '2608.11612'
url: https://arxiv.org/abs/2608.11612
pdf_url: https://arxiv.org/pdf/2608.11612
published: '2026-08-11'
collected: '2026-08-17'
category: Training
direction: 大模型训练 · 优化器加速
tags:
- Optimizer
- Muon
- LLM Training
- Distributed Training
- Kernel Optimization
one_liner: 从算法、内核、通信全栈优化Muon正交化开销，速度最高提升6倍且可直接替换
practical_value: '- 训练自研垂直域LLM/生成式推荐模型时，可直接替换现有Muon优化器为Dion3，最高降低6倍优化器步开销，且不损失甚至略提升模型效果

  - 做分布式训练性能优化时，可复用其megabatching通信策略，将同形状权重的通信合并为少量批次，通信绑定场景下最多降低35%步时

  - 涉及大矩阵正交化类运算的场景，可复用Gram Newton-Schulz+对称GEMM内核的优化思路，非对称矩阵下最高可节省68% FLOP

  - 训练资源紧张时，可调整Dion3的行采样比例f（推荐1/4或1/8），配合η=原学习率/√f的缩放规则，在不损失效果前提下进一步降低训练成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
Muon是当前前沿LLM（如Kimi K2、GLM-5）的首选训练优化器，相比AdamW收敛步数更少，但每步三次方时间复杂度的Newton-Schulz正交化步骤开销是AdamW的26倍，分布式场景下通信开销进一步放大，限制了其通用落地。

### 方法关键点
- 算法层：提出Gram Newton-Schulz正交化算法，迭代小尺寸对称Gram矩阵而非原始大矩阵，数学上与标准Newton-Schulz等价，结合重启策略解决半精度下的数值不稳定问题，非对称矩阵下最多省68% FLOP
- 内核层：基于CuteDSL实现对称GEMM内核，利用Gram矩阵对称性仅计算下三角再复制到上三角，相比cuBLAS最高有2倍速度提升
- 更新规则：按ℓ1范数采样部分动量矩阵行做正交化，配合误差反馈机制避免遗漏小梯度，仅修改优化轨迹不损失效果
- 通信层：提出megabatching策略，将同形状权重的分布式通信合并为单批次，通信轮次从O(N)降到O(1)

### 关键结果
- 7B参数LLM训练场景下，Dion3将Muon的优化器步开销从AdamW的26倍降到4倍，最高提速6倍
- 1B/3B/7B/14B参数模型训练中，采样比例f=1/4的Dion3相比NorMuon基线，验证损失最多降0.027，下游任务精度最高提升0.7个百分点
- 高宽比更大的MoE架构下，仅Gram Newton-Schulz+对称内核就可实现2倍正交化速度提升

最值得记住的一句话：Dion3是可直接落地的生产级Muon优化方案，全栈优化的单个模块也可拆分复用至其他需要正交化的训练场景。
