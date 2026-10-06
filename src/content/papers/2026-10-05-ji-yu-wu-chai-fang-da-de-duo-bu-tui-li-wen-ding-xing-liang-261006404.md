---
title: Quantifying the Stability of Multi-Step Reasoning via Error Amplification
title_zh: 基于误差放大的多步推理稳定性量化研究
authors:
- Dongyue Li
- Ziniu Zhang
- Minxuan Duan
- Hongyang R. Zhang
affiliations:
- Northeastern University
arxiv_id: '2610.06404'
url: https://arxiv.org/abs/2610.06404
pdf_url: https://arxiv.org/pdf/2610.06404
published: '2026-10-05'
collected: '2026-10-06'
category: Reasoning
direction: 大模型多步推理稳定性优化
tags:
- Multi-step Reasoning
- Chain-of-Thought
- Jacobian Regularization
- Quantization-aware Training
- Length Generalization
one_liner: 提出基于输入Jacobian谱范数的多步推理稳定性量化方法，配套正则化策略提升长序列推理表现
practical_value: '- 做Agent多步工具调用、长链推理任务时，可引入Jacobian谱范数乘积作为推理稳定性量化指标，提前识别高风险长推理链路，避免错误累积导致最终结果失效

  - 对于依赖长CoT的生成式推荐（如用户购物路径规划、复杂需求商品组合推荐），可采用思考步骤压缩策略，在不损失关键信息的前提下采样核心推理步骤，降低误差放大概率同时提升推理速度

  - 业务场景微调LLM做推理类任务时，可加入低比特量化感知训练作为正则化手段，在压缩模型体积的同时抑制推理误差累积，尤其对长输入泛化场景提升明显'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
多步推理（如Chain-of-Thought）能显著提升LLM任务表现，但自回归生成过程中中间步骤的误差会随推理步数累积放大，导致长序列推理性能骤降，常规监督微调未对该问题做显式约束，且缺乏可量化的推理稳定性度量指标。

### 方法关键点
- 理论推导多步推理的误差上界由每一步输入空间Jacobian矩阵的谱范数乘积决定，将该乘积定义为误差放大因子，作为推理稳定性的量化指标
- 提出两种正则化策略降低误差放大因子：① CoT长度压缩，均匀采样核心推理步骤减少推理链路长度；② Quantization-aware Training，通过训练时权重量化约束Jacobian谱范数
- 结合上述两种策略实现Jacobian正则化训练，在微调阶段同时抑制误差累积

### 关键实验
在CLRS-Text的5个图算法推理任务、LEGO的2个符号状态跟踪任务上，对比SFT-CoT、Implicit CoT、Coconut等基线，平均测试精度提升3.5%，比训练序列长10%的长输入泛化场景下平均提升8.2%，误差放大因子较基线降低3-8×。

### 核心结论
多步推理的稳定性本质由每一步的输入敏感度决定，通过压缩推理长度+约束Jacobian范数可以低成本且有效地缓解长推理链的误差累积问题。
