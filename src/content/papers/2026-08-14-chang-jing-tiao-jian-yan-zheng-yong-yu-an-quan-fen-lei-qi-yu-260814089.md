---
title: 'Regime-Conditional Verification: Correctness Estimation for Adapting and Monitoring
  Safety Classifiers'
title_zh: 场景条件验证：用于安全分类器适配与监控的正确性评估方法
authors:
- Thiago Sandoval
- Ufuk Topcu
affiliations:
- The University of Texas at Austin
arxiv_id: '2608.14089'
url: https://arxiv.org/abs/2608.14089
pdf_url: https://arxiv.org/pdf/2608.14089
published: '2026-08-14'
collected: '2026-08-17'
category: LLM
direction: LLM安全分类器适配与漂移检测
tags:
- Safety-Classifier
- Distribution-Shift
- Prediction-Correction
- Model-Monitoring
- Lightweight-Wrapper
one_liner: 轻量无训练修改的安全分类器包装层，同时实现预测纠错与无标签分布漂移检测
practical_value: '- 电商/广告场景的内容安全分类器可直接复用RCV包装层逻辑，无需重训原有模型即可对齐平台安全策略，降低迭代成本

  - 可将基于模型内部表征的正确性概率估计作为无标签漂移信号，用于搜索推荐系统的召回/排序模型效果监控，减少标注成本

  - 维护优先更新轻量校正层、仅必要时重训底座模型的迭代范式，可复用在大流量LLM Agent服务的运维链路中，降低算力开销'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
LLM部署配套的安全分类器存在两类核心问题：1）训练时学习的策略与部署方预期策略不匹配；2）流量分布漂移/对抗攻击导致性能持续下降，现有重训优化方案成本极高。

### 方法关键点
轻量包装层RCV无需重训原有安全分类器：1）从分类器内部表征输出单条预测与部署方策略不一致的概率，选择性修正高概率错误的预测；2）复用正确性估计信号作为无标签分布漂移检测指标，搭建维护闭环：仅当轻量校正层无法修复漂移时才触发底座分类器微调。

### 关键结果数字
- 覆盖3款开源安全分类器+2个基准数据集，所有组合下均提升策略对齐度，最多可召回81%之前漏判的不安全内容
- 10类训练时未见过的攻击场景下100%检测到攻击；绝大多数漂移场景仅更新校正层即可修复，无需重训底座模型
