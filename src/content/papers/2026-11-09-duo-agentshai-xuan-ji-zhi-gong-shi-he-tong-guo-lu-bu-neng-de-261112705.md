---
title: 'Multi-Agent Screening: What Agreement and Acceptance Cannot Tell You'
title_zh: 多Agent筛选机制：共识和通过率不能反映的真实效果
authors:
- Benjamin Chang
- Dell Zhang
affiliations:
- University of Cambridge
- XSci, London
arxiv_id: '2611.12705'
url: https://arxiv.org/abs/2611.12705
pdf_url: https://arxiv.org/pdf/2611.12705
published: '2026-11-09'
collected: '2026-11-10'
category: MultiAgent
direction: 多Agent筛选 · 召回估计与预算优化
tags:
- Multi-Agent Screening
- Recall Estimation
- Agentic Retrieval
- Incomplete Judgments
- LLM-as-a-Judge
one_liner: 揭示多Agent筛选场景下四类证据的统计边界，给出无偏召回估计与成本优化方法
practical_value: '- 多Agent召回/内容审核场景不要用Agent间共识度作为效果指标，避免奖励同构模型的共通偏差，优先基于随机抽样的未过审item做无偏评估

  - 估算多Agent召回上限可直接复用Lincoln-Petersen捕获重捕获公式，新增同类型Agent的增益上限等于当前仅被单Agent检出的相关item占比除以现有Agent数

  - 需要准确评估整体召回时，对未过审pool做随机抽样审计的样本量仅和精度要求、过审率相关，和Agent数量无关，可直接用论文给出的样本量计算公式做预算规划

  - 多Agent筛选链路要单独记录每个Agent的检出item明细，不要只用聚合打分阈值做过审判断，方便后续做召回边界分析和ROI评估'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前Agentic检索、多AI审核、多通路召回等场景普遍存在「Agent算力成本低但人类评估成本极高」的矛盾，仅能对Agent筛选通过的item做标注，传统基于Agent共识、过审通过率的评估方法存在严重偏差，无法准确估计真实召回、判断新增Agent的ROI，也无法合理分配有限的人类评估预算。

### 方法关键点
- 定义多Agent筛选框架的四类可观测证据：Agent输出共识、人类对过审item的接受率、不同Agent检出item的重叠度、未过审item的随机抽样审计结果
- 从理论上证明仅靠Agent共识无法判断筛选正确性，仅靠过审接受率只能得到精度和召回的下界
- 基于Agent正相关假设，用Lincoln-Petersen捕获-重捕获方法给出召回的上界；同构Agent假设下给出新增Agent的增益上限
- 给出无需任何Agent假设的无偏召回估计方法，以及未过审item随机抽样审计的样本量计算公式

### 关键结果
以AI审稿仿真场景验证：3个AI评审从1000篇投稿筛选出200篇（过审率a=0.2），人类通过率p=0.6，仅靠通过率得到召回区间为[13%, 100%]；加入重叠度分析后召回区间缩小到[13%, 44%]；新增1个同构AI评审最多新增30篇合格投稿；仅需抽样192篇未过审投稿即可得到±5%精度、95%置信度的无偏召回估计。

### 核心结论
多Agent筛选的效果不能靠共识或通过率评估，必须结合未过审样本的随机审计才能得到无偏的召回估计
