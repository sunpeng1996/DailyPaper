---
title: 'SMC-ES: Automated synthesis of formally verified control policies'
title_zh: SMC-ES：可形式化验证控制策略的自动化合成
authors:
- Riccardo Curcio
- Toni Mancini
- Enrico Tronci
arxiv_id: '2607.15003'
url: https://arxiv.org/abs/2607.15003
pdf_url: https://arxiv.org/pdf/2607.15003
published: '2026-07-16'
collected: '2026-07-20'
category: Other
direction: 安全强化学习 · 形式化验证控制策略合成
tags:
- Reinforcement-Learning
- Formal-Verification
- Evolutionary-Strategy
- Safety-Critical-Control
- Statistical-Model-Checking
one_liner: 融合进化策略与统计模型校验，生成带安全鲁棒性形式化保障的控制策略
practical_value: '- 高风险业务场景（如金融电商合规推荐、营销活动风险管控Agent）可参考「策略优化+统计校验」双路架构，兼顾性能与合规要求

  - 可复用δ（置信度）+ε（允许故障率）的双参数风险边界定义方法，量化业务可容忍的风险阈值

  - 若需对大模型驱动的推荐Agent策略做安全校验，可借鉴其统计抽样验证逻辑，低成本获取策略安全置信度'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
安全关键场景下强化学习生成的控制策略缺乏形式化安全保障，无法满足高可靠性部署要求。

### 方法关键点
SMC-ES框架融合进化策略（ES）与统计模型校验（SMC）：
1. 预定义置信度参数δ、允许故障率ε两个安全边界指标
2. 由ES优化策略性能，同步通过SMC对生成策略做形式化校验，输出安全证书：至少1-δ置信度下，策略违反安全属性的概率不超过ε

### 关键结果
在Gymnasium、Safety Gymnasium连续控制任务上测试，相比主流无模型DRL、Safe-DRL基线，仅增加可接受的计算开销，即可获得性能相当、同时带性能/安全/鲁棒性形式化保障的控制策略
