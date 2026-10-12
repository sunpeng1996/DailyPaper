---
title: Incremental Retrieval-Augmented Generation for Human-in-the-Loop Decision Support
title_zh: 面向人在回路决策支持的增量检索增强生成系统iRAG
authors:
- Federico Mazzoni
- Andrea Failla
affiliations:
- Independent Researcher
- Institute of Information Science and Technologies (ISTI), CNR, Italy
arxiv_id: '2610.12666'
url: https://arxiv.org/abs/2610.12666
pdf_url: https://arxiv.org/pdf/2610.12666
published: '2026-10-08'
collected: '2026-10-12'
category: RAG
direction: 增量RAG · 人在回路混合决策
tags:
- RAG
- Human-in-the-Loop
- Hybrid Decision-Making
- Concept Drift
- Learning-to-Defer
one_liner: 结合RAG与混合决策框架，实现从空知识库起步随人类决策迭代的人在回路决策支持系统
practical_value: '- 动态KB的RAG可引入指数时间衰减权重（λ_RAG）调整新旧知识检索优先级，适配电商大促规则变更、广告审核标准更新等高频迭代场景，可控调节稳定性-可塑性tradeoff

  - 三阶段人机协作状态机（静默观察→异议提示→自主决策）可直接复用在Agent自动审核、智能客服等场景，通过Fading Empirical Accuracy（FEA）阈值控制授权节奏，降低上线风险

  - 高概念漂移场景下，增量RAG配合人在回路控制器比无状态控制的RAG收益更明显，40%漂移率下决策错误率相对降低25%以上，可直接复用到规则频繁变动的业务链路'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
传统RAG依赖预构建的静态知识库，无法适配知识需要随业务决策动态积累、且存在概念漂移的场景；现有混合决策（HDM）系统需要频繁重训模型，审计性差，也没有和RAG的动态检索能力结合，无法支撑从空知识库起步的人机协同决策需求。

### 方法关键点
- iRAG知识库直接存储历史<输入, 最终决策>对，无需预构建，每次决策后自动追加记录
- 检索阶段引入指数时间衰减因子λ_RAG，对较早入库的知识降低检索权重，灵活适配知识迭代的稳定性-可塑性tradeoff
- 设计三阶段人机协作状态机：静默观察阶段仅记录模型与人类决策的一致性；异议提示阶段模型决策与人类不一致时，附带检索证据提出修正建议；自主决策阶段模型满足一致性阈值后可自主决策，仅在不确定时defer给人类
- 采用Fading Empirical Accuracy（FEA）作为状态切换核心指标，对早期一致性观测做衰减加权，避免旧观测影响当前模型可靠性判断

### 关键实验
在模拟CRM客服ticket的合成数据集上测试，设置10%/40%两种概念漂移率，对比无控制器的原生RAG基线：10%漂移率下，无衰减的iRAG与基线准确率相当（5.52% vs 5.50%错误率）；40%漂移率下，iRAG所有配置的错误率为9.51%~10.52%，比基线的14.03%相对降低25%~32%，同时模型自主处理的ticket占比仅26%~36%，远低于基线的60%，风险更低。

### 核心结论
检索时间衰减并非通用优化手段，其收益随业务场景的概念漂移率提升而升高，低漂移场景下无衰减的静态检索反而整体准确率更优
