---
title: Top-K Is Not a Budget for Hybrid Retrieval
title_zh: RAG混合检索场景下固定Top-K无法作为访问成本预算
authors:
- Chunran Zhang
affiliations:
- Southwest Jiaotong University
arxiv_id: '2609.15143'
url: https://arxiv.org/abs/2609.15143
pdf_url: https://arxiv.org/pdf/2609.15143
published: '2026-09-14'
collected: '2026-09-16'
category: RAG
direction: RAG混合检索 · 成本优化
tags:
- Hybrid Retrieval
- RRF
- Budgeted Retrieval
- RAG
- Cost Optimization
one_liner: DiBud预算约束混合检索方法，增量返回RRF精确前缀，大幅降低长尾检索开销
practical_value: '- 电商搜索、RAG问答系统的混合检索环节可直接复用DiBud的预算约束机制，替代固定Top-L截断，避免query或语料变化导致的效果波动，同时降低长尾query的访问成本

  - 多路召回（稀疏+稠密召回等）的RRF融合环节可复用精确前缀认证逻辑，无需预设召回截断深度，在有限访问预算下最大化可保证的有效召回结果数量

  - 流量高峰时段可动态调整访问预算B来削峰，在保证95%以上nDCG的前提下最高可降低99%的检索访问开销，平衡服务稳定性和检索效果'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
RAG常用混合检索方案依赖固定Top-L截断的稠密+稀疏召回结果做RRF融合，固定截断深度无法适配query分布变化、语料迭代场景，效果-成本 tradeoff 易失效；无截断的精确Top-K检索存在访问成本长尾分布问题，少数query消耗上千倍于中位数的访问资源，固定Top-K无法约束成本。
### 方法关键点
- DiBud（Direct Budgeting）直接将访问预算B作为输入，不预设输出结果数K，增量读取稀疏/稠密召回列表
- 维护未读条目贡献上下界，当前条目的得分下界超过所有其他候选上界时，将其认证为精确前缀的下一个结果，保证返回结果顺序与全量RRF排序完全一致
- 选路策略优先读取阻塞当前结果认证的召回通道，否则选择读取后能最大程度降低未读贡献上界的通道，最大化有限预算下的认证结果数
- 预算耗尽时直接返回已认证的精确前缀，无需完成固定K的检索
### 关键实验
在TREC-DL 2019/2020、NFCorpus等5个公开query集上验证，对比基线为平衡读取（交替读两路召回）、全量精确Top-20检索：① 2048访问预算下，前100位平均认证结果数比平衡读取高7.86%；② 校准为保留95% nDCG@20的预算时，持有集query保留95.05%~97.68%的nDCG@20，比完成全量精确Top-20减少65.92%~99.53%的访问开销。
### 核心结论
固定Top-K不是混合检索的成本预算，直接约束访问开销、动态调整返回结果数的方案能在保证效果的前提下大幅降低长尾成本。
