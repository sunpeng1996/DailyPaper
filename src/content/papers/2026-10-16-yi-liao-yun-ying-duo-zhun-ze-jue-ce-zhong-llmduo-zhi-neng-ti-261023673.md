---
title: On the possibilities and limitations of LLM-based multi-agent systems for multi-criteria
  decision-making in healthcare operations management
title_zh: 医疗运营多准则决策中LLM多智能体系统的可行性与局限性
authors:
- Marco Boresta
- Tommaso Giovannelli
- Sepehr Namirad
- Giulia Riccardi
affiliations:
- University of Cincinnati
- Istituto di Analisi dei Sistemi ed Informatica (IASI), CNR, Rome
- Sapienza University of Rome
arxiv_id: '2610.23673'
url: https://arxiv.org/abs/2610.23673
pdf_url: https://arxiv.org/pdf/2610.23673
published: '2026-10-16'
collected: '2026-10-19'
category: MultiAgent
direction: 多智能体决策 · 偏好可靠性评估
tags:
- MultiAgent
- PreferenceElicitation
- RobustOptimization
- DecisionMaking
- LLM
one_liner: 提出LLM-PADA框架审计多智能体生成偏好的可靠性，结合鲁棒优化量化偏好不确定性对决策的影响
practical_value: '- 多角色Agent协作定多目标权重时，不要盲目采用智能体协商收敛的结果，机械平均的聚合方式反而能完整保留不同角色的偏好差异，可直接复用在电商推荐/广告排序兼顾体验、营收、成本的多目标调权场景

  - LLM的两两选择结果强烈依赖选项的展示顺序，做偏好采集、A/B测试评估类Agent系统时，必须对选项顺序做随机化校正，避免结果偏差

  - 多目标优化的权重输入存在不确定性时，用鲁棒加权和优化替代固定平均权重，可大幅降低最坏场景下的决策损失，可落地到推荐排序调权、营销资源分配等场景'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
医疗运营多准则决策需要权衡患者等待时间、医护 workload、运营成本等多个目标，人工采集不同利益相关方的偏好成本高、难以反复迭代；现有方案用LLM多智能体模拟利益相关方生成偏好权重，但缺乏可靠性校验机制，偏好不确定性对最终决策的影响也未被量化。
### 方法关键点
- 提出LLM-PADA四步框架：偏好采集→可靠性校验→权重不确定集构建→鲁棒决策分析，同时支持显式偏好打分、隐式偏好推断两种采集模式
- 显式偏好聚合对比三类协议：仅交换分数的数值协商、带论据交换的论证协商、无额外LLM调用的机械平均
- 隐式偏好推断引入展示顺序校正项，对比仅用顺序的基线模型评估偏好预测效果
- 基于偏好分布构建百分位箱型不确定集，对比平均权重优化、鲁棒加权和优化的决策差异
### 关键结果
基于本地部署的Qwen3.5-4B开展实验，覆盖门诊排班、急诊室配置两个场景：
1. 显式偏好实验中，LLM协商协议会让初始的角色差异化偏好消失67%以上，机械平均则能100%保留角色差异；16组对比中有10组鲁棒优化和平均权重优化选出的排班方案不同
2. 隐式偏好实验中，仅2/6的角色-模型组合能通过属性特征提升超过展示顺序基线的预测效果
### 核心结论
用LLM多智能体生成多目标优化的权重输入前必须做可靠性审计，盲目信任协商收敛的偏好会导致决策偏离各利益相关方的真实诉求。
