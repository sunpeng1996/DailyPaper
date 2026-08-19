---
title: Grading Needs a Rubric, Not Intelligence
title_zh: 开放式答题批改依赖评分标准而非大模型智能
authors:
- Jhen-Ke Lin
affiliations:
- National Yang Ming Chiao Tung University
arxiv_id: '2608.17938'
url: https://arxiv.org/abs/2608.17938
pdf_url: https://arxiv.org/pdf/2608.17938
published: '2026-08-18'
collected: '2026-08-19'
category: Eval
direction: 大模型评测 · 低成本自动批改方案
tags:
- small-language-model
- grading
- rubric
- cost-efficiency
- evaluation
- benchmark
one_liner: 提出ANY-TO-BENCH架构，靠明确评分标准让低成本小模型实现媲美前沿大模型的开放式答题批改效果
practical_value: '- 做LLM生成类任务（如电商文案、Agent客服回答、搜索Query改写）的自动评测时，优先基于官方标准答案+明确评分规则设计prompt，可大幅降低对大模型能力要求，用小模型即可完成评测，显著降本

  - 批量类评测任务可采用「大模型一次性提取标准化评测规则+小模型跑批量打分」的两级架构，比全链路用前沿大模型的性价比高1-2个数量级

  - 验证内部评测规则有效性时，可通过消融不同评分项确认核心权重，官方标准答案是评测鲁棒性的核心，无标准答案场景的评测一致性会下降30%左右'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前开放式问题的大模型自动评测普遍依赖前沿大模型，成本高且存在长度偏好、同模型族偏好等偏差，规模化落地性价比低。
### 方法
提出ANY-TO-BENCH两级架构：仅在数据摄入阶段用前沿大模型单次读取源文档，提取问题对应的评分规则（rubric）；所有重复批量批改任务全部调用低成本小模型完成。测试覆盖2个模型族的6种低成本配置、3个推理effort等级，24道开放式题共生成3456条评分数据。
### 关键结果
1. 答案本身解释95.6%的评分方差，评审模型差异仅解释0.2%；提升答题模型推理能力最多提分0.143满分值，提升评审模型推理能力仅影响0.006满分值
2. 仅保留标准答案时评分效果无明显下降，移除标准答案后评分一致性ICC从0.888降至0.628，可靠性大幅下降
3. 基于rubric的评分无长度偏好、同模型族偏好问题
