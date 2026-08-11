---
title: What Would Fix This RAG Failure? Auditing Counterfactual Response with Paired
  Evidence Interventions
title_zh: RAG故障诊断：基于成对证据干预的反事实响应审计
authors:
- Wenzhang Du
affiliations:
- Independent Researcher, China
arxiv_id: '2608.08944'
url: https://arxiv.org/abs/2608.08944
pdf_url: https://arxiv.org/pdf/2608.08944
published: '2026-08-09'
collected: '2026-08-11'
category: RAG
direction: RAG故障诊断 · 反事实响应审计
tags:
- RAG
- Failure Diagnosis
- Counterfactual Intervention
- Offline Audit
- Evidence Sensitivity
one_liner: 提出Pair-ID离线审计框架，通过成对证据干预定量定位RAG故障的反事实修复路径
practical_value: '- RAG系统排障可复用Pair-ID控制变量设计：固定query/检索状态/LLM，仅调整召回内容，精准定位是召回缺漏还是冗余干扰导致的错误，适配电商客服、商品问答等RAG场景的离线迭代

  - 修复策略可直接参考量化结论：优先尝试补全缺失召回（修复率~32.8%），其次尝试删除冗余无关召回（修复率~13.6%），可快速覆盖大部分可修复故障

  - 实验评估可借鉴哈希抽样+语义匹配对照组方法，排除prompt长度、证据位置等混杂变量干扰，得到更可信的策略效果验证

  - RAG故障诊断模型不要追求跨LLM通用分类，修复路径和底层LLM强相关，每个业务所用LLM需单独训练适配的故障分类器'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前RAG故障诊断仅能从失败轨迹推测原因，无法验证不同修复操作的实际效果，相同错误可能对应完全不同的修复路径（召回缺漏、冗余干扰、两者都有、不可修复），缺乏定量的离线审计方法明确故障对不同证据干预的响应规律。

### 方法关键点
- 提出Pair-ID审计框架：固定同一个失败query的检索状态、LLM、解码参数，交叉执行两项证据操作：添加缺失支撑证据、删除已验证无关冗余证据，生成4种干预组合下的响应向量，标注故障对应的修复类型
- 设计前置哈希抽样避免选择偏倚：从11105条Qwen3-4B验证失败的多跳QA样本中，按SHA-256排序固定抽取1200条样本，全程不干预抽样结果保证客观性
- 引入长度/位置匹配的语义对照组，排除prompt长度、证据位置差异对结果的干扰，验证修复效果确实来自证据内容本身

### 关键结果
数据集采用HotpotQA和2WikiMultiHopQA，对比基线包括边际概率基线、多数向量基线、全上下文观测诊断模型。核心数字：添加缺失支撑可修复32.8%的JOINT类故障，删除冗余可修复13.6%的所有合格故障；现有最强观测诊断模型的macro AUROC仅0.678，精确向量准确率0.637低于多数向量基线0.646；4款LLM的边际修复率趋势一致，但单query修复路径一致性仅0.538~0.765。

**最值得记住的结论**：RAG故障的修复路径是LLM依赖的而非query固有属性，近7成可修复RAG故障可通过补全召回+删除冗余的组合操作覆盖，离线审计是比通用故障分类更可靠的迭代手段。
