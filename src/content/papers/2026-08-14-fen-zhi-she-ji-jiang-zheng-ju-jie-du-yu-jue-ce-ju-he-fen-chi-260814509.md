---
title: 'Split the Labor: Separating Evidence Interpretation from Decision Aggregation'
title_zh: 分治设计：将证据解读与决策聚合分离的推理框架
authors:
- Zhelun Wu
affiliations:
- Atlassian
arxiv_id: '2608.14509'
url: https://arxiv.org/abs/2608.14509
pdf_url: https://arxiv.org/pdf/2608.14509
published: '2026-08-14'
collected: '2026-08-17'
category: Agent
direction: Agent 多源信息推理架构优化
tags:
- Evidence Aggregation
- LLM Reasoning
- Count-Scale Drift
- Survival Analysis
- Decision Support
one_liner: 提出多源证据推理分治架构，拆解为单源解读加结构化聚合，解决计数尺度漂移缺陷
practical_value: '- 多源信息召回/审核场景可复用分治架构：单源用LLM输出<假设、可靠性桶、理由、来源>四元组，聚合层用可解释规则计算，解决长上下文稀释、归因难问题，同时降低token成本

  - 多信号打分/风险识别场景可直接复用calibrated log-likelihood ratio聚合方法，替换现有加权求和阈值规则，解决count-scale
  drift导致的证据量不均场景误判问题，适配电商风控、广告反作弊等场景

  - 时序生存分析任务可参考容量拆分方案：小序列模型做基础语义/时序特征抽取，树模型处理带删失的标签拟合，中小规模结构化数据下效果优于端到端神经网络，可迁移到用户生命周期预测、复购预测等场景

  - 可靠性桶设计可复用：不用LLM输出的不可靠置信度，改用可观测属性（如抽取理由是否有依据、源长度）划分等级，权重从历史数据估计，比手动调权更稳定'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前LLM做多源证据推理普遍将所有源拼接为单prompt，同时完成证据解读和决策，存在四大缺陷：归因难、低质量源稀释有效信息、长上下文性能退化、无有效证据也强制生成结论；同时通用的加权求和聚合规则存在count-scale drift，证据量多的实例阈值自动降低，导致误判率上升。

### 方法关键点
- 分治架构：拆分证据解读与决策聚合两个步骤，定义四字段证据元组<假设、可靠性桶、理由、来源>作为中间接口，每个源单独解读，仅引入因果上下文（无未来信息）
- 聚合层用calibrated log-likelihood ratio替代普通加权求和，解决count-scale漂移问题，新增依赖块折扣处理同源证据的重复计算
- 时序生存分析场景下做容量拆分：小GRU做辅助语义抽取，梯度提升树处理带删失的多风险时序损失，避免单模型同时学习表征与时序结构的容量冲突

### 关键结果
- 静态归因任务（162条标注售后工单）：带因果上下文的单源解读+先验fallback对比端到端拼接prompt，precision从0.645提升到0.772，macro F1从0.425提升到0.466，instance F1持平
- 时序预测任务（2.3万条工单数据）：拆分架构AUPRC达0.921，比手工特征基线0.805提升0.116，远优于端到端神经网络的0.316

最值得记住的：多源信息融合系统的性能瓶颈往往不在单源解读的模型能力，而在跨源聚合的规则设计，合理拆分任务比盲目堆大模型上下文收益更高。
