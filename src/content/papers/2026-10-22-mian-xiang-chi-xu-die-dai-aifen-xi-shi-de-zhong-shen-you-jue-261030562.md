---
title: Lifetime-valid decisions by continually evolving AI analysts
title_zh: 面向持续迭代AI分析师的终身有效决策验证框架
authors:
- Xiaojing Sun
- Yuhan Zeng
- Xiao Wang
affiliations:
- Purdue University
arxiv_id: '2610.30562'
url: https://arxiv.org/abs/2610.30562
pdf_url: https://arxiv.org/pdf/2610.30562
published: '2026-10-22'
collected: '2026-10-24'
category: Agent
direction: Agent 决策风险持续管控
tags:
- AI-Agent
- Type-I-Error
- Continual-Validation
- A-B-Testing
- Risk-Management
one_liner: 提出持续验证框架，可保障任意迭代的AI分析师决策I类错误率终身受控
practical_value: '- 电商A/B测试决策Agent迭代时，可复用该持续验证机制：每次更新前用原假设为真的模拟数据集测试，确保误上线无收益功能的概率终身受控

  - 可直接复用阈值计算逻辑：根据业务可接受的目标错误率α、终身风险δ，计算验证阈值α''=(α-δ)/(1-δ)，平衡风险和迭代效率

  - 对于分析路径固定的LLM Agent，可直接验证所有路径的最坏情况I类错误，无需重复调用LLM，大幅降低验证的算力成本

  - 迭代频繁的推荐/广告策略Agent，可参考该方法避免过拟合历史测试集、错误率随迭代累积升高的问题'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
AI Agent 已广泛用于生物等效性分析、产品A/B测试上线判断等决策场景，传统I类错误控制方法仅适用于固定流程；而Agent自身存在内部采样随机性，且持续迭代过程中易过拟合历史评估反馈，导致I类错误风险随迭代次数累积升高，缺乏全生命周期层面的风险控制机制。
### 方法关键点
- 每次Agent迭代更新后、上线前，使用全新生成的原假设（H0）为真的模拟数据集开展验证
- 阈值设计：设定目标I类错误率α、终身风险δ，计算验证阈值α'=(α-δ)/(1-δ)，仅当更新版本在所有测试场景下I类错误率的上置信界≤α'时允许上线
- 错误预算采用级数拆分，无论迭代多少次，终身上线不合规版本的概率不超过预设δ
- 成本优化：对分析路径固定的Agent，直接验证所有路径的最坏情况I类错误，无需重复调用LLM，大幅降低验证算力成本
### 关键实验
覆盖两类AI分析师场景：生物等效性分析Agent、电商产品A/B测试决策Agent，对比无验证、静态基准测试、改进测试、Learn then Test四个基线：
- 无验证时两类场景的I类错误率最高达0.098、0.183，使用本方法后最高仅为0.045、0.044，同时分别保留了最优有效更新82%、96%的统计效力
- 本方法在690个未见过的离网测试场景中，I类错误率超过0.05的占比仅3.5%，鲁棒性显著优于基线
### 核心结论
AI Agent迭代的风险不会随迭代次数消失，只有每次更新前用全新的、覆盖边界场景的H0模拟数据验证，才能终身保障决策的统计严谨性。
