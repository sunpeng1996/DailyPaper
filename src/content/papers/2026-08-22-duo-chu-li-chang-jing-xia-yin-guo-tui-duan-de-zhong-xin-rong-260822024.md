---
title: Barycentric Fused Gromov-Wasserstein Balancing for Causal Inference under Multiple
  Treatments
title_zh: 多处理场景下因果推断的重心融合Gromov-Wasserstein平衡方法
authors:
- Yuki Murakami
- Takumi Hattori
- Kohsuke Kubota
affiliations:
- NTT DOCOMO, INC.
- Yokohama City University
arxiv_id: '2608.22024'
url: https://arxiv.org/abs/2608.22024
pdf_url: https://arxiv.org/pdf/2608.22024
published: '2026-08-22'
collected: '2026-08-25'
category: Other
direction: 多处理因果推断 · 营销决策优化
tags:
- Causal Inference
- Treatment Effect Estimation
- Wasserstein Distance
- Observational Data
- Marketing Analytics
one_liner: 提出BFG-WB目标对齐多处理表示分布，将计算复杂度从二次降为线性，提升因果效应估计精度
practical_value: '- 电商多触达组合营销场景中，可复用BFG-WB的线性复杂度表示对齐方法替代原两两平衡方案，大幅降低多策略效果归因的计算开销

  - 做用户异质性营销效果估计时，可引入Fused Gromov-Wasserstein约束保留用户局部相似结构，提升反事实策略预估的可靠性

  - 组合优惠、多触点推送等多处理场景的策略优选，可直接适配CIHSI-Net框架做因果效应预估，减少不必要的A/B测试成本'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
多处理同时作用下的异质性单处理与交互效应估计是营销等场景决策的核心需求，现有两两处理表示平衡方法复杂度随处理模式数呈二次增长，且无法保留跨处理的局部邻接结构，导致反事实估计效果退化。
### 方法关键点
提出CIHSI-Net深度学习框架，核心基于新型BFG-WB优化目标：将每个处理模式的表示分布对齐到共享Wasserstein重心，实现全局对齐的同时将计算复杂度从二次降为线性；通过Fused Gromov-Wasserstein差异约束保留局部近邻结构，保障异质性效应估计的可靠性。
### 关键结果
仿真实验中CIHSI-Net效果持续超越SOTA基线，在真实营销数据的复杂多处理场景下验证了实际应用价值。
