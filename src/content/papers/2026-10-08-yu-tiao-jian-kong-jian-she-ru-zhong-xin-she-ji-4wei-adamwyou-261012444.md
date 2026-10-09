---
title: 'Rounding in Preconditioner Space: Redesigning 4-bit AdamW Optimizer-State
  Quantization'
title_zh: 预条件空间舍入：重新设计4位AdamW优化器状态量化方法
authors:
- Hanyang Li
- Shao Tang
- Daniel Thomas Braithwaite
- Gregory Dexter
- Leonardo Neves
- Aman Gupta
- Hiroto Udagawa
- Abhishek Shivanna
- Daniel Silva
- Rohan Ramanath
affiliations:
- University of California, Berkeley
- Nubank
arxiv_id: '2610.12444'
url: https://arxiv.org/abs/2610.12444
pdf_url: https://arxiv.org/pdf/2610.12444
published: '2026-10-08'
collected: '2026-10-09'
category: Training
direction: 大模型训练 · 4位AdamW量化
tags:
- AdamW
- 4-bit Quantization
- LLM Training
- Stochastic Rounding
- NF4
one_liner: 从预条件空间视角提出两种4位AdamW量化方案，相比TorchAO损失差距最高降70%
practical_value: '- 训练侧直接复用官方开源实现：电商/推荐场景下的大模型SFT（如个性化文案生成、Agent领域微调、推荐大模型训练）可直接使用该4位AdamW方案，优化器显存开销从8字节/参降至1.06字节/参，压缩比达7.53倍，不降低训练效果的前提下大幅降本

  - 量化设计思路迁移：做业务侧模型压缩（如Embedding量化、排序模型低比特部署）时，不能仅追求数值重建误差最小，要结合量化后的值对下游任务/更新的实际影响调整量化策略，避免表面误差低但业务效果掉点

  - 敏感层差异化量化trick：可参考仅LM头最后10%训练用随机舍入的设计，对推荐系统的用户/物品Embedding层、排序头、多任务头这些对误差敏感的层单独设计量化/舍入规则，不用全局统一配置，兼顾压缩比和效果'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
大模型训练中AdamW的FP32一阶、二阶矩缓存占8字节/参数，显存开销极高；现有4位优化器量化方案要么存在零点故障（小的二阶矩被量化为0导致更新步长过大），要么排除零点引入正下界抑制预条件，且传统状态空间舍入的量化误差会在迭代中累积，导致训练损失远高于32位AdamW。

### 方法关键点
1. 两种二阶矩量化路线：ZIP-SR采用含零点的二阶矩码本，在预条件空间计算随机舍入概率，将零点选中概率降至O(ε)从根本上避免零点故障；ZE-EDEN采用不含零点的二阶矩码本，新增EDEN块校准抵消正下界带来的预条件畸变。
2. 一阶矩统一采用NF4码本，前90%训练步用就近舍入，仅最后10%训练步将LM头的一阶矩切换为随机舍入，避免后期径向偏差导致的损失飙升。
3. 整体存储开销与TorchAO 4位AdamW完全一致，无额外参数开销。

### 关键实验
对比基线为TorchAO 4位AdamW、32位AdamW，实验覆盖130M~2.7B参数的GPT/Llama系列预训练，以及3B/8B模型全参数SFT。所有模型尺寸下均缩小了与32位AdamW的验证损失差距，最大降幅达70%；SFT场景下下游任务得分与32位AdamW几乎无差异，优化器显存相比FP32版本降低87%。

### 核心结论
优化器状态量化的核心目标不是最小化状态空间的重建误差，而是最小化对后续优化更新的影响。
