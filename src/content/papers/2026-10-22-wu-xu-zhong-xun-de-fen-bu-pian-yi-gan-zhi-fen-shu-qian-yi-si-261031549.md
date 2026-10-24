---
title: Shift-aware score transport for privacy auditing without retraining
title_zh: 无需重训的分布偏移感知分数迁移隐私审计方法
authors:
- Yaohong Yang
- Gauri Pradhan
- Qi Chen
- Samuel Kaski
- Antti Honkela
affiliations:
- ELLIS Institute Finland
- Aalto University, Finland
- University of Helsinki, Finland
- University of Manchester, United Kingdom
arxiv_id: '2610.31549'
url: https://arxiv.org/abs/2610.31549
pdf_url: https://arxiv.org/pdf/2610.31549
published: '2026-10-22'
collected: '2026-10-24'
category: Other
direction: 机器学习隐私审计 · 无重训分布偏移适配
tags:
- Privacy-Auditing
- Membership-Inference
- Distribution-Shift
- Score-Transport
- No-Retraining
one_liner: 面向无重训权限的观测式隐私审计场景，提出分布偏移感知的分数迁移方法提升评估稳定性与下界紧致性
practical_value: '- 上线的大推荐/LLM模型做隐私审计时，若没有重训、控制训练数据的权限，可复用该方法用OOD非成员样本完成审计，无需修改原模型

  - 分布偏移下的分数迁移修正思路可迁移到推荐效果离线评估场景，解决离线测试集与线上真实分布不一致导致的评估偏差问题

  - 保守校正的设计逻辑可复用在所有需输出下界的评估任务中，如隐私风险、模型鲁棒性下界估算，避免输出过乐观的不可靠结论'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
基于成员推理攻击的隐私审计默认成员、非样本同分布，在无法插入金丝雀、控制数据组成、重训目标模型的观测式审计场景下（如已上线的大模型），可用非成员样本常存在分布偏移，导致推理分数失真，审计结果误差大。
### 方法关键点
1. 从OOD非成员样本学习数据表示与成员推理分数的映射关系，迁移到目标协变量分布，估算反事实的同分布非成员分数分布；
2. 引入保守校正模块，基于非成员数据构造的校准任务估计表示空间偏移带来的审计膨胀量，修正迁移引入的误差。
### 关键结果
在多组存在分布偏移的数据集上，相比基线方法，隐私估计稳定性大幅提升，同时保留更紧致的隐私损失下界。
