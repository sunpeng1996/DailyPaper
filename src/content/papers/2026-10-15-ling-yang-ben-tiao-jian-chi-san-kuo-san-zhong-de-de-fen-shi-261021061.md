---
title: Score Mismatch and Set-Constrained Sampling in Zero-Shot Conditional Discrete
  Diffusion
title_zh: 零样本条件离散扩散中的得分失配与集合约束采样
authors:
- Renxiang Huang
- Yuchen Liang
- Yingbin Liang
- Ness Shroff
- Lifeng Lai
arxiv_id: '2610.21061'
url: https://arxiv.org/abs/2610.21061
pdf_url: https://arxiv.org/pdf/2610.21061
published: '2026-10-15'
collected: '2026-10-17'
category: Training
direction: 离散扩散 · 零样本条件生成优化
tags:
- Discrete Diffusion
- Zero-shot Generation
- Score Matching
- Sampling Method
- Conditional Generation
one_liner: 首个理论分析离散扩散得分失配问题，提出RHC采样器降低零样本条件生成偏差
practical_value: '- 生成式推荐场景（商品文案生成、约束候选集生成）可直接复用RHC采样器替代传统Conditional SEDD采样，零样本条件下无需额外finetune即可降低生成偏差

  - 搜索query改写、商品标题补全、关键词约束生成等场景，可通过该方法实现坐标级集合约束（比如强制包含指定商品属性词），无需重新训练条件扩散模型

  - 离散扩散模型落地前可参考论文给出的KL散度上界公式，量化得分失配带来的效果损失，提前评估零样本复用的可行性，降低试错成本'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
离散扩散是序列、文本类生成的主流范式，但零样本条件生成场景下（无条件训练的模型直接复用做条件生成）存在严重得分失配问题，传统Conditional SEDD采样器偏差随维度、词表规模线性升高，无明确理论分析和优化方案。
### 方法关键点
1. 首次完成得分失配离散扩散的理论分析，推导KL散度上界，明确失配带来的额外偏差来源；
2. 覆盖文本补全、句子生成、坐标级集合约束等多类零样本条件生成场景；
3. 提出Randomized Hard Clamping (RHC)采样器，可直接通过无条件得分+吸收速率精确计算分配概率，无需额外训练条件扩散模型。
### 关键结果
数值模拟及真实数据集实验均验证，RHC采样器相比传统Conditional SEDD采样器偏差显著降低，生成效果更优。
