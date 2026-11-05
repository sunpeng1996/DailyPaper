---
title: 'One Basket, Many Experts: Decorrelated Re-ranking for Financial Asset Recommendation'
title_zh: 面向零售投资者的金融资产推荐去相关重排方法DSER
authors:
- Ryuki Unno
- Keigo Sakurai
- Koshi Watanabe
- Keisuke Maeda
- Takahiro Ogawa
- Miki Haseyama
affiliations:
- Hokkaido University
arxiv_id: '2611.05952'
url: https://arxiv.org/abs/2611.05952
pdf_url: https://arxiv.org/pdf/2611.05952
published: '2026-11-04'
collected: '2026-11-05'
category: RecSys
direction: 金融推荐 · 重排优化 · 多目标权衡
tags:
- re-ranking
- financial recommendation
- portfolio optimization
- multi-objective tradeoff
- decorrelation
one_liner: 提出可调替换槽位数的去相关重排方法DSER，以微小相关性损失提升资产组合风险调整后收益
practical_value: '- 重排阶段可采用「保留TopK高相关结果+剩余槽位做业务目标优化」的架构，将多目标权衡转化为可解释、可审计的单参数调节，规避黑盒模型不可控问题

  - 跨品类电商搭配推荐场景可复用去相关思路，在保留用户兴趣匹配度的同时，提升推荐结果的品类多样性、连带转化率

  - 多目标优化场景无需强行拟合加权损失，可通过「部分保序+部分替换」的轻量化策略，快速产出可落地的tradeoff方案'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有金融资产推荐仅优化用户相关性，结果集中于少数热门资产，收益率高度相关，限制组合风险调整后收益，且多目标权衡隐含在黑盒模型中不可控。
### 方法关键点
提出DSER重排框架，固定保留Top(N-m)个高相关性推荐结果，剩余m个槽位替换为与现有池收益率低相关的替代资产；m为业务方可手动调节的整数参数，实现相关性与组合收益的明确、可审计权衡。
### 关键结果数字
在FAR-Trans零售经纪数据集实验，仅替换少量槽位即可提升风险调整后收益，相关性损失小于5%；收益增益覆盖真实交易成本后依然成立，相关性损失在各市场周期稳定，收益增益随市场周期变化。
