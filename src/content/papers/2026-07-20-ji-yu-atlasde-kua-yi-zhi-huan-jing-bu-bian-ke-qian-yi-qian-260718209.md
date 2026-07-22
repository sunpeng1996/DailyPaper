---
title: Unveiling Invariant and Transferable Latent Factors Across Heterogeneous Environments
  via ATLAS
title_zh: 基于ATLAS的跨异质环境不变可迁移潜因子挖掘方法
authors:
- Yihong Gu
- Katherine Liao
- Tianxi Cai
affiliations:
- Harvard University
arxiv_id: '2607.18209'
url: https://arxiv.org/abs/2607.18209
pdf_url: https://arxiv.org/pdf/2607.18209
published: '2026-07-20'
collected: '2026-07-22'
category: Other
direction: 跨域迁移 · 潜因子解耦与表征对齐
tags:
- Transfer Learning
- Invariant Representation
- Factor Model
- Heterogeneous Environment
- OOD Prediction
one_liner: 提出ATLAS框架，分离异质环境下的不变与异质潜因子，提升跨域预测的可迁移性与鲁棒性
practical_value: '- 跨域推荐场景可借鉴ATLAS的不变因子分离思路，从不同站点、人群、运营场景的行为数据中提取全局通用的用户/物品表征，降低跨域冷启动成本

  - 多环境部署预测模型时，可复用「辅助标签监督提取可迁移异质因子」的trick：有少量目标域标签时大幅提升跨域预测效果，无标签时切换为仅用不变因子的鲁棒预测模式

  - 论文给出的潜因子恢复非渐进误差界，可作为跨域表征对齐质量的评估参考，用于校验表征的迁移可靠性'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：跨异质环境部署预测模型时，协变量分布偏移、特征结构异质性会导致模型泛化能力大幅下降，现有迁移方法难以同时满足表征可解释性、跨域预测鲁棒性的需求，缺乏通用的潜因子解耦与迁移框架。
**方法关键点**：1. 基于不变性原理，在最小结构假设下实现两类潜因子的解耦：不变因子（跨环境共享载荷）、异质因子（环境特异载荷）；2. 提出ATLAS统一流程：先分离对齐的不变因子与未对齐的异质因子，再利用部分环境的辅助标签从异质因子中额外提取预测相关的可迁移因子；3. 自适应支持两种推理模式：新环境有辅助标签时调用全潜信号预测，无标签时切换为仅用不变因子的鲁棒预测模式。
**关键结果**：下游潜因子回归任务达到近Oracle性能，给出了不变/异质因子恢复、响应不变因子识别的严格非渐进误差界，从理论上保证了迁移稳定性。
