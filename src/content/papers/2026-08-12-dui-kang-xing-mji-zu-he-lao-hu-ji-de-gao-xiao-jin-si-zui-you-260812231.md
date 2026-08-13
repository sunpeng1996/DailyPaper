---
title: An Efficient Near-Optimal Algorithm for Adversarial $m$-Set Bandits
title_zh: 对抗性m集组合老虎机的高效近似最优算法
authors:
- Francesco Bacchiocchi
- Tommaso Cesari
- Roberto Colomboni
affiliations:
- Politecnico di Milano
- University of Ottawa
- University of Bristol
arxiv_id: '2608.12231'
url: https://arxiv.org/abs/2608.12231
pdf_url: https://arxiv.org/pdf/2608.12231
published: '2026-08-12'
collected: '2026-08-13'
category: Other
direction: 组合对抗老虎机算法优化
tags:
- Combinatorial Bandit
- Adversarial Bandit
- Regret Bound
- Online Learning
- Efficient Algorithm
one_liner: 无需枚举指数级动作空间，实现m集对抗老虎机多项式时间运行、最优高概率regret界
practical_value: '- 电商凑单/搭配等多物品组合推荐场景，可借鉴该算法的m个物品选优逻辑，避免枚举所有组合大幅降低算力消耗

  - 推荐/广告系统仅能获得组合收益反馈（如套餐转化率、多广告位整体转化）时，可复用其参数化采样分布设计，替代需枚举组合的EXP3类算法

  - 在线广告多广告位组合投放场景，可基于该算法实现多项式时间的投放策略迭代，大幅降低内存占用'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
对抗性m集组合老虎机每次从d个物品中选取m个，仅能观测选中组合的聚合损失，动作空间规模为$inom{d}{m}$，呈指数级增长；现有最优EXP3-KW算法直接实现需要指数级存储空间，而已有多项式时间算法的regret界劣于理论最优。

### 方法关键点
利用组合损失由d维物品损失向量决定的结构特性，无需显式枚举所有动作，仅用d个参数表示采样分布，整个算法在多项式时间内运行。

### 关键结果
针对自适应非预知对抗方，以至少$1-\delta$的概率保证regret为$R_T=O\left(\sqrt{dT\log(K/\delta)}\right)$，完全匹配现有最优高概率regret界，解决了Maiti等人提出的公开问题。
