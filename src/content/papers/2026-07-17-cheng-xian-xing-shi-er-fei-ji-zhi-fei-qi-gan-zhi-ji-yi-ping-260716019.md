---
title: 'Presentation, Not Mechanism: A Render Confound in Deprecation-Aware Memory
  Evaluation'
title_zh: 呈现形式而非机制：废弃感知记忆评估中的渲染混淆问题
authors:
- Zhaoyang Jiang
- Zhizhong Fu
- Zicheng Li
- Yunsoo Kim
- Jiacong Mi
- Xuanqi Peng
- Fei Teng
- Honghan Wu
affiliations:
- University of Glasgow
- Shanghai Sixth People's Hospital, Shanghai Jiao Tong University School of Medicine
- University of Electronic Science and Technology of China
- University College London
arxiv_id: '2607.16019'
url: https://arxiv.org/abs/2607.16019
pdf_url: https://arxiv.org/pdf/2607.16019
published: '2026-07-17'
collected: '2026-07-20'
category: Agent
direction: Agent长时记忆评估 · 渲染混淆控制
tags:
- Agent_Memory
- RAG_Evaluation
- Deprecation_Aware
- Structured_Memory
- Temporal_Reasoning
one_liner: 发现结构化记忆性能优势多来自prompt排版，而非细粒度废弃感知机制
practical_value: '- 做Agent/RAG系统架构对比时，必须固定prompt的布局格式，避免把排版易读性的增益错误归因到算法机制本身

  - 业务中处理动态更新的商品/政策/用户偏好数据时，仅需用粗粒度的二进制生效/废弃标记就能满足大部分当前状态查询需求，无需投入成本做细粒度关系建模

  - 做溯源类查询（比如用户历史偏好变更、商品价格调整记录）时，核心是留存已废弃的历史数据，而非给数据加复杂的关系类型标签

  - 新记忆系统上线前建议加渲染匹配对照组，快速定位性能提升的真实来源，避免过度工程'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前Agent、RAG系统需要处理持续更新的动态数据（工单、百科修订、政策日志、长对话历史等），现有结构化记忆方案的评估往往同时修改底层机制和prompt呈现形式，无法准确区分性能提升的真实来源，极易导致系统过度设计，浪费研发成本。

### 方法关键点
- 提出证据状态修订（ESR）任务框架，按冲突位置划分为3个能力层级，明确不同查询类型需要的最小记忆能力
- 设计**渲染匹配对照实验**：固定prompt的布局格式，仅开启/关闭废弃感知机制，精准分离排版易读性和底层机制的贡献
- 构建包含2907条高一致性问答的ESR-Bench，覆盖GitHub工单、维基百科修订、DyKnow动态知识流等场景
- 对比三类基准方案：无废弃标记的GraphRAG+abstain基线、Zep/Graphiti风格的粗粒度边失效存储、带关系类型的细粒度RevisionLedger

### 关键结果
- 细粒度RevisionLedger在回退变更场景看似比flat基线准确率高+0.182，其中+0.159来自排版优化，机制贡献仅+0.021~+0.025，统计上不显著
- 固定渲染格式后，粗粒度边失效方案比细粒度ledger准确率高0.084，是当前状态查询的最优选择
- 溯源查询场景下，留存废弃数据的粗粒度方案就能覆盖大部分需求，细粒度方案仅带来0.111的边际增益，且仍可能来自排版差异

**最值得记住的一句话：评估记忆架构时必须固定渲染格式，业务中应选用能覆盖查询需求的最粗粒度留存状态**
