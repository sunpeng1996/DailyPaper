---
title: 'What Survives Into Context: A Diagnostic for Budget-Constrained Multi-Hop
  RAG and When Submodular Evidence Packing Improves It'
title_zh: 预算受限多跳RAG诊断框架及子模证据打包优化方案
authors:
- Ananto Nayan Bala
affiliations:
- Ahsanullah University of Science and Technology
arxiv_id: '2607.00725'
url: https://arxiv.org/abs/2607.00725
pdf_url: https://arxiv.org/pdf/2607.00725
published: '2026-07-01'
collected: '2026-07-02'
category: RAG
direction: 检索增强生成 · 上下文压缩与评估
tags:
- RAG
- Multi-hop QA
- Submodular Optimization
- Context Selection
- Evaluation Metric
one_liner: 提出answer-in-context RAG诊断指标与子模证据打包方法，明确优化适用边界
practical_value: '- 评估指标替换：电商/导购Agent等RAG系统可放弃recall@k，改用answer-in-context作为上下文质量核心评估指标，尤其端侧小模型、KV
  cache预算紧张的场景，对最终回答质量的预测准确率提升近一倍

  - 小模型RAG优化：3B及以下参数量的多跳RAG场景（比如多属性商品查询、多步骤售后问题解答），可直接复用子模打包算法，在相同token成本下回答F1最高提升5.1，或在相同回答质量下减少30%token消耗

  - 大模型RAG降本：7B及以上参数量的RAG系统无需开发复杂打包策略，直接用简单的相关性排序拼接即可，14B以上模型用子模打包反而会降低效果，节省工程开发和计算成本

  - 预算点选择：RAG上下文预算设置遵循倒U型规律，避免过紧（无法容纳多份证据）或过松（冗余内容太多），160token是多跳QA场景的最优预算点'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有RAG系统默认采用recall@k作为检索质量评估指标，仅统计召回文档集中的黄金文档占比，但在上下文预算紧张场景下，打包环节会丢弃大量召回内容，recall完全无法反映LLM最终接收到的上下文质量。尤其多跳RAG需要组合多份互补证据，一旦打包阶段丢弃关键桥接证据，即使召回全量黄金文档也无法得到正确答案，缺少直接关联最终回答质量的评估指标，且打包策略缺乏可解释的适用边界。

### 方法关键点
- 定义answer-in-context诊断指标：判断标准化后的标准答案是否作为连续token span出现在最终打包的上下文中，直接对齐LLM输入质量
- 将上下文打包建模为预算约束下的单调子模最大化问题，目标函数加权融合相关性、查询覆盖、代表性、多样性四个维度，所有子项均归一化到[0,1]区间，采用按token边际增益的贪心算法求解
- 实验全程固定召回候选集，仅对比打包策略的差异，排除召回效果对结论的干扰

### 关键结果
- answer-in-context与回答F1的相关性达0.39~0.55，远高于recall@k的~0.31，在召回全量黄金文档的样本中仍能带来4.6倍的EM差距，增量R²达0.17
- HotpotQA数据集、160token预算、3B Qwen2.5模型下，子模打包相比启发式、MMR、naive打包分别提升F1 2.2、4.2、5.1，且token消耗比基线低约7个
- 明确适用边界：仅同时满足多跳互补结构、召回已覆盖全量黄金证据、预算适中（~160token）、模型参数量<=3B四个条件时，子模打包优于启发式策略；7B模型收益消失，14B模型反而下降2.9 F1

### 最值得记住的结论
预算受限RAG的核心瓶颈不是召回覆盖，而是标准答案能否在打包后保留在上下文中，复杂上下文优化策略的收益会随模型能力上升快速消失甚至反转。
