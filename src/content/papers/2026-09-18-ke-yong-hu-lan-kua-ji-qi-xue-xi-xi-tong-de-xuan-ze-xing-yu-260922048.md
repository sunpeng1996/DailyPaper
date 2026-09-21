---
title: 'Available Guardrails: Certifying Selective Prediction across ML Systems'
title_zh: 《可用护栏：跨机器学习系统的选择性预测认证方法》
authors:
- Parivesh Priye
- Yufeng Wang
- Haibin Ling
- Michael Chaykowsky
affiliations:
- Rivian and Volkswagen Group Technologies
- Stony Brook University
- Westlake University
arxiv_id: '2609.22048'
url: https://arxiv.org/abs/2609.22048
pdf_url: https://arxiv.org/pdf/2609.22048
published: '2026-09-18'
collected: '2026-09-21'
category: Eval
direction: ML系统安全 · 选择性预测认证
tags:
- Selective Prediction
- Safety Guardrail
- Model Certification
- Finite Sample Estimation
- Dynamic Programming
one_liner: 提出选择性预测安全门可用性计算框架，量化安全-粒度-流量权衡，提升有限数据下认证覆盖率
practical_value: '- 电商推荐/广告的置信度过滤模块可直接复用该框架的精确二项式反演方法，做不同人群/类目维度的预测可靠性认证，确保服务精度达标

  - Agent工具调用的安全门场景可借鉴报告分区动态规划算法，在固定精度要求下平衡服务粒度与流量覆盖率，避免小流量单元无有效认证的问题

  - 有限校准数据场景下可直接采用「规划集生成候选分区+验证集选优」的两阶段策略，相比原生平衡方法可提升6%左右的有效服务覆盖率'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有ML系统（含LLM工具调用、推荐、内容审核等）的选择性预测安全门，需针对不同报告单元（人群、类目、工具等）实现目标精度的可靠性认证，但有限校准数据下大量小粒度单元无法得到有效认证，传统方法覆盖率极低。
### 方法关键点
1. 基于精确二项式反演实现安全门可用性可计算，通过固定组序下的动态规划做报告分区选择，显式建模安全、粒度、服务流量的权衡关系；
2. 采用两阶段分区策略（规划集生成候选分区、验证集选优）+ 家族错误预算跨单元重分配，缓解有限数据的性能损失。
### 关键结果
对比基线支持平衡方法，真值感知规划器平均覆盖率提升0.157，朴素估算器仅提升0.005；两阶段策略平均覆盖率提升0.06，在3个意图路由数据集60组模型效果中59组一致正向。
