---
title: 'ParEvalLayer: When Partial LLM-Agent Evaluations Support a Decision'
title_zh: ParEvalLayer：基于部分观测的LLM Agent评估决策框架
authors:
- Wei-Jung Huang
- Bonan Shen
affiliations:
- Independent Researcher, United States
arxiv_id: '2608.02444'
url: https://arxiv.org/abs/2608.02444
pdf_url: https://arxiv.org/pdf/2608.02444
published: '2026-08-03'
collected: '2026-08-04'
category: Eval
direction: Agent评测 · 早期停止决策框架
tags:
- LLM Agent
- Evaluation
- Early Stopping
- Benchmarking
- Statistical Validation
one_liner: 提出轻量决策层，可在观测15%-25%评测任务时输出可靠的两Agent系统对比结论
practical_value: '- 自研Agent导购、生成式推荐等策略效果对比时，可复用ParEvalLayer的分层判断逻辑：先按场景、商品类目、用户价值分层做覆盖校验，再做bootstrap显著性检验，无需跑完所有测试case即可提前得出可靠结论，降低评测成本

  - 电商大促前多版推荐/广告策略的小流量AB测可借鉴该框架的提前终止逻辑：预设效果提升阈值、人群/场景覆盖要求、错误容忍度，满足条件即可提前全量上线新策略，缩短迭代周期

  - 发布内部策略评测结论时，不要仅披露部分观测的平均得分，必须同步说明决策阈值、覆盖情况、未决case占比，避免因采样偏差导致错误的策略上线决策'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
LLM Agent全量Benchmark评测成本极高，需消耗大量API预算、计算资源与时间，业界往往基于部分观测任务的得分提前下结论，但早期采样易遗漏关键场景、低成本任务优先运行会扭曲样本分布，仅靠部分得分无法保证结论和全量评测一致，亟需一套具备统计保障、可解释的部分评估决策机制。
### 方法关键点
- 输入为两个待对比Agent系统的配对任务 outcomes，提前预设对比策略：包含效果提升阈值、任务分层规则（如按场景、难度、领域分组）、决策错误容忍度、未决case上限、资源限制。
- 决策逻辑分层执行：首先校验已观测任务是否满足分层覆盖要求（每个分组按占比分配最低样本量，避免采样偏差），未满足则继续评测；其次对已观测配对差值做bootstrap重采样，计算得分超过阈值的尾概率；若还有剩余预算则继续评测，预算耗尽时，尾概率低于预设cutoff则输出promote（新系统更优）/reject（新系统不优），否则输出abstain（证据不足）。
- 采用全量记录回灌的验证方式：基于已完成的公开Benchmark全量数据，模拟不同观测比例下的决策结果，和全量结论对比校验准确率。
### 关键实验
在SWE-bench、AppWorld、OSWorld-Verified、tau-bench等6个公开Agent Benchmark上验证，对比无分层校验、强制决策等baseline。核心结果：在0pp提升阈值下，AppWorld仅需15%任务量、OSWorld-Verified需20%、tau-bench需25%即可输出和全量评测一致的结论，决策错误率<5%，未决case占比<25%；SWE-bench等任务难度差异极大的Benchmark则需要90%以上任务量才能得到可靠结论。
### 核心结论
部分Agent评测应该输出决策而不是仅输出得分，任何脱离决策规则、分层覆盖要求、未决case占比的部分评测结论都是不可靠的。
