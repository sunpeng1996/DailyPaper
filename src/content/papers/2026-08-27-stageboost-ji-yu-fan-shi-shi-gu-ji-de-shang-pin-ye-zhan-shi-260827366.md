---
title: 'Stageboost: Recommending Signals Based on Counterfactual Estimation'
title_zh: Stageboost：基于反事实估计的商品页展示信号推荐
authors:
- Darpan Singhal
- Matan Mandelbrod
- Tal Franji
- Manasa Kolla
- Vipul Gaba
- Yuri Brovman
affiliations:
- eBay India
- eBay Israel
- eBay USA
arxiv_id: '2608.27366'
url: https://arxiv.org/abs/2608.27366
pdf_url: https://arxiv.org/pdf/2608.27366
published: '2026-08-27'
collected: '2026-08-28'
category: RecSys
direction: 商品详情页信号推荐 · 反事实估计
tags:
- Counterfactual Estimation
- XGBoost
- E-commerce Conversion
- Signal Recommendation
- A-B Testing
one_liner: eBay提出两阶段XGBoost反事实信号推荐框架，优化商品详情页信号配置提升GMV
practical_value: '- 商品详情页的高价值信号（稀缺、免邮、售后）可分位置做个性化排序，优先对高客单价商品展示转化增益高的信号

  - 两阶段树模型架构可复用：第一阶段预估单个信号对转化的反事实增益，第二阶段做多位置信号组合全局最优

  - 小流量AB测试可优先观测高客单价品类的转化变化，这类用户对上下文信号敏感度更高，指标增益更显著'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
电商商品详情页是用户转化核心触点，页面上的稀缺、售后、物流类上下文提示信号对用户购买决策影响大，传统单信号排序未考虑多位置组合的全局最优，也无法准确度量单个信号对转化的真实增益。

### 方法关键点
两阶段XGBoost架构Stageboost：第一阶段基于反事实估计建模单个信号在对应位置对用户转化的边际增益；第二阶段在多位置信号数量上限约束下，做全局组合优化输出最优信号投放策略，覆盖稀缺类、信任类两类核心信号位。

### 关键结果
线上AB测试整体GMV提升0.08%，配件品类GMV提升0.58%，增益主要来自高客单价商品的转化率提升。
