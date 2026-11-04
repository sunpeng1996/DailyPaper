---
title: 'DualEvolve: Dual-Level Self-Evolution of Mechanism and Orchestration for Recommendation'
title_zh: DualEvolve：面向推荐系统的机制与编排双层自进化框架
authors:
- Tianqi Gao
- Chenxu Wang
- Wenxuan Yang
- Yueqi Mou
- Biao Tang
- Ming Liu
- Peng Yan
affiliations:
- Independent Researcher
- Meituan
arxiv_id: '2611.04439'
url: https://arxiv.org/abs/2611.04439
pdf_url: https://arxiv.org/pdf/2611.04439
published: '2026-11-03'
collected: '2026-11-04'
category: Agent
direction: Agent 推荐系统自进化优化
tags:
- Self-Evolution
- LLM Agent
- Recommender System
- Thompson Sampling
- Orchestration Optimization
one_liner: 提出双层自进化框架，协同优化推荐机制与Agent编排流程，实现推荐效果与迭代效率双提升
practical_value: '- 可复用双循环进化架构：内循环优化推荐模型代码+外循环优化Agent工作流的设计，直接复用在企业推荐系统AutoML迭代链路，减少算法工程师重复改模调参工作量

  - 低成本筛选trick：高低保真两阶段候选模型筛选机制，低训练预算初筛保留top候选再做全量训练，可降低大模型驱动的模型迭代算力成本

  - 编排优化方案：基于决策质量/实验严谨性/分析深度/搜索新颖性4个维度的流程评分，结合Thompson sampling选择编排动作的方法，可直接迁移到其他Agent工作流优化场景

  - 奖励完整性设计：把评估逻辑和准入规则放在Agent可编辑范围之外的设计，避免自进化过程中Agent钻评估漏洞，可复用在所有自进化Agent系统的安全设计中'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有LLM Agent驱动的推荐系统自动迭代方案仅基于最终推荐效果选择模型更新，缺少对实验流程质量的优化信号，容易陷入无效重复实验，无法持续提升迭代效率，同时存在进化漂移、钻评估漏洞的风险。

### 方法关键点
- 双层进化架构：内循环（机制进化）用5个固定角色的LLM Agent（诊断器/提案器/编码器/分析师/优化器）自动迭代推荐模型与训练代码，通过高低保真两阶段筛选+噪声/成本感知的准入门限判断是否更新基线模型
- 外循环（编排进化）：固定GLM-5.2评分器从决策质量、实验严谨性、分析深度、搜索新颖性4个维度评估每轮实验流程质量，用Thompson sampling选择保持现状/修改编排规则/修改技能规则3种动作，基于下一轮的流程评分残差更新动作效用估计，优化后续实验流程
- 奖励完整性边界：评估逻辑、模型准入规则固定不可被Agent编辑，避免自进化过程中出现违规利用评估漏洞的问题

### 关键实验结果
在MovieLens-1M、3个Amazon Reviews 2023子集共4个数据集，覆盖NCF/NGCF/SASRec/GRU4Rec 4种主流推荐模型，对比Base、OpenEvolve、DeepEvolve 3个基线，在64组设置-指标对比中全部取得最优，相对DeepEvolve的宏观平均提升为HR@5 7.6%、NDCG@5 9.0%，LLM token消耗比DeepEvolve低49%-63%，进化得到的编排规则可跨任务迁移带来1%-7%的效果提升。

最值得记住的一句话：自进化系统不仅要优化最终任务效果，更要优化迭代过程本身，同时必须把评估逻辑放在可编辑范围之外保障进化安全。
