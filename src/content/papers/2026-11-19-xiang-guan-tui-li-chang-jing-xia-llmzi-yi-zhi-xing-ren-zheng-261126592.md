---
title: 'Realized versus Population Reliability: Anytime-Valid Self-Consistency Certification
  under Correlated Reasoning'
title_zh: 相关推理场景下LLM自一致性认证的两类可靠性区分与修正方案
authors:
- Terence D. Agbeyegbe
- Toneukarin G. Agbeyegbe
affiliations:
- CUNY Hunter College and Graduate Center
- Rutgers University
arxiv_id: '2611.26592'
url: https://arxiv.org/abs/2611.26592
pdf_url: https://arxiv.org/pdf/2611.26592
published: '2026-11-19'
collected: '2026-11-20'
category: Reasoning
direction: LLM推理 · 可靠性认证
tags:
- Self-Consistency
- Anytime-Valid Inference
- LLM Reasoning
- Reliability Certification
- Hypothesis Testing
one_liner: 揭示LLM自一致性认证的两类可靠性边界，提出总体可靠性修正的跨样本e-process方案
practical_value: '- 做LLM Agent/生成式推荐的推理稳定性校验时，单prompt多rollout的自一致性结果仅代表该次采样下的推理可靠性，不能直接推广到全任务/全query集的效果评估，避免高估系统整体准确率

  - 评估生成式推荐/Agent回答的全量可靠性时，优先采用1个rollout per prompt的采样策略，相同总调用预算下得到的总体效果估计方差最小；仅当prompt
  prefill成本远高于rollout成本时，再适当增加单prompt采样数

  - 做LLM相关AB测试或效果验收时，若存在推理路径共享、prompt难度异质性等带来的相关性，直接复用独立采样下的显著性检验阈值会导致过认证，需改用跨prompt的统计量构造检验过程'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM自一致性的任意有效认证均假设多rollout采样条件独立，但实际场景中共享推理前缀、prompt难度异质性会导致采样结果正相关，原有方法的错误控制假设不成立，易出现过认证，无法区分单prompt单次推理与全任务整体的可靠性。
### 方法关键点
- 引入聚类数据的随机效应/组内相关模型建模采样相关性，将原单一零假设拆分为两类：已实现零假设（当前prompt采样推理下的候选答案占优）、总体零假设（模型在全任务上的候选答案平均占优）
- 原有betting e-process仅对已实现零假设保持任意有效性，用作总体零假设检验时渐近错误率至少为π=P(µ(Z)>0)，不受预设显著性水平ϵ限制
- 单prompt的有效样本量上限为1/ρ，仅增加单prompt采样数无法提升总体可靠性估计的精度，也无法恢复总体零假设的检验有效性
- 提出跨prompt的e-process构造实现总体零假设的任意有效控制，纯rollout预算下最优采样策略为1个rollout per prompt，仅当存在固定prompt prefill成本时再增加单prompt采样数
### 关键实验
- 仿真验证：单单元证书对总体零假设的过认证率趋近于π，跨单元方案可将错误率稳定控制在ϵ=0.05以下
- 实测Claude Haiku 4.5：GSM8K任务ρ=0.435，模型自一致性极强（θ=0.96），两类可靠性差距不显著；AIME任务ρ=0.48，总体平均margin θ=-0.15<0，原有单prompt证书过认证率达24%远高于ϵ=0.05，跨prompt方案过认证率为0
### 核心结论
自一致性认证的结果仅能直接代表当前prompt的单次推理可靠性，若要推广到全任务级别的可靠性声明，必须基于独立prompt样本构造统计检验，而非单纯增加单prompt采样数
