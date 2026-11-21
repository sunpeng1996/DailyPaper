---
title: Time Series Structure Learning with Local Causal Parent Discovery
title_zh: 基于局部因果父节点发现的时间序列结构学习方法
authors:
- Jacqueline Maasch
- Shu Wan
- Hank Zhu
- Huan Liu
- Zhiguang Wang
affiliations:
- Cornell Tech
- Abel AI
- Arizona State University
arxiv_id: '2611.26232'
url: https://arxiv.org/abs/2611.26232
pdf_url: https://arxiv.org/pdf/2611.26232
published: '2026-11-18'
collected: '2026-11-21'
category: Other
direction: 非平稳多变量时间序列因果结构学习
tags:
- Time-Series
- Causal-Discovery
- Graphical-Model
- Structure-Learning
- Non-Stationarity
one_liner: 提出ITPD局部因果发现算法，大幅降低大规模非平稳时间序列因果结构学习的计算开销
practical_value: '- 电商用户行为时序因果归因可复用ITPD局部到全局的挖掘思路，规避全图因果检验的高复杂度，适配高维用户/商品特征场景

  - 大促、节假日等用户行为漂移的非平稳时序场景，可直接采用ITPD做因果关系挖掘，比传统平稳假设方法更贴合业务数据分布

  - 低阶条件独立性检验替换高阶检验的trick可迁移到推荐特征重要性排序场景，显著降低离线特征挖掘的计算开销'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
时间序列数据存在自相关、分布漂移、维度灾难问题，传统因果发现算法本身计算和样本复杂度高，进一步阻碍了其在大规模非平稳时序场景的落地。
### 方法关键点
提出约束式迭代时序父节点发现算法ITPD，采用局部到全局学习范式：依次挖掘每个变量的因果父集，拼接得到全局因果图；利用时序结构先验、图划分、局部马尔可夫条件，将高阶条件独立性检验替换为低阶版本，大幅压缩计算量。
### 关键结果
- 精确oracle下，ITPD的检验次数、平均条件集大小均优于所有基线
- 仿真基准测试中，F1值和运行耗时处于帕累托最优前沿，1000节点以上大图速度显著超越基线
- 2000节点大规模图场景下，速度比迭代IAMB、DF-PC、PCMCI分别快2.3×、9.1×、40.9×
