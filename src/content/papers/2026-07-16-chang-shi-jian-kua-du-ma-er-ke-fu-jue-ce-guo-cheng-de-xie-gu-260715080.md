---
title: Evaluating covariate balance for long time horizon Markov decision processes
title_zh: 长时间跨度马尔可夫决策过程的协变量平衡评估
authors:
- Joshua Spear
- Rebecca Pope
- Neil J Sebire
affiliations:
- UCL GOS Institute of Child Health
- NIHR GOSH UCL BRC
arxiv_id: '2607.15080'
url: https://arxiv.org/abs/2607.15080
pdf_url: https://arxiv.org/pdf/2607.15080
published: '2026-07-16'
collected: '2026-07-19'
category: Eval
direction: 离线RL 决策稳健性评估
tags:
- offline-RL
- covariate-balance
- off-policy-evaluation
- MDP
- causal-inference
one_liner: 针对离线RL治疗推荐场景验证协变量平衡诊断能力，指出现有相关研究统计稳健性存在缺陷
practical_value: '- 做推荐系统序贯决策、Agent策略的离线训练时，可引入协变量平衡检验排查隐藏混淆变量、模型误配问题，降低上线后策略偏倚

  - 离线RL策略上线前不能仅依赖传统OPE指标，需额外补充鲁棒性校验流程，规避统计稳健性不足带来的业务风险

  - 长跨度序贯决策场景（如用户生命周期运营、长期推荐收益优化），需重点校验MDP假设合理性，搭配因果诊断工具提升策略可信度'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
离线RL广泛应用于医疗、工业等仅能做全离线分析的序贯决策场景，现有离线RL研究极少引入因果推断领域成熟的稳健性诊断流程，长周期MDP场景下隐藏混淆、模型误配风险缺乏有效校验。
### 方法关键点
针对离线RL生成最优治疗推荐的任务，引入协变量平衡诊断方案，检测研究中是否存在未观测混淆变量、模型设定错误问题，验证现有协变量平衡指标对这类场景的适配性。
### 关键结果
两种结论必居其一：要么现有离线RL治疗推荐研究存在高偏倚风险，要么现有协变量平衡指标不足以评估这类研究的有效性；所有现有相关离线RL研究均无法被证明具备统计稳健性。
