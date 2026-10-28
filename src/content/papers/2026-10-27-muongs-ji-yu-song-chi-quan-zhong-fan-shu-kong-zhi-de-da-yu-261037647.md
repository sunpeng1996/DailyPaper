---
title: 'MuonGS: Pretraining LLMs with Relaxed Weight-Norm Control'
title_zh: MuonGS：基于松弛权重范数控制的大语言模型预训练优化器
authors:
- Athanasios Glentis
- Dawei Li
- Mingyi Hong
affiliations:
- University of Minnesota
arxiv_id: '2610.37647'
url: https://arxiv.org/abs/2610.37647
pdf_url: https://arxiv.org/pdf/2610.37647
published: '2026-10-27'
collected: '2026-10-28'
category: Training
direction: LLM预训练优化 · 权重范数控制
tags:
- Muon
- Optimizer
- LLM Pretraining
- Weight Norm Control
- MoE
one_liner: 提出通过Gram-Schmidt投影移除更新径向分量的MuonGS优化器，LLM预训练比MuonH最高获15%token等效加速
practical_value: '- 训练业务侧中小规模LLM（如生成式推荐的Item理解模型、Agent工具调用微调底座）时，可直接替换现有MuonH优化器，无需调weight
  decay，长训练周期下最多省15%token训练成本

  - 训练MoE结构的推荐/广告大模型时，MuonGS可直接复用，能获得比MuonH更低的验证困惑度，提升训练效率

  - 优化器迭代可参考核心trick：通过移除更新的径向分量控制权重范数增长速度，平衡探索能力与训练稳定性，调参成本远低于固定范数约束/weight decay方案'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前LLM预训练中，权重衰减、显式范数约束等范数控制手段已被证明能提升优化器效果，但学界缺乏统一理论解释其作用机制；现有约束方案（如MuonH的固定范数）限制了参数探索空间，vanilla Muon又存在权重范数增长过快、有效学习率累积过慢（仅对数级）的问题，长期训练效率低，亟需更宽松的范数控制方案平衡探索能力与训练稳定性。
### 方法关键点
- 提出**累积有效学习率$C_T$**作为全训练轨迹的探索能力度量，证明$C_T$的持续增长是训练后期持续优化的必要条件：现有MuonW/固定范数约束可实现$C_T$线性增长，vanilla Muon仅对数级增长
- 设计MuonGS优化器：对Muon的更新方向做Gram-Schmidt投影，移除沿当前权重的径向分量，仅保留切向更新，消除权重范数的一阶增长，仅保留二阶增长
- 理论证明MuonGS的权重范数最多随步数$√t$增长，$C_T$可实现$Ω(√T)$级增长，训练后期窗口的累积量仍能持续提升，优于vanilla Muon
### 关键实验
在FineWeb/Ultra-FineWeb数据集上，对比基线为MuonH、MuonW、vanilla Muon：
1. 160M/400M dense模型长训练周期（8倍Chinchilla token量）下，比MuonH最高获得15%的token等效加速
2. 135M激活/1B总参数MoE模型在10.8B/21.6B token训练量下，验证困惑度均低于MuonH

最值得记住的结论：权重范数控制不需要严格限制范数上限，只要控制范数增长速度足够慢，就能在保障探索能力的同时提升长期训练效率。
