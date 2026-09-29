---
title: 'When Privacy Moves ML-Mediated Decisions On Device: Information and Incentive
  Misalignment in Auctions'
title_zh: 端侧ML决策下的拍卖信息与激励错配问题研究
authors:
- Dipankar Sarkar
affiliations:
- Skelf Research
arxiv_id: '2609.33312'
url: https://arxiv.org/abs/2609.33312
pdf_url: https://arxiv.org/pdf/2609.33312
published: '2026-09-26'
collected: '2026-09-29'
category: RecSys
direction: 端侧广告拍卖 · 预算机制优化
tags:
- on-device-auction
- budget-pacing
- ad-auction
- incentive-alignment
- privacy-preserving-ads
one_liner: 量化端侧拍卖的预算同步超支效应 给出信息错配上界与激励错配修复方案
practical_value: '- 端侧隐私广告系统设计中，预算同步滞后导致的超支无法通过pacing控制器调优解决，可选择提高同步频率或采用escrow式设备预算预分配，平衡超支风险与预算利用率

  - 现有端侧拍卖的runner-up scaled score定价规则存在非诚实竞价漏洞，改用critical-base-bid定价可修复单轮拍卖DSIC属性，无需改动原有排序逻辑

  - PI控制器仅在1-2个tick的极短滞后场景下能降低超支，滞后超过5个tick时与普通比例控制器效果一致，无需投入资源优化长滞后下的控制器策略

  - 端侧pacing通过压低成交价而非减少参与提升曝光，相同预算下可拿到11.5倍曝光量，该特性可用于优化投放效果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
隐私合规驱动广告拍卖等ML决策从云端迁移到端侧，共享预算的跨设备同步滞后会导致传统集中式pacing算法完全失效，同时端侧拍卖的定价规则存在未被发现的激励设计缺陷，两类问题的影响此前没有被系统量化。

### 方法关键点
- 搭建端侧拍卖仿真环境：覆盖50台设备、36个分垂直广告campaign、100个tick投放窗口，预算同步滞后Δ可在0~50区间调整，支持均质流量/突发流量、均质设备/异构设备配置
- 对比三类pacing策略：ASAP全量投放、比例Even控制器、PI控制器，验证两种定价规则：原生score-space定价、critical-base-bid定价
- 推导有限窗口下的预期超支上界，量化同步滞后、流量到达强度、单请求支付上限对超支的影响

### 关键结果
- 20倍预算压力下，Even pacing在1个tick滞后时超支17.77%，50个tick滞后时超支达1669.31%；即便是2倍低预算压力，50个tick滞后超支仍达106.95%
- 本地可见预算拒付规则仅能消除0滞后下的超支，1个tick滞后下仍有11.88%的跨设备超支
- 原生score-space定价下98.23%的多竞价者拍卖存在可盈利的竞价偏离，改用critical-base-bid定价后无单轮可盈利偏离，符合DSIC属性
- PI控制器仅在Δ=1、Δ=2短滞后场景下分别降低10.33、3.23个百分点超支，滞后超过5个tick后与比例控制器效果完全一致

### 核心结论
端侧决策的经济问题本质是信息一致性问题，控制器调优无法解决不可见的跨设备状态差异。
