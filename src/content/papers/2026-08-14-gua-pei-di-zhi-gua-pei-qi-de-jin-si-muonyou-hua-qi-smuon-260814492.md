---
title: Approximate Muon with low-rank adapters
title_zh: 适配低秩适配器的近似Muon优化器sMuon
authors:
- Ben Anson
- Conor Houghton
- Edward Milsom
affiliations:
- University of Bristol
- University of Bath
arxiv_id: '2608.14492'
url: https://arxiv.org/abs/2608.14492
pdf_url: https://arxiv.org/pdf/2608.14492
published: '2026-08-14'
collected: '2026-08-17'
category: Training
direction: 低秩适配 · 训练优化器
tags:
- LoRA
- Muon
- Optimizer
- PEFT
- SFT
- ReLoRA
one_liner: 提出纯矩阵乘法实现的sMuon优化器，高效适配LoRA低秩微调与预训练场景
practical_value: '- 业务中做LLM的LoRA微调（比如Agent工具调用微调、电商文案生成模型SFT）时，可直接替换AdamW为sMuon，几乎无额外训练开销即可获得稳定效果提升，适配Muon预训练基座时提升更明显

  - sMuon的纯矩阵乘法实现兼容现有GPU加速框架，无需引入SVD/QR等复杂算子，可直接接入现有LoRA训练流水线，无需修改底层算子

  - 做垂域大模型ReLoRA低秩预训练（比如电商垂域大模型轻量化预训练）时，优先选用sMuon替代AdamW，可在不增加训练耗时的前提下降低约4.4%的验证损失'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
Muon优化器在LLM预训练阶段效果显著优于AdamW，但无法直接适配主流PEFT方案LoRA：LoRA的低秩参数化结构无法满足Muon对权重更新做正交化的数学要求，现有适配方案要么忽略层全局几何导致效果不佳，要么引入SVD等复杂算子带来极大训练开销，亟需兼顾效果与效率的LoRA+Muon方案。

### 方法关键点
- 对低秩场景下的Muon目标做线性化近似，忽略二阶小项，通过最小二乘将正交化后的全层梯度投影到LoRA可表达的低秩子空间，保证权重更新的谱分布尽可能均匀
- 设计纯矩阵乘法的高效实现，替代Riemannion等方案依赖的SVD分解，所有算子均适配现有GPU硬件加速，内存占用低于AdamW
- 引入拆分权重衰减与动量投影机制，保证LoRA参数化（B,A）等价变换时的优化一致性，避免优化方向受参数化方式影响

### 关键实验
对比AdamW、per-factor Muon、LoRA-Muon、Riemannion四个baseline，覆盖4个基座（3个AdamW预训练、1个Muon预训练Moonlight-16B）、11个常识与代码SFT benchmark，以及ReLoRA预训练场景：在Muon预训练的Moonlight-16B基座上，sMuon在11个任务中6个取得最优效果；ReLoRA预训练场景下，sMuon验证损失低至3.66，与最优baseline Riemannion持平，但训练速度比Riemannion快30%，仅比AdamW慢不到1%；LoRA rank=64时，Riemannion单步开销占总训练步的33%，sMuon仅占0.8%。

**最值得记住的一句话**：针对Muon预训练基座做LoRA微调时，用sMuon替代AdamW是几乎无成本的效果提升手段。
