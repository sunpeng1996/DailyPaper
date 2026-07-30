---
title: 'Actions Have Consequences: Detecting Outcome Performativity using Intervention
  Testing'
title_zh: 基于干预测试的Outcome Performativity（结果执行性）检测方法
authors:
- Brandon Gower-Winter
- Georg Krempl
affiliations:
- Utrecht University
arxiv_id: '2607.26908'
url: https://arxiv.org/abs/2607.26908
pdf_url: https://arxiv.org/pdf/2607.26908
published: '2026-07-29'
collected: '2026-07-30'
category: Eval
direction: 推荐系统因果效应评估方法
tags:
- Causal Inference
- A-B Testing
- Performativity Detection
- Sample Complexity
- Recommender Systems
one_liner: 提出OPAB干预检测框架，可检测ML预测对结果的因果影响并给出样本复杂度边界
practical_value: '- 电商推荐/广告场景可直接复用OPAB框架，通过A/B分流不同预测策略，检测推荐结果是否反向影响用户行为（如推低价品是否拉低后续付费意愿），辅助长期价值建模

  - 可复用论文推导的样本复杂度边界，在高客单价品类、合规敏感类等实验成本高的场景，提前估算最小实验流量，降低试错成本

  - 针对无法开展全量干预的场景，可参考不可区分区域分析，预判当前样本量是否足够支撑检测结论置信度，避免错误归因'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有ML系统普遍假设预测不会干预待预测的真实结果，但推荐、信贷、医疗等场景广泛存在「预测反向因果影响结果」的Outcome Performativity现象，缺乏低成本、标准化的检测方案。
### 方法关键点
提出OPAB（Outcome Performativity A/B Detection）检测框架，通过对比不同预测策略（干预组）的结果分布差异显著性，判断是否存在执行性；推导多假设场景下的样本复杂度边界，明确检测所需最小样本量。
### 关键结果
在Open Bandits数据集验证OPAB可有效检测执行性；同时明确存在不可区分区域，即当干预样本量低于推导的阈值时，无法得到置信的检测结论。
