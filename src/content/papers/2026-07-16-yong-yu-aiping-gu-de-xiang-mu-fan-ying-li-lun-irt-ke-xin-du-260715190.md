---
title: Can We Trust Item Response Theory for AI Evaluation?
title_zh: 《用于AI评估的项目反应理论(IRT)可信度分析》
authors:
- Han Jiang
- Sunbeom Kwon
- Jinwen Luo
- Ziang Xiao
- Susu Zhang
affiliations:
- Johns Hopkins University
- University of Illinois Urbana-Champaign
- University of California, Los Angeles
arxiv_id: '2607.15190'
url: https://arxiv.org/abs/2607.15190
pdf_url: https://arxiv.org/pdf/2607.15190
published: '2026-07-16'
collected: '2026-07-17'
category: Eval
direction: AI模型评估 · IRT可信度分析
tags:
- IRT
- LLM Evaluation
- Benchmark
- Statistical Modeling
- Estimator
one_liner: 对比4种IRT估计器在AI基准场景的表现，明确IRT用于AI评估的适用边界与可信条件
practical_value: '- 做LLM能力评估、推荐系统A/B测试人群分层/测评题目筛选时，可参考本研究的IRT适用条件，避免小样本/非正态分布场景下误用IRT得到错误结论

  - 大样本基准评估场景优先选用可扩展IRT估计器，小样本评估场景优先选用经典MML/MCMC估计器，保证参数推断可靠性

  - 用IRT做推荐系统冷启动用户/物品能力建模时，需先校验样本分布，避免能力分布多峰/偏态导致的参数估计失真'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有AI基准广泛采用原本面向人类测试设计的IRT实现模型能力估计、系统排序、高信息题目筛选、基准质量诊断，但AI基准数据存在待评估模型少、题目量极大、能力分布偏态/多峰等与人类测试场景的显著差异，IRT的可靠性未被验证。
### 方法关键点
基于6个主流LLM基准的真实题目参数与能力分布，模拟3种常用IRT模型的响应矩阵，对比边际最大似然、MCMC、变分推断、神经伪孪生估计器4种当前主流IRT估计工具，覆盖18000种模拟条件，系统评估计算可行性、可扩展性，以及模型排序、性能预测、题目特征推断的可靠性。
### 关键结果
经典IRT估计器在大规模基准场景下计算不可行，可扩展估计器在小样本/非正态分布模型集场景下的题目级推断与排序结果不可靠，明确了可信使用IRT所需的样本量与诊断指标。
