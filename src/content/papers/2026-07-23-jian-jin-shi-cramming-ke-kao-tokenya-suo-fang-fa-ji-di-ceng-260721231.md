---
title: 'Progressive Cramming: Reliable Token Compression and What It Reveals'
title_zh: 渐进式Cramming：可靠Token压缩方法及底层机制揭示
authors:
- Dmitrii Tarasov
- Timofei Lashukov
- Elizaveta Goncharova
- Andrey Kuznetsov
affiliations:
- FusionBrain Lab
- HSE University
- Innopolis University
arxiv_id: '2607.21231'
url: https://arxiv.org/abs/2607.21231
pdf_url: https://arxiv.org/pdf/2607.21231
published: '2026-07-23'
collected: '2026-07-24'
category: LLM
direction: LLM Token压缩 机制分析
tags:
- Token Compression
- Progressive Cramming
- LLM Mechanism
- Attention Sink
- Context Compression
one_liner: 提出逐token扩展的渐进式token压缩方法，量化压缩边界并揭示其能力损失的底层机制
practical_value: '- 做RAG/长上下文Agent的上下文压缩时，不能仅以token重建准确率为指标，必须同步验证下游任务效果，完美重建也可能导致语义能力完全崩溃

  - 优化单embedding压缩方案时，可引入低维投影约束（如256维仿射子空间），既能提升压缩容量和信息增益，还能降低优化复杂度

  - 做KV cache/长文本生成压缩优化时，可参考渐进式逐段验证的思路，避免早期token错误引发的自回归生成完全失效'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
原有token cramming方法采用固定token预算和99%重建阈值，残留1%错误几乎全部集中在序列首2个token，导致自回归生成完全失效，同时学界无法明确压缩embedding是编码了可迁移语义，还是仅通过 brittle steering 实现重建，也无法精准量化压缩的真实边界。

### 方法关键点
- 逐token扩展目标前缀，每一步从之前的最优embedding热启动优化，直到无法在预设优化预算内实现100%重建，精准定位压缩成功/失败的边界
- 引入低维投影约束，将压缩embedding限制在低维仿射子空间，仅优化低维系数+投影矩阵，大幅稳定优化过程
- 设计注意力敲除（attention knockout）因果干预方法，定位压缩导致下游能力损失的具体层来源

### 关键结果
在PG19、Fanfics数据集上对比原始full cramming基线：
1. Llama3.1-8B上渐进式cramming实现1438±380个token的100%自回归重建准确率，而full cramming虽能压缩1568个token，自回归准确率仅40.44±48.63%
2. 压缩embedding的优化轨迹仅需30-100个PCA分量即可解释99%方差，远低于2048-4096的原始embedding维度
3. 前置压缩embedding会导致HellaSwag、ARC-Easy准确率下降15-20个百分点，生成任务上能力几乎完全崩溃，因果分析证明损失来自模型早期层交互，而非后期的注意力汇聚

### 核心结论
完美的token重建率不等于语义保留，基于重建目标优化的压缩embedding本质依赖脆弱的模型转向实现，无法支撑下游任务的语义使用
