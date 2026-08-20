---
title: 'Grouping the Stochastic Machine: Precision, Not Capability, as the Frontier
  Metric for AI Systems'
title_zh: 随机机器分组评估：以精度而非能力作为AI系统前沿度量
authors:
- George Andrikopoulos
affiliations:
- Independent researcher, London, United Kingdom
arxiv_id: '2608.19140'
url: https://arxiv.org/abs/2608.19140
pdf_url: https://arxiv.org/pdf/2608.19140
published: '2026-08-19'
collected: '2026-08-20'
category: Eval
direction: 大模型评估 · 可靠性度量
tags:
- LLM Evaluation
- Reliability Metric
- Precision Measurement
- Model Benchmarking
- Stochastic Output
one_liner: 提出以重复请求下输出一致性（精度）为前沿AI核心度量，配套低成本无偏测量与问题归因框架
practical_value: '- 大模型驱动的推荐文案生成、Agent决策链路中，可复用该精度度量方法：固定temperature下重复测试相同prompt，量化输出稳定性，筛除一致性差的模型/prompt方案

  - 故障归因可参考论文框架：若输出一致但不符合业务要求，属于prompt/规则问题，可通过prompt工程/规则补丁修复；若输出离散波动大，属于模型/采样策略问题，需换模型或调整采样参数

  - 业务侧模型选型不要只看公开榜单能力得分，必须补充自定义业务确定性任务的精度测试，优先选择一致性更高的方案，降低线上bad case概率'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
当前前沿大模型benchmark普遍仅评估平均能力（中心趋势），完全忽略落地中最核心的输出稳定性问题，无法区分不同类型的故障，对业务问题归因无指导价值。

### 方法关键点
1. 提出「精度（grouping）」作为核心差异化度量，定义为相同请求、固定temperature下输出结果的集中度；
2. 测量方案低成本无偏：基于可确定性打分的固定任务集多次运行，计算单任务结果一致性，无需引入模型判分环节；
3. 可直接指导故障归因：输出一致但偏离目标属于规则/prompt问题（类似瞄偏，可通过补丁修复），输出离散波动属于模型/采样问题（类似硬件缺陷，需换模型调整采样）。

### 关键结果
实测某类任务仅新增1条规则就将精度从0/5提升至5/5，完全解决一致性偏差问题；基于规则构造的任务集无评估价值，前沿模型已内化显性规则，评估必须采用真实业务任务。
