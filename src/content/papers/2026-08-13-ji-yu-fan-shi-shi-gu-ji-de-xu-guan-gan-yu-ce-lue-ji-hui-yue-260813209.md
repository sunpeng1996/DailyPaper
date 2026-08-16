---
title: Chance-constrained selection of sequential intervention strategies from counterfactual
  estimates
title_zh: 基于反事实估计的序贯干预策略机会约束选择方法
authors:
- Minkyoung Kim
- Beakcheol Jang
affiliations:
- Graduate School of Information, Yonsei University
arxiv_id: '2608.13209'
url: https://arxiv.org/abs/2608.13209
pdf_url: https://arxiv.org/pdf/2608.13209
published: '2026-08-13'
collected: '2026-08-16'
category: Other
direction: 因果决策 · 序贯干预预算约束优化
tags:
- Causal Inference
- Chance-constrained Programming
- Prescriptive Analytics
- Sequential Intervention
- Counterfactual Estimation
one_liner: 提出预测-优化框架，通过机会约束限定序贯干预成本超预算概率，预测器可灵活替换
practical_value: '- 电商用户留存运营的序贯触达（优惠券、push）场景可复用该框架，约束营销预算超支概率，替代传统均值成本管控方案，降低预算浪费风险

  - 预测-优化解耦架构可直接复用，预测模块可对接现有业务的成本/效果预估模型，无需推翻原有链路即可落地机会约束能力

  - 可通过扫描写实的容忍超支概率生成安全-效用 frontier，供运营方根据业务阶段灵活选择平衡策略，适配预算刚性/效果优先等不同需求'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
传统序贯干预决策仅约束成本均值，无法管控超预算的概率，现有尾端约束方法依赖预设模型而非观测数据推导，且仅支持单点决策，不适配多阶段资源受限场景。
### 方法关键点
1. 预测-优化两阶段解耦架构，预测模块可灵活替换，兼容任意输出收益值与成本分布的估计器；
2. 优化阶段对有限候选策略做整体机会约束打分，直接限定累积成本超预算的概率，无需跨阶段拆分成本；
3. 提供无分布的有限样本边界，扫描写实超支概率可生成安全-效用权衡 frontier。
### 关键结果
在5个跨领域测试环境（含1个真实数字健康微随机试验数据集）中，相比点估计基线方法，该框架可严格将预算超支率控制在设定阈值内，仅产生可量化的效用损失。
