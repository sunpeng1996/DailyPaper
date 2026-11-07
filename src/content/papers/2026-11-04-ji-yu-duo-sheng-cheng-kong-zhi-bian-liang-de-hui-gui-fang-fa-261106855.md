---
title: Regression with Many Generated Controls
title_zh: 基于多生成控制变量的回归方法研究
authors:
- Timothy Christensen
- Daniel Vebman
affiliations:
- Department of Economics, Yale University
arxiv_id: '2611.06855'
url: https://arxiv.org/abs/2611.06855
pdf_url: https://arxiv.org/pdf/2611.06855
published: '2026-11-04'
collected: '2026-11-07'
category: Other
direction: 计量回归 · 内生性控制
tags:
- Regression
- Endogeneity
- Causal Inference
- Generated Controls
- Proxy Variables
one_liner: 针对存在内生协变量的回归场景，给出基于多生成控制变量的无验证数据一致估计方案与实操建议
practical_value: '- 电商/广告因果效应估计（如推荐增量、广告归因）场景中，若存在不可观测混淆变量，可通过不同ML/LLM生成多套代理控制变量，无需验证数据即可得到一致无偏的效应估计

  - 无需筛选最优代理变量，只要生成的代理集合覆盖潜变量的信息足够丰富，直接全量纳入或提取公共因子作为控制，偏差显著低于单一代理方案

  - 观测性A/B测试结果校正场景中，可替代传统工具变量方法，降低对工具变量「相关性、外生性」的强假设要求'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
线性回归场景中若存在内生协变量，控制混淆所需的核心变量通常为不可观测的潜变量，仅能通过多套ML/LLM方法生成多个有偏代理作为控制，现有四类常用处理方案的估计目标、有效性边界缺乏明确推导，从业者选择无明确依据。
### 方法关键点
针对「全量代理纳入控制、代理提取因子控制、工具变量估计、非线性变体」四类主流方案，基于透明假设推导各方案的隐含估计目标，明确不同方案可还原目标参数的适用条件。
### 关键结果
只要生成的控制变量集合覆盖潜变量的信息足够丰富，无需依赖验证数据即可实现目标参数的一致估计，同时给出了不同场景下的方案选择实操建议。
