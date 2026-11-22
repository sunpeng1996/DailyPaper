---
title: Simple Private Noisy SGD is Minimax-Optimal under Population Strong Convexity
title_zh: 群体强凸条件下简单私有噪声SGD达到极小极大最优
authors:
- Valentin Roth
- Marco Avella Medina
arxiv_id: '2611.26515'
url: https://arxiv.org/abs/2611.26515
pdf_url: https://arxiv.org/pdf/2611.26515
published: '2026-11-19'
collected: '2026-11-22'
category: Training
direction: 差分隐私训练 · 优化算法理论
tags:
- Differential Privacy
- Noisy SGD
- Minimax Optimality
- Convex Optimization
- GLM
one_liner: 证明群体强凸场景下最简差分私有噪声SGD可达极小极大最优收敛率，消去现有结果多对数项
practical_value: '- 做差分隐私约束的推荐/广告CTR模型训练时，可直接采用最简固定步长单轮Noisy SGD，无需额外复杂trick即可达到最优收敛效率

  - 针对逻辑回归等强凸GLM类基线模型，该方案可消去多对数项冗余开销，在满足隐私合规要求的同时降低训练误差

  - 隐私预算分配可参考论文的Renyi DP下误差上界推导公式，量化平衡训练精度与隐私保护等级'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
传统SGD在凸广义线性模型（GLM）场景已被证明达到统计极小极大最优，但最简差分私有版本Noisy SGD在强凸损失下是否具备同等最优性尚无定论，现有私有SGD收敛率结果存在冗余多对数项。
### 方法关键点
基于标准凸分析，推导Renyi DP约束下、紧凑凸域内光滑强凸Lipschitz损失上，固定步长、固定批量的单轮Noisy SGD的参数估计误差上界；基于Score Attack框架推导对应场景的极小极大下界，验证上界与下界完全匹配。
### 关键结果
首次给出私有逻辑回归场景下Noisy SGD的极小极大最优收敛率，完全消去现有结果中的多对数项，且期望和高概率场景下收敛率保持一致。
