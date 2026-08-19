---
title: Toward the Optimal Regret-Instability Trade-off in Multi-Armed Bandits
title_zh: 多臂老虎机中后悔与不稳定性的最优权衡研究
authors:
- Kaifei Wang
- Yinyu Ye
- Han Zhong
arxiv_id: '2608.17841'
url: https://arxiv.org/abs/2608.17841
pdf_url: https://arxiv.org/pdf/2608.17841
published: '2026-08-18'
collected: '2026-08-19'
category: RecSys
direction: 多臂老虎机 后悔-不稳定性权衡优化
tags:
- Multi-Armed Bandits
- UCB
- Regret Minimization
- Online Learning
- Exploration
one_liner: 推导多臂老虎机后悔-不稳定性乘积有限时间下界，给出匹配下界的可调SLE-UCB算法
practical_value: '- 电商冷启动/新商品探索场景可引入SLE-UCB算法，在保证探索收益（低regret）的同时降低多轮实验的流量分配波动，减少业务策略震荡

  - 多场景流量分配任务可参考regret-不稳定性乘积下界结论，根据业务对流量稳定性的容忍度灵活调整超参数，在收益和稳定性间做trade-off

  - 在线A/B实验的策略选型可参考本文的不稳定性度量方式，量化评估相同收益下不同探索算法的流量波动程度，适配业务需求'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有多臂老虎机(MAB)算法仅用regret衡量效果，相近regret的不同算法在独立运行时的臂拉取次数（对应推荐场景的流量分配）波动差异极大，缺乏两者权衡的有限时间理论支撑与匹配算法。

### 方法关键点
1. 定义不稳定度为终端拉取次数的最大标准差，推导无正则假设下的有限时间regret-不稳定度乘积下界；
2. 可调SLE-UCB算法融合动态下包络索引与递减拉取次数稳定项；
3. 离线前缀表示法消除在线决策路径依赖，结合Efron-Stein不等式控制拉取方差。

### 关键结果
有限时间下界满足$R_{K,T}S_{K,T} \ge CT^{3/2}$，SLE-UCB的乘积上界为$O(T^{3/2}\log K)$，T维度完全匹配下界，K维度仅差对数因子，解决了已有研究中臂相关的regret-不稳定度边界的开放问题。
