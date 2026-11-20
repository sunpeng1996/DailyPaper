---
title: Cost-Aware Agentic Feature Optimization System for Fleet-Scale Ranking Models
title_zh: 面向大规模集群排序模型的成本感知智能特征优化系统
authors:
- Chang Yang
- Yao Xuan
- Wendan Yan
- Nhat Le
- Jiang Liu
- Longhao Jin
- Zhen Peggy Yao
- Alireza Vahdatpour
- Djordje Gligorijevic
affiliations:
- Meta, Inc.
arxiv_id: '2611.26531'
url: https://arxiv.org/abs/2611.26531
pdf_url: https://arxiv.org/pdf/2611.26531
published: '2026-11-19'
collected: '2026-11-20'
category: RecSys
direction: 排序模型优化 · LLM Agent自动特征工程
tags:
- FeatureSelection
- LLMAgent
- AdsRanking
- CostOptimization
- RankingModel
one_liner: 基于LLM Agent实现集群级排序模型特征自动优化，兼顾效果与服务、特征流水线双成本
practical_value: '- 交叉特征生成可复用「LLM粗筛召回 + 特征重要性重排」的两级策略，避免全量遍历组合爆炸，LLM可基于全集群特征效果数据持续微调，优化召回准确率

  - 多任务排序模型的特征重要性融合可采用帕累托最优方案，无需人工调优各任务权重，还能保留仅对单任务高价值的特征

  - 多模型共享特征池的场景可复用pipeline trimming机制，优先选择已上线特征，零额外流水线成本的前提下完成特征迭代，文中方案可降本2.3%无明显效果损失

  - 算力有限的模型超参/特征搜索可采用LLM Agent驱动的异步搜索框架，仅需10~25次trial即可拿到显著收益，大幅降低调优成本'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
大互联网平台的排序模型集群需要从数万级共享特征池选特征，传统人工特征工程效率低，现有自动特征方案仅针对单模型优化，未同时兼顾单模型服务成本（QPS、内存、延迟）与集群共享的特征流水线成本，也无法跨模型复用特征优化的历史经验。
### 方法关键点
1. LLM驱动特征生成：跨模型共享微调的召回LLM，基于特征的静态语义、历史效果信号从千万级交叉特征候选中召回高潜子集，解决组合爆炸问题，优化过的模型越多，召回准确率越高；
2. 特征重要性融合：融合permutation importance、Shapley、Kernel SHAP、高价值流量切片专属重要性的多个排序结果，多任务模型采用帕累托最优选择特征，无需人工设置任务权重；
3. 成本约束Agent搜索：LLM Researcher Agent通过observe-reason-act异步搜索特征组合，约束单模型FLOPs、QPS、内存上限，新增pipeline trimming步骤，优先选用集群已上线特征，不额外增加共享流水线成本。
### 关键结果
在Meta 7个生产广告排序模型上，单模型预算内平均NE降低0.31%；pipeline trimming步骤平均降低特征流水线成本2.3%，效果损失在测量噪声范围内；优化后的模型上线后A/B测试核心线上指标提升0.20%。
> 最值得记住的一句话：集群级特征优化的核心收益不是单纯加特征，而是在成本约束下重新平衡不同类型特征的配比，ROI远高于单维度特征扩量。
