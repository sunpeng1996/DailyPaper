---
title: Initialization Improves LLM-Driven Discovery
title_zh: 初始化优化可提升大模型驱动的自主发现效果
authors:
- Mansi Sakarvadia
- Marco Ciccone
- Colin Raffel
affiliations:
- University of Chicago
- Vector Institute
- University of Toronto
arxiv_id: '2610.00707'
url: https://arxiv.org/abs/2610.00707
pdf_url: https://arxiv.org/pdf/2610.00707
published: '2026-09-29'
collected: '2026-10-13'
category: LLM
direction: 大模型自主发现 · 推理迭代优化
tags:
- LLM-driven Discovery
- Mode Collapse
- Initialization
- Iterative Optimization
- Inference Optimization
one_liner: 针对LLM自主发现的模态坍塌问题，提出初始并行探索的通用初始化方案，跨任务实现稳定增益
practical_value: '- 做Agent迭代优化类任务（自动prompt调优、商品文案迭代、推荐策略搜索）时，先执行一轮并行探索生成初始池，再进入迭代优化环节，可大幅降低模态坍塌概率，提升最终效果

  - 迭代类LLM业务任务无需过度投入复杂的多样性干预逻辑，优先提升初始探索池的质量，成本更低且收益更稳定

  - 可复用「早期探索结果性能可预测最终任务效果」的结论，提前终止表现差的迭代分支，显著节省推理成本'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
LLM驱动的迭代式自主发现任务（算法/药物/定理发现等）普遍存在模态坍塌问题，迭代过程中生成多样性骤降，最终成功率低；现有多样性干预策略增益不稳定，不同harness设计的效果差异大，无通用优化方案。
### 方法关键点
构建包含12种harness的Modular测试套件，覆盖5类异质发现任务；验证迭代早期探索结果的性能与最终成功率强相关，模态坍塌是核心失败模式；通用初始化干预策略为：正式迭代优化前先执行一轮并行探索，筛选最优早期结果作为后续迭代的初始值。
### 关键结果
在全部12种harness、5类测试任务上均取得一致正向增益，无负向收益场景，相比现有多样性优化方案的效果稳定性大幅提升，可直接适配各类LLM驱动的迭代优化场景。
