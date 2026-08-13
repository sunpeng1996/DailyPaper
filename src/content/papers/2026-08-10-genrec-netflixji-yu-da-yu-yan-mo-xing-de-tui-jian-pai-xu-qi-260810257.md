---
title: 'GenRec: An LLM-Backed Recommendation Ranker at Netflix'
title_zh: GenRec：Netflix基于大语言模型的推荐排序器
authors:
- Ying Li
- Shradha Sehgal
- Arjun Rao
- Rein Houthooft
- Yaochen Zhu
- Ashish Rastogi
affiliations:
- Netflix
- Amazon
arxiv_id: '2608.10257'
url: https://arxiv.org/abs/2608.10257
pdf_url: https://arxiv.org/pdf/2608.10257
published: '2026-08-10'
collected: '2026-08-12'
category: GenRec
direction: 生成式推荐 · LLM排序器两阶段训练
tags:
- GenRec
- LLM4Rec
- Context Engineering
- Two-phase Training
- Reward Modeling
one_liner: 提出两阶段训练的LLM推荐排序器，用更少标签超过Netflix成熟生产排序器同时优化落地成本
practical_value: '- 可复用两阶段训练范式：先做领域基础预训练对齐平台用户/内容语义，再做高频轻量任务后训练，平衡效果与迭代效率

  - 可迁移上下文优化方案：通过高信号事件保留、低信号事件过滤、重复行为压缩，可将上下文长度降至1/3且无明显效果损失，直接降低推理成本

  - 工程落地可采用prefill-only推理模式：给LLM新增catalog-aware排序头，单前向传播完成全候选集打分，避免自回归解码的高延迟，适配高流量推荐场景

  - 训练侧可复用奖励加权排序损失：将长期用户价值、业务规则信号转化为样本权重，无需复杂RL流程即可对齐业务目标，落地成本低'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统推荐系统依赖海量人工特征与定制化架构，新内容、新场景接入需重构特征与模型，迭代效率极低；开箱即用的LLM做推荐存在热门偏置、生成库外物品、个性化不足等问题，无法直接落地生产。
### 方法关键点
- 采用两阶段训练范式：Phase1基于开源LLM，用Netflix私有数据预训练得到领域基础模型，平衡内容理解、用户建模等通用能力；Phase2用排序专属数据、多维度奖励信号做高频后训练，快速适配业务变化
- 输入侧做精细化上下文工程：将用户历史、物品元数据、上下文自然语言化，通过高信号事件留全、低信号事件过滤、重复行为压缩等策略，在有限token预算下最大化信息密度
- 模型层在decoder-only LLM基础上新增catalog-aware排序头，用户上下文编码后直接与物品embedding计算打分，严格限制输出为库内物品
- 推理采用prefill-only模式，单前向传播完成全候选集打分，基于vLLM部署，避免自回归解码的高延迟
### 关键结果
仅用1/40的Phase2标注数据，离线MRR相对成熟生产排序器提升1.6%；线上A/B测试切10%流量运行4周，短期主页engagement提升0.115%，长期核心指标提升0.006%，均统计显著。上下文长度压缩到原1/3时无明显效果损失，推理成本同步降低2/3。Phase1领域预训练比直接用开源LLM做底座效果高10-20%，Phase2后训练再提35-50%效果。
最值得记住的结论：LLM原生推荐的核心转变是从特征工程转向上下文工程、从定制架构转向通用基础骨干，可在更低迭代成本下超过传统成熟系统的效果。
