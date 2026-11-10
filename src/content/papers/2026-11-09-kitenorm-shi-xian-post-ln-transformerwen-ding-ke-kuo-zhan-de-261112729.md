---
title: 'KiteNorm: Variance Regularisation for Stable and Scalable Post-LN Transformers'
title_zh: KiteNorm：实现Post-LN Transformer稳定可扩展训练的方差正则化方法
authors:
- Leon A. Trochelmann
- Sajad Movahedi
- Shiwei Liu
- Antonio Orvieto
affiliations:
- ELLIS Institute Tübingen
- MPI for Intelligent Systems
- Tübingen AI Center
arxiv_id: '2611.12729'
url: https://arxiv.org/abs/2611.12729
pdf_url: https://arxiv.org/pdf/2611.12729
published: '2026-11-09'
collected: '2026-11-10'
category: Training
direction: 大模型训练 · Transformer归一化优化
tags:
- Transformer
- LayerNorm
- Post-LN
- Training Stability
- Regularization
one_liner: 提出结合残差缩放、方差正则与标量双归一化的KiteNorm，大幅提升Post-LN Transformer训练稳定性与性能
practical_value: '- 业务中训练自定义LLM（如电商导购Agent、生成式推荐基座）时，可直接替换现有归一化方案为KiteNorm，无需改动其他架构即可提升训练稳定性，支持更大学习率，降低训练成本

  - 方差正则化trick可直接复用：复用LayerNorm计算过程中已输出的方差值，添加`ReLU(σ²-1)`正则项，几乎无额外计算开销，即可缓解训练后期梯度消失/发散问题

  - 标量化LayerNorm设计可借鉴：将LayerNorm原本维度级的γ/β参数替换为全局标量，减少参数开销的同时提升深层模型性能，尤其适配资源受限的端侧LLM场景

  - 若业务模型采用Post-LN结构且遇到深层训练不稳定问题，可直接使用残差缩放系数`1/(2L)`，无需额外调参即可缓解训练早期秩塌陷问题'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
Post-LN Transformer的参数效率优于当前主流的Pre-LN架构，但随深度增加易出现梯度消失、秩塌陷问题，无法稳定扩展到深层；现有Post-LN优化方案大多依赖初始化策略，大学习率下稳定性骤降，始终无法超过Pre-LN基线，亟需新的归一化方案打破这一困境。

### 方法关键点
- 残差缩放：固定残差分支缩放系数为`1/(2L)`，训练早期即可抑制隐状态方差膨胀和秩塌陷，与skip分支缩放数学等价且更适配后续正则逻辑
- 方差正则化：新增ReLU正则项，仅当隐状态方差超过1时才计入损失，正则项复用LayerNorm已计算的方差值，几乎无额外计算开销，防止训练中后期突发不稳定
- 标量双归一化：采用双LN结构分别处理skip和残差分支，将LN的γ/β从维度级向量改为全局标量，减少参数的同时给优化器更直接的分支尺度控制信号

### 关键实验
在SlimPajama、FineWeb数据集上训练decoder-only Transformer，最高参数量达1.3B，对比GPT-2 Pre-LN、KEEL、LNS等7种主流基线：48层模型下最优验证perplexity达19.08，比最优Pre-LN基线低0.75；1.3B Llama风格模型下最优学习率范围是Pre-LN的2倍，Pre-LN在5e-3学习率下发散而KiteNorm保持稳定；深度、宽度、训练预算、batch size四个维度的缩放定律均全面优于Pre-LN基线。

### 核心结论
Post-LN结构的参数效率优势完全可以通过方差约束释放，无需依赖复杂初始化优化，训练全程控制隐状态方差是提升深层Transformer稳定性的核心。
