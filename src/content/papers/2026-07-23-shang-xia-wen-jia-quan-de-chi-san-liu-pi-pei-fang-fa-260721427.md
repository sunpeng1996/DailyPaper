---
title: Context-weighted Discrete Flow Matching
title_zh: 上下文加权的离散流匹配方法
authors:
- Daniil Cherniavskii
- Daniel Severo
- Karen Ullrich
affiliations:
- University of Amsterdam
- Meta FAIR
arxiv_id: '2607.21427'
url: https://arxiv.org/abs/2607.21427
pdf_url: https://arxiv.org/pdf/2607.21427
published: '2026-07-23'
collected: '2026-07-24'
category: Training
direction: 离散生成模型 · 训练与采样优化
tags:
- Discrete Flow Matching
- CTMC
- Cross-Entropy Loss
- Generative Modeling
- Sampling Optimization
one_liner: 针对离散流匹配训练目标偏差问题，引入上下文加权采样与损失，大幅降困惑度同时保留任意顺序生成能力
practical_value: '- 生成式推荐的候选item/Semantic ID生成场景，可参考上下文加权损失思路，对高确定性对应token降低权重、高不确定性token提升权重，过滤无效训练信号

  - 非自回归商品标题、营销push文案生成场景，可替换原离散流匹配/扩散采样器为上下文加权版本，几乎无额外开销即可提升生成质量，同时保留任意顺序生成灵活性

  - LLM微调做序列生成任务时，可借鉴按局部上下文密度加权交叉熵的思路，替代普通交叉熵损失，降低生成困惑度'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
传统离散流匹配（DFM）的因子化训练目标对难度差异极大的预测目标同等对待，混合高熵模糊token和可预测token的训练信号，导致生成效果受限；实证发现token预测不确定性和邻域局部上下文密度高度相关。
### 方法关键点
1. 对DFM底层的连续时间马尔可夫链（CTMC）做轻量化修改，引入局部上下文信息设计上下文加权采样器；
2. 提出缩放交叉熵损失，对不同token的训练信号按上下文关联的不确定性做重加权。
### 关键结果
在OpenWebText数据集上生成困惑度最高降低63%，生成质量与强基线半自回归块扩散持平，同时保留任意顺序生成能力，额外计算开销可忽略。
