---
title: 'SalesLoop: Reinforcement Learning from Performance Feedback for Sales Lead
  Ranking'
title_zh: SalesLoop：基于业绩反馈强化学习的销售线索排序框架
authors:
- Chenyu Zhang
affiliations:
- Li Auto Inc.
arxiv_id: '2607.20655'
url: https://arxiv.org/abs/2607.20655
pdf_url: https://arxiv.org/pdf/2607.20655
published: '2026-07-22'
collected: '2026-07-24'
category: RecSys
direction: 线索排序 · 强化学习闭环优化
tags:
- LeadRanking
- ReinforcementLearning
- GRPO
- ClosedLoopOptimization
- LLM4CRM
one_liner: 适配GRPO构建判别式排序闭环框架，基于真实业务反馈迭代线索排序模型，线上转化提升4.7%-8.7%
practical_value: '- 可复用「对数位置衰减+转化速度加权」的业绩感知奖励设计，解决离线指标和线上业务目标不匹配的问题，适用于长转化周期的高价值商品/线索排序场景

  - Discriminative GRPO的设计思路可迁移：把生成式GRPO的组内相对优势思想用到判别式排序任务上，用batch内标准化的reward构造listwise损失，优化Top-K排序效果

  - 长周期转化场景的闭环迭代范式可参考：用月度迭代+上一版本参数warm start的方式，在避免灾难性遗忘的同时适配时序分布漂移，平衡模型稳定性和更新效率

  - 高价值排序场景可复用「listwise损失+点wise BCE正则」的组合目标，既保证Top-K排序质量，又避免单目标优化带来的校准漂移问题'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业界CRM线索排序长期存在离线指标优秀但线上业务表现不达预期的痛点，核心来自三个不可忽视的gap：一是离线评价指标（如AUC）与线上业务目标不匹配，历史转化标签混杂了销售人力投入的混淆变量，模型易学错信号；二是点wise训练目标与业务需要的listwise Top-K排序效果不匹配，点wise精度再高，高转化线索没进入运营承接窗口也无法产生价值；三是时序分布漂移，市场、用户行为、营销策略持续变化，静态模型上线后效果会持续衰减。
### 方法关键点
- 构建「部署→观测→奖励→更新」的闭环迭代框架，每月基于真实转化反馈更新模型，主动适配时序分布漂移
- 设计业绩感知奖励：转化标签 × 对数位置衰减系数（排名越靠前权重越高）× 转化速度系数（转化越快权重越高），直接对齐业务价值，解决离线线上指标 mismatch
- 提出Discriminative GRPO：将生成式GRPO的组内相对优势思想适配到判别式排序任务，以batch为组做reward标准化得到相对优势，用KL散度对齐模型得分分布和优势分布，直接优化listwise排序效果
- 训练目标组合listwise损失和点wise BCE正则，避免校准漂移；迭代时用上一版本参数warm start，用低学习率更新避免遗忘历史知识
### 关键结果
离线测试比最优静态基线NDCG@K提升7.9%、P@K提升15.8%；160天线上A/B测试覆盖16.5M线索、280名销售，两个省级市场累计转化分别提升4.7%（p=0.047）、8.7%（p=0.002），效果随迭代时间持续累积；排序模型Top-10%召回达44.1%，识别出的销售漏判高意向线索转化率是人工基线的2.3倍。
> 最值得记住的结论：长转化周期的高价值排序场景，不要死磕离线指标，基于真实业务反馈的闭环迭代能带来持续的线上业务增益。
