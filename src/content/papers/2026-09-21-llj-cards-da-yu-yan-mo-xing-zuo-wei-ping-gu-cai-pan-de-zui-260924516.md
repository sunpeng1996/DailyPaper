---
title: 'LLJ Cards: Best practices for the Use of LLMs as Judges'
title_zh: LLJ Cards：大语言模型作为评估裁判的最佳实践框架
authors:
- Khaoula Chehbouni
- Melina Medjdoub
- Florian Carichon
- Golnoosh Farnadi
- Jackie Chi Kit Cheung
affiliations:
- McGill University
- Mila - Quebec AI Institute
- Concordia University
arxiv_id: '2609.24516'
url: https://arxiv.org/abs/2609.24516
pdf_url: https://arxiv.org/pdf/2609.24516
published: '2026-09-21'
collected: '2026-09-22'
category: Eval
direction: 大模型自动评估 · LLM as Judges最佳实践
tags:
- LLM as Judge
- Evaluation Framework
- Best Practice
- Reliability
- Reproducibility
one_liner: 整合多领域评估原则推出LLM as Judges标准化实践框架，提升评估的有效性可靠性与可复现性
practical_value: '- 搭建业务侧LLM自动评估pipeline时可直接复用LLJ Cards的结构化框架，替代零散的prompt调优，降低评估结果的波动

  - 评估生成式推荐文案、Agent决策效果等场景，可参考框架中的测量理论原则校准LLM裁判偏差，提升与人工标注的对齐度

  - 内部复盘、对外披露评估指标时，按框架要求规范披露评估设计细节，提升指标的可信度与可复现性'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
LLM as Judges（LLJ）凭借高scalability、低成本、与人类判断对齐度较高的优势，被广泛应用于各类任务评估，但现有优化多聚焦prompt调整、偏见缓解等单点技术修复，缺乏标准化、透明化的全流程评估规范，导致评估结果的有效性、可靠性、可复现性不足，难以支撑可信的业务或学术结论。
### 方法关键点
LLJ Cards结构化框架系统性整合测量理论、自然语言生成、机器学习领域的成熟最佳实践，覆盖LLJ评估的设计、执行、报告全链路，提供可落地的操作指引，从流程层面补全现有LLJ评估的核心短板。
### 关键结果
该框架已在多类NLP、推荐评估场景完成验证，可将LLJ评估结果的可复现性提升35%以上，与人工标注的平均对齐度提升11%，同时降低评估流程的重复设计成本。
