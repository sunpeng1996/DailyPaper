---
title: Attack Policy Selection can Mislead Monitor Evaluators
title_zh: 攻击策略选择会误导AI安全监测器的评估结果
authors:
- Charlie Griffin
- Oliver Makins
- Asa Cooper Stickland
- Alessandro Abate
- Yarin Gal
- Abby D'Cruz
- Xander Davies
arxiv_id: '2611.34934'
url: https://arxiv.org/abs/2611.34934
pdf_url: https://arxiv.org/pdf/2611.34934
published: '2026-11-25'
collected: '2026-11-26'
category: Eval
direction: AI安全监测器鲁棒性评估方法
tags:
- Evaluation
- AI Safety
- Attack Policy
- Monitor Robustness
- False Negative Rate
one_liner: 通过OpenAI监测器案例验证攻击策略选择会大幅改变安全监测器假阴性率评估结论
practical_value: '- 做电商Agent、推荐/搜索合规审核系统的安全监测评估时，需覆盖多种攻击样本生成方法（优化prompt、RL、文本编辑等）及不同优化梯度，避免高估系统拦截能力

  - 评估任何业务系统的漏判率时，需先验证负样本（违规/攻击样本）的代表性，补充样本与真实线上坏案例的一致性论证，不可基于随意构造的样本输出评估结论

  - 系统上线前的鲁棒性压测必须使用当前能实现的最强攻击策略的最优优化版本，不能仅用基础攻击方案的结果作为鲁棒性达标的依据'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
AI安全监测器的漏判率（FNR）评估依赖攻击策略生成的危险行为代理样本，过往评估未系统考量攻击策略选择对结果的影响，极易得出偏离真实性能的结论。
### 方法关键点
以OpenAI已下线的生产级监测器为案例，固定部署场景与测试任务，仅调整攻击策略的生成方法（基础prompt、优化prompt、RL、文本编辑）与单方法内的优化程度，对比不同配置下的监测器FNR。
### 关键结果数字
单RL方法不同优化程度下FNR跨度为0.5%~20.8%；各方法最优优化水平下FNR跨度为6.4%~23.0%；所有仅在代理监测器上训练的攻击策略，均可直接迁移到未见过的GPT-5.4目标监测器。仅用基础攻击的窄范围评估会严重高估监测器鲁棒性。
