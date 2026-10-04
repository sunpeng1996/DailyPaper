---
title: 'Tolerance-Based Fairness Auditing: Violation Certification and Sensitivity
  Screening'
title_zh: 基于容忍度的公平性审计：违规认证与敏感度筛查
authors:
- Jie Tang
- Chuanlong Xie
- Lixing Zhu
affiliations:
- School of Statistics, Beijing Normal University, Zhuhai
arxiv_id: '2610.01005'
url: https://arxiv.org/abs/2610.01005
pdf_url: https://arxiv.org/pdf/2610.01005
published: '2026-10-01'
collected: '2026-10-04'
category: Eval
direction: 算法公平性评估 · 审计框架
tags:
- fairness auditing
- empirical likelihood
- algorithm fairness
- statistical testing
- evaluation
one_liner: 提出适配两类审计目标的统一容忍度算法公平性审计统计框架
practical_value: '- 电商/广告/推荐场景公平性审计可直接复用双目标框架：正式合规上报用违规认证方法控制错报率，日常巡检用敏感度筛查方法控制漏判率

  - 多子群（如不同年龄、性别、地域用户群体）同步审计时，可结合约束经验似然检验+误报率控制方案，避免子群过多导致的假阳性膨胀

  - 容忍阈值可结合业务合规要求（如相关法规、平台规则）自定义，灵活适配不同场景的公平性考核要求'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
算法大规模落地背景下算法不公问题凸显，当前公平性审计缺乏适配不同场景容忍阈值的统一量化方案，实际业务中不公平容忍度受合规、伦理、场景约束差异大，需针对不同审计目标的科学判定方法。
### 方法关键点
1. 构建双目标统一容忍度公平审计框架：违规认证优先控制虚假违规判定，适配正式合规场景；敏感度筛查优先减少漏判，适配日常预警巡检场景。
2. 违规认证场景采用带最不利点校准的约束经验似然检验，支持多子群同步审计时的误报率控制。
3. 敏感度筛查场景基于自适应边界代理原则，提出拆分/调整拆分经验似然检验，适配早预警需求。
### 关键结果
数值实验验证了两类方法在误差控制与敏感度上的差异化权衡特性，在公开COMPAS数据集上完成预测公平性审计的落地验证。
