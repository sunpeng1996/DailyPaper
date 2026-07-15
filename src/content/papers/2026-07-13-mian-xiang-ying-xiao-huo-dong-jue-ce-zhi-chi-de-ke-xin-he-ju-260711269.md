---
title: 'Trustworthy synthetic data for campaign decision support: strategy simulation
  fidelity and the PolicySynth framework'
title_zh: 面向营销活动决策支持的可信合成数据：策略仿真保真度与PolicySynth框架
authors:
- Tung Dang
- The Hung Phung
- Son Lam Nguyen
- Tu Nguyen
affiliations:
- Graduate School of Science, The University of Tokyo
- Faculty of Human Resource Management, Trade Union University
- Institute for Business Management Development, Academy Of Finance
- Ministry of Industry and Trade, Hanoi
arxiv_id: '2607.11269'
url: https://arxiv.org/abs/2607.11269
pdf_url: https://arxiv.org/pdf/2607.11269
published: '2026-07-13'
collected: '2026-07-15'
category: RecSys
direction: 合成数据 · 营销活动决策支持
tags:
- synthetic-data
- decision-support
- marketing-campaign
- privacy-preserving
- evaluation-metric
one_liner: 提出决策对齐的合成数据评估指标SSF、PolicySynth框架与三轴部署标准，支撑营销活动仿真决策
practical_value: '- 营销活动仿真评估合成数据时，放弃仅用分布相似性的标准，改用SSF指标衡量决策对齐度，避免错误的活动上线决策

  - 合成数据生成器可引入生产环境的用户 churn/转化预打分模块作为条件约束，提升决策相关特征的对齐效果

  - 合成数据落地必须通过三轴质量门：决策对齐度、成员推理抗性、新记录生成率，同时保障决策可靠性与隐私合规

  - 合成数据仅适合做方向性go/no-go筛选，ROI估算需额外做量级校正，不可直接用合成数据输出的绝对值做预算规划'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
隐私约束下无法直接用真实用户数据做营销活动what-if分析，现有合成数据仅用分布相似性评估，无法保证与真实数据输出一致的活动决策，易误导运营判断。
### 方法关键点
1. 提出策略仿真保真度（SSF）指标，衡量合成数据与真实数据输出相同go/no-go活动决策的比例；
2. 设计PolicySynth框架，生成器引入生产环境的churn打分器作为条件约束，对齐决策相关的用户特征结构；
3. 制定三轴部署质量标准：决策对齐度、成员推理抗性、新记录生成率，作为最低上线要求。
### 关键结果
在电信流失、银行获客数据集上，PolicySynth平均SSF分别达0.923、0.960；种子间方差较CTGAN低10倍（电信）、2.5倍（银行）；月度重训后决策波动仅±1.2pp，远低于CTGAN的±11.5pp；仅优化SSF的基线存在隐私泄露风险，验证三轴标准必要性。
