---
title: 'The Price of Correlated Tests: How Strict Should a Model Release Gate Be?'
title_zh: 关联测试的代价：模型发布门槛应该设多严？
authors:
- Marco Pollanen
affiliations:
- Department of Mathematics & Statistics, Trent University
arxiv_id: '2610.00993'
url: https://arxiv.org/abs/2610.00993
pdf_url: https://arxiv.org/pdf/2610.00993
published: '2026-10-01'
collected: '2026-10-04'
category: Eval
direction: 机器学习模型上线评估 · 发布门槛优化
tags:
- model_release
- correlated_tests
- ML_testing
- confidence_bounds
- deployment_evaluation
one_liner: 量化测试相关性对模型发布门槛的影响，给出最优门槛计算与基于标注数据的验证流程
practical_value: '- 推荐/广告/Agent模型上线前的多维度测试无需强制全量通过，可根据业务可靠性目标设置最低测试通过数，在达标前提下保留更多优质模型

  - 上线前先计算测试用例间的隐相关性，高相关测试会大幅抬升达标所需的测试量，可优先裁剪高相关低价值测试用例，降低测试成本

  - 复用文中的二项式边界验证流程，仅需少量标注样本即可验证发布门槛的有效性，无需全量标注测试集，大幅降低上线前的验证成本'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有模型发布流程普遍要求全量自动化测试通过，易误拒大量实际服务效果优异的模型，也无法量化通过模型的实际可信度，测试间的相关性会进一步放大上述缺陷。
### 方法关键点
1. 将发布门槛定义为优化问题：在满足预设可靠性目标的约束下，最大化优质模型的保留率
2. 基于双类隐因子模型显式量化两类错误成本，将复杂计算简化为一维积分
3. 提出基于精确二项式边界的验证流程，仅需标注数据即可完成候选门槛的有效性认证
### 关键结果数字
同配置下实现99%可靠性目标，独立测试仅需8个，隐相关0.3时需74个，隐相关0.5时需5182个，此时优质模型保留率不足10%；全过门槛下测试集规模越大，优质模型保留率越趋近于0。
