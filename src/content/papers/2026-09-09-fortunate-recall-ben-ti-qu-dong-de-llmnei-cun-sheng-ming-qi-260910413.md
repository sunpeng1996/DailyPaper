---
title: 'Fortunate Recall: Ontology-Driven Memory Lifecycle Management for Persistent
  Coherence in LLMs'
title_zh: Fortunate Recall：本体驱动的LLM内存生命周期管理实现持久一致性
authors:
- Ansuman Mullick
- Eray Tüzün
affiliations:
- Bilkent University
arxiv_id: '2609.10413'
url: https://arxiv.org/abs/2609.10413
pdf_url: https://arxiv.org/pdf/2609.10413
published: '2026-09-09'
collected: '2026-09-10'
category: Agent
direction: Agent长时内存生命周期优化
tags:
- LLM Agent
- Memory Management
- Ontology
- Lifecycle Policy
- Hallucination Reduction
one_liner: 提出可组合的行为本体分层LLM内存生命周期策略层，显著降幻觉提升长时记忆正确性
practical_value: '- 电商个性化导购Agent可复用行为分类逻辑，给用户身份属性、短期偏好、临时订单、待办优惠券等不同类型记忆设置差异化过期/替换策略，避免用旧偏好做推荐

  - 推荐系统用户兴趣画像更新可借鉴slot-key supersession机制，对（用户ID，偏好类目）槽位的新事实自动覆盖旧事实，同时保留低置信度探索性兴趣，解决兴趣更新滞后问题

  - RAG系统增量文档更新可复用事件时间有效性+确定性生命周期层设计，仅摄入阶段调用一次LLM打标签，检索阶段用纯规则过滤过期/旧版文档，大幅降低检索侧LLM调用成本同时提升召回准确率'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前LLM长时记忆系统对所有事实采用统一存储和检索策略，内存无限膨胀的同时检索精度持续下降，无法区分需长期保留的身份类事实、需更新的偏好类事实、自动过期的临时事务类事实，导致幻觉率高、长会话一致性差。

### 方法关键点
- 构建10+1行为分类本体，按事实的时间变化特征而非认知类型分类，每个类别配置差异化生命周期策略（半衰期、替换规则、过期逻辑）
- 内存生命周期层为纯确定性数学逻辑，仅在摄入阶段调用LLM提取事实并打分类、槽位键、生命周期状态、事件时间锚点4种元数据，检索阶段仅做一次轻量LLM候选筛选，其余逻辑纯规则执行，单步延迟中位数47μs
- 核心机制包括差异化时间衰减、slot-key置信度加权替换、事件时间有效性校验、分类感知检索路由4类

### 关键结果
- 自建516题时间歧义基准LifecycleBench，FR-Bank实现76.9%通过率，领先Mem0（61%）、A-MEM（65.3%）、Memory-R1（66.9%）、MemoryOS（70.5%）
- 在标准LongMemEval-S基准达到75.2%通过率，对标准检索任务无明显性能损耗；相比Mem0，全查询幻觉率从32.2%降至13.0%，正确回答率从18.6%提升至31.2%
- 消融实验显示通用生命周期元数据贡献核心正确性收益，行为本体额外将幻觉率减半，分类粒度达到7类后收益饱和

**最值得记住的一句话**：LLM长时记忆的核心瓶颈不是检索精度，而是生命周期管理，纯规则的分层生命周期策略可以用极低的计算成本大幅降低幻觉、提升长会话一致性
