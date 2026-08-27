---
title: 'The "Curse of Knowledge" in LLM Query Simulation: Concept Provenance for Tracing
  Answer-Side Intrusion'
title_zh: LLM查询模拟中的「知识诅咒」：概念溯源追踪答案侧概念侵入
authors:
- Chenglong Ma
- Xinye Wanyan
- Danula Hettiachchi
- Ziqi Xu
- Jeffrey Chan
affiliations:
- RMIT University
arxiv_id: '2608.25245'
url: https://arxiv.org/abs/2608.25245
pdf_url: https://arxiv.org/pdf/2608.25245
published: '2026-08-26'
collected: '2026-08-27'
category: QueryRec
direction: LLM查询生成 · 边界合规诊断
tags:
- Query Generation
- IR Evaluation
- Concept Provenance
- Boundary Compliance
- LLM Evaluation
one_liner: 提出概念溯源框架识别LLM生成查询的答案侧概念侵入，支持信息访问边界合规诊断
practical_value: '- 电商搜索query/推荐候选query生成场景，可复用概念溯源的优先级校验逻辑，过滤未出现在用户前置知识、历史搜索query中的答案侧独有概念，避免生成不符合真实用户预搜索信息状态的query，减少检索结果偏离用户真实需求的情况

  - 生成式推荐/搜索的query效果评估时，在现有多样性、相关性指标之外，可新增HCIR作为辅助校验指标，避免因侵入概念拉高检索相关性虚高导致的评估失真

  - LLM用户模拟场景下，可复用「过生成+概念溯源过滤+人类高频词对齐质量兜底」的方案，每类需求仅需生成5个候选query即可覆盖95%的合规query，兼顾生成效率与边界合规性'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
LLM生成搜索query被广泛用于信息检索评估增强、用户模拟等场景，但现有重叠度、多样性、检索效果等指标无法区分人类长尾词汇变异和答案侧概念侵入——即query隐含只有完成搜索后才能获得的知识，违反预搜索用户的信息访问边界，导致评估结果失真。
### 方法关键点
- 定义4类概念溯源分区，按优先级依次为：背景故事支持(Z0)、人类高频使用(Z1)、人类长尾使用(Z2)、答案侧侵入(Z3auto)，仅未出现在背景/人类query中、同时在相关文档中高显著的概念被判定为侵入
- 提出HCIR（隐藏概念侵入率）指标，衡量query中非通用概念中Z3auto的占比，采用双提取pipeline保证检测鲁棒性
- 设计5类prompt生成对照：通用、高知识、边界约束、oracle文本、oracle术语
### 关键结果
在UQV100数据集的77004条生成query、8个LLM上验证：
- 答案侧概念平均占非通用概念的7.4%，97%的topic存在侵入，topic特征可解释67%的侵入率方差
- 删除侵入概念后nDCG@10下降Cohen's d=-0.47，高于随机删除的d=-0.34，说明侵入概念携带额外检索信号
- 仅靠prompt优化无法完全消除侵入，生成后溯源过滤可实现99%的侵入消除，每topic生成5个候选即可覆盖95%合规query
> 最值得记住：LLM生成查询的答案侧概念侵入对整体评估指标影响极小，但会显著改变单query检索结果，适合作为边界合规诊断指标而非评估偏移预测指标
