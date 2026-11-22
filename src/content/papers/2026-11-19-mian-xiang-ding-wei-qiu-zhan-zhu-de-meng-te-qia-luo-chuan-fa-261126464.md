---
title: Monte Carlo Pass Search for Setpieces
title_zh: 面向定位球战术的蒙特卡洛传球搜索方法
authors:
- Andrew Kang
arxiv_id: '2611.26464'
url: https://arxiv.org/abs/2611.26464
pdf_url: https://arxiv.org/pdf/2611.26464
published: '2026-11-19'
collected: '2026-11-22'
category: Other
direction: 体育战术优化 · 反事实模拟
tags:
- Monte-Carlo-Search
- Counterfactual-Simulation
- World-Model
- Sports-Analytics
- Expected-Goals
one_liner: 提出蒙特卡洛传球搜索MCPS，通过世界模型模拟反事实定位球场景优化战术，提升xG
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 4
source: arxiv-cs.AI
depth: abstract
---

### 动机
定位球贡献约1/3非点球预期进球（xG），现有评估方法仅基于实际发生事件，存在结果偏差、无法提供反事实参考等局限，难以支撑战术优化决策。
### 方法关键点
提出蒙特卡洛传球搜索（MCPS）框架，将角球、高空任意球视为执行路径与未来场景的分布而非单一事件；融合3D球体物理模型、22名球员行为生成模型、门将决策模型、触球预测模型构建世界模型，模拟反事实传球路线、球员站位、跑位的多种可能，通过价值模型打分筛选最优方案。
### 关键结果数字
在2025/26赛季意甲30场比赛249次传球数据上，最优传球路线比实际传球xG高0.0085（+28%）；同步优化球员站位可额外提升0.0027~0.0033 xG，进一步优化跑位可再提升0.0007 xG。
