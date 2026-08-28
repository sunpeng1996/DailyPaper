---
title: 'When Interference Graphs Evolve: Doubly Robust Estimation of Dynamic Peer
  Effects'
title_zh: 动态演化干扰图场景下的同伴效应双重鲁棒估计
authors:
- Xiaojing Du
affiliations:
- Adelaide University
arxiv_id: '2608.27187'
url: https://arxiv.org/abs/2608.27187
pdf_url: https://arxiv.org/pdf/2608.27187
published: '2026-08-27'
collected: '2026-08-28'
category: Other
direction: 因果推断 · 动态网络同伴效应估计
tags:
- Causal Inference
- Dynamic Graph
- Doubly Robust
- Peer Effect
- Network Estimation
one_liner: DynaNet-DR双重鲁棒估计器，解决动态演化交互图场景下的同伴效应因果估计难题
practical_value: '- 评估电商社交裂变、好友推荐效果时，可复用DynaNet-DR的控制对照框架，区分自身干预、同伴曝光、网络演化三类效应，避免高估拉新/促销活动的单点效果

  - 动态图上的因果估计可复用时间分解倾向得分+归一化增强的结构，搭配固定截断、有限样本稳定trick提升小流量实验的效应估计准确率

  - 评估用户社交互动相关推荐策略收益时，可参考摘要量索引的对比评估范式，无需反事实生成边即可完成效果校验'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
动态演化交互图场景下的同伴效应估计是推荐、社交平台干预评估的核心难点，经典因果估计的无干扰假设不成立，现有方法无法区分干预前网络历史、动态同伴曝光、干预后网络变化三类不同因果作用，易导致效应估计偏差。
### 方法关键点
受控对比框架将潜在结果按自身干预、时间聚合同伴曝光、干预后演化摘要三个维度索引，定义自身干预、同伴曝光、受控网络演化等多类对比量；DynaNet-DR动态网络双重鲁棒估计器融合时间分解倾向得分与归一化增强模块，只要结果回归或倾向得分估计任意一个正确，估计结果就具备一致性，落地实现加入代表分预测、固定截断、有限样本稳定优化。
### 关键结果
在固定真实时序图序列的半合成基准测试中，DynaNet-DR的估计精度优于所有面向全维度剖面的同类方法
