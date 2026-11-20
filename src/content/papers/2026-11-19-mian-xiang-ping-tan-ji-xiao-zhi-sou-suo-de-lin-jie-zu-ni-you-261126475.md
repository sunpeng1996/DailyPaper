---
title: 'A new algorithmic approach for finding flat minima: critically damped Polyak
  stepsizes'
title_zh: 面向平坦极小值搜索的临界阻尼Polyak步长优化算法
authors:
- Francesco Caporali
- Jason M. Altschuler
- Boris Hanin
arxiv_id: '2611.26475'
url: https://arxiv.org/abs/2611.26475
pdf_url: https://arxiv.org/pdf/2611.26475
published: '2026-11-19'
collected: '2026-11-20'
category: Training
direction: 模型训练 · 自适应步长与平坦极小值优化
tags:
- Optimizer
- StepSize
- FlatMinima
- LLM Fine-tuning
- SAM
one_liner: 提出临界阻尼Polyak自适应步长规则，兼顾损失下降与收敛到泛化性更好的平坦极小值
practical_value: '- LLM微调（含推荐场景的LoRA、prompt微调）可直接替换原有步长策略，获得与SAM相当的平坦极小值效果，省去SAM两次前向的计算开销

  - 过参数化推荐模型（大尺寸双塔、排序模型）训练引入CDP步长，可提升泛化性，降低分布偏移下的性能掉点

  - 无需手动设计学习率衰减策略，CDP步长会随离极小值流形的距离自适应收缩，大幅降低训练调参成本'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
过参数化模型（大推荐模型、LLM）的损失存在大量全局极小值，平坦极小值对应泛化性更好的解，但现有自适应步长策略难以兼顾损失收敛效率与平坦极小值搜索，SAM等平坦优化方法需额外前向计算开销。
### 方法关键点
1. 提出临界阻尼Polyak（CDP）步长：在经典Polyak步长基础上乘以4倍系数加轻度阻尼因子，在稳定性边缘运行自适应匹配局部曲率
2. 步长随离极小值流形的距离自动收缩，无需额外手动设置学习率衰减，可自然收敛到局部锐度最小的插值解
### 关键结果
- 理论上首次对广泛局部二次目标给出锐度与损失下降的一致时间保证
- 实验上达到与SAM相当的平坦化效果，可直接用于非线性师生网络、预训练LLM微调场景，无额外计算开销
