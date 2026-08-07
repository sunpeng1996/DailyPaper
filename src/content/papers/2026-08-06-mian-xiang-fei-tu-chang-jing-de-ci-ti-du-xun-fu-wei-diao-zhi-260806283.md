---
title: The Tamed Subgradient Unadjusted Langevin Algorithm beyond Convexity
title_zh: 面向非凸场景的次梯度驯服未调整朗之万算法
authors:
- Iosif Lytras
- Nikolaos Makras
- Sotirios Sabanis
affiliations:
- University of Edinburgh, UK
- National Technical University of Athens, Greece
- Athena/Archimedes Research Centre, Greece
arxiv_id: '2608.06283'
url: https://arxiv.org/abs/2608.06283
pdf_url: https://arxiv.org/pdf/2608.06283
published: '2026-08-06'
collected: '2026-08-07'
category: Training
direction: 大模型训练优化 · 非凸非光滑场景算法
tags:
- Langevin Algorithm
- Subgradient Optimization
- Non-convex Optimization
- LLM Training
- Convergence Bound
one_liner: 提出SG-TULA次梯度朗之万采样算法，非凸非光滑场景收敛更优，LLM预训练效果对标AdamW与Muon
practical_value: '- 推荐/Agent场景下的非凸非光滑大模型微调任务，可尝试SG-TULA替代AdamW，避免梯度爆炸同时具备理论收敛保障

  - 带正则的LLM预训练/轻量化微调流程，可复用坐标增强版SG-TULA实现，省去梯度平滑操作的计算开销

  - 非凸优化算法选型时，可参考文中Wasserstein-2距离收敛界作为算法效果的量化评估依据'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有优化算法的理论分析多基于凸性+全局Lipschitz梯度假设，无法覆盖LLM、推荐排序模型等梯度超线性增长、非光滑、非凸共存的实际场景，传统次梯度类朗之万算法存在收敛速率慢、需额外高开销平滑操作的问题。
### 方法关键点
提出SG-TULA算法，直接基于次梯度离散化朗之万扩散过程，引入taming技术处理超线性梯度，无需复杂平滑操作；推导Wasserstein-2距离下的非渐近收敛界，所有常数明确关联模型维度与逆温度。
### 关键结果
收敛速率优于现有所有次梯度朗之万算法；坐标增强版SG-TULA用于GPT-2系LLM正则预训练，效果与微调后的AdamW、Muon相当，且具备二者没有的非渐近收敛保证。
