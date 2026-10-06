---
title: 'Agentic RAG Evaluation: Budget Allocation Across Questions, Trajectories,
  and Reads'
title_zh: Agentic RAG评估：问题、检索轨迹与读取的预算分配优化
authors:
- Jingjie Ning
- Xueqi Li
- Yibo Kong
affiliations:
- Carnegie Mellon University
arxiv_id: '2610.05034'
url: https://arxiv.org/abs/2610.05034
pdf_url: https://arxiv.org/pdf/2610.05034
published: '2026-10-04'
collected: '2026-10-06'
category: Eval
direction: Agentic RAG · 评估预算优化
tags:
- Agentic_RAG
- RAG_Evaluation
- Budget_Allocation
- Sampling_Strategy
- Cost_Optimization
one_liner: 量化Agentic RAG评估预算分配的精度与成本边界，给出高性价比采样策略
practical_value: '- 做RAG/Agent系统效果评估时，相同token预算下优先扩大测试问题覆盖量，比增加多轮检索轨迹/重复读取次数的精度提升效率高33%以上，适合电商大促、广告策略的快速AB测场景

  - 轻量RAG评估可直接采用单读取（R=1）策略，对Flash类轻量模型的效率损失不超过10%，能大幅降低评估算力成本

  - 评估预算有限时可直接用1/√Q的简单规则预估标准误差，不需要复杂的嵌套方差模型，预测误差控制在3.5%以内，适合搜索推荐的日常策略迭代评估

  - 降低LLM解码温度到0可将答案不一致率从14.3%降到3.4%，且几乎不影响策略对比精度，适合需要高一致性的电商导购RAG效果验收'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
Agentic RAG的评估预算需要在测试问题数量、检索轨迹数、答案重复读取次数三者间分配，不同分配方案对评估精度、算力/检索成本的影响差异极大，过往没有量化的边界参考，导致工业界评估要么精度不足浪费迭代机会，要么成本过高拖慢节奏。

### 方法关键点
- 基于HotpotQA、MuSiQue两个多跳QA数据集，对比两种RAG策略（固定多查询、自适应反馈查询）的评估效果
- 设计嵌套抽样实验，控制三组分配方案的总模型token消耗一致（约34M），分别测试多问题、多轨迹、多读取三种分配倾向的精度
- 分别验证嵌套方差模型、Q-only（仅问题数缩放）两种预测方法的精度预估误差，同时测试不同模型、解码温度对评估效率的影响

### 关键结果数字
- 相同token预算下，扩大问题覆盖量的方案比5次读取的方案标准误差低33%，比3次轨迹的方案低12.6%
- Q-only缩放的精度预测误差仅3.5%，优于嵌套模型的4.0%，且不需要额外轨迹审计数据
- 单读取策略相对最优配置的效率损失为0-9.9%，温度0可将答案不一致率从14.3%降到3.4%，不影响策略对比精度

### 核心结论
Agentic RAG评估优先把预算投入到更多测试问题上，比增加检索/生成重复次数的投入产出比高得多。
