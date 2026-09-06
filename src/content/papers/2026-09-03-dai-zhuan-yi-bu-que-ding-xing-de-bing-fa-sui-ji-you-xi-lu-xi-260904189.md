---
title: Robust PAC Learning of Concurrent Stochastic Games
title_zh: 带转移不确定性的并发随机游戏鲁棒PAC学习框架
authors:
- Angel Y. He
- David Parker
affiliations:
- University of Oxford, Department of Engineering Science
- University of Oxford, Department of Computer Science
arxiv_id: '2609.04189'
url: https://arxiv.org/abs/2609.04189
pdf_url: https://arxiv.org/pdf/2609.04189
published: '2026-09-03'
collected: '2026-09-06'
category: MultiAgent
direction: 多智能体博弈 · 纳什均衡学习
tags:
- Multi-Agent Learning
- PAC Learning
- Nash Equilibrium
- Stochastic Games
- Robust Learning
one_liner: 首个面向带转移不确定性的通用和并发随机游戏的PAC学习框架，可输出近似纳什均衡或证明其不存在
practical_value: '- 广告竞价、平台供需等多智能体博弈场景，可借鉴其转移核鲁棒置信集构建方法，降低动态估计误差对均衡求解的干扰

  - 纳什margin刻画方法可迁移用于判断多主体博弈场景是否存在真实均衡，避免无意义的寻优开销

  - 样本复杂度理论界可用于多智能体交互类任务的采样预算预评估'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有并发随机游戏（CSG）纳什均衡求解方法大多假设转移概率完全已知，未知转移场景下的估计误差易导致均衡失效，且无成熟框架可同时处理均衡不存在的边界情况。
### 方法关键点
1. 构建基于采样数据的转移核$L^1$置信集，结合鲁棒MDP探索机制保证联合状态-动作对的覆盖度，求解鲁棒CSG得到社会福利最优的$ε$-纳什均衡
2. 提出纳什margin刻画规则，可二择一输出符合要求的近似均衡，或给出精确均衡不存在的可信证明
### 关键结果
满足最小可达性条件$p_{​reach}>0$时，算法样本复杂度为$O\left( R_{\max}^2 H^4 |S|^2 |A| / (p_{​reach} ε^2) \right)$，基准CSG测试中性能接近最优，样本复杂度与理论推导一致
