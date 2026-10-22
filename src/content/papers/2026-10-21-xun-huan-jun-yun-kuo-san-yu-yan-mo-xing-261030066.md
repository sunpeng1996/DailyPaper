---
title: Looped Uniform Diffusion Language Models
title_zh: 循环均匀扩散语言模型
authors:
- Saiteja Utpala
- Chieh-Hsin Lai
- Yuki Mitsufuji
- Praneeth Vepakomma
affiliations:
- MBZUAI
- Sony Group Corporation
- MIT
arxiv_id: '2610.30066'
url: https://arxiv.org/abs/2610.30066
pdf_url: https://arxiv.org/pdf/2610.30066
published: '2026-10-21'
collected: '2026-10-22'
category: LLM
direction: 扩散大模型 · 训练推理效率优化
tags:
- UDLM
- Diffusion-LLM
- Looped-Transformer
- Training-Efficiency
- Inference-Optimization
one_liner: 通过循环复用Transformer中间层大幅提升均匀扩散语言模型的训练与推理效率
practical_value: '- 业务侧如果用扩散类大模型做生成式推荐文案、搜索query改写、push推送话术生成，可直接复用中间层循环架构，无需新增参数就能降低2-3倍训练成本

  - 推理端采用自适应循环策略，根据隐层状态变化阈值提前终止循环，可减少26%-35%的推理计算量，不降低生成质量，适配低延迟的在线推荐/搜索场景

  - 训练时优先选择FLOP-proportional循环采样策略，小循环次数采样更频繁，可在零样本下游任务上进一步减少12%的推理循环次数，平衡训练与推理成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
均匀扩散语言模型（UDLM）推理能力优于掩码扩散模型，但训练时需从无标记的噪声上下文去噪，FLOP消耗远高于同规模掩码扩散模型，训练效率低是落地的核心瓶颈；此前循环层复用仅在掩码扩散模型上验证有效，UDLM场景下的收益尚不明确。

### 方法关键点
- 复用UDLM的2块Transformer中间层做循环计算，不新增参数，不改变原有训练目标与采样器逻辑
- 设计三种循环次数采样策略：均匀采样、FLOP-proportional采样（小循环次数采样频率更高，平衡各循环次数的训练FLOP占比）、噪声-proportional采样（高噪声输入匹配更大循环次数）
- 推理支持自适应循环：当连续两次循环的隐层状态相对变化低于阈值时停止，最高循环次数限制为12

### 关键实验
在OpenWebText、FineWeb-Edu数据集上与无循环UDLM baseline对比，核心结果：
1. 训练侧：达到baseline相同验证NLL，最多节省2.8×（OpenWebText）、3.3×（FineWeb-Edu）训练FLOP
2. 推理侧：相同NFE下，生成困惑度比baseline低9.8%，7个域外数据集零样本困惑度平均低11.5%
3. 自适应循环：零样本多选任务上匹配12次固定循环的精度，最多减少34.8%循环次数；FLOP-proportional采样训练的模型比均匀采样再少12%循环次数

### 核心结论
循环复用Transformer中间层是无参提升扩散语言模型训练推理效率的高性价比方案，匹配业务场景选择循环次数采样策略可进一步放大成本收益。
