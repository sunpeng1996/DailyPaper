---
title: 'Rule of Thumb: Explaining Artificial Intelligence Systems using Partial Information'
title_zh: 《经验法则：基于局部信息的人工智能系统解释方法》
authors:
- Kaivalya Rawal
- Daria Onitiu
- Brent Mittelstadt
- Sandra Wachter
- Chris Russell
affiliations:
- University of Oxford
- Hasso Plattner Institute
- Weizenbaum Institute
arxiv_id: '2608.10766'
url: https://arxiv.org/abs/2608.10766
pdf_url: https://arxiv.org/pdf/2608.10766
published: '2026-08-11'
collected: '2026-08-12'
category: Other
direction: 黑盒AI可解释性 · 模型无关解释方案
tags:
- XAI
- Black-box Model
- Model-agnostic
- LLM Interpretability
- Feature Importance
one_liner: 提出模型无关的RoT黑盒AI解释方法，仅用局部特征定位决策关键项，速度远优于同类方案
practical_value: '- 可复用RoT的黑盒特征重要性计算逻辑，对线上部署的推荐/广告排序黑盒模型做无侵入式决策归因，无需拿到模型权重即可定位bad
  case核心影响特征

  - 针对电商场景大模型零-shot分类任务（如商品类目打标、用户评论情感识别），用RoT快速校验决策逻辑合理性，降低标注校验成本

  - RoT符合AI监管对可解释性的要求，可直接集成到推荐/广告系统的合规审计链路，满足监管披露要求'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有XAI方法大多需要访问模型内部权重、梯度，无法适配黑盒部署的LLM、第三方推荐/广告系统等场景；大模型零-shot能力的标注校验成本极高，同时AI监管对决策可解释性的要求也存在落地缺口。
### 方法关键点
RoT（Rule of Thumb）解释框架仅依赖单样本的局部特征输入输出对，无需模型访问权限，通过优化目标定位对决策贡献最高的核心特征，完全模型无关，自带适配从业者的可视化界面。
### 关键结果
速度比同类黑盒解释方案快数倍，适配LLM零-shot分类、无权限黑盒AI审计、科学发现三大场景，完全满足主流AI监管的可解释性要求，配套代码已开源。
