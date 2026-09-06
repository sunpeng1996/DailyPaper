---
title: Conditioning Degenerate Diffusion Models
title_zh: 退化扩散模型的条件生成方法
authors:
- Uğur Aydın
- Tamer Başar
affiliations:
- University of Illinois Urbana Champaign
- Department of Electrical and Computer Engineering, UIUC
- Coordinated Science Laboratory, UIUC
arxiv_id: '2609.04090'
url: https://arxiv.org/abs/2609.04090
pdf_url: https://arxiv.org/pdf/2609.04090
published: '2026-09-03'
collected: '2026-09-06'
category: Training
direction: 生成式模型 · 退化扩散模型训练
tags:
- Diffusion Models
- Causal Optimal Transport
- Generative Modeling
- Minimum Entropy Control
- Degenerate Diffusion
one_liner: 基于因果最优运输定义近似损失，解决退化扩散模型的条件生成引导问题
practical_value: '- 扩散类生成式推荐模型遇条件密度不光滑场景时，可尝试引入因果最优运输替代score匹配损失

  - 最小熵控制思路可迁移到扩散模型引导生成环节，降低生成item/文案的随机性

  - 核心为理论贡献，上层推荐/Agent业务团队直接可复用价值较低'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有条件生成模型训练高度依赖score函数做引导，当扩散模型系数奇异、底层条件密度不存在或不光滑时，传统score引导方法完全失效，缺少低假设下的可行方案。
### 方法关键点
1. 基于因果最优运输定义近似损失函数，在最低假设下求解最小熵控制项作为生成引导信号，无需依赖光滑条件密度
2. 利用鞅问题良定的条件扩散过程的可预测表示特性，完成因果最优运输的形式化刻画，保证理论完备性
### 关键结果
理论上证明了所提损失函数的一致性，可在退化扩散场景下实现稳定的条件生成引导，适配密度不存在/不光滑的极端情况
